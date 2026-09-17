#!/usr/bin/env python3
"""
YouTube-Transkription mit Fallback: erst Untertitel (yt-dlp), sonst Whisper.
Bleibt standardmäßig in der Originalsprache des Videos (keine automatische Übersetzung).

Nutzung:
    python transcribe_youtube.py <YouTube-URL> [--lang de,en] [--whisper-model small]
                                  [--out-dir transcripts] [--force-whisper] [--keep-audio]
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def ensure_ffmpeg_on_path():
    """Frisch per winget installiertes ffmpeg landet nicht sofort im PATH der laufenden
    Shell/des Prozesses (PATH wird erst bei neuem Prozessstart aus der Registry gelesen).
    Als Fallback direkt im winget-Paketordner suchen und PATH für diesen Prozess erweitern."""
    if shutil.which("ffmpeg"):
        return
    packages_dir = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Packages"
    if not packages_dir.exists():
        return
    for candidate in packages_dir.glob("Gyan.FFmpeg_*/**/ffmpeg.exe"):
        os.environ["PATH"] = str(candidate.parent) + os.pathsep + os.environ["PATH"]
        return


def run_yt_dlp(args, cwd=None):
    cmd = [sys.executable, "-m", "yt_dlp"] + args
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|]', "_", name).strip()
    return name[:150] if len(name) > 150 else name


def get_title(url: str) -> str:
    result = run_yt_dlp(["--print", "%(title)s", "--no-playlist", url])
    if result.returncode != 0 or not result.stdout.strip():
        return "video"
    return sanitize_filename(result.stdout.strip().splitlines()[0])


def vtt_to_text(vtt_path: Path) -> str:
    content = vtt_path.read_text(encoding="utf-8", errors="ignore")
    blocks, current = [], []
    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line or line == "WEBVTT" or line.startswith(("Kind:", "Language:", "STYLE", "NOTE", "::cue")):
            continue
        if "-->" in line:
            if current:
                blocks.append(" ".join(current))
                current = []
            continue
        if line.isdigit():
            continue
        clean = re.sub(r"<[^>]+>", "", line).strip()
        if clean:
            current.append(clean)
    if current:
        blocks.append(" ".join(current))

    # Rolling-Untertitel (auto captions) enthalten oft Wortüberlappungen zwischen Blöcken -> dedupen
    words: list[str] = []
    for block in blocks:
        block_words = block.split()
        max_overlap = min(len(words), len(block_words))
        overlap = 0
        for k in range(max_overlap, 0, -1):
            if words[-k:] == block_words[:k]:
                overlap = k
                break
        words.extend(block_words[overlap:])
    return " ".join(words)


def _fetch_subs(url: str, sub_langs: str, auto: bool, tmp_dir: Path) -> str | None:
    args = [
        "--skip-download",
        "--write-subs",
        "--sub-langs", sub_langs,
        "--sub-format", "vtt",
        "--no-playlist",
        "-o", str(tmp_dir / "%(id)s.%(ext)s"),
        url,
    ]
    if auto:
        args.insert(2, "--write-auto-sub")

    result = run_yt_dlp(args)
    if result.returncode != 0:
        print(f"  yt-dlp Untertitel-Versuch fehlgeschlagen: {result.stderr.strip().splitlines()[-1] if result.stderr.strip() else 'unbekannter Fehler'}")
        return None

    vtt_files = sorted(tmp_dir.glob("*.vtt"))
    if not vtt_files:
        return None

    text = vtt_to_text(vtt_files[0])
    return text if text.strip() else None


def get_original_language(url: str) -> str | None:
    """YouTube markiert in den automatischen Untertiteln die tatsächliche Tonspur-Sprache
    mit dem Suffix "-orig" (z.B. "en-orig"), alle anderen Sprachcodes dort sind maschinell
    übersetzt. Das ist der zuverlässigste Weg, die echte Originalsprache eines Videos zu
    bestimmen, unabhängig davon, welche manuellen/automatischen Untertitel sonst existieren."""
    result = run_yt_dlp(["-j", "--skip-download", "--no-playlist", url])
    if result.returncode != 0 or not result.stdout.strip():
        return None
    try:
        info = json.loads(result.stdout.strip().splitlines()[0])
    except (json.JSONDecodeError, IndexError):
        return None
    for lang_code in info.get("automatic_captions", {}):
        if lang_code.endswith("-orig"):
            return lang_code[: -len("-orig")]
    return None


def try_subtitles(url: str, lang: str | None, tmp_dir: Path) -> str | None:
    if lang:
        # Explizit gewünschte Sprache(n) - kann auch von YouTube automatisch übersetzte
        # Untertitel einschließen, das ist hier bewusst gewollt.
        return _fetch_subs(url, lang, auto=True, tmp_dir=tmp_dir)

    # Kein --lang angegeben: NIE automatisch übersetzte oder anderssprachige Untertitel
    # verwenden, immer die tatsächliche Originalsprache des Videos.
    original_lang = get_original_language(url)
    if not original_lang:
        # Originalsprache nicht sicher bestimmbar -> lieber Whisper nutzen als raten
        return None

    # 1) Von Menschen erstellte Untertitel exakt in der Originalsprache.
    text = _fetch_subs(url, original_lang, auto=False, tmp_dir=tmp_dir)
    if text:
        return text

    # 2) Automatische Untertitel, aber nur die als Original markierte Tonspur.
    return _fetch_subs(url, f"{original_lang}-orig", auto=True, tmp_dir=tmp_dir)


def transcribe_with_whisper(url: str, model_name: str, tmp_dir: Path, keep_audio: bool, out_dir: Path, title: str) -> str:
    print(f"  Lade Audio herunter...")
    result = run_yt_dlp(
        [
            "-f", "bestaudio",
            "-x", "--audio-format", "mp3",
            "--no-playlist",
            "-o", str(tmp_dir / "%(id)s.%(ext)s"),
            url,
        ]
    )
    if result.returncode != 0:
        raise RuntimeError(f"Audio-Download fehlgeschlagen: {result.stderr.strip()}")

    audio_files = sorted(tmp_dir.glob("*.mp3"))
    if not audio_files:
        raise RuntimeError("Kein Audio nach dem Download gefunden.")
    audio_path = audio_files[0]

    if keep_audio:
        keep_path = out_dir / f"{title}.mp3"
        keep_path.write_bytes(audio_path.read_bytes())
        print(f"  Audio gespeichert: {keep_path}")

    print(f"  Transkribiere mit Whisper (Modell: {model_name}) - das kann je nach Videolänge dauern...")
    import whisper  # Import erst hier, damit --help schnell bleibt, wenn Whisper nicht gebraucht wird

    model = whisper.load_model(model_name)
    result = model.transcribe(str(audio_path))
    return result["text"].strip()


def main():
    parser = argparse.ArgumentParser(description="YouTube-Video transkribieren (Untertitel, sonst Whisper-Fallback).")
    parser.add_argument("url", help="YouTube-Video-URL")
    parser.add_argument("--lang", default=None, help="Explizite Untertitel-Sprache(n), Komma-getrennt (z.B. de,en). Ohne Angabe wird immer die Originalsprache des Videos verwendet, nie eine von YouTube automatisch übersetzte Fassung.")
    parser.add_argument("--whisper-model", default="small", choices=["tiny", "base", "small", "medium", "large"], help="Whisper-Modellgröße (Standard: small)")
    parser.add_argument("--out-dir", default="transcripts", help="Ausgabeverzeichnis (Standard: ./transcripts)")
    parser.add_argument("--force-whisper", action="store_true", help="Untertitel-Versuch überspringen und direkt Whisper nutzen")
    parser.add_argument("--keep-audio", action="store_true", help="Heruntergeladene Audiodatei zusätzlich behalten")
    args = parser.parse_args()

    ensure_ffmpeg_on_path()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Ermittle Videotitel...")
    title = get_title(args.url)
    print(f"Video: {title}")

    text = None
    source = None

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)

        if not args.force_whisper:
            print("Versuche vorhandene Untertitel zu laden...")
            text = try_subtitles(args.url, args.lang, tmp_dir)
            if text:
                source = "Untertitel (yt-dlp)"
            else:
                print("  Keine passenden Untertitel gefunden.")

        if text is None:
            text = transcribe_with_whisper(args.url, args.whisper_model, tmp_dir, args.keep_audio, out_dir, title)
            source = f"Whisper ({args.whisper_model})"

    out_path = out_dir / f"{title}.txt"
    out_path.write_text(text, encoding="utf-8")

    print(f"\nFertig. Quelle: {source}")
    print(f"Transkript gespeichert: {out_path}")


if __name__ == "__main__":
    main()
