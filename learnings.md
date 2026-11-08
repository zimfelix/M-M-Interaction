# Learnings für weitere Uni-Projekte

Erkenntnisse aus dem HCI-Projekt „M-M Interaction“ (Pilz-Growbox mit Bedienfeld und App, Präsentation 05.11.2026, Booklet abgegeben 08.11.2026) für **künftige Uni-Projekte**: Konzept, Prototyp, Präsentation, Booklet. **Nicht** für Coding- oder Harness-Projekte; anders als die `learnings.md` in den GitHub-Projekten mit Harness v6 fließt diese Datei **nicht** in `agentic-harness-v6` ein.

Status je Eintrag: **offen** = noch nicht in einem weiteren Projekt geprüft · **bestätigt** = hat sich wieder bewährt.

## ✅ Beibehalten (lief gut)

- **offen · Jede Entscheidung sofort mit Folie und Fachbegriff notieren.** Muster: „Folie N sagt … → deshalb …“, in einer Tabelle mit Nummer (E1, E2 …) und Persona. Nicht erst fürs Booklet sammeln. *Beleg: In der Präsentation wurden die Entscheidungen mit den Fachbegriffen der Folien gelobt.*
- **offen · Fortschritt sichtbar machen.** Zwischenstände einfrieren (bei uns Bedienfeld v1 → v7, Box-Skizzen v1 → v3) und den Weg vom Konzept zum Prototyp zeigen. *Beleg: Der Fortschritt mit Konzept wurde gelobt.*
- **offen · Ein starkes, einfaches Signal bleibt hängen.** Bei uns ein oranger Punkt, der auf schwarzem Display blinkt. Ein solches Bild merkt sich das Publikum eher als zehn Details. *Beleg: „Der orange Punkt war cool.“*
- **offen · Design vor Funktionen, besonders bei Apps und Bedienfeldern.** In etwa 90 % der Präsentationen stand das Design weit vor den Funktionen. Für künftige Apps und Bedienfelder also zuerst Gestaltung und Interaktion ausarbeiten (klarer Zustand, wenige Elemente, konsistente Farben); Funktionen dürfen simuliert sein. *Beleg: Beobachtung bei den Präsentationen am 05.11.2026; unser Ansatz „Interaktion vor Technik“ lag damit richtig.*
- **offen · README-Aufbau, der allein reicht.** Pro Projektschritt ein Ordner (`01-konzept/` … `04-final/`), jede README kurz und mit Inhalt direkt: Status → **Bild oben** → **✅ Final** (Entscheidungen) → **🛤 Arbeitsweg** (Fortschritt) → **Dateien** → **Links** unten. Final und Arbeitsweg getrennt halten, dann sieht man Ergebnis und Weg auf einen Blick. Regel gleich zu Beginn in die `AGENTS.md` des Projekts schreiben.
- **offen · Vorführmodus mit wenigen festen Fällen.** Ein versteckter Admin-Modus mit nur zwei Fällen und „Zurücksetzen“ macht die Live-Demo planbar.
- **offen · Vorlesungsbezug über Fachbegriffe, nicht über Foliennummern.** Der Begriff steht im Text als „(Begriff)“ direkt hinter der Aussage, unten wiederholt eine Leiste „Aus der Vorlesung“ genau diese Begriffe. Nur Begriffe verwenden, die wirklich auf den Folien stehen. *Beleg: Der Professor konnte mit Foliennummern wenig anfangen; Begriffe waren schon in der Präsentation gelobt.*
- **offen · Gemeinsame Maße, kein Einheitsdesign.** Eine Vorlage legt nur Kopf, Titel, Schriftgrößen, Textfarben und Fuß fest; Layout und Grafiken bleiben je Seite frei. So passen Seiten mehrerer Leute zusammen, ohne eintönig zu wirken (`04-final/vorlage-seite.html`).
- **offen · Jede Entscheidung mit ehrlichem Nachteil.** Tabelle „Entscheidung · Grund (Begriff) · Nachteil“: Der Nachteil zeigt, dass abgewogen wurde, statt nur zu begründen.

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
- **offen · Format und Maß-Vorlage am ersten Tag mit dem Team festlegen.** Bei uns entstand die gemeinsame Vorlage erst am Abend vor dem letzten Tag; danach wurden alle Seiten angeglichen (119 von 256 Commits an den letzten zwei Tagen).
- **offen · Widersprüche zwischen Konzept und Bau sofort im Team entscheiden.** Taster oder Schiebeschalter, Tank mit Öffnung oder Schieber: Das stand am 06.11. als offen im Plan und bei der Abgabe noch widersprüchlich im Booklet.
- **offen · Final-Check einen Tag vor der Abgabe.** Text aller Seiten herausziehen und gezielt prüfen: Widersprüche, gleiche Begriffe für dasselbe (bei uns „Wasser leer“, „Tank leer“, „Wasser fehlt“), fehlende Zahlen, Fachbegriffe gegen die Folien. Dann bleibt Zeit, Teammitglieder zu ihren Seiten zu fragen.
- **offen · Promptverzeichnis laufend mitschreiben.** Pro wichtigem Prompt eine Zeile (Schritt · Prompt sinngemäß), statt es am Ende aus dem Git-Verlauf zusammenzusuchen.
- **offen · Häufige Rückfragen vorab beantworten können.** Für jede auffällige Gestaltungsentscheidung eine Ein-Satz-Antwort bereithalten. *Beispiel: „Warum Blau statt Schwarz?“ → Schwarz bedeutet Standby, Blau bedeutet „läuft“; Schwarz gibt es als Option „Hoher Kontrast“.*

