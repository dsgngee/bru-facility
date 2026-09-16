# Content-Plan: BRU GmbH Website

## Kontext

Der Nutzer ist UX/UI-Designer und erstellt im Auftrag der BRU GmbH (Facility Service Frankfurt: Bau, Reinigung, Umfeldbetreuung) eine neue Website. Als Grundlage dienen die Referenzseite [facilityup.de](https://facilityup.de/) (strukturelle Orientierung) und ein bestehender Unternehmensflyer (Leistungs- und USP-Content). Dieser Content-Plan ist die Grundlage für die Designarbeit (mehrere Entwürfe in unterschiedlichen Stilen zur Auswahl für den Kunden).

Die Analyse ergab: BRU bietet mit ca. 58 Einzelleistungen in 5 Hauptkategorien deutlich mehr als facilityup.de (6 Kategorien, alles auf einer Seite). Außerdem widerspricht sich der Flyer beim Einsatzgebiet ("deutschlandweit im Einsatz" vs. "Frankfurt am Main und Umgebung"). Diese und weitere offene Punkte wurden über ein strukturiertes Discovery-Interview mit dem Nutzer geklärt.

## Entscheidungen aus dem Discovery-Interview

| Thema | Entscheidung |
|---|---|
| Hauptziel der Website | Leads generieren **und** Vertrauen schaffen (Website auch als Prüfinstrument für Bestandskontakte) |
| Zielgruppen-Priorität | Gleichgewichtig – Privathaushalte und Gewerbe gleich sichtbar |
| Einsatzgebiet | Rhein-Main als Kern, deutschlandweit auf Anfrage |
| Ausgangslage | Komplett neuer Webauftritt (keine bestehende Seite) |
| Leistungstiefe | 5 Kategorie-Seiten, Einzelleistungen als Listen (keine 58 Einzelseiten) |
| 24h-Notdienst | Sehr prominent (Sticky-Element + eigene Sektion) |
| Zusatzseiten ggü. Referenz | Keine – Struktur von facilityup.de reicht |
| Sprache | Nur Deutsch |
| Content-Assets | Noch keine Fotos vorhanden – werden später KI-generiert |
| Trust-Signale | Nur allgemein erwähnen (keine Detail-Nachweise/Zertifikate) |
| Kontaktformular | Erweitert: Dropdown "Welche Leistung?" + Datei-Upload |
| Tonalität | Premium/hochwertig positioniert |

**Zwei Besucher-Intentionen:** Die Seite muss zwei unterschiedliche Absichten bedienen – (1) neue Interessenten, die gezielt eine Leistung anfragen wollen, und (2) Personen, die BRU bereits kennen und die Website zur Vertrauensprüfung nutzen (Seriosität, Substanz, Professionalität checken, bevor sie beauftragen oder empfehlen). Konsequenz: klare CTAs für Pfad 1, aber genauso wichtig sind glaubwürdige, greifbare Signale (Team, Erfahrung, Arbeitsweise, echte Präsenz statt reiner Marketing-Sprache) für Pfad 2 – besonders auf "Über uns".

## Strategische Grundlagen

**Tonalität:** Durchgehend Sie-Form. Gehobener, hochwertiger Wortschatz (z. B. "Exzellenz", "Sorgfalt", "Werterhalt", "maßgeschneidert" – Anschluss an Flyer-Formulierungen wie "derselben Sorgfalt für ein Ergebnis, das überzeugt"), aber nicht steif – der persönliche Charakter aus dem Flyer ("Ihr verlässlicher Partner", "fester Ansprechpartner") bleibt erhalten. Kürzere Sätze wie bei facilityup.de werden vermieden zugunsten einer etwas wertigeren Sprache. Keine leeren Superlative.

**Differenzierung gegenüber facilityup.de:**

| Aspekt | facilityup.de | BRU GmbH |
|---|---|---|
| Leistungsbreite | 6 Kategorien, kompakt | 5 Kategorien, ~58 Einzelleistungen, gruppiert dargestellt |
| Notdienst | Nicht vorhanden | Prominentes Alleinstellungsmerkmal |
| Tonalität | Sachlich-professionell | Premium, persönlich |
| Trust-Elemente | Keine (keine Zertifikate/Bewertungen) | Allgemeine Erwähnung von Qualifikation, ausbaufähig |
| Formular | 5 einfache Felder | + Leistungs-Dropdown, Datei-Upload |
| Erfahrung | "über 5 Jahre" | "über 10 Jahre" |
| Direktkontakt | Kein Chat-Kanal | Sticky WhatsApp-Button auf jeder Seite |

## Terminologie-Klärung: "Umfeldbetreuung"

Der Flyer nennt als dritte Säule neben "Bau" und "Reinigung" den Begriff "Umfeldbetreuung" – kein etablierter deutscher Fachbegriff. Wahrscheinlichste Bedeutung: Sammelbegriff für die Betreuung des unmittelbaren Gebäude-Umfelds, also Garten-/Außenanlagenpflege, Winterdienst und Hausmeisterservice zusammen. **Nicht identisch mit "Facility Management"** (das ist der etablierte Oberbegriff für das gesamte Gebäudemanagement inkl. Reinigung/Technik – im Flyer bereits als Markenzeile "FACILITY SERVICE" genutzt). Da die Eigentümer nicht muttersprachlich Deutsch sprechen, ist eine ungenaue Eigenprägung wahrscheinlich – **muss beim Kunden verifiziert werden** (siehe "Offene Punkte"). Konsequenz für diesen Plan: Die Navigation verwendet bewusst klar verständliche Kategorienamen (Garten & Außenanlagen, Winterdienst, Hausmeisterservice) statt "Umfeldbetreuung". Möchte der Kunde den Begriff dennoch als Marken-Tagline behalten (wie im Flyer "Bau · Reinigung · Umfeldbetreuung"), kann er als Subline unter dem Logo ergänzt werden, unabhängig von der Navigations-Benennung.

## Globale Elemente (auf allen Seiten)

- **Header/Navigation:** Logo, Nav (Start · Über uns · Leistungen mit Dropdown der 5 Kategorien · Kontakt), Telefonnummer sichtbar
- **Sticky WhatsApp-Button:** fixiert (z. B. unten rechts), auf jeder Seite sichtbar, verlinkt auf WhatsApp-Chat (`wa.me`-Link) – schnellster Kontaktweg neben Anruf
- **Sticky Notdienst-Hinweis:** Badge/Button im Header "24h-Notdienst" mit Telefonnummer
- **Footer:** Kontakt (Telefon, E-Mail, WhatsApp, Adresse), Leistungs-Links, Impressum, Datenschutz

## Sitemap

```
/                              Startseite
/ueber-uns/                    Über uns
/leistungen/                   Leistungen – Übersicht
  /leistungen/gebaeudereinigung/
  /leistungen/bau-renovierung-sanierung/
  /leistungen/garten-aussenanlagen/
  /leistungen/winterdienst/
  /leistungen/hausmeisterservice/
/kontakt/                      Kontakt (inkl. Anfrageformular)
/impressum/
/datenschutz/
```

## Seiten im Detail

### 1. Startseite

1. **Header:** siehe "Globale Elemente"
2. **Hero:** Premium-Headline (z. B. "Ihr Rundum-Partner für Bau, Reinigung und Umfeldbetreuung in Frankfurt am Main"), Subline mit Kernversprechen, Primär-CTA "Kostenlose Beratung anfragen", Telefon als Sekundär-CTA, kurze Trust-Zeile (10+ Jahre Erfahrung · Zertifiziertes Fachpersonal · 24h-Notdienst)
3. **Kurzvorstellung "Wer wir sind":** 2–3 Sätze, Verweis auf /ueber-uns/
4. **USP-Block** (4–6 Karten, aus Flyer): über 10 Jahre Erfahrung; Privathaushalte & Gewerbe; zertifiziertes Fachpersonal; kurze Reaktionszeiten; 24h-Notdienst (hervorgehoben); fester Ansprechpartner
5. **Leistungsübersicht:** 5 Kacheln (Bild, Titel, Kurztext, "Mehr erfahren" → jeweilige Kategorie-Seite)
6. **24h-Notdienst-Sektion:** eigener Akzent-Bereich, große Telefonnummer, kurzer Text zu dringenden Fällen
7. **"Wie wir arbeiten" (3 Schritte):** Kontaktaufnahme → individuelle Analyse & Angebot → Umsetzung mit festem Ansprechpartner
8. **"Warum BRU GmbH":** 4 Gründe + CTA
9. **Team-Teaser:** kurzer Verweis auf das Team als Vertrauensanker (Qualifikation, Erfahrung, echte Gesichter statt nur Text), Verweis auf /ueber-uns/
10. **FAQ** (5 Fragen, BRU-spezifisch): Welches Gebiet deckt ihr ab? Gibt es feste Verträge/Abos (z. B. Winterdienst, Gartenpflege)? Wie schnell seid ihr im Notfall vor Ort? Arbeitet ihr auch für Privathaushalte? Wie läuft eine Anfrage ab?
11. **Kontakt-CTA-Sektion** vor dem Footer
12. **Footer:** siehe "Globale Elemente"

### 2. Über uns

Zentrale Seite für Besucher, die BRU bereits kennen und die Website zur Vertrauensprüfung nutzen – Substanz und Glaubwürdigkeit stehen hier vor Marketing-Sprache.

- Intro im Flyer-Ton ("Ihr verlässlicher Partner")
- Firmengeschichte & Werte (10+ Jahre, Frankfurt am Main, kontinuierliche Weiterbildung)
- Team-Sektion (Bildbrief: professionelles Team-/Einsatzfoto, später KI-generiert)
- Arbeitsweise: individuelle Analyse, persönliche Beratung, maximale Flexibilität, enger Kontakt
- Qualifikations-Hinweis, allgemein gehalten ("zertifiziertes Fachpersonal", "kontinuierliche Weiterbildung" – ohne Einzelnachweise)
- CTA zu /kontakt/

### 3. Leistungen – Übersicht

- Intro
- 5 Kategorie-Kacheln (wie Startseite, etwas ausführlicher)
- CTA: "Ihre Leistung ist nicht dabei? Sprechen Sie uns an"

### 4–8. Leistungs-Kategorieseiten (gemeinsames Template)

Aufbau je Seite: Intro/Nutzenversprechen → Leistungsgruppen mit Einzelleistungen (als Listen/Karten, keine eigenen URLs) → kurzer "Warum BRU"-Absatz → ggf. Notdienst-/Rufbereitschaftshinweis → CTA "Unverbindliches Angebot anfragen" (verlinkt zu /kontakt/ mit vorausgewähltem Dropdown-Wert).

**Gebäudereinigung** (15 Einzelleistungen aus dem Flyer, gruppiert):
- Privat & Wohnen: Privathaushalte, Entrümpelung
- Gewerbe & Büro: Büros & Gewerbe, Treppenhäuser, Sanitäranlagen
- Spezialbereiche: Fitnessstudios, Praxen & Kliniken, Schulen & Kitas, Gastronomie & Hotellerie, Industriereinigung
- Spezialreinigung: Fensterreinigung, Fassadenreinigung, Teppich- & Polsterreinigung, Desinfektionsreinigung, Bauendreinigung

**Bau, Renovierung & Sanierung** (14 Einzelleistungen):
- Innenausbau: Trockenbau, Maler- & Tapezierarbeiten, Fliesen- & Bodenverlegung, Boden- & Parkettverlegung, Elektroinstallation
- Sanierung & Renovierung: Renovierung, Sanierung, Neubau-Unterstützung
- Montage & Technik: Küchenmontage, Klimaanlagenmontage, Türen- & Fenstermontage
- Rückbau & Gebäudehülle: Abbrucharbeiten, Dacharbeiten, Fassadenarbeiten

**Garten- & Außenanlagenpflege** (11 Einzelleistungen):
- Gestaltung & Anlage: Pflasterarbeiten, Kunstrasen, Neubepflanzung
- Regelmäßige Pflege: Rasenschnitt, Heckenschnitt, Baumschnitt, Bewässerung, Gartenpflege im Abo
- Entsorgung & Sonderpflege: Laubentsorgung, Teichpflege, Winterfest machen

**Winterdienst** (9 Einzelleistungen) – Rufbereitschaft/Notfall-Räumdienst hier mit Verweis auf 24h-Notdienst:
- Räumung & Streuung: Schneeräumung, Streudienst, Parkplatzräumung, Notfall-Räumdienst
- Planung & Organisation: Räum- & Streupläne, Saisonverträge, Rufbereitschaft
- Sicherheit & Nachweis: Dokumentation, Streugutlagerung

**Hausmeisterservice** (Gebäudeinstandhaltung & Hausmeisterservice, 9 Einzelleistungen) – Notfälle hier ebenfalls mit Verweis auf 24h-Notdienst:
- Regelmäßige Betreuung: Kontrollgänge, Technische Wartung, Anlagenprüfung
- Organisation & Koordination: Handwerker-Koordination, Mülltonnenmanagement, Zutrittsmanagement
- Ansprechpartner & Notfälle: Fester Ansprechpartner, Notfälle, Kleinreparaturen

### 9. Kontakt

- Intro
- 4 Kontaktblöcke: Telefon, E-Mail, WhatsApp, Adresse + hervorgehobene Notdienst-Nummer
- Formular (erweitert): Name, Telefon, E-Mail, Unternehmen (optional), Dropdown "Welche Leistung interessiert Sie?" (5 Kategorien + "Sonstiges/Notdienst"), Freitext "Ihr Anliegen", Datei-Upload (z. B. Fotos bei Schäden), Datenschutz-Checkbox
- Empfehlung über die Referenzseite hinaus: eingebundene Karte (Google Maps), da facilityup.de hier keine hat – sinnvolle Standard-UX-Ergänzung

### 10–11. Impressum & Datenschutz

Rechtlich vorgeschriebene Standardseiten. Inhalte müssen vom Kunden/rechtlich geprüft geliefert werden – im Content-Plan nur als Platzhalter-Seiten vorgesehen.

## Bildkonzept (kurz)

Da noch keine echten Fotos vorliegen und diese später KI-generiert werden, hier die Bildbriefs für die Designphase:
- Hero: modernes Gebäude/Frankfurt-Bezug kombiniert mit Handwerker/Team-Motiv
- USP-Icons: schlicht, zur Premium-Tonalität passend
- Team-Foto: professionell, einsatznah, nicht steril
- Je Kategorie-Seite: ein repräsentatives Motiv (z. B. Reinigung: streifenfreies Fenster; Garten: gepflegte Außenanlage; Winterdienst: geräumter Gehweg)

### Fotoersatz-Pipeline (Umsetzung) — abgeschlossen für alle vier Varianten

Die ursprünglichen Platzhalter (ein gemeinsamer, wiederverwendeter 7-Bilder-Pool ohne EXIF-Daten) wurden ersetzt durch ein Bildsystem mit eigenem Stil je Variante: Umgebungs-/Objekt-Motive automatisiert über Google AI Studio (`scripts/generate_images.py`, Modell `gemini-3-pro-image` alias "Nano Banana Pro"), Personen-Motive automatisiert über die Higgsfield-CLI (`higgsfield generate create gpt_image_2_5 …`). Kein gestelltes "Team-Foto" mit erkennbaren Gesichtern (Vertrauensrisiko bei fingierten Mitarbeitern) – stattdessen Personen nur anonymisiert gezeigt (Rückenansicht, Silhouette, Fokus auf die Tätigkeit statt aufs Gesicht, Hände-Detail).

Reihenfolge: zuerst `corporate` als Pilot (Gold-Standard-Loop), nach Freigabe auf `premium` und `modern` mit jeweils eigenem Style-Brief übertragen. Als vierte Variante kam `referenz` hinzu (siehe "Vierte Variante" unten), ebenfalls mit eigenem Style-Brief. Alle generierten Rohvarianten liegen zur Nachvollziehbarkeit in `<variante>/assets/_generated/` (per `.gitignore` ausgeschlossen); die finalen, komprimierten Bilder liegen direkt in `<variante>/assets/`.

**Motiv-Zuordnung je Variante** (nicht jede Variante nutzt jedes Motiv als Foto):
- `corporate`: nur `gebaeude` (Hero) + `handshake` (Beratung) – die 5 Leistungen sind dort Emoji-Icons, kein Foto je Kategorie.
- `premium`: alle 7 Motive (`gebaeude`, `bau`, `garten`, `winterdienst`, `reinigung`, `hausmeister`, `handshake`) – Hero + 5 Service-Rows + Galerie.
- `modern`: 6 Motive, **kein** `gebaeude` (das Modern-Hero hat nur ein Angebots-Formular, kein Bild) – `bau`, `garten`, `winterdienst`, `reinigung`, `hausmeister` als Service-Card-Bild, `handshake` in der Über-uns-Sektion.
- `referenz`: alle 7 Motive, wie `premium` – Hero, Über-uns-Collage, 5 Service-Karten, Ablauf-Schritte (farbig getönt) und "Warum"-Sektion teilen sich denselben Bildpool.

**Style-Brief Corporate** (abgeleitet aus `corporate/styles.css`: Teal `#0b7d76`, Orange-Akzent `#fb923c`, Off-White-Hintergrund, klare Sans-Serif-Typografie):
Photoreal, natürliches Tageslicht, klarer, leicht kühler Weißabgleich mit dezentem Teal-Unterton in Schatten. Aufgeräumte, architektonische Komposition mit viel Negativraum, Augenhöhe oder leicht erhöht, keine Weitwinkel-/Fisheye-Verzerrung. Wirkt wie mit einer Vollformat-DSLR bei 50–85mm aufgenommen, natürliche Tiefenschärfe, realistischer fotografischer Kontrast (kein HDR, nicht überschärft). Vermeiden: Illustrations-/3D-Render-Look, übersättigte Farben, perfekte Symmetrie, plastikhafte/wächserne Oberflächen, verzerrte Architekturlinien, Lens-Flares, gestellte Stockfoto-Lächeln.

**Style-Brief Premium** (abgeleitet aus `premium/styles.css`: fast schwarzer Hintergrund `#14201f`, cremefarbene Schrift `#f3f1ea`, Serifenschrift "Fraunces"):
Cinematic, editorial, dramatisches Streiflicht (späte Nachmittags-/Blaue-Stunde-Stimmung), tiefe Schatten mit warmen Lichtern (bewusstes Chiaroscuro statt Tageslicht-Schnappschuss). Leicht warme bis neutrale Farbtemperatur mit tiefem Blaugrün-Schwarz-Unterton in den Schatten. Viel Negativraum für Textüberlagerung, Augenhöhe, geringe Schärfentiefe, wirkt wie Vollformatkamera mit lichtstarkem 35–50mm-Objektiv. Vermeiden: helle Tageslicht-Schnappschuss-Optik, Illustrations-/3D-Render-Look, übersättigte Farben, harte Mittagsschatten, plastikhafte Oberflächen.

**Style-Brief Modern** (abgeleitet aus `modern/styles.css`: warmes Off-White `#fffdf8`, große Rundungen, Schrift "Plus Jakarta Sans", kräftige Orange-/Gelb-Akzente):
Photoreal, helle, freundliche Lifestyle-/Markenfotografie. Weiches, gleichmäßiges Tageslicht, warmer, leicht goldener Weißabgleich, lebendige aber geschmackvolle Farbsättigung (nicht neonhaft), fröhliche, zugängliche Stimmung, aufgeräumter Hintergrund, sanfte natürliche Schatten, natürliches Bokeh wie bei einer modernen spiegellosen Kamera. Vermeiden: dunkle/melancholische Töne, harter Kontrast, kalter Blaustich, klinischer/steriler Look, übersättigte Neonfarben, Illustrations-/3D-Render-Look.

Die exakten Prompts für alle automatisierten Google-Motive liegen in `scripts/generate_images.py` (`PROMPTS`), die Style-Briefs sind dort bereits als `STYLE_BRIEFS` je Variante hinterlegt.

**Higgsfield-Prompts (Personen-Motive, automatisiert über `higgsfield generate create gpt_image_2_5`):**
- *Handshake Corporate/Premium* (dunkel/editorial): "Close-up handshake between two people in business-casual attire in front of a modern glass office building at dusk, dramatic warm architectural lighting against deep teal-black shadows, cinematic editorial photography, faces out of focus or cropped out of frame so no specific person is identifiable, photoreal, no exaggerated smiles, no staged stock-photo look." – Format 3:2 (Premium) bzw. 4:3 (Corporate).
- *Handshake Modern* (hell/freundlich): "Close-up handshake between two people in casual-friendly attire outside a bright modern building on a sunny day, warm golden natural daylight, cheerful and approachable lifestyle photography, faces out of focus or cropped out of frame so no specific person is identifiable, photoreal, no staged stock-photo look." – Format 4:3.
- *Hausmeister Premium* (dunkel/editorial): "A facility maintenance worker in dark workwear, seen from behind or in profile with face not visible or out of focus, adjusting a light fixture in a modern commercial building corridor at dusk, dramatic warm architectural lighting against deep teal-black shadows, cinematic editorial photography, photoreal, no specific person identifiable." – Format 3:2.
- *Hausmeister Modern* (hell/freundlich): "A facility caretaker in friendly casual workwear, seen from behind or in profile with face not visible or out of focus, checking equipment in a bright modern building corridor, warm cheerful natural daylight, lifestyle photography, photoreal, no specific person identifiable." – Format 4:3.

Alle vier Prompts folgen der Anonymisierungs-Regel aus der Fotoersatz-Pipeline (kein Gesicht als eindeutig identifizierbare Einzelperson im Fokus – erreicht über Rückenansicht, Silhouette oder Bildausschnitt).

## SEO-Hinweise (kurz)

| Seite | Fokus-Thema |
|---|---|
| Startseite | Facility Service Frankfurt am Main |
| Gebäudereinigung | Gebäudereinigung Frankfurt / Rhein-Main |
| Bau, Renovierung & Sanierung | Renovierung & Sanierung Frankfurt |
| Garten & Außenanlagen | Gartenpflege Frankfurt / Rhein-Main |
| Winterdienst | Winterdienst Frankfurt / Rhein-Main |
| Hausmeisterservice | Hausmeisterservice Frankfurt |

Lokale Bezüge (Frankfurt am Main, Rhein-Main) konsequent in Title/H1 der jeweiligen Seite verwenden – auch wegen der Entscheidung "Rhein-Main als Kern".

## Offene Punkte für Rücksprache mit dem Kunden

1. Gibt es eine separate Notdienst-Rufnummer, oder gilt dieselbe Nummer (0156 650 251 66) für Notfälle?
2. Wie weit reicht "Rhein-Main als Kern" konkret (Umkreis in km oder Liste der Städte)? Wichtig für Homepage-Text und lokales SEO.
3. Öffnungszeiten des Büros (im Flyer nicht angegeben) – für Footer/Kontaktseite.
4. Existieren konkrete Nachweise (Handwerkskammer, Innung, Versicherung), die später zu einer eigenen Trust-Sektion ausgebaut werden könnten?
5. Gibt es ein Google-Unternehmensprofil / Bewertungen, die künftig eingebunden werden könnten?
6. Was genau ist mit "Umfeldbetreuung" gemeint (siehe Abschnitt "Terminologie-Klärung") – soll der Begriff auf der Seite überhaupt auftauchen (z. B. als Tagline) oder reichen die verständlichen Kategorienamen?
7. Ist die vorhandene Mobilnummer (0156 650 251 66) WhatsApp-Business-fähig, oder gibt es/braucht es eine eigene WhatsApp-Nummer für den Sticky-Button?
8. Da "Vertrauen schaffen" jetzt explizites Hauptziel ist: Sollen die bislang nur allgemein erwähnten Trust-Signale (Zertifikate, Mitgliedschaften, Versicherung, Bewertungen) doch stärker ausgebaut werden, sobald konkrete Nachweise vorliegen?

## Selbstprüfung / Qualitätscheck

**1. Aufgabenverständnis:** Erstellung eines Content-Plans (Seitenstruktur + Inhalte je Seite) für die BRU-Website auf Basis von Referenzseiten-Analyse (facilityup.de), Flyer-Content und Discovery-Interview – als Grundlage für spätere, separate Design-Entwürfe. Kein Design, kein Code in diesem Schritt. ✅ erfüllt.

**2. Vollständigkeit der Flyer-Leistungen:** Alle 5 Flyer-Kategorien mit allen 58 Einzelleistungen sind den 5 Kategorieseiten zugeordnet (15 + 14 + 11 + 9 + 9 = 58). Keine Leistung wurde weggelassen.

**3. Abgleich mit der Referenzseite** (facilityup.de-Elemente → BRU-Entsprechung):

| facilityup.de-Element | Im BRU-Plan | Abweichung & Grund |
|---|---|---|
| Hero + USP-Block | ✓ Startseite | Mehr USPs (6 statt 3), da mehr Substanz vorhanden |
| Leistungs-Kacheln | ✓ Startseite + Leistungen-Übersicht | 5 statt 6 Kategorien, dafür mit Unterseiten statt Ankern |
| 3-Schritte-Ablauf | ✓ Startseite | inhaltlich identisch übernommen |
| Warum-Block + FAQ | ✓ Startseite | FAQ-Fragen an BRU angepasst |
| Kontaktformular | ✓ Kontaktseite | erweitert um Dropdown + Upload (bewusste Abweichung) |
| Keine Trust-Elemente | Nur allgemein erwähnt | bewusste Kundenentscheidung, ausbaufähig |
| Keine Notdienst-Erwähnung | Prominente eigene Sektion | bewusste Differenzierung |

**4. Rückverfolgbarkeit der Interview-Entscheidungen:** Alle 12 im Interview abgefragten Punkte sind im Abschnitt "Entscheidungen aus dem Discovery-Interview" gelistet und an der jeweiligen Stelle im Plan umgesetzt (siehe Tabelle oben).

**5. Verbleibende Annahmen/Risiken:** Die acht offenen Punkte oben sind bewusst nicht selbst beantwortet, sondern als Klärungsbedarf markiert, um keine Fakten zu erfinden (z. B. Öffnungszeiten, genauer Einsatzradius, echte Zertifikate).

## Ausblick (nicht Teil des aktuellen Scopes)

WhatsApp-Bot für automatisierte Erstantworten/Terminanfragen – als mögliches Zusatzangebot für den Kunden zu einem späteren Zeitpunkt, unabhängig vom initialen Website-Launch.

## Vierte Variante: „Referenz“

Nach Sichtung der drei ursprünglichen Entwürfe (Corporate, Premium, Modern) hat der Kunde zusätzlich facilityup.de als gestalterisches Vorbild benannt – diesmal nicht nur strukturell (wie beim ursprünglichen content-plan), sondern explizit für das visuelle Design. Die vierte Variante `referenz` übernimmt daher bewusst die charakteristischen Bausteine von facilityup.de (Foto-Hero mit Checklist-Zeile, laufendes Marken-Ticker-Band, Über-uns-Fotocollage, Leistungs-Kacheln mit Icon-Kreis, dreistufiger Ablauf als farbige Bildkarten, diagonal geschnittenes CTA-Banner, Statistik-Leiste, Akkordeon-FAQ) sowie die Farbpalette (Petrol-Navy, Orange-Akzent, Blau-Akzent) und Typografie (Google Font „Kumbh Sans“) des Vorbilds.

Der Content bleibt identisch zu den anderen drei Varianten (gleiche USPs, alle 5 Leistungskategorien mit sämtlichen Einzelleistungen, gleiche FAQ, gleiches erweitertes Kontaktformular). Bewusste Verbesserungen gegenüber dem Vorbild: eigene 24h-Notdienst-Sektion samt Sticky-Button (im Original nicht vorhanden), Google-Maps-Alternative (OpenStreetMap-Einbettung) auf der Kontaktseite, ausklappbare Leistungs-Tags statt einer kurzen Liste (da BRU ca. 58 statt 6 Einzelleistungen hat), sowie Reduced-Motion-Rücksicht beim Ticker-Band.

## Nächste Schritte

Grundlage für mehrere Design-Entwürfe in unterschiedlichen visuellen Stilen, aus denen der Kunde wählen kann. Beim Start der Design-Session diese Datei (`content-plan.md`) als Grundlage referenzieren.
