# Projekt-Brief: M-M Interaction

Ausgangsbeschreibung für den Agenten. **Keine bestätigte Spec** – offene Punkte unten zuerst mit Felix klären.

## Ursprünglicher Auftrag (Felix, wörtlich)

"wir bauen eine growbox, die von eienr app aus gesteuert werden kann und zb pilze growt. birt bauen also in real ein mini gewaechshaus, brauchen dann ein Interface, das man auch manuell am Gewächshaus bedienen kann, und nutzen dafür welche Technik? Diesen Raspberry Pi. Aber dieser Bildschirm ist ja nicht der Raspberry Pi, oder? also ein minibild ist der computer mit lcd display"

## Ziel

Ein reales Mini-Gewächshaus (Growbox), zunächst z. B. für **Pilzzucht**, das
- **lokal am Gerät** über ein Display/Touch-Interface bedienbar ist und
- **aus der Ferne** über eine App gesteuert werden kann.

## Bisheriger Stand

- GitHub-Repo `zimfelix/M-M-Interaction` (privat), lokal `~/Code/M-M-Interaction`.
- Geklärt: Ein Raspberry Pi ist ein Einplatinencomputer **ohne** eigenes Display; das Display ist ein separates Bauteil. Es gibt aber Komplettgeräte (Rechner + Touchscreen).
- Vorläufige Empfehlung (nicht entschieden): Raspberry Pi 5 + offizielles Touch Display 2.

Grobes Zielbild:

```
Sensoren (Temp/Feuchte/CO₂) ──► Steuerrechner ──► Relais/MOSFET ──► Lüfter, Befeuchter, Licht
                                     │
                     ┌───────────────┴───────────────┐
               Touch-Display (lokal)         App über WLAN (fern)
```

Hardware-Optionen für Steuerung + Display:

| Variante | Kurzbewertung |
|---|---|
| Pi 5 + Touch Display 2 | flexibel, gut dokumentiert – Empfehlung |
| Komplettgerät (z. B. Seeed reTerminal, CM4 + 5″) | kompakt, teurer, weniger Anschlüsse |
| ESP32 mit Display ("Cheap Yellow Display") | günstig, sparsam; App und UI aufwendiger |

## Offen – vor der Umsetzung klären

1. ✅ **Arbeitsmodus** – entschieden, siehe unten.
2. ✅ **Harness** – entschieden, siehe unten.
3. ✅ **Wer ist „wir“?** – entschieden, siehe unten (Teamgröße nicht relevant). Team, Rollen, Zuständigkeiten (Hardware/Software), Name „M-M“ – Bedeutung?
4. ✅ **Zweck und Umfang** – entschieden, siehe unten. Ursprüngliche Frage: Hobby, Schul-/Uniprojekt, Prototyp für ein Produkt? Termin? Budget?
5. ✅ **Kulturen** – entschieden, siehe unten. Ursprüngliche Frage: nur Pilze (welche Sorten?) oder auch Pflanzen? Daraus folgen Zielwerte (Feuchte, Temperatur, CO₂, Licht, Frischluft).
6. ✅ **Box** – entschieden, siehe unten. Ursprüngliche Frage: Größe, Material, selbst gebaut oder umgebauter Schrank/Zelt? Wasserversorgung, Strom, Sicherheit (Netzspannung, Feuchtigkeit!).
7. ✅ **Steuerrechner + Display:** Pi + Display, Komplettgerät oder ESP32? Bereits vorhandene Hardware?
8. ✅ **Sensoren/Aktoren:** konkrete Auswahl (z. B. SCD41 für CO₂/Temp/Feuchte; Ultraschallvernebler, Lüfter, LED, ggf. Heizung).
9. ✅ **App:** Was heißt „App“ – Web-App im Browser (am einfachsten), native Handy-App oder z. B. Home Assistant? Nur im Heim-WLAN oder auch unterwegs? Wer darf zugreifen?
10. ✅ **Funktionen:** nur Anzeigen + manuell schalten oder automatische Regelung mit Zielwerten, Zeitplänen, Verlauf/Diagrammen, Alarmen?
11. ✅ **Technologie-Stack Software:** Sprache (vermutlich Python auf dem Pi), lokale UI-Technik, Kommunikation (HTTP/WebSocket, MQTT).

## Entscheidungen im Project Init

Von Felix bestätigt. Diese Tabelle ist der maßgebliche Stand; Überholtes wird ersetzt.

