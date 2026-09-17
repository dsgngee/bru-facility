#!/usr/bin/env python3
"""
Bildgenerierung für die BRU-Homepage-Varianten über die Google Gemini API (Nano Banana Pro /
gemini-3-pro-image). Liest den API-Key aus der Umgebungsvariable GOOGLE_API_KEY (bzw. aus einer
lokalen .env-Datei im Projekt-Root) und speichert erzeugte Bilder in einen Review-Ordner
(<variante>/assets/_generated/), statt live Assets direkt zu überschreiben.

Nutzung:
    python scripts/generate_images.py --variant corporate --motif gebaeude
    python scripts/generate_images.py --variant corporate --motif gebaeude --n 3
    python scripts/generate_images.py --variant corporate --all

Nur Motive ohne Personen sind hier hinterlegt (gebaeude, bau, garten, winterdienst, reinigung).
Personen-Motive (handshake, hausmeister/Handwerker im Einsatz) laufen laut Plan über Higgsfield
und werden manuell in dessen Web-UI erzeugt (siehe Bildkonzept-Abschnitt in content-plan.md).
"""

import argparse
import os
import sys
from pathlib import Path

from google import genai
from google.genai import types

ROOT = Path(__file__).resolve().parent.parent
MODEL_DEFAULT = "models/gemini-3-pro-image"


