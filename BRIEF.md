# Projekt-Brief: M-M Interaction

Maßgeblicher Stand des Projekts. Die Tabelle „Entscheidungen“ ist verbindlich; Überholtes wird ersetzt, ältere Varianten stehen in der Git-Historie.

## Ziel

Eine kleine Growbox für Pilze (Uni-Projekt HCI), die **am Gerät** über ein eingebautes iPhone und einen Taster und **aus der Ferne** über eine App bedient wird. Schwerpunkt ist die Mensch-Maschine-Interaktion.

## Zielbild

```
 Taster ──►┐                         ┌──► LED im Deckel
           ▼                         │
     Raspberry Pi (einziger Zustand, Web-Server) ··► später: Vernebler, Lüfter
           │ WLAN
     ┌─────┴───────────────┐
 iPhone 13 mini         App (Teammitglied)
 im Bedienfeld
```

Zeichnungen der Box: `02-box-bau/README.md` (Bilder) bzw. `02-box-bau/zeichnungen/index.html` (interaktiv).

## Offen

- **Aufstellort:** Wo und wie steht die Box (Zugang vorn und zum Tank, Abstand für Lüftung, keine Heizung/Sonne, Display-Blickwinkel)?
- **Hardware Heizung:** Heizmatte oder PTC-Heizer über Relais (Einkauf) oder nur simuliert.
- **Cognitive Walkthrough** (Folie 129) mit einer älteren Person: optional bis zur Abgabe, sonst als Grenze im Booklet (S5).
- **Pilz als Status:** Das Pilz-Gesicht (froh/besorgt) gibt es; seit v7 wächst der Pilz in drei Stufen und zeigt „Erntebereit“. Ob er „alles gut“ noch deutlicher zeigen soll, ist offen.
- **Farben 3D-Druck:** Rahmen schwarz oder grau (Variante A oder B aus `02-box-bau/zeichnungen/skizze-farben.html`; C entfällt, weil Taster und Griffe jetzt beige sind); Sockel dunkelbraun ist nicht verfügbar.
- **Power-User-Persona (B):** Kultur bleibt Pilze, also ein erfahrener Pilzzüchter, der alles trackt. Entwurf in `04-final/entscheidungen-folien.md`; Name und Details offen.
- **Türschalter** (Magnetschalter, meldet „Tür offen“ ans Display): echt, simuliert oder weglassen?
- **LED-Elektronik (später):** Streifen sind **adressierbar, 5 V, 3 Kontakte, 10 mm breit**. Ansteuerung, Netzteil und Code folgen, wenn die Box steht; der Code steuert bisher eine einzelne LED.

## Feedback aus der Präsentation (05.11.)

- **Oranger Warnpunkt** (Standby: Display schwarz, nur der Punkt blinkt) kam gut an.
- Gelobt wurden der **Fortschritt vom Konzept bis zum Prototyp** und die **Bedienfeld-Entscheidungen mit Bezug auf die Fachbegriffe der Folien**. → Beides ist der Schwerpunkt von Felix' Booklet-Teil.
- Frage **„Warum Blau statt Schwarz?“** Antwort: Schwarz bedeutet Standby (Display aus, nur der Warnpunkt), Blau bedeutet „Box läuft“. Für schwache Augen gibt es Schwarz als Option **Hoher Kontrast** (E25, `01-konzept/folien-recherche.md`).

## Entscheidungen

Von Felix bestätigt. Diese Tabelle ist der maßgebliche Stand; Überholtes wird ersetzt.

