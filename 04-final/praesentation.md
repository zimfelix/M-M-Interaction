# Präsentation 05.11.2026 · 7 Minuten

**Rahmen:** 7 Minuten für Prototyp, Bedienfeld und App. Leitidee: **Dieselbe Box, zwei Menschen.** Typ A (Ingrid, 72, wenig Technik) erklärt das **Bedienfeld**, Typ B (Power-User) erklärt die **App**.

Begründungen im Detail: [`entscheidungen-folien.md`](entscheidungen-folien.md) (E1–E29). Folienbelege: [`../01-konzept/folien-recherche.md`](../01-konzept/folien-recherche.md).

## Bewertungskriterien (Folie 5) – wo wir sie erfüllen

| Kriterium (Folie 5) | Wo in der Präsentation |
|---|---|
| Bezug zu Theorien und Konzepten der Vorlesung | bei jedem Schritt eine Folie (rechte Spalte unten) |
| Beachtung der HCI-Grundprinzipien | Norman: Affordance, Mapping, Feedback, Constraints (72–87); Nielsen (130); Barrierefreiheit (23, 63, 66) |
| Einbezug und Beschreibung verwendeter Technologien | Teil 2: iPhone als Display, Raspberry Pi, Taster/LED, ein Zustand für Box und App (MVC) |

## Ablauf (7:00)

| Zeit | Wer | Teil | Inhalt | Folie |
|---|---|---|---|---|
| 0:00–0:40 | Felix | **1 Einstieg** | Aufgabe Option B Growbox (Folie 5). Folie 8 „Die unbedienbare Mikrowelle“ neben unserer Box: „Unsere Box ist eine Mikrowelle für Pilze. Deshalb wenige, eindeutige Bedienelemente.“ | 5, 8 |
| 0:40–1:40 | Felix | **2 Werdegang + Box** | Skizzen → Papier → Klick-Prototyp → v6 (3 Bilder aus `01-konzept/bedienfeld/verlauf/`); Box-Skizze/Mockup: Display rechts, Taster darunter, Tank mit Sichtfenster. Technik in einem Satz: iPhone zeigt die Web-Oberfläche vom Raspberry Pi, Taster und LED am Pi, Box und App lesen **einen** Zustand. | 104–107, 119–125, 99–100 |
| 1:40–2:10 | Felix | **3 Konzeptidee** | „Die Box regelt selbst, der Mensch macht wenig: Wasser nachfüllen, ernten, neu ansetzen.“ Aufteilung: Was den Körper an der Box braucht, ist an der Box; Details sind in der App. | 56, G 10 (Cascading Information) |
| 2:10–4:40 | Felix | **4 Typ A · Ingrid** (Bedienfeld live) | siehe Use Cases A | siehe unten |
| 4:40–6:30 | App-Teammitglied | **5 Typ B · Power-User** (App) | siehe Use Cases B | siehe unten |
| 6:30–7:00 | alle | **6 Fazit** | „Dieselbe Box, zwei Menschen: Ingrid braucht nur das Display, der Power-User bekommt in der App mehr Kontrolle, ohne dass die Box für Ingrid komplizierter wird.“ Ein Satz Evaluation: Farbsimulation gemacht, Cognitive Walkthrough und Nielsen-Check geplant. | 23, 129, 130 |

### Use Cases A · Ingrid (2:30, Bedienfeld)

Am schnellsten mit dem Live-Szenario: Zahnrad → Admin-Modus → **„Mensch ist dran“**.

| # | Was wir zeigen | Ein Satz dazu | Folie |
|---|---|---|---|
| A1 | Startbild „Alles gut“, Ring „3 Tage bis zur Ernte“ | Ein Blick, eine Aussage, Fortschritt wie ein Countdown | 16–17, 26, G 10 |
| A2 | Warnpunkt **blinkt**, „Wasser leer“ | Blinken ist präattentiv, aus der Ferne sichtbar; Status nie nur über Farbe | 27, 23 |
| A3 | Handlung + Knopf **AUFGEFÜLLT** | Meldung spezifisch, konstruktiv, höflich | 83–85, 59 |
| A4 | „Tank voll · Nebler läuft wieder“ → Meldungen: Verlauf **grün** | Feedback; Erledigtes sieht erledigt aus | 82, 59, 76 |
| A5 | **echter Taster** an der Box → Licht an | Haptisch, eine feste Bedeutung, Ergebnis sichtbar | 33, 72–74, 60 |
| A6 | KLIMA: alles AUTO, nichts zu verstellen | Automatik sichtbar machen, Eingriff nur in der App | 56, 59 |

Optional, falls Zeit bleibt: Einstellungen → Darstellung → **Hoher Kontrast** (Folie 66).

### Use Cases B · Power-User (1:50, App)

Abstimmen mit dem App-Teammitglied: Was davon kann die App am 05.11.?

| # | Was wir zeigen | Ein Satz dazu | Folie |
|---|---|---|---|
| B1 | Push in der App: dieselbe Meldung, dieselben Wörter wie an der Box | Ein Modell, zwei Ansichten; äußere Konsistenz | 99–100, 80–81 |
| B2 | Advanced Analytics: Verlauf Feuchte/CO₂ | Übersicht an der Box, Detail in der App | 101–102 |
| B3 | „1 Min lüften“ in der App → an der Box „läuft noch 60 s (vom Handy)“ | Flexibilität für Fortgeschrittene, Box bleibt einfach | 57–58, 60 |
| B4 | Eigene Sorte anlegen → an der Box unter SORTEN | Autonomie, Achiever/Free Spirit | 140, G 14 |