def load_env_file(path: Path) -> None:
    """Lädt KEY=VALUE-Zeilen aus einer .env-Datei in os.environ, falls noch nicht gesetzt."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


# Bildstil je Variante, wird in jeden Prompt eingesetzt. Gedacht als kurze, konkrete Bildregie
# statt vagem "professionelles Foto" -- siehe content-plan.md Bildkonzept für die Herleitung.
STYLE_BRIEFS = {
    "corporate": (
        "Photoreal, natural daylight, clean and slightly cool white balance with a subtle teal "
        "undertone in shadows (brand color #0b7d76). Orderly, architectural composition with "
        "generous negative space, shot at eye level or slightly elevated, no fisheye/wide-angle "
        "distortion. Looks like a full-frame DSLR photo shot with a 50-85mm lens, natural shallow "
        "depth of field, realistic photographic contrast (not HDR, not over-sharpened). Avoid: "
        "illustration/3D-render look, oversaturated colors, perfect symmetry, plastic/waxy "
        "surfaces, warped architectural lines, lens flares, staged stock-photo smiles."
    ),
    "premium": (
        "Photoreal, cinematic editorial photography with moody, dramatic directional light "
        "(late-afternoon or dusk quality), rich deep shadows with warm highlights -- deliberate "
        "chiaroscuro, not flat daylight. Slightly warm-to-neutral color temperature with a deep "
        "teal-black undertone in the shadows (matches near-black background #14201f). Generous "
        "negative space for text overlay, eye-level shot, shallow depth of field, looks like a "
        "full-frame camera with a fast 35-50mm prime lens. Avoid: bright flat daylight snapshot "
        "look, illustration/3D-render look, oversaturated colors, harsh midday shadows, plastic "
        "surfaces, cheap stock-photo brightness."
    ),
    "modern": (
        "Photoreal, bright and friendly lifestyle/brand photography. Soft even natural daylight, "
        "warm and slightly golden white balance (matches warm off-white background #fffdf8), "
        "vivid but tasteful color saturation (not neon), cheerful and approachable mood, clean "
        "uncluttered background, gentle natural shadows, natural bokeh as on a modern mirrorless "
        "camera. Avoid: dark/moody tones, harsh contrast, cold blue color cast, clinical/sterile "
        "look, oversaturated neon colors, illustration/3D-render look."
    ),
    "referenz": (
        "A single continuous photograph (not a collage, grid, triptych or multi-panel composite). "
        "Photoreal, bright and clean documentary-style corporate photography, closely modeled on "
        "straightforward trade/facility-service stock photography. Neutral-to-cool natural "
        "daylight, crisp clarity, matter-of-fact eye-level framing that favors a close-up on one "
        "hand, tool or surface over a wide establishing shot. Minimal styling, realistic textures, "
        "natural photographic contrast (not HDR, not over-sharpened), looks like a single frame "
        "shot on a modern mirrorless camera with a 35-50mm lens, shallow depth of field. Avoid: "
        "collage/grid/multi-image composites, split-frame layouts, illustration/3D-render look, "
        "oversaturated colors, moody/dark cinematic lighting, staged stock-photo smiles, lens "
        "flares, dreamy soft-focus blur, any visible text/lettering/logos/signage, and any "
        "recognizable real building or landmark -- use a plausible generic, fictional building "
        "instead."
    ),
}

# variant -> motif -> (prompt_template, aspect_ratio)
# aspect_ratio: "1:1" | "2:3" | "3:2" | "3:4" | "4:3" | "9:16" | "16:9" | "21:9"
# Hinweis: person_generation wird von der Gemini Developer API (im Gegensatz zur Enterprise-API)
# nicht unterstützt -- "keine Personen im Bild" steht deshalb explizit im Prompt-Text.
#
# Nur Motive, die die jeweilige Variante tatsächlich als <img> einbindet, sind hier hinterlegt.
# corporate zeigt die 5 Leistungen nur als Emoji-Icons (kein bau/garten/winterdienst/reinigung/
# hausmeister-Foto im Markup) -- braucht also nur "gebaeude". premium/modern nutzen dagegen alle
# 7 Motive als Foto und werden hier ergänzt, sobald der Corporate-Pilot freigegeben ist.
CATEGORY_MOTIFS = {
    "bau": (
        "Close-up of a modern professional construction/renovation site run by a certified "
        "trade company: contemporary cordless power tools (drill, impact driver) and clean "
        "modern equipment resting loose on a new plywood surface, neatly stacked fresh "
        "lumber and drywall panels, against a modern building facade under renovation. "
        "The tools and equipment look new, high-quality and well-maintained -- not "
        "vintage, rusty, or antique. No people in frame. {style}",
        "3:2",
    ),
    "garten": (
        "A well-maintained commercial property garden and grounds, trimmed hedges, clean "
        "paved pathways, healthy greenery, no people in frame. {style}",
        "3:2",
    ),
    "winterdienst": (
        "A cleared, snow-free walkway in front of a commercial building after professional "
        "winter snow removal, fresh snow still visible at the edges, no people in frame. "
        "{style}",
        "3:2",
    ),
    "reinigung": (
        "Extreme close-up of a streak-free, freshly cleaned glass facade window reflecting "
        "daylight and sky, visible cleanliness and clarity, no people in frame. {style}",
        "3:2",
    ),
}

# variant -> motif -> (prompt_template, aspect_ratio)
# Nur Motive, die die jeweilige Variante tatsächlich als <img> einbindet, sind hier hinterlegt.
# corporate zeigt die 5 Leistungen nur als Emoji-Icons -> braucht nur "gebaeude".
# premium nutzt alle 7 Motive als Foto (inkl. Hero "gebaeude"), modern nutzt 6 (kein Hero-Foto,
# das Modern-Hero hat nur ein Formular). hausmeister/handshake sind Personen-Motive und laufen
# über Higgsfield (siehe content-plan.md), deshalb nicht in diesem Google-Skript.
# Zusätzliche Motive nur für die Rezensionen-Karussell-Karten auf premium/index.html.
# Jeder Prompt endet auf einen expliziten "Unebenheiten"-Zusatz (siehe Nutzer-Feedback: generierte
# Bilder sollen nicht zu perfekt/glatt wirken), zusätzlich zum gemeinsamen STYLE_BRIEFS-Text.
REVIEW_MOTIFS = {
    "rez-reinigung-praxis": (
        "A professional cleaning cart with spray bottles and folded microfiber cloths in a "
        "bright modern medical practice corridor, glossy just-mopped floor with faint uneven "
        "wet streaks catching the light, one cloth slightly crumpled, no people in frame. "
        "{style} Keep the honest imperfections of one real handheld photo: a little glare, "
        "an off-centre framing, a visible cable -- must not look airbrushed or rendered. No "
        "legible text, logos or signage anywhere in frame.",
        "3:2",
    ),
    "rez-reinigung-wohnung": (
        "A tidy, freshly cleaned private living room, warm low-angle afternoon light through "
        "a window, a folded microfiber cloth and spray bottle left on a side table, a cushion "
        "slightly out of place, no people in frame. {style} Keep it looking like one real "
        "handheld photo: soft uneven window light, a faint dust mote in the sunbeam, an "
        "imperfect off-centre framing -- avoid a sterile, digitally perfect look. No legible "
        "text, logos or signage anywhere in frame.",
        "3:2",
    ),
    "rez-garten-privat": (
        "A newly finished private garden at golden hour: fresh lawn with faint uneven mowing "
        "stripes, a young trimmed hedge, a new stone terrace with simple outdoor furniture, a "
        "garden hose loosely coiled at the edge, no people in frame. {style} Keep believable "
        "real-world imperfections: one plant pot not perfectly aligned, long natural shadows, "
        "slightly imperfect framing -- must look like an honest photo, not a rendered scene. "
        "No legible text, logos or signage anywhere in frame.",
        "3:2",
    ),
    "rez-garten-gewerbe": (
        "The shared courtyard grounds of a multi-unit residential building, trimmed hedges and "
        "healthy lawn along a paved path, a few fallen leaves not yet swept, a coiled hose near "
        "a maintenance shed, no people in frame. {style} Keep natural documentary imperfections: "
        "uneven late-day light, a slightly cluttered utility corner, asymmetric framing -- "
        "avoid a too-perfect staged look. No legible text, logos or signage anywhere in frame.",
        "3:2",
    ),
    "rez-winterdienst-parkplatz": (
        "A commercial customer parking lot at pre-dawn blue hour, cleared of snow with visible "
        "tire tracks and grit scattered on the asphalt, low snow piles pushed to the edges, "
        "faint streetlamp glow, no people in frame. {style} Keep real-photo imperfections: "
        "uneven grit scatter, a slightly crooked snow pile, soft cold-air haze, natural grain "
        "-- must not look digitally perfect or rendered. No legible text, logos or signage "
        "anywhere in frame.",
        "3:2",
    ),
    "rez-bau-treppenhaus": (
        "A stairwell mid-renovation in a residential building: fresh paint on one wall still "
        "slightly uneven at the edge, protective cardboard taped loosely over stair treads, a "
        "folded ladder and a bucket with a brush resting on it, masking tape peeling slightly "
        "at one corner, no people in frame. {style} Keep honest imperfections of one real "
        "photo: uneven work light, visible dust on the floor, off-centre composition -- avoid "
        "a sterile CGI-clean look. No legible text, logos or signage anywhere in frame.",
        "3:2",
    ),
    "rez-gebaeude-wohnanlage": (
        "A large modern residential apartment complex exterior at dusk, several balconies with "
        "a few lived-in details like a bicycle or a plant, warm window lights switching on one "
        "by one, well-kept entrance area, no people in frame. {style} Keep real-photograph "
        "imperfections: slightly uneven window lighting, one balcony less tidy than the others, "
        "natural atmospheric haze, imperfect asymmetric framing. No legible text, logos or "
        "signage anywhere in frame.",
        "16:9",
    ),
}

PROMPTS = {
    "corporate": {
        "gebaeude": (
            "A modern commercial office/mixed-use building exterior in Frankfurt am Main, "
            "Germany, daytime, well-maintained facade, clean architecture, no people in frame. "
            "{style}",
            "3:4",
        ),
    },
    "premium": {
        "gebaeude": (
            "A striking modern commercial building exterior in Frankfurt am Main, Germany, "
            "photographed at dusk with architectural lighting, well-maintained facade, no "
            "people in frame. {style}",
            "16:9",
        ),
        **CATEGORY_MOTIFS,
        **REVIEW_MOTIFS,
    },
    "modern": {
        motif: prompt for motif, prompt in CATEGORY_MOTIFS.items()
    },
    "referenz": {
        "gebaeude": (
            "A modern commercial office/mixed-use building exterior in Frankfurt am Main, "
            "Germany, daytime, well-maintained facade, clean architecture, no people in frame. "
            "{style}",
            "16:9",
        ),
        **{motif: (prompt, "4:3") for motif, (prompt, _ar) in CATEGORY_MOTIFS.items()},
    },
}


def build_client() -> genai.Client:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("GOOGLE_API_KEY ist nicht gesetzt (siehe .env im Projekt-Root).")
    return genai.Client(api_key=api_key)


def generate(client: genai.Client, variant: str, motif: str, model: str, n: int, image_size: str) -> None:
    if variant not in PROMPTS or motif not in PROMPTS[variant]:
        sys.exit(f"Kein Prompt für Variante={variant!r} Motiv={motif!r} definiert.")
    prompt_template, aspect_ratio = PROMPTS[variant][motif]
    prompt = prompt_template.format(style=STYLE_BRIEFS[variant])

    out_dir = ROOT / variant / "assets" / "_generated"
    out_dir.mkdir(parents=True, exist_ok=True)

    for i in range(1, n + 1):
        resp = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["Image"],
                image_config=types.ImageConfig(
                    aspect_ratio=aspect_ratio,
                    image_size=image_size,
                ),
            ),
        )
        saved = False
        for cand in resp.candidates:
            for part in cand.content.parts:
                inline = getattr(part, "inline_data", None)
                if inline:
                    ext = "png" if "png" in inline.mime_type else "jpg"
                    out_path = out_dir / f"{motif}_{i}.{ext}"
                    out_path.write_bytes(inline.data)
                    print(f"gespeichert: {out_path.relative_to(ROOT)}")
                    saved = True
        if not saved:
            print(f"Kein Bild erhalten für {motif} (Versuch {i}).")


def main() -> None:
    load_env_file(ROOT / ".env")
    parser = argparse.ArgumentParser(description="Bilder für BRU-Homepage-Varianten generieren.")
    parser.add_argument("--variant", required=True, choices=sorted(PROMPTS.keys()))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--motif", choices=sorted({m for v in PROMPTS.values() for m in v}))
    group.add_argument("--all", action="store_true", help="alle Motive der Variante erzeugen")
    parser.add_argument("--n", type=int, default=1, help="Anzahl Varianten pro Motiv")
    parser.add_argument("--model", default=MODEL_DEFAULT)
    parser.add_argument("--image-size", default="2K", choices=["1K", "2K", "4K"])
    args = parser.parse_args()

    client = build_client()
    motifs = list(PROMPTS[args.variant].keys()) if args.all else [args.motif]
    for motif in motifs:
        generate(client, args.variant, motif, args.model, args.n, args.image_size)


if __name__ == "__main__":
    main()
