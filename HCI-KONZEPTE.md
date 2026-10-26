# HCI-Konzepte aus der Vorlesung – Bezug zur Growbox

> - **Typ:** Projektdoku
> - **Zuständigkeit:** Konzepte aus den Vorlesungsfolien (Prof. Zagel, HCI WS26 + Thementeil Gamification) sammeln und je einer Anwendung an der Growbox zuordnen, als Grundlage für Interaktionskonzept, Prototyp und Booklet.
> - **Gilt bei:** Konzept-, Design- und Evaluationsentscheidungen zur Bedienung; Schreiben des Booklets.
> - **Ladebeziehungen:** Ausgangslage und Entscheidungen: `BRIEF.md`. Quellen: `~/Desktop/WS26_HCI - Vorlesungsfolien.pdf` (151 Folien), `~/Desktop/HCI - Vorlesungsfolien_Gamification.pdf` (17 Folien).
> - **Nicht zuständig:** Entscheidungen festhalten (→ `BRIEF.md`).

Status: **Vorschläge**. Was davon eingebaut wird, entscheidet das Team. Spalte „Folien“ = Seitenzahl im PDF (geprüft) zum Zurückverweisen.

## Prüfungsleistung (Folie 5)

- Option B: **Bedienoberfläche für eine „Growbox“**, 3er-Teams
- **Booklet** je 5 Seiten pro Person (50 %) + **Prototyp** (50 %)
- Bewertet: Bezug zu Theorien/Konzepten der Vorlesung, Beachtung der HCI-Grundprinzipien, Einbezug und Beschreibung verwendeter Technologien
- Folie nennt Präsentation 05.11. 10:00 und Abgabe 08.11. 23:59 (Jahr auf der Folie: 2025 → für 2026 bestätigen)

## 1. Wahrnehmung und Kognition

| Konzept | Folien | Anwendung an der Growbox |
|---|---|---|
| Model Human Processor (Card, Moran, Newell 1983): Wahrnehmen → Denken → Handeln | 16–17 | Jeder Bildschirm hat genau eine Hauptaussage („Alles gut“ / „Braucht Wasser“) und eine Hauptaktion. |
| Präattentive Wahrnehmung: Farbe **oder** Form allein wird sofort erkannt, Kombination nicht | 26–27 | Zustand auf einen Blick durch **eine** Dimension (Farbe des Hintergrunds/LED-Rings); Details erst beim Hinsehen. |
| Farbenblindheit (Rot-Grün, ca. 8 % der Männer) | 23 | Zustand nie nur über Rot/Grün: zusätzlich Symbol und Text (redundante Codierung). |
| Auditory Icons vs. Earcons | 31 | Alarm als Auditory Icon (z. B. Tropfgeräusch bei „zu trocken“), statt abstraktem Piepen, dessen Bedeutung man lernen muss. |
| Begrenztes Kurzzeitgedächtnis, recognize-act-Zyklus | 37–38 | Höchstens 3–4 Kacheln pro Bildschirm; nichts muss man sich merken. |
| Vergessen (Ebbinghaus), Kontext | 41–42 | Die Box wird nur alle paar Tage bedient → alles sichtbar, keine versteckten Gesten oder Menüs. |
| Kognitive Belastung (intrinsisch / extrinsisch / lernbezogen) | 45–47 | Extrinsische Last minimieren: keine Messwerte mit Nachkommastellen, sondern „passt / zu trocken“. |

## 2. Motorik und technischer Rahmen

| Konzept | Folien | Anwendung |
|---|---|---|
| Fitts' Law (Zeit hängt von Zielgröße und Abstand ab) | 50 | Große Touch-Kacheln, physischer Taster groß und am Gehäuserand; wichtig für ältere Nutzer und Kinder. |
| Steering Law (enge Pfade sind langsam/fehleranfällig) | 51 | Keine schmalen Schieberegler; lieber +/– Tasten oder feste Stufen. |
| Zeitliche Auflösung: < 100 ms direkt, < 1 s kausal, darüber andere Rückmeldung nötig | 64–65 | Tippen gibt sofort Rückmeldung. Weil Vernebler/Lüfter erst nach Minuten wirken, zeigt das Display „Feuchte steigt …“ als Fortschritt. |
| Sichtabstand / Auflösung | 63 | Schriftgröße für ca. 50–70 cm Abstand und 5″-Display auslegen. |