## Kurzfassung 3:00 (nur Ingrid)

Für den Fall, dass nur 3 Minuten bleiben, oder als einzelner Durchlauf am Bedienfeld. Eine Person (Ingrid, 72, Lesebrille, zitternde Hände), ein Live-Durchlauf; Typ B kommt nur im Schlusssatz vor. Live-Szenario: Zahnrad → Admin-Modus → **„Mensch ist dran“**.

| Zeit | Was live passiert | Was wir sagen | Folie |
|---|---|---|---|
| 0:00–0:20 | Folie 8 neben der Box | „Unsere Box sieht aus wie eine Mikrowelle, deshalb hat sie wenige, eindeutige Bedienelemente. Nutzerin: Ingrid, 72. Die Box regelt selbst, Ingrid macht nur drei Dinge: Wasser, Licht, Ernte.“ | 8 |
| 0:20–0:50 | Startbild „Alles gut“, Ring „3 Tage bis zur Ernte“ | „Ein Blick genügt: Form, Farbe und Text sagen dasselbe, auch bei Rot-Grün-Schwäche. Der Ring zeigt den Fortschritt bis zur Ernte.“ | 26, 23, 16–17, G 10 |
| 0:50–1:40 | Szenario: Warnpunkt **blinkt** → „Wasser leer“ mit Handlung → auf das **Sichtfenster** zeigen → **AUFGEFÜLLT** → „Tank voll · Nebler läuft wieder“, Verlauf grün | „Blinken sieht man auch aus 3 m Entfernung. Die Meldung sagt, was zu tun ist und welcher Knopf, ohne Schuld. Die Linie im Sichtfenster entspricht dem Balken auf dem Display. Nach dem Tippen kommt sofort eine Rückmeldung.“ | 27, 63, 83–85, 77–79, 82 |
| 1:40–2:05 | **echten Taster** drücken → LED an, Display bestätigt | „Ein Knopf, eine Bedeutung, spürbar unter dem Finger, kein Modus. Das Ergebnis sieht man durchs Plexiglas.“ | 33, 50, 72–74, 60 |
| 2:05–2:35 | KLIMA antippen (alles AUTO), dann Zahnrad → Darstellung → **Hoher Kontrast** | „Die Box zeigt, was sie selbst regelt, und Ingrid kann nichts versehentlich verstellen. Für schwache Augen gibt es hohen Kontrast.“ | 56, 59, 61, 66 |
| 2:35–3:00 | zurück zu „Alles gut“ | „Wer mehr will, zoomt in der App ins Detail. Box und App sind zwei Ansichten desselben Zustands (MVC). Getestet haben wir mit …“ (Ergebnis des Cognitive Walkthrough) | 99–102, 129 |

- **Stärkster Moment:** Taster drücken, und Licht und Display reagieren gleichzeitig (Haptik und Feedback in einem). Ist die Box nicht verkabelt, den Taster im Admin-Modus auslösen und das offen sagen.
- **Vorher erledigen, sonst fehlt der Schlusssatz:** ein kurzer Cognitive Walkthrough (Folie 129) mit einer älteren Person, Aufgaben wie A1–A5.
- **Mögliche Rückfragen:** Hilfe/Anleitung fehlt noch (Nielsen Nr. 10, Folie 130); der Taster hat noch kein Licht-Symbol; Orange am Taster/Griff kollidiert mit Orange = Warnung auf dem Display (Folie 80).

## Technik am Tag

```
 Mac ──HDMI──► Whiteboard
   ├─ Fenster 1: Bedienfeld, Ansicht „Vollbild in der Box“
   └─ Fenster 2: App (iPhone-Spiegelung oder Browser)
 echte Box auf dem Tisch: Taster, Tank, Sichtfenster
```

- Bedienfeld: https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi (Mac bei claude.ai angemeldet). **Ersatz ohne Internet:** eingefrorene Kopie `python3 -m http.server -d 04-final/bedienfeld-v6 8000`, dann `http://localhost:8000/vorschau-iphone.html`.
- **Vorher:** Zahnrad → Admin-Modus → **Zurücksetzen** (Standardfarben, keine alten Meldungen).
- **Probe mit Stoppuhr:** 7 Minuten sind knapp. Teil 4 und 5 sind die Puffer: Bei Zeitnot A5/A6 und B4 weglassen.

## Risiken

| Risiko | Gegenmittel |
|---|---|
| claude.ai auf dem Präsentations-Mac nicht angemeldet | lokaler Ersatz (siehe oben) |
| App-Funktion aus Teil B fehlt noch | als Mockup zeigen und so benennen |
| Szenario läuft zu schnell | Situationen einzeln im Admin-Modus auslösen |
| Fragen zu offenen Punkten | Warnlicht (A) und Taster-Kopplung (B): Entscheidung vom 04.11. nennen, siehe [`entscheidungen-folien.md`](entscheidungen-folien.md#offen-für-mittwoch-0411) |