## 🧰 Baukasten: zum Wiederverwenden

Elemente aus Booklet und Präsentation, die gut funktioniert haben. Quelle ist jeweils `04-final/booklet.html` (Seite) bzw. die genannte Datei; für ein neues Projekt Datei kopieren und Farben/Inhalte tauschen.

```
Seite:  Fortschrittsbalken + Kapitelkopf ─► Titel (2. Zeile Akzent) ─► Einleitung 2–3 Zeilen
        ─► Inhalt frei (Tabelle, Vorher/Nachher, annotierter Screen …) ─► Leiste „Aus der Vorlesung“ ─► Fuß
```

| Element | So geht's | Wo |
|---|---|---|
| **Maß-Vorlage** | feste Werte je Textart (Titel 40 px, Einleitung 15 px, Text 12,5 px, Label 11 px Versalien), drei Textfarbstufen, Ränder; messbar per `getComputedStyle` | `04-final/vorlage-seite.html` |
| **Inhalt als Kapitel-Strahl** | je Kapitel ein Vorschaubild mit Seiten-Chip, rechts Kapitelname und Seitentitel; ein durchgehender senkrechter Strahl mit einem Punkt pro Seite; aus drei Entwürfen gewählt | S. 02, CSS `.p02 .toc2` |
| **Fortschrittsbalken + Kapitelkopf** | dünner Balken oben, Trennstriche an Kapitelgrenzen, Erledigtes in Akzentfarbe; Kopf „04 · KONZEPTWEG BOX I“ mit römischer Zahl für Unterseiten → Orientierung ohne Seitenverweise | alle Seiten, CSS `.prog` |
| **Leiste „Aus der Vorlesung“** | Mono-Label + Begriffe mit „ · “, Linien oben und unten, höchstens eine Zeile; nur Begriffe, die im Text als „(Begriff)“ stehen, in derselben Reihenfolge | z. B. S. 04, 13, 15 |
| **Entscheidungstabelle** | Spalten Entscheidung · Grund (Begriff) · Nachteil; erste Spalte fett | S. 04, 06, 21 |
| **Vorher/Nachher mit Nummern** | V1 und Final nebeneinander, Nummernkreise im Bild (leer = vorher, gefüllt = jetzt), darunter nummerierte Tabelle Art · Änderung · Grund | S. 13 |
| **Annotierter Screen + Ablauf-Band** | Screen mittig, Erklärungen mit geschwungenen Linien; darunter ein farbiges Band mit dem Use Case als Bildfolge (Standby → Meldung → zurück) | S. 15 |
| **Konzeptweg als Zeitleiste** | V1 klein, V2/V3 groß, Punkte mit Datum über den Bildern, darunter Abwägungstabelle | S. 04 |
| **Weggelassen · und der Preis** | Karten „✕ Was · Warum · Preis“ plus Ausblick-Zeitstrahl Heute → Als Nächstes → Dann → Später | S. 18 |
| **Promptverzeichnis** | Anhang, zwei Spalten Schritt · Prompt (sinngemäß), gegliedert nach Projektstufen (Vorarbeit, Struktur, Inhalt, Seiten, Feinschliff) | S. 25–29 |
| **Booklet als eine HTML-Datei** | A4-Seiten 794 × 1123 px, Doppelseiten mit Pfeiltasten, `?uebersicht` mit Klick-Zoom, Seiten anderer per `iframe` eingebettet | `04-final/booklet.html` |
| **PDF und Screens per Headless-Brave** | PDF mit Zwei-Seiten-Ansicht (Cover links); Screens aus dem Klick-Prototyp mit fester Uhrzeit, damit alle Bilder gleich aussehen | `04-final/booklet-pdf.py` |
| **Spickzettel für Live-Demo** | Zeitmarken-Strahl, je Abschnitt *Tipp-Anweisung kursiv* + Sprechtext, Probelauf-Tabelle „Bin ich hier spätestens?“, „Zu lang? Zuerst X weglassen“ | `04-final/praesentation.md` |
| **Rückfragen-Tabelle** | Risiko/Frage → Ein-Satz-Antwort, vorab für jede auffällige Gestaltungsentscheidung | `04-final/praesentation.md` |

Kleine Stilregeln: Aufzählungen in Labels mit „ · “ trennen; Titel als Aussage mit Punkt („Ein Taster. Eine Bedeutung.“); Nummernkreise mit Verbindungslinie für Schritte; Orange/Signalfarbe nur für eine Bedeutung.