## 3. Mentale Modelle und Fehler

| Konzept | Folien | Anwendung |
|---|---|---|
| Mentale Modelle: Designer-, System-, Benutzermodell (Norman) | 56 | Metapher „Die Box ist ein Lebewesen, das Bedürfnisse zeigt“ statt „Gerät mit Relais“. |
| Flexibilität: mehrere Wege zum Ziel | 57–58 | Licht per Touch, per Taster **oder** per App schalten. |
| Gulf of Execution / Gulf of Evaluation | 59 | Ausführung: Aktion ist offensichtlich. Bewertung: Ergebnis sichtbar, denn die LED leuchtet durch das Plexiglas (natürliches Feedback). |
| Fehlerarten, besonders **Modusfehler** | 60 | Möglichst keine Modi; wenn „Automatik/Manuell“ nötig ist, Modus dauerhaft sichtbar anzeigen. |
| Murphys Law | 61 | Kritisches (z. B. Alarm aus) nur mit Bestätigung oder rückgängig machbar. |

## 4. UI-Grundregeln (Norman, Nielsen)

| Konzept | Folien | Anwendung |
|---|---|---|
| Affordances (Gibson 1979, Norman) | 72–73 | Taster sieht drückbar aus; Kacheln sehen wie Knöpfe aus, nicht wie Text. |
| Constraints: physisch, logisch, kulturell | 74–76 | Kulturell: Rot = Problem. Logisch: Nicht Mögliches ausgrauen. Physisch: Taster nur in einer Richtung drückbar. |
| Mappings (Herdplatten-Beispiel) | 77–79 | Anordnung auf dem Display entspricht der Box: Licht-Kachel oben (Lampe oben), Feuchte unten. |
| Konsistenz (syntaktisch, semantisch, terminologisch, innere, äußere) | 80–81 | **Äußere Konsistenz mit der App des Teammitglieds:** gleiche Symbole, Begriffe und Farben auf Display und App. |
| Feedback (visuell, akustisch, haptisch) | 82 | Jede Aktion: Kachel ändert sich + kurzer Ton; Taster klickt fühlbar. |
| Fehlertoleranz, aussagekräftige Fehlermeldungen (spezifisch, konstruktiv, höflich) | 83–85 | „Wassertank fast leer – bitte bis zur Markierung auffüllen“ statt „Fehler 3“. |
| Physikanalogie | 86–87 | Feuchte als Füllstand (Wasserglas), Licht als Sonnen-Symbol. |
| 10 Usability-Heuristiken (Nielsen) | 130 | Checkliste für Design **und** analytische Evaluation (siehe 7). |

## 5. Interaktionsstile und GUI-Muster

| Konzept | Folien | Anwendung |
|---|---|---|
| Direkte Manipulation (sichtbar, schnell, umkehrbar) | 96 | Grundstil des Displays. |
| Dialoge / Sprachassistenten | 91–94 | Optional als Ausblick (z. B. „Wie geht es meinen Pilzen?“); nicht im Kern. |
| **Model View Controller** | 99–100 | Ein Modell (Zustand der Box, auf dem Pi), zwei Views (Display, App). Das ist die Grundlage für die Synchronität und schlägt die Brücke zwischen HCI-Theorie und Technik. |
| Zoomable UIs (Übersicht → Detail) | 101–102 | Startbild: nur Zustand. Antippen zoomt in Details (Verlauf, Messwerte) für Interessierte. |

## 6. Vorgehen: User Centered Design

| Konzept | Folien | Anwendung |
|---|---|---|
| Double Diamond (Norman), UCD nach Dix/Benyon, HCD nach ISO 9241-210, Design Thinking | 104–107 | Rahmen für die Gliederung des Booklets: Verstehen → Konzept → Prototyp → Evaluation. |
| UX: vor / während / nach der Nutzung; Usability vs. Freude | 108 | Auch das Erleben „nach der Nutzung“ einplanen (Erntemoment, Rückblick). |
| Anforderungen: Interviews, Fragebögen, Fokusgruppen, Beobachtung | 110–117 | Kurze Interviews mit 3–5 Personen verschiedenen Alters. |
| **Personas** | 118 | 3 Personas über Altersgruppen hinweg (z. B. Kind, Studentin, Senior). |
| Skizzen & Prototypen (Buxton); Auflösung vs. Detailgenauigkeit (Houde & Hill 1997); Papierprototyp; Wireframes | 119–125 | Prototyp-Strategie: Papier → Klick-Prototyp auf dem echten 5″-Display → Box. |

