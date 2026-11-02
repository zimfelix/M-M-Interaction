# Präsentation 05.11.2026 – Ablauf

Idee: **Dieselbe Box, zwei Menschen.** Wir zeigen das Bedienfeld live auf dem Whiteboard und spielen Use Cases durch, zuerst mit **A · Ingrid, 72** (nur Box), dann mit **B · Power-User** (Box + App). Zu jedem Schritt nennen wir die Entscheidung und die Folie. Alle Begründungen im Detail: [`entscheidungen-folien.md`](entscheidungen-folien.md) (E1–E29), Folienbelege: [`../01-konzept/folien-recherche.md`](../01-konzept/folien-recherche.md).

Zeiten sind ein Vorschlag für ca. 12 Minuten. Bitte an die tatsächliche Redezeit anpassen.

## Technik

```
 Mac ──HDMI──► Whiteboard / Beamer
  │  Fenster 1: Bedienfeld-Vorschau, Ansicht „Vollbild in der Box“
  │  Fenster 2: App des Teammitglieds (iPhone-Spiegelung oder Browser)
  │
 echte Box auf dem Tisch: iPhone im Bedienfeld + Taster + LED  ← für den Taster-Moment
```

- **Bedienfeld:** https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi, oben „Vollbild in der Box“ wählen. Dafür muss der Mac bei claude.ai angemeldet sein.
- **Ersatz ohne Internet:** im Projektordner `python3 -m http.server -d 01-konzept/bedienfeld 8000` starten und `http://localhost:8000/vorschau-iphone.html` öffnen.
- **Vorher zurücksetzen:** Zahnrad → Admin-Modus → Zurücksetzen. So startet die Vorführung bei „Alles gut“, mit Standardfarben und ohne alte Meldungen.
- **Live-Szenarien** laufen von selbst (Zahnrad → Admin-Modus → Vorführung): „Mensch ist dran“ (Tank leer → auffüllen → ernten) und „Box regelt selbst“ (Kälte → Heizung → wieder gut). Das spart Klicks auf dem Whiteboard.
- **Rollen:** Felix zeigt die Box (Taster, Tank, Sichtfenster), das App-Teammitglied zeigt Teil B, die dritte Person führt durch Einstieg, Konzept und Fazit.

## Ablauf

| Zeit | Teil | Was man sieht | Was wir sagen | Folie |
|---|---|---|---|---|
| 1 min | **Einstieg** | Folie 8 „Die unbedienbare Mikrowelle“ neben unserer Box (sieht aus wie eine Mikrowelle) | „Unsere Box ist eine Mikrowelle für Pilze. Deshalb hat sie wenige, eindeutige Bedienelemente.“ | 8 |
| 1 min | **Konzept** | Grafik „Box regelt selbst / Mensch macht wenig“ und die Aufteilungsregel Box ↔ App | Die Box regelt das Klima selbst. Der Mensch füllt Wasser nach, erntet, setzt neu an. Was den Körper an der Box braucht, ist an der Box; Details sind in der App. Ein Zustand, zwei Ansichten. | 99–100, G 10 (Cascading Information) |
| 4 min | **A · Ingrid** | Bedienfeld live, Szenario „Mensch ist dran“ | siehe Use Cases A | siehe unten |
| 3 min | **B · Power-User** | App + Bedienfeld nebeneinander | siehe Use Cases B | siehe unten |
| 1 min | **Gamification** | Ring, „3 Tage bis zur Ernte“, Sorten mit Schwierigkeit | Progression, Countdown, Appointments; Flow durch Schwierigkeitsstufen; bewusst keine Punkte oder Ranglisten | G 10, G 12, G 14, G 15 |
| 1,5 min | **Evaluation** | Simulation Rot-Grün-Schwäche (Grün und Orange werden gleich), Kontrastwerte, Plan | Eigene Messung statt Behauptung; Cognitive Walkthrough und Nielsen-Check; ehrliche Grenzen | 23, 66, 129, 130 |
| 0,5 min | **Fazit** | Startbild „Alles gut“ | „Dieselbe Box, zwei Menschen: Ingrid braucht nur das Display, der Power-User bekommt mehr Kontrolle, ohne dass es für Ingrid komplizierter wird.“ | – |

