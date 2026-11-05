# Learnings für weitere Uni-Projekte

Erkenntnisse aus dem HCI-Projekt „M-M Interaction“ (Pilz-Growbox mit Bedienfeld und App, Präsentation 05.11.2026) für **künftige Uni-Projekte**: Konzept, Prototyp, Präsentation, Booklet. **Nicht** für Coding- oder Harness-Projekte; anders als die `learnings.md` in den GitHub-Projekten mit Harness v6 fließt diese Datei **nicht** in `agentic-harness-v6` ein.

Status je Eintrag: **offen** = noch nicht in einem weiteren Projekt geprüft · **bestätigt** = hat sich wieder bewährt.

## ✅ Beibehalten (lief gut)

- **offen · Jede Entscheidung sofort mit Folie und Fachbegriff notieren.** Muster: „Folie N sagt … → deshalb …“, in einer Tabelle mit Nummer (E1, E2 …) und Persona. Nicht erst fürs Booklet sammeln. *Beleg: In der Präsentation wurden die Entscheidungen mit den Fachbegriffen der Folien gelobt.*
- **offen · Fortschritt sichtbar machen.** Zwischenstände einfrieren (bei uns Bedienfeld v1 → v7, Box-Skizzen v1 → v3) und den Weg vom Konzept zum Prototyp zeigen. *Beleg: Der Fortschritt mit Konzept wurde gelobt.*
- **offen · Ein starkes, einfaches Signal bleibt hängen.** Bei uns ein oranger Punkt, der auf schwarzem Display blinkt. Ein solches Bild merkt sich das Publikum eher als zehn Details. *Beleg: „Der orange Punkt war cool.“*
- **offen · Design vor Funktionen, besonders bei Apps und Bedienfeldern.** In etwa 90 % der Präsentationen stand das Design weit vor den Funktionen. Für künftige Apps und Bedienfelder also zuerst Gestaltung und Interaktion ausarbeiten (klarer Zustand, wenige Elemente, konsistente Farben); Funktionen dürfen simuliert sein. *Beleg: Beobachtung bei den Präsentationen am 05.11.2026; unser Ansatz „Interaktion vor Technik“ lag damit richtig.*
- **offen · README-Aufbau, der allein reicht.** Pro Projektschritt ein Ordner (`01-konzept/` … `04-final/`), jede README kurz und mit Inhalt direkt: Status → **Bild oben** → **✅ Final** (Entscheidungen) → **🛤 Arbeitsweg** (Fortschritt) → **Dateien** → **Links** unten. Final und Arbeitsweg getrennt halten, dann sieht man Ergebnis und Weg auf einen Blick. Regel gleich zu Beginn in die `AGENTS.md` des Projekts schreiben.
- **offen · Vorführmodus mit wenigen festen Fällen.** Ein versteckter Admin-Modus mit nur zwei Fällen und „Zurücksetzen“ macht die Live-Demo planbar.

## 🔁 Nächstes Mal anders

- **offen · Konzept, Ziel und Zielgruppe gleich zu Beginn nennen.** Die anderen Gruppen hatten zur selben Aufgabe ganz andere Konzepte. Ohne diesen Rahmen kann das Publikum die Entscheidungen nicht einordnen. Gilt für Präsentation **und** Booklet.
- **offen · Einstieg mit persönlicher Geschichte.** „Wie bin ich drauf gekommen?“ in ein bis zwei Sätzen (z. B. ein Erlebnis im Urlaub), danach erst das Konzept.
- **offen · Konzept first: erst CAD und Klick-Prototyp in Claude, dann den physischen Prototyp bauen.** Die Box zuerst im CAD und App, Bedienfeld und Features als Klick-Prototyp in Claude (claude.ai-Artifact) durchspielen, erst danach bauen, statt direkt ins Prototyping zu gehen. Wenn das Konzept steht, kann man beim Bau kreativer sein. **Fachbegriff:** Prototypen mit steigender **Fidelity** (Detailgenauigkeit), also Skizze → CAD/Klick-Prototyp → gebaute Box; Fehler werden dort geklärt, wo Ändern am wenigsten kostet. Vorlesung: Skizzen und Prototypen (Buxton), **Auflösung vs. Detailgenauigkeit** (Houde & Hill 1997), Papierprototyp, Wireframes (HCI-Folien 119–125). *Vorbild: die 3D-Growbox von Lukas (andere Gruppe, 05.11.2026), die genau so vorgegangen ist und sehr gut war.*
- **offen · Mit einem Tablet präsentieren statt mit einem eingebauten Handy.** Es ist größer fürs Publikum und lässt sich einfach am Whiteboard zeigen.
- **offen · Präsentation aufbauen wie die von Moritz** (andere Gruppe, 05.11.2026):
  - **Zielgruppe** ausdrücklich benennen
  - ein **Spiel** bzw. Mitmach-Element fürs Publikum einbauen
  - **Live-Tests** benennen, falls es welche gab (mit wem, was kam heraus)
  - **am Ende das Problem benennen**, also offene Probleme und Grenzen
- **offen · Eigene Gedanken, Stärken und Abwägungen aktiv aussprechen.** Was bewusst weggelassen wurde, laut als Entscheidung benennen, z. B. „**bewusst** minimalistisches Design: keine Uhr, nur drei Kacheln“. Sonst wirkt es, als hätte man etwas vergessen. Dazu die Stärken des Produkts (z. B. der App) ausdrücklich nennen statt sie nur zu zeigen.
- **offen · Häufige Rückfragen vorab beantworten können.** Für jede auffällige Gestaltungsentscheidung eine Ein-Satz-Antwort bereithalten. *Beispiel: „Warum Blau statt Schwarz?“ → Schwarz bedeutet Standby, Blau bedeutet „läuft“; Schwarz gibt es als Option „Hoher Kontrast“.*
