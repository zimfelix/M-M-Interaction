# Präsentation 05.11.2026 · 7 Minuten

**Rahmen:** 7 Minuten für Prototyp, Bedienfeld und App. Leitidee: **Dieselbe Box, zwei Menschen.** Typ A (Ingrid, 72, wenig Technik) erklärt das **Bedienfeld**, Typ B (Power-User) erklärt die **App**.

Begründungen im Detail: [`entscheidungen-folien.md`](entscheidungen-folien.md) (E1–E30). Folienbelege: [`../01-konzept/folien-recherche.md`](../01-konzept/folien-recherche.md).

## Bewertungskriterien (Folie 5) – wo wir sie erfüllen

| Kriterium (Folie 5) | Wo in der Präsentation |
|---|---|
| Bezug zu Theorien und Konzepten der Vorlesung | bei jedem Schritt eine Folie (rechte Spalte unten) |
| Beachtung der HCI-Grundprinzipien | Norman: Affordance, Mapping, Feedback, Constraints (72–87); Barrierefreiheit (23, 63, 66); **Nielsen (130) als Maßstab:** [Nielsen-Check](entscheidungen-folien.md#nielsen-check-folie-130), 9 von 10 erfüllt, Lücke „Help and documentation“ offen benannt |
| Einbezug und Beschreibung verwendeter Technologien | Teil 2: iPhone als Display, Raspberry Pi, Taster/LED, ein Zustand für Box und App (MVC) |

## Ablauf (7:00)

| Zeit | Wer | Teil | Inhalt | Folie |
|---|---|---|---|---|
| 0:00–0:30 | Felix | **1 Einstieg** | Aufgabe Option B Growbox (Folie 5). Folie 8 „Die unbedienbare Mikrowelle“ neben unserer Box: „Unsere Box ist eine Mikrowelle für Pilze. Deshalb wenige, eindeutige Bedienelemente.“ | 5, 8 |
| 0:30–1:15 | Felix | **2 Werdegang + Box** | Skizzen → Papier → Klick-Prototyp → v6 (3 Bilder aus `01-konzept/bedienfeld/verlauf/`); Box-Skizze v3 (`02-box-bau/bilder/skizze-box-v3.svg`): Display rechts, beiger Taster mit Licht-Symbol darunter, Tank mit Sichtfenster; Orange gibt es nur für Warnungen. Technik in einem Satz: iPhone zeigt die Web-Oberfläche vom Raspberry Pi, Taster und LED am Pi, Box und App lesen **einen** Zustand. | 104–107, 119–125, 99–100 |
| 1:15–1:40 | Felix | **3 Konzeptidee** | „Die Box regelt selbst, der Mensch macht wenig: Wasser nachfüllen, ernten, neu ansetzen.“ Aufteilung: Was den Körper an der Box braucht, ist an der Box; Details sind in der App. | 56, G 10 (Cascading Information) |
| 1:40–4:40 | Felix | **4 Typ A · Ingrid** (Bedienfeld live, 3:00) | siehe Use Cases A | siehe unten |
| 4:40–6:30 | App-Teammitglied | **5 Typ B · Power-User** (App, 1:50) | siehe Use Cases B | siehe unten |
| 6:30–7:00 | alle | **6 Fazit** | „Dieselbe Box, zwei Menschen: Ingrid braucht nur das Display, der Power-User bekommt in der App mehr Kontrolle, ohne dass die Box für Ingrid komplizierter wird.“ Ein Satz Evaluation: Nielsen-Check 9 von 10 (Hilfe fehlt noch), Farbsimulation gemacht, Cognitive Walkthrough mit einer älteren Person: „…“ (Ergebnis eintragen). | 23, 129, 130 |

### Use Cases A · Ingrid (1:40–4:40, Bedienfeld)

Eine Person: Ingrid, 72, Lesebrille, zitternde Hände, ohne Handy. Live-Szenario: Zahnrad → Admin-Modus → **„Mensch ist dran“**.

| Zeit | # | Was live passiert | Was wir sagen | Folie |
|---|---|---|---|---|
| 1:40–2:10 | A1 | Startbild „Alles gut“, Ring „3 Tage bis zur Ernte“ | „Ein Blick genügt: Form, Farbe und Text sagen dasselbe, auch bei Rot-Grün-Schwäche. Der Ring zeigt den Fortschritt bis zur Ernte.“ | 26, 23, 16–17, G 10 |
| 2:10–3:00 | A2–A4 | Warnpunkt **blinkt** → „Wasser leer“ mit Handlung → auf das **Sichtfenster** zeigen → **AUFGEFÜLLT** → „Tank voll · Nebler läuft wieder“, Verlauf grün | „Blinken sieht man auch aus 3 m Entfernung. Die Meldung sagt, was zu tun ist und welcher Knopf, ohne Schuld. Die Linie im Sichtfenster entspricht dem Balken auf dem Display. Erledigtes ist grün mit Haken.“ | 27, 63, 83–85, 77–79, 82, 59 |
| 3:00–3:35 | A5 | **echten Taster** drücken → LED an, Display bestätigt | „Ein Knopf, eine Bedeutung, spürbar unter dem Finger, kein Modus. Das Licht-Symbol sagt, was er tut; das Ergebnis sieht man durchs Plexiglas.“ | 33, 50, 72–74, 60 |
| 3:35–4:05 | A6 | KLIMA antippen: alles AUTO, nichts zu verstellen | „Die Box zeigt, was sie selbst regelt, und Ingrid kann nichts versehentlich verstellen.“ | 56, 59, 61 |
| 4:05–4:25 | A7 | Zahnrad → Darstellung → **Hoher Kontrast**, zurück | „Für schwache Augen: hoher Kontrast. Warnungen bleiben an Form und Text erkennbar.“ | 66, 23 |
| 4:25–4:40 | – | zurück zu „Alles gut“ | **Überleitung Consistency:** „Orange heißt bei uns überall Warnung, auf dem Display und an der Box. Dieselben Wörter und Farben sieht der Power-User in der App.“ | 80–81 |

- **Stärkster Moment:** Taster drücken, und Licht und Display reagieren gleichzeitig (Haptik und Feedback in einem). Ist die Box nicht verkabelt, den Taster im Admin-Modus auslösen und das offen sagen.
- **Vorher erledigen:** ein kurzer Cognitive Walkthrough (Folie 129) mit einer älteren Person, Aufgaben A1–A6. Das Ergebnis kommt in den Fazit-Satz.

### Use Cases B · Power-User (1:50, App)

Abstimmen mit dem App-Teammitglied: Was davon kann die App am 05.11.? **Roter Faden ist Consistency** (Folie 80–81, Nielsen 130): B1 zuerst zeigen, damit die Überleitung aus Teil 4 trägt. Vor der Probe die App-Spalte im [Nielsen-Check](entscheidungen-folien.md#nielsen-check-folie-130) abhaken (gleiche Wörter laut [`begriffe-box-app.md`](../01-konzept/begriffe-box-app.md), kein Rot, Orange nur für Warnungen).

| # | Was wir zeigen | Ein Satz dazu | Folie |
|---|---|---|---|
| B1 | Push in der App: dieselbe Meldung, dieselben Wörter wie an der Box | Ein Modell, zwei Ansichten; äußere Konsistenz | 99–100, 80–81 |
| B2 | Advanced Analytics: Verlauf Feuchte/CO₂ | Übersicht an der Box, Detail in der App | 101–102 |
| B3 | „1 Min lüften“ in der App → an der Box „läuft noch 60 s (vom Handy)“ | Flexibilität für Fortgeschrittene, Box bleibt einfach | 57–58, 60 |
| B4 | Eigene Sorte anlegen → an der Box unter SORTEN | Autonomie, Achiever/Free Spirit | 140, G 14 |

## Technik am Tag

```
 Mac ──HDMI──► Whiteboard
   ├─ Fenster 1: Bedienfeld, Ansicht „Vollbild in der Box“
   └─ Fenster 2: App (iPhone-Spiegelung oder Browser)
 echte Box auf dem Tisch: Taster, Tank, Sichtfenster
```

- Bedienfeld: https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi (Mac bei claude.ai angemeldet). **Ersatz ohne Internet:** eingefrorene Kopie `python3 -m http.server -d 04-final/bedienfeld-v6 8000`, dann `http://localhost:8000/vorschau-iphone.html`.
- **Vorher:** Zahnrad → Admin-Modus → **Zurücksetzen** (Standardfarben, keine alten Meldungen).
- **Probe mit Stoppuhr:** 7 Minuten sind knapp. Teil 4 und 5 sind die Puffer: Bei Zeitnot A7 (Hoher Kontrast) und B4 weglassen; A5 (Taster) bleibt immer.

## Risiken

| Risiko | Gegenmittel |
|---|---|
| claude.ai auf dem Präsentations-Mac nicht angemeldet | lokaler Ersatz (siehe oben) |
| App-Funktion aus Teil B fehlt noch | als Mockup zeigen und so benennen |
| Szenario läuft zu schnell | Situationen einzeln im Admin-Modus auslösen |
| Frage nach Hilfe/Anleitung (Nielsen Nr. 10) | Lücke offen benennen, Vorschlag Karte an der Box, siehe [Nielsen-Check](entscheidungen-folien.md#nielsen-check-folie-130) |
| Fragen zu offenen Punkten | Warnlicht (A) und Taster-Kopplung (B): Entscheidung vom 04.11. nennen, siehe [`entscheidungen-folien.md`](entscheidungen-folien.md#offen-für-mittwoch-0411) |