### Use Cases A · Ingrid (nur Box)

| # | Use Case | Was passiert auf dem Display | Entscheidung · Folie |
|---|---|---|---|
| A1 | **Im Vorbeigehen** | „Alles gut“, grüner Haken, Ring „3 Tage bis zur Ernte“, Warnpunkt dunkel | E1, E2, E13 · 16–17, 26 |
| A2 | **Aus der Ferne sehen, dass etwas nicht stimmt** | Szenario starten: Warnpunkt **blinkt**, „Wasser leer“ mit Dreieck | E22 · 27 (Blinken präattentiv), 63 (Sichtabstand) |
| A3 | **Verstehen und handeln** | „Tank im Technikraum auffüllen, dann AUFGEFÜLLT drücken.“ + großer Knopf | E8 · 83–85, 59 |
| A4 | **Nachfüllen an der Box** | Felix zeigt Einfüllöffnung und Sichtfenster; auf dem Display Füllstand `62 % · 4 T` | E15, E14 · 77–79, 86–87 |
| A5 | **Rückmeldung** | „Tank voll · Nebler läuft wieder“, dann „Alles gut“; Meldungen → Verlauf **grün mit Haken** | E9, E27 · 82, 59, 76 |
| A6 | **Licht mit dem Taster** | Felix drückt den echten Taster, LED geht an; Display bestätigt kurz | E10 · 33 (Homunculus), 49, 72–74 |
| A7 | **Nicht eingreifen müssen** | KLIMA antippen: alles AUTO, kein Knopf zum Verstellen | E6, E7 · 56, 59, 60 |
| A8 | **Schlecht sehen** | Zahnrad → Darstellung → Hoher Kontrast | E26, E21 · 66, 23 |

### Use Cases B · Power-User (Box + App)

| # | Use Case | Was passiert | Entscheidung · Folie |
|---|---|---|---|
| B1 | **Unterwegs informiert** | Push in der App mit derselben Meldung und denselben Wörtern wie an der Box | E17, E18 · 99–100, 80–81 |
| B2 | **Verstehen, warum** | Advanced Analytics: Verlauf von Feuchte und CO₂ | E19 · 101–102 (Zoomable UI) |
| B3 | **Eingreifen, wenn er will** | In der App „1 Min lüften“ → an der Box unter KLIMA „läuft noch 60 s (vom Handy)“ | E7, E17 · 57–58, 99–100 |
| B4 | **Eigene Sorte** | In der App anlegen → an der Box unter SORTEN sichtbar, ändern nur in der App | E19, E28 · 140 (Autonomie), G 14 |
| B5 | **Box und Handy koppeln** | Handy-Symbol oben → Code → VERBUNDEN → Symbol verschwindet | E24 · 130 |

## Was wir zeigen, nicht nur sagen

- **Folienbilder** klein neben dem Live-Bild: 8 (Mikrowelle), 27 (Blinken), 33 (Homunculus), G 10 (Mechaniken), G 12 (Flow)
- **Eigene Messungen:** Rot-Grün-Simulation unserer Statusfarben, Kontrastwerte vorher/nachher
- **Entwicklungsverlauf** in 3 Bildern (v1 → v4 → v6) aus `01-konzept/bedienfeld/verlauf/`: Das zeigt den nutzerzentrierten Prozess (104–107)

## Risiken

| Risiko | Gegenmittel |
|---|---|
| claude.ai auf dem Präsentations-Mac nicht angemeldet | lokaler Ersatz (siehe Technik) |
| App-Funktionen aus Teil B noch nicht fertig | B mit dem Teammitglied abstimmen; Fehlendes als Mockup zeigen und so benennen |
| Szenario läuft zu schnell | Situationen einzeln im Admin-Modus auslösen statt Szenario |
| Alte Zustände im Browser (Kontrast, Meldungen) | vorher Admin → Zurücksetzen |
