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
3. **Wer ist „wir“?** Team, Rollen, Zuständigkeiten (Hardware/Software), Name „M-M“ – Bedeutung?
4. **Zweck und Umfang:** Hobby, Schul-/Uniprojekt, Prototyp für ein Produkt? Termin? Budget?
5. **Kulturen:** nur Pilze (welche Sorten?) oder auch Pflanzen? Daraus folgen Zielwerte (Feuchte, Temperatur, CO₂, Licht, Frischluft).
6. **Box:** Größe, Material, selbst gebaut oder umgebauter Schrank/Zelt? Wasserversorgung, Strom, Sicherheit (Netzspannung, Feuchtigkeit!).
7. **Steuerrechner + Display:** Pi + Display, Komplettgerät oder ESP32? Bereits vorhandene Hardware?
8. **Sensoren/Aktoren:** konkrete Auswahl (z. B. SCD41 für CO₂/Temp/Feuchte; Ultraschallvernebler, Lüfter, LED, ggf. Heizung).
9. **App:** Was heißt „App“ – Web-App im Browser (am einfachsten), native Handy-App oder z. B. Home Assistant? Nur im Heim-WLAN oder auch unterwegs? Wer darf zugreifen?
10. **Funktionen:** nur Anzeigen + manuell schalten oder automatische Regelung mit Zielwerten, Zeitplänen, Verlauf/Diagrammen, Alarmen?
11. **Technologie-Stack Software:** Sprache (vermutlich Python auf dem Pi), lokale UI-Technik, Kommunikation (HTTP/WebSocket, MQTT).

## Entscheidungen im Project Init

Von Felix bestätigt. Am Ende des Init werden sie nach `agentic-harness/harness/project.md` bzw. `agentic-harness/docs/` übertragen.

| # | Thema | Entscheidung |
|---|---|---|
| 1 | Arbeitsmodus | **Shipping**: zügig eine nutzbare Box; Erklärungen kurz und entscheidungsorientiert. |
| 1 | Selbst bauen | **Felix (bzw. das Team) baut Hardware und Verkabelung selbst**, nach Anleitung des Agenten; die Software schreibt der Agent. |
| 1 | Autonomie | Innerhalb eines freigegebenen Schritts schreibt, testet und committet der Agent lokal selbst. **Rückfrage vor:** Push, neuen Dependencies, Architekturänderungen, Einkäufen. |
| 2 | Harness | **Agentic Harness aus `~/Code/leadfinder` übernommen** (Export unverändert, Commit `30d74e2`); dieser Brief liegt jetzt unter `agentic-harness/project/brief.md`. |