## 7. Evaluation

| Konzept | Folien | Anwendung |
|---|---|---|
| Formativ vs. summativ (Scriven 1967) | 126 | Formativ: Papierprototyp testen und ändern. Summativ: Endstand messen. |
| Qualitativ/quantitativ, analytisch/empirisch (Axt-Beispiel) | 127–128 | Beides: Heuristik-Check (analytisch) + Nutzertest (empirisch). |
| Cognitive Walkthrough (Folie: „Analytische Methoden“, 3 Fragen: klar? erkennbar? Rückmeldung?) | 129 | Für 3 Kernaufgaben: Licht an, Alarm verstehen und quittieren, Zustand ablesen. |
| Probanden: Alter, Vorkenntnisse, Sehkraft … | 133 | Tester bewusst über Altersgruppen streuen, denn das ist eure Kernanforderung. |
| Feld- vs. Laborstudie | 136 | Kurzer Labortest an der Uni reicht. |
| **AttrakDiff** (pragmatische vs. hedonische Qualität), PANAS | 141–142 | AttrakDiff-Kurzform als Fragebogen nach dem Test. |

## 8. Experience Design

| Konzept | Folien | Anwendung |
|---|---|---|
| Maslow; Sheldon: Autonomie, **Kompetenz**, **Verbundenheit**, Stimulation … | 138, 140 | Kompetenz: „Ich halte meine Pilze am Leben“. Verbundenheit: Ernte in der App teilen. |
| Hassenzahl: Warum (Motive) → Was (Handlungsziele) → Wie (motorische Ziele) | 139 | Booklet-Argument: nicht nur „Wie schalte ich Licht“, sondern „Warum: etwas wachsen sehen“. |
| Storyboard, Mockups, Prototyp in Aktion (CliqueTrip-Beispiel) | 143–150 | Ein Storyboard „Ein Tag mit der Growbox“ ins Booklet und in die Präsentation. |

## 9. Gamification (Thementeil)

| Konzept | Folie | Anwendung |
|---|---|---|
| Gamification = Spieldesign-Elemente in Nicht-Spiel-Kontexten (Deterding et al. 2011); Spiel nach Huizinga, Suits, Wittgenstein | 4–7 | Definition und Abgrenzung im Booklet. |
| McGonigal: Blissful Productivity, Urgent Optimism, Social Fabric, Epic Meaning | 8–10 | „Epic Meaning“: aus Abfall/Substrat wird Essen. |
| Gamification Mechanics, z. B. Progression, Achievements, Appointments, Countdown, Levels | 10 | **Progression:** Wachstumsfortschritt bis zur Ernte. **Appointments:** täglicher kurzer Check. **Achievement:** erste Ernte. |
| **Flow** (Csikszentmihalyi): klare Ziele, Balance von Anforderung und Können, sofortiges Feedback | 12 | Die drei Voraussetzungen sind zugleich Designregeln für das Display. |
| Bartle Player Types; **Marczewski User Types (Hexad)** | 13–14 | Vor allem Achiever (Fortschritt) und Socialiser (teilen) ansprechen; Hexad in Personas einbauen. |
| Serious Games: Characterizing Goal, Balance Lernen ↔ Spiel | 15–17 | Ernstes Ziel (Pilze erfolgreich züchten) bleibt vorn, Spielelemente unterstützen nur. |

## Stärkste Hebel für Konzept und Bewertung

1. **Lebewesen-Metapher** (mentales Modell) + präattentiver Zustand + Progression (Gamification) → ein Konzept, das viele Theorien zugleich belegt.
2. **Mehrere Wege** (Touch, Taster, App) über **ein gemeinsames Modell (MVC)** → HCI-Prinzip und Technik in einem.
3. **Alle Altersgruppen**: Fitts, redundante Codierung, keine Modi, Recognition statt Recall, Personas und Tester über Altersgruppen.
4. **Evaluation**: Nielsen-Heuristiken + Cognitive Walkthrough (analytisch) + kurzer Nutzertest mit AttrakDiff (empirisch).
