# Booklet-Plan für das Treffen am 07.11.

Stand 06.11. abends. Grundlage: `booklet.html` (13 Seiten, Grünton), Notizen vom 06.11., Git-Historie von `BRIEF.md`.
Begriff: Im Booklet heißt eine Booklet-Seite **Seite**. „Folie“ meint nur die Vorlesungsfolien (z. B. „Folie 80 Konsistenz“).

## Abgleich Notizen ↔ Stand

| Punkt | Stand | Was fehlt |
|---|---|---|
| Grün für alles | ✅ entschieden (`BRIEF.md`), `booklet.html` | `booklet-felix.html` entfernt (06.11.), es gibt nur noch `booklet.html` |
| mindestens 15 Seiten | 13 | Titel, Inhalt, Konzeptweg, Szenario, 3. Abwägung |
| Inhaltsverzeichnis mit Strichen | Segmentleiste existiert in der schwarzen Fassung (`3fa3252`) | als Inhaltsseite und Leiste auf jeder Seite in Grün |
| Überschneidungen | offen | siehe unten |
| 3. Abwägungstabelle (Entscheidung · Grund (Folie) · Nachteil) | 2 Tabellen: Box (S. 09), Farbe (S. 11) | Bedienfeld, Stoff in `entscheidungen-folien.md` (E1–E31) |
| Konzeptweg V1 → V3 | nur Skizzenleiste v1 → v3 | eigene Seite, siehe unten |
| Bedienung im echten Szenario | Case 1/2 (S. 12) | Seite „Die erste Woche“ |

## Überschneidungen und Widersprüche

- **Mikrowelle doppelt:** S. 02 (Kollege) und S. 08 (Felix) beginnen gleich. S. 08 steigt künftig direkt mit V3 ein.
- **Drei Versionszählungen:** „17 Versionen“ = 3D-Modell, „v1–v7“ = Bedienfeld, „Skizze v1–v3“ = Box. Eine Benennung festlegen (Vorschlag: Box V1–V3, Bedienfeld v1–v7, 3D-Modell „Stand 1–17“).
- **Inhaltliche Widersprüche, morgen entscheiden:**

| Thema | Kollege (3D-Modell) | Felix (`BRIEF.md`) |
|---|---|---|
| Licht | Schiebeschalter | Taster (S. 09 baut darauf auf) |
| Display | Handsensor weckt es | immer an, Ruhemodus gestrichen |
| Tank | Schieber nach hinten | Einfüllöffnung oben + Sichtfenster vorn |
| Maße | 27,5 × 20 × 20 cm | 33,5 × 25 × 20 cm |
| Kamera | ja, hinten rechts | nicht entschieden |

## Konzeptweg der Box (Vorschlag)

```
V1  26.10.  Aquarium + Bedienteil       Plexi-Kasten ca. 20 cm; Pi + 5″-Touchdisplay
            (Idee, keine Zeichnung)      in eigenem Gehäuse daneben, per Kabel
               │ zwei Geräte, Kabel dazwischen, Display ohne festen Platz
               ▼
V2  27.10.  Mikrowelle kompakt           Kammer 20 × 20 × 20, Technikraum 7,5 cm,
            = Skizze + Druck Kollege     LED im Deckel, Sockel 5 cm, iPhone statt Display
               │ Druckbett, Kabel im Deckel, kein Platz für den Tank
               ▼
V3  27.10.–02.11.  Mikrowelle groß       33,5 × 25 × 20, Gestell aus Profilen, LED im Rahmen,
            = Skizzen von Felix          Tank mit Sichtfenster (29.10.), beige = anfassen (02.11.)
```

- Daten und Inhalte stammen aus `BRIEF.md` in Git (Commits `a967d02`, `d71565b`, `c9ddd6e`, `a70c69b`, `0c91b58`).
- Die Gründe für V1 → V2 (ein Gerät statt zwei, vertraute Form, Folie 8) sind hergeleitet und **noch zu bestätigen**.
- Für V1 gibt es keine Zeichnung, die Box-Blätter 15–18 der Konzept-Skizzen sind nicht mehr vorhanden. Entweder von Hand skizzieren oder im Stil der anderen Skizzen nachzeichnen, beschriftet als „nachgezeichnet“.
- Auf die Konzeptseite gehört auch der Oberflächen-Weg: Leitideen A/B/C → Wahl B.

## Seitenplan (17 Seiten)

| # | Seite | Quelle |
|---|---|---|
| 01 | Titel (gemeinsam) | neu |
| 02 | Inhalt mit Segmentleiste | neu |
| 03 | Für wen: Ingrid + Leitideen | S. 07 |
| 04 | Konzeptweg V1 → V3 + Abwägungstabelle | neu |
| 05 | V2: Alles begann mit einer Mikrowelle | Kollege S. 02 |
| 06 | Vom Papier ins CAD | Kollege S. 03 |
| 07 | Vom Rohdruck zum Prototyp | Kollege S. 04 |
| 08 | 3D-Modell: 17 Stände | Kollege S. 05 |
| 09 | Jedes Detail hat einen Zweck | Kollege S. 06 (nach den Entscheidungen anpassen) |
| 10 | V3 annotiert, ohne doppelte Mikrowelle | S. 08 |
| 11 | Ein Taster. Eine Bedeutung. (Abwägung 1) | S. 09 |
| 12 | Ein Blick. Startbild | S. 10 |
| 13 | Warum Blau statt Schwarz? (Abwägung 2) | S. 11 |
| 14 | Die erste Woche: auspacken → Sorte wählen → Tag 1 → nachfüllen → ernten | neu |
| 15 | Eine Warnung. Ein Knopf. | S. 12 |
| 16 | Die Hürde passt zum Risiko | S. 13 |
| 17 | Abwägungen Bedienfeld (Abwägung 3) | neu, aus E1–E31 |

Hinweis zu S. 14: Das Bedienfeld hat keine Ersteinrichtung, es startet direkt mit „Auster, 15 Tage“. Entweder zeigt das Szenario die vorhandenen Abläufe (SORTEN → Sorte → Starten, als Screenshots), oder es wird eine Ersteinrichtung als neue Funktion entschieden.

## Morgen zu klären

1. Taster oder Schiebeschalter? Display immer an oder Handsensor? (betrifft S. 09–13)
2. Gründe für V1 → V2 → V3 bestätigen; wer zeichnet V1?
3. Gibt es das erwähnte Video zur Ursprungsidee? Dann ein Standbild für S. 04.
4. Ersteinrichtung für S. 14: vorhandene Abläufe zeigen oder neu bauen?
5. Platzhalter des Kollegen füllen: Name, CAD-Programm, Druckzeit, Filament.
6. Einheitliche Benennung der Versionen (siehe oben).