| # | Thema | Entscheidung |
|---|---|---|
| 1 | Arbeitsmodus | **Shipping**: zügig eine nutzbare Box; Erklärungen kurz und entscheidungsorientiert. |
| 1 | Selbst bauen | **Felix (bzw. das Team) baut Hardware und Verkabelung selbst**, nach Anleitung des Agenten; die Software schreibt der Agent. |
| 1 | Autonomie | Innerhalb eines freigegebenen Schritts schreibt, testet und committet der Agent lokal selbst. **Rückfrage vor:** Push, neuen Dependencies, Architekturänderungen, Einkäufen. |
| 2 | Harness | **Schlank, ohne Agentic Harness** (am 2026-10-26 übernommen und wieder entfernt). Projektregeln: `AGENTS.md`; Entscheidungen: diese Datei; Vorlesungsbezug: `01-konzept/HCI-KONZEPTE.md`. |
| 3 | Team und Rollen | Uni-Projektgruppe aus **4 Personen** (bestätigt 2026-11-02; Folie 5 nennt 3er-Teams) → Booklet 4 × 5 = 20 Seiten. **Felix:** baut die Growbox physisch inklusive Bedienfeld (Mechatronik ist neu für ihn). **Die App baut ein anderes Teammitglied.** Unser Teil muss so laufen, dass Box, Display und App synchron sind. |
| 4 | Zweck | **Uni-Projekt mit Schwerpunkt Mensch-Maschine-Interaktion (HMI).** Die Bedienung am Gerät muss sehr einfach sein und möglichst alle Altersgruppen abdecken. Die Kultur ist zweitrangig. |
| 4 | Budget | **150–300 €** für die gesamte Hardware. |
| 4 | Termin | **Präsentation 05.11.2026, 10:00 (gehalten) · Abgabe 08.11.2026, 23:59**: Booklet 5 Seiten pro Person + Prototyp (Folie 5, von Felix bestätigt). |
| 3 | Name | **„M-M“ = Mensch-Maschine** → M-M Interaction = Mensch-Maschine-Interaktion (HMI). |
| 6 | Box | **Aufbau wie eine Mikrowelle, außen 335 × 250 × 200 mm:** links die Pilzkammer (250 breit) aus 3-mm-Plexi, rechts der blickdichte **Technikraum** (85 breit, volle Tiefe) mit Bedienfeld vorn. **Gestell aus dem 3D-Drucker** wie beim Creality K2 Plus: schwarze Profile 15 × 15 mit Eck- und T-Stücken, Scheiben in Nuten, senkrechtes Profil zwischen Tür und Bedienfeld; Sockel 30 mm dunkelbraun gedruckt; Deckel abnehmbar mit Griff. Alle Teile ≤ 250 mm für das 255er-Druckbett. **3D-Modelle** (`04-final/3d-modell/`) dienen nur zum Anschauen; dass ihre Maße abweichen, ist egal (2026-11-05). Zeichnungen: `02-box-bau/README.md`; ältere Fassungen bleiben als Dokumentation erhalten, neue Stände kommen als neue Dateien (z. B. `-v2`). |
| 6 | Tür und Griff | **Fronttür aus Plexi, Scharniere links**, langer **senkrechter Stangengriff** (wie IKEA) zwischen Tür und Bedienfeld. |
| 6 | Farbprinzip | **Bedienen vs. Gestalt farblich unterscheiden:** Teile zum Anfassen/Bedienen heben sich farblich vom Rahmen ab. Handybox (Bedienfeld-Front) fest **schwarz glänzend**; **Taster, Türgriff und Deckelgriff beige**, Taster mit eingeprägtem **Licht-Symbol** (2026-11-02). **Orange nur für Warnungen** (wie auf dem Display, Konsistenz Folie 80); LEDs warmweiß, in Zeichnungen hellgelb. Rahmen schwarz oder grau (Variante C mit beigem Rahmen entfällt). Skizze: `02-box-bau/zeichnungen/skizze-box-v3.html`. |
| 5 | Kultur | **Pilze** (z. B. ein fertig durchwachsenes Austernpilz-Zuchtset, damit innerhalb von 2 Wochen etwas sichtbar ist). |
| 6 | Lage der Elektronik | **Im Technikraum:** Pi und Kabel oben hinter dem Bedienfeld; Lüfter mit Schlitzen zur Pilzkammer. In der Pilzkammer nur LED und ggf. Sensor. |
| 6 | Wassertank (Variante A) | **Entschieden 2026-10-29:** Nachfüllen ist die Hauptaufgabe des Menschen, deshalb **Einfüllöffnung oben auf dem Technikraum, hinten rechts** (Wasser von oben eingießen wie bei einer Kaffeemaschine, Tank bleibt drin). Tank unten im Technikraum **hinter einer Trennwand**, getrennt von Pi und iPhone; Einfüllöffnung mit Abstand zum Display. **Sichtfenster mit Füllstandslinie** von außen (Mapping zur Display-Anzeige: Füllstandsbalken „Wassertank“ auf dem Startbild ↔ Füllstandslinie im Sichtfenster; Reichweite „reicht ca. X Tage“ im Klima-Fenster). Einfüllöffnung Ø ca. 4 cm mit Klappe. Tank unten vorn, Pi oben, dazwischen Trennwand (Wasser unten, Elektronik oben); Sichtfenster vorn unter dem Taster. Skizze: `02-box-bau/zeichnungen/skizze-box-v2.html`. Verworfen: B Schublade im Sockel (Sockel 30 → 70 mm), C Tank seitlich außen. |
| 7 | Bedienkonzept | **Touch-Display (iPhone) + ein physischer Taster** mit fester Bedeutung **Licht an/aus** (kein Modus; Ergebnis direkt durchs Plexiglas sichtbar). |
| 8 | Aktoren | **Licht: 4 LED-Streifen rundum im oberen Rahmen**, verdeckt im LED-Kanal der oberen Profile (Schürze außen, Blende innen); Deckel bleibt kabelfrei. Lüfter und Vernebler sind im Technikraum vorgesehen, aber nicht Teil des Prototyps. |
| 4 | **Schwerpunkt** | **Interaktionskonzept vor Technik.** HCI-Prüfungsleistung (Prof. Zagel), Option B: Booklet je 5 Seiten pro Person (50 %) + Prototyp (50 %), bewertet nach Bezug zu Vorlesungstheorien, HCI-Grundprinzipien und beschriebener Technik. Funktionen sind zweitrangig; die Uni hat fast alle Bauteile. Ein Prototyp darf auch Papier- oder Klick-Prototyp sein. |
| 7–8 | Hardware | **Raspberry Pi bleibt Steuerrechner; als Display dient ein fest eingebautes iPhone 13 mini** (statt Touch Display 2), das die Web-Oberfläche des Pi über WLAN zeigt; Dauerstrom per Kabel. **Echt:** Taster und LED. **Simuliert:** Feuchte und Temperatur (für die Vorführung umschaltbar). Lüfter, Vernebler und Sensor sind nicht Teil des Prototyps. |
| – | **Leitidee** | **B „Radikal einfach“:** ein großer Zustand (Farbe + Symbol + ein Satz), darunter drei große Kacheln. Verworfen: A „Pilz-Begleiter“ (Charakter, Gamification), C „Physisch zuerst“ (Taster/Drehknopf/LED-Ring). |
| 10 | Startbild | **Drei Zustände, immer Form + Farbe + Text:** „Alles gut“ (grüner Kreis mit Haken) · **Warnung** (gelbes Warndreieck, ISO 7010) · **„Erntebereit“** (beiger Kreis mit Pilz, 2026-11-04). Pilz wächst in drei Stufen mit kurzem Sprüh-Effekt. **Blinken nur beim Warnpunkt im Standby.** Details: `01-konzept/bedienfeld/README.md` → Spezifikation v7. |
| 10 | Bedienfeld (Box) | **Stand v7 (05.11.2026)**, Spezifikation mit Bild: `01-konzept/bedienfeld/README.md`; eingefroren: `04-final/bedienfeld-v7/`; Begründungen: `04-final/entscheidungen-folien.md` (E1–E31). Kern: <br>• **Display schlank, Erweitertes in der App** (1 Min lüften/befeuchten, Analytics) <br>• Kopfzeile 44 pt: Sorte · Warnpunkt · Handy · Zahnrad; keine Uhr <br>• Ring bis zur Ernte, drei einheitliche Werte, **3 Kacheln KLIMA · MELDUNGEN · SORTEN** <br>• **Rahmen = drückbar, Trennstrich = nur Text** <br>• KLIMA zeigt Automatik mit Bedingungen, **ohne Eingriff** <br>• Neu ansetzen: mitten im Wachstum 2 s halten, nach der Ernte nur „Sicher?“; „Kleine Pause“ möglich <br>• **Eigene Sorte** (2026-11-05): in der App jederzeit, an der Box **nur nach der Ernte**, Werte eingeklappt unter **Erweitert** <br>• Einstellungen: Handy · Urlaub · Sprache · Darstellung (Blau / Hoher Kontrast / Individuell) · Hilfe · Admin <br>• **Kein Ruhemodus**; **Standby** nur bei „Tank leer“ (schwarz, oranger Punkt blinkt) <br>• Admin-Modus: 2 Fälle (Tank leer · Pilze fertig mit 5-s-Zeitraffer) + Zurücksetzen; Start bei 15 Tagen <br>• Barrierefreiheit: Kontrast ≥ 4,5 : 1, Ziele ≥ 44 pt, Status nie nur Farbe <br>Ältere Stände: `01-konzept/bedienfeld/verlauf/`. |
| 9 | App-Aufbau | **Separate App:** einfache Startseite + 5 Unterseiten, eine davon **Advanced Analytics**. |
| – | Booklet und Präsentation | **Story mit zwei Personen** (2026-11-02): **A** Ingrid (nur Box) und **B** Power-User (App als Zusatz); **jede Entscheidung auf A oder B zurückführbar**, mit Folie: `04-final/entscheidungen-folien.md`. **Präsentation am 05.11. gehalten** (5 Min., ohne Folien: 3D-Entwurf → Bedienfeld Felix 2 Min. → App Anlin; Ablauf `04-final/praesentation.md`). **Booklet: 5 Seiten pro Person**; Felix: Box + Bedienfeld an Typ A (`04-final/booklet-felix.md`). **Schwerpunkt (2026-11-05):** Fortschritt vom Konzept über Box und Bedienfeld und die Entscheidungen mit Fachbegriffen der Folien. Grundlage **Bedienfeld v7** (`04-final/bedienfeld-v7/`), v6 als Vorher-Stand. Booklet-Inhalte in anderen Dateien sind mit **📘** markiert. **Gesamt-Booklet (2026-11-06):** ein gemeinsames Booklet **im Grünton** (Creme/Waldgrün/Salbei) mit den Seiten „Design & Bau“ des Kollegen: `04-final/booklet.html`; **19 Seiten (07.11.; 17 ohne Titel und Inhalt)**: 03–04 Einstieg (03 Zielgruppe vom Kollegen, 04 Anforderungen + Nutzungskontext) · **05–07 Konzept** = die Box (Konzeptweg V1→V3, Aufbau V3, Bedienteile) · **08–11 CAD & Bau** (Seiten des Kollegen, Stand 07.11. abends, unverändert eingebettet aus `04-final/booklet-design-bau/seiten/`, nur Seitennummern angepasst; S. 10 „Alle Features“ bleibt mit Schiebeschalter und Handsensor; S. 11 „Zwei Größen“ neu) · **12 Technik** · **13–19 Bedienfeld**: Konzept 13–15 (Entstehung I + II, Farbe) · Bedienung 16–18 (Startbild, Fall 1–3, Neu ansetzen) · Weggelassen & offen 19. Hintergründe der Kollegen-Seiten dürfen abweichen. Entscheidungstabellen auf S. 05, 07, 13, 14, 15, 19. Kamera fest, bewusst nicht beweglich (Abwägung S. 05). Ansicht „Übersicht 6×3“ mit Zoom. **Verweise (07.11.):** Fachbegriffe der Vorlesung als Überschriften und im Text nennen (z. B. Double Diamond, Persona, Hassenzahl Warum · Was · Wie, Nutzungskontext, Nutzermerkmale); Folien- und Seitennummern nur sparsam, weil der Professor mit den Nummern wenig anfangen konnte. Was in „Aus der Vorlesung“ steht, muss auf der Seite auch sichtbar vorkommen. Grundlage der Ergänzungen: Folie 5 (Theorie, HCI-Grundprinzipien, **Technologien**) und UCD-Prozess (Folie 105–112). |
| – | Begriffe Box ↔ App | Gleiche Wörter, Symbole und Farben in Box und App: `01-konzept/begriffe-box-app.md` (für das App-Teammitglied). |
| – | Priorität | **Interface und Interaktion vor Pi:** Pi-Software und Display-Code ruhen vorerst; das Repo-Display zeigt noch die alte Oberfläche. |
| – | Prototyp | **Papierprototyp → Klick-Prototyp auf dem eingebauten iPhone an der Box**, Messwerte simuliert und für die Vorführung umschaltbar. |
| 9 | App-Anbindung | **Live-Synchronität im Prototyp:** Der Pi hält den einzigen Zustand und bietet eine Schnittstelle (HTTP + Live-Updates) an; Display und App des Teammitglieds sind zwei Ansichten davon (MVC). |
| 11 | Display-Technik | **Web-Oberfläche vom Pi, im Vollbild auf dem iPhone** (Safari, gesperrt per Geführtem Zugriff); am Laptop ohne Hardware testbar. |
| – | Gamification | **Leicht, ohne Spielfigur:** Wachstumsbalken bis zur Ernte (Progression, Flow) und ein Ernte-Moment mit Teilen über die App (Achievement, Socialiser). Vorschlag aus den Konzept-Skizzen 10–11. |
| – | Konzept-Skizzen | Oberfläche: Blätter 01–14 mit Vorlesungsbezug, https://claude.ai/artifact/7MF2tG589SHFE4ghP35TE9 (privat). Die Blätter 15–18 dort (Box) sind überholt; maßgeblich für die Box ist `02-box-bau/`. |
| – | Architektur | **Freigegeben 2026-10-27:** Python + FastAPI auf dem Pi (HTTP + WebSocket), Web-Oberfläche ohne Framework, gpiozero für Taster/LED, simulierte Messwerte. Ordnerstruktur siehe nächste Zeile. |
| – | Ordnerstruktur | **Freigegeben 2026-10-28:** nach Projektschritten `01-konzept/`, `02-box-bau/`, `03-software/`, `04-final/` (2026-11-02 umbenannt von `04-evaluation/`: Präsentation, Booklet, Evaluation); `AGENTS.md` und `BRIEF.md` im Root. Software im `src`-Layout (`03-software/src/growbox/`: `core/` stabiler Kern ohne FastAPI/GPIO, `hardware/` echt oder simuliert hinter einer Schnittstelle, `simulation/`, `api/`, `web/`), Dependencies in `pyproject.toml`. Autostart auf dem Pi (`deploy/`) erst, wenn der Pi da ist. |