| # | Thema | Entscheidung |
|---|---|---|
| 1 | Arbeitsmodus | **Shipping**: zügig eine nutzbare Box; Erklärungen kurz und entscheidungsorientiert. |
| 1 | Selbst bauen | **Felix (bzw. das Team) baut Hardware und Verkabelung selbst**, nach Anleitung des Agenten; die Software schreibt der Agent. |
| 1 | Autonomie | Innerhalb eines freigegebenen Schritts schreibt, testet und committet der Agent lokal selbst. **Rückfrage vor:** Push, neuen Dependencies, Architekturänderungen, Einkäufen. |
| 2 | Harness | **Schlank, ohne Agentic Harness** (am 2026-10-26 übernommen und wieder entfernt). Projektregeln: `AGENTS.md`; Entscheidungen: diese Datei; Vorlesungsbezug: `HCI-KONZEPTE.md`. |
| 3 | Team und Rollen | Uni-Projektgruppe. **Felix:** baut die Growbox physisch und das Mini-Display an der Box (Mechatronik ist neu für ihn). **Die App baut ein anderes Teammitglied.** Unser Teil muss so laufen, dass Box, Display und App synchron sind. |
| 4 | Zweck | **Uni-Projekt mit Schwerpunkt Mensch-Maschine-Interaktion (HMI).** Die Bedienung am Gerät muss sehr einfach sein und möglichst alle Altersgruppen abdecken. Die Kultur ist zweitrangig. |
| 4 | Bedienidee | Wenige große Funktionen, z. B. **Alarm**, **Licht**, **Temperatur**; der genaue Inhalt ist noch offen. |
| 4 | Budget | **150–300 €** für die gesamte Hardware. |
| 4 | Termin | **Präsentation 05.11.2026, 10:00 · Abgabe 08.11.2026, 23:59** (Folie 5, von Felix bestätigt). |
| 3 | Name | **„M-M“ = Mensch-Maschine** → M-M Interaction = Mensch-Maschine-Interaktion (HMI). |
| 6 | Box | **Aufbau wie eine Mikrowelle:** links die Pilzkammer (ca. 20 × 20 × 20 cm) aus Plexi mit LED im Deckel und blickdichtem Sockelrand (ca. 5 cm, Erde verdeckt); rechts ein blickdichter **Technikraum** (ca. 8 cm breit, volle Tiefe, Holz oder gedruckt) mit Bedienfeld vorn. Skizze: `konzept/skizze-box.html`. |
| 6 | Tür und Griff | **Fronttür aus Plexi, Scharniere links**, langer **senkrechter Stangengriff** (wie IKEA) zwischen Tür und Bedienfeld. |
| 5 | Kultur | **Pilze** (z. B. ein fertig durchwachsenes Austernpilz-Zuchtset, damit innerhalb von 2 Wochen etwas sichtbar ist). |
| 6 | Lage der Elektronik | **Im Technikraum hinter dem Bedienfeld:** Pi, Kabel, später Wassertank (Vernebler) und Lüfter mit Schlitzen zur Pilzkammer. In der Pilzkammer nur LED und ggf. Sensor. |
| 7 | Bedienkonzept | **Touch-Display + ein physischer Taster** mit fester Bedeutung **Licht an/aus** (kein Modus; Ergebnis direkt durchs Plexiglas sichtbar). |
| 8 | Aktoren | **LED-Licht** gesetzt; Lüfter und Vernebler empfohlen, Bestätigung offen. |
| 4 | **Schwerpunkt** | **Interaktionskonzept vor Technik.** HCI-Prüfungsleistung (Prof. Zagel), Option B: Booklet je 5 Seiten pro Person (50 %) + Prototyp (50 %), bewertet nach Bezug zu Vorlesungstheorien, HCI-Grundprinzipien und beschriebener Technik. Funktionen sind zweitrangig; die Uni hat fast alle Bauteile. Ein Prototyp darf auch Papier- oder Klick-Prototyp sein. |
| 7–8 | Hardware | **Raspberry Pi bleibt Steuerrechner; als Display dient ein fest eingebautes iPhone 13 mini** (statt Touch Display 2), das die Web-Oberfläche des Pi über WLAN zeigt; Dauerstrom per Kabel. **Echt:** Taster und LED. **Simuliert:** Feuchte und Temperatur (für die Vorführung umschaltbar). Lüfter, Vernebler und Sensor sind nicht Teil des Prototyps. |
| – | **Leitidee** | **B „Radikal einfach“:** ein großer Zustand (Farbe + Symbol + ein Satz), darunter drei große Kacheln. Verworfen: A „Pilz-Begleiter“ (Charakter, Gamification), C „Physisch zuerst“ (Taster/Drehknopf/LED-Ring). |
| 10 | Startbild | Große **Zustandsanzeige mit 3 Stufen** – „Alles gut“ / „Bald kümmern“ / „Jetzt handeln“ – jeweils Farbe + Symbol + ein Satz. |
| 10 | Kacheln | **Licht · Klima · Hinweise.** Klima = Feuchte + Temperatur; Hinweise = Alarme mit Handlungsanweisung. |
| – | Prototyp | **Papierprototyp → Klick-Prototyp auf dem eingebauten iPhone an der Box**, Messwerte simuliert und für die Vorführung umschaltbar. |
| 9 | App-Anbindung | **Live-Synchronität im Prototyp:** Der Pi hält den einzigen Zustand und bietet eine Schnittstelle (HTTP + Live-Updates) an; Display und App des Teammitglieds sind zwei Ansichten davon (MVC). |
| 11 | Display-Technik | **Web-Oberfläche vom Pi, im Vollbild auf dem iPhone** (Safari, gesperrt per Geführtem Zugriff); am Laptop ohne Hardware testbar. |
| – | Gamification | **Leicht, ohne Spielfigur:** Wachstumsbalken bis zur Ernte (Progression, Flow) und ein Ernte-Moment mit Teilen über die App (Achievement, Socialiser). Vorschlag aus den Konzept-Skizzen 10–11. |
| – | Konzept-Skizzen | 14 Skizzen mit Vorlesungsbezug: https://claude.ai/artifact/7MF2tG589SHFE4ghP35TE9 (privat). |
| – | Architektur | **Freigegeben 2026-10-27:** Python + FastAPI auf dem Pi (HTTP + WebSocket), Web-Oberfläche ohne Framework, gpiozero für Taster/LED, simulierte Messwerte. Struktur: `box/`, `docs/api.md`, `konzept/`. |
