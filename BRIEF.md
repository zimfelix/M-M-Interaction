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

- **Türschalter** (Magnetschalter, meldet „Tür offen“ ans Display): echt, simuliert oder weglassen?
- **LED-Elektronik (später):** Streifen sind **adressierbar, 5 V, 3 Kontakte, 10 mm breit**. Ansteuerung, Netzteil und Code folgen, wenn die Box steht; der Code steuert bisher eine einzelne LED.

## Entscheidungen

Von Felix bestätigt. Diese Tabelle ist der maßgebliche Stand; Überholtes wird ersetzt.

| # | Thema | Entscheidung |
|---|---|---|
| 1 | Arbeitsmodus | **Shipping**: zügig eine nutzbare Box; Erklärungen kurz und entscheidungsorientiert. |
| 1 | Selbst bauen | **Felix (bzw. das Team) baut Hardware und Verkabelung selbst**, nach Anleitung des Agenten; die Software schreibt der Agent. |
| 1 | Autonomie | Innerhalb eines freigegebenen Schritts schreibt, testet und committet der Agent lokal selbst. **Rückfrage vor:** Push, neuen Dependencies, Architekturänderungen, Einkäufen. |
| 2 | Harness | **Schlank, ohne Agentic Harness** (am 2026-10-26 übernommen und wieder entfernt). Projektregeln: `AGENTS.md`; Entscheidungen: diese Datei; Vorlesungsbezug: `01-konzept/HCI-KONZEPTE.md`. |
| 3 | Team und Rollen | Uni-Projektgruppe. **Felix:** baut die Growbox physisch inklusive Bedienfeld (Mechatronik ist neu für ihn). **Die App baut ein anderes Teammitglied.** Unser Teil muss so laufen, dass Box, Display und App synchron sind. |
| 4 | Zweck | **Uni-Projekt mit Schwerpunkt Mensch-Maschine-Interaktion (HMI).** Die Bedienung am Gerät muss sehr einfach sein und möglichst alle Altersgruppen abdecken. Die Kultur ist zweitrangig. |
| 4 | Budget | **150–300 €** für die gesamte Hardware. |
| 4 | Termin | **Präsentation 05.11.2026, 10:00 · Abgabe 08.11.2026, 23:59** (Folie 5, von Felix bestätigt). |
| 3 | Name | **„M-M“ = Mensch-Maschine** → M-M Interaction = Mensch-Maschine-Interaktion (HMI). |
| 6 | Box | **Aufbau wie eine Mikrowelle, außen 335 × 250 × 200 mm:** links die Pilzkammer (250 breit) aus 3-mm-Plexi, rechts der blickdichte **Technikraum** (85 breit, volle Tiefe) mit Bedienfeld vorn. **Gestell aus dem 3D-Drucker** wie beim Creality K2 Plus: schwarze Profile 15 × 15 mit Eck- und T-Stücken, Scheiben in Nuten, senkrechtes Profil zwischen Tür und Bedienfeld; Sockel 30 mm dunkelbraun gedruckt; Deckel abnehmbar mit Griff. Alle Teile ≤ 250 mm für das 255er-Druckbett. Zeichnungen: `02-box-bau/README.md`; ältere Fassungen bleiben als Dokumentation erhalten, neue Stände kommen als neue Dateien (z. B. `-v2`). |
| 6 | Tür und Griff | **Fronttür aus Plexi, Scharniere links**, langer **senkrechter Stangengriff** (wie IKEA) zwischen Tür und Bedienfeld. |
| 5 | Kultur | **Pilze** (z. B. ein fertig durchwachsenes Austernpilz-Zuchtset, damit innerhalb von 2 Wochen etwas sichtbar ist). |
| 6 | Lage der Elektronik | **Im Technikraum hinter dem Bedienfeld:** Pi, Kabel, später Wassertank (Vernebler) und Lüfter mit Schlitzen zur Pilzkammer. In der Pilzkammer nur LED und ggf. Sensor. |
| 7 | Bedienkonzept | **Touch-Display (iPhone) + ein physischer Taster** mit fester Bedeutung **Licht an/aus** (kein Modus; Ergebnis direkt durchs Plexiglas sichtbar). |
| 8 | Aktoren | **Licht: 4 LED-Streifen rundum im oberen Rahmen**, verdeckt im LED-Kanal der oberen Profile (Schürze außen, Blende innen); Deckel bleibt kabelfrei. Lüfter und Vernebler sind im Technikraum vorgesehen, aber nicht Teil des Prototyps. |
| 4 | **Schwerpunkt** | **Interaktionskonzept vor Technik.** HCI-Prüfungsleistung (Prof. Zagel), Option B: Booklet je 5 Seiten pro Person (50 %) + Prototyp (50 %), bewertet nach Bezug zu Vorlesungstheorien, HCI-Grundprinzipien und beschriebener Technik. Funktionen sind zweitrangig; die Uni hat fast alle Bauteile. Ein Prototyp darf auch Papier- oder Klick-Prototyp sein. |
| 7–8 | Hardware | **Raspberry Pi bleibt Steuerrechner; als Display dient ein fest eingebautes iPhone 13 mini** (statt Touch Display 2), das die Web-Oberfläche des Pi über WLAN zeigt; Dauerstrom per Kabel. **Echt:** Taster und LED. **Simuliert:** Feuchte und Temperatur (für die Vorführung umschaltbar). Lüfter, Vernebler und Sensor sind nicht Teil des Prototyps. |
| – | **Leitidee** | **B „Radikal einfach“:** ein großer Zustand (Farbe + Symbol + ein Satz), darunter drei große Kacheln. Verworfen: A „Pilz-Begleiter“ (Charakter, Gamification), C „Physisch zuerst“ (Taster/Drehknopf/LED-Ring). |
| 10 | Startbild | Große **Zustandsanzeige mit 3 Stufen** – „Alles gut“ / „Bald kümmern“ / „Jetzt handeln“ – jeweils Farbe + Symbol + ein Satz. |
| 10 | Kacheln | **Licht · Klima · Hinweise.** Klima = Feuchte + Temperatur; Hinweise = Alarme mit Handlungsanweisung. |
| – | Prototyp | **Papierprototyp → Klick-Prototyp auf dem eingebauten iPhone an der Box**, Messwerte simuliert und für die Vorführung umschaltbar. |
| 9 | App-Anbindung | **Live-Synchronität im Prototyp:** Der Pi hält den einzigen Zustand und bietet eine Schnittstelle (HTTP + Live-Updates) an; Display und App des Teammitglieds sind zwei Ansichten davon (MVC). |
| 11 | Display-Technik | **Web-Oberfläche vom Pi, im Vollbild auf dem iPhone** (Safari, gesperrt per Geführtem Zugriff); am Laptop ohne Hardware testbar. |
| – | Gamification | **Leicht, ohne Spielfigur:** Wachstumsbalken bis zur Ernte (Progression, Flow) und ein Ernte-Moment mit Teilen über die App (Achievement, Socialiser). Vorschlag aus den Konzept-Skizzen 10–11. |
| – | Konzept-Skizzen | Oberfläche: Blätter 01–14 mit Vorlesungsbezug, https://claude.ai/artifact/7MF2tG589SHFE4ghP35TE9 (privat). Die Blätter 15–18 dort (Box) sind überholt; maßgeblich für die Box ist `02-box-bau/`. |
| – | Architektur | **Freigegeben 2026-10-27:** Python + FastAPI auf dem Pi (HTTP + WebSocket), Web-Oberfläche ohne Framework, gpiozero für Taster/LED, simulierte Messwerte. Ordnerstruktur siehe nächste Zeile. |
| – | Ordnerstruktur | **Freigegeben 2026-10-28:** nach Projektschritten `01-konzept/`, `02-box-bau/`, `03-software/`, `04-evaluation/`; `AGENTS.md` und `BRIEF.md` im Root. Software im `src`-Layout (`03-software/src/growbox/`: `core/` stabiler Kern ohne FastAPI/GPIO, `hardware/` echt oder simuliert hinter einer Schnittstelle, `simulation/`, `api/`, `web/`), Dependencies in `pyproject.toml`. Autostart auf dem Pi (`deploy/`) erst, wenn der Pi da ist. |
