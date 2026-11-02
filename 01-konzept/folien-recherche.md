# Folien-Recherche: Was sagen die Folien konkret zum Bedienfeld?

Stand 02.11.2026, geprüft an den Original-PDFs in `01-konzept/folien/` (nur lokal, per `.gitignore` ausgeschlossen). **Folie N** = Seite im HCI-PDF, **G N** = Seite im Gamification-PDF. Bezug: Bedienfeld v5.

Wichtig fürs Booklet: Viele Folien sind **Bildbeispiele ohne Text**. Die Aussage dahinter kam in der Vorlesung mündlich. Wir zitieren deshalb das Beispiel und formulieren die Folgerung selbst. Was gar nicht auf den Folien steht, ist unten als **externe Quelle** markiert.

## 1. Drei Knöpfe unten – oder anders?

Die Folien geben **keine Knopfzahl vor**. Sie liefern aber Prinzipien, mit denen sich 3 Kacheln gut begründen lassen:

| Folie | Was die Folie zeigt | Argument für das Bedienfeld |
|---|---|---|
| **8** „Die unbedienbare Mikrowelle“ | Mikrowelle mit Tastenfeld neben Mikrowelle mit 2 Drehknöpfen | Unsere Box ist wie eine Mikrowelle aufgebaut. **Wenige, eindeutige Bedienelemente** statt vieler Tasten. Starker Einstieg für die Präsentation. |
| **50** Fitts' Law | große Ziele, Abstandsminimierung, Ecken und Kanten sind leicht zu treffen | Große Kacheln am unteren Rand, nah am Taster. Breitere Kacheln (3 statt 4) = größeres Ziel. |
| **130** Nielsen | *Aesthetic and minimalist design*, *Recognition rather than recall*, *Visibility of system status* | Nur 3 Kacheln, jede mit **Symbol + Wort** (Wiedererkennen statt Erinnern). Die Zahl an „Meldungen“ zeigt den Systemstatus. |
| **81** überraschende Inkonsistenz | Telefon- vs. Taschenrechner-Ziffernblock | Eine Leiste unten mit Symbol + Wort kennt man vom Smartphone (Tab-Leiste). Nutzt die App dieselbe Leiste, sind Box und App **äußerlich konsistent** (Folie 80). |
| **72–73** Affordances, „Was ist verkehrt?“ | PULL-Griff an einer Drucktür, Handy mit Mini-Tasten | Kacheln sehen wie Knöpfe aus (Rahmen, Symbol). Der Statustext „Alles gut“ ist zwar antippbar, sieht aber nicht so aus. Deshalb braucht es die Kachel **Meldungen** als sichtbaren Weg. |
| **57–58** Flexibilität | Menü **und** Tastenkürzel, mehrere Ansichten | Meldungen sind auf zwei Wegen erreichbar: über den Status und über die Kachel. Licht über Taster und App. |
| **96** Direkte Manipulation | Objekte und Aktionen sichtbar, schnell, umkehrbar | Die nötige Handlung steht als großer Knopf **direkt unter dem Status** („Geerntet“, „Aufgefüllt“), nicht in einem Menü. |
| **101–102** Zoomable UIs | Karte, Prezi: Übersicht → Detail | Startbild = Übersicht. Die Kacheln zoomen ins Detail, die App zoomt noch weiter. |

**Alternativen, geprüft:**

| Variante | Für | Gegen | Urteil |
|---|---|---|---|
| **3 Kacheln unten** (heute) | Minimalismus (130), Fitts (50), bekannt vom Smartphone (80–81) | eine Zeile Platz | ✅ behalten |
| 2 Kacheln, Meldungen nur über den Status | noch minimalistischer (Folie 8) | Der Status sieht nicht drückbar aus (72–73), und die Meldungszahl als Systemstatus (130) fehlt | ❌ |
| Gar keine Kacheln, alles über Antippen des Status | maximal ruhig | versteckte Bedienung, schlecht für seltene Nutzer (Vergessen, Folie 41) | ❌ |
| Mehr Funktionen direkt am Zustand (Aktion unter dem Status) | direkte Manipulation (96), Gulf of Execution (59) | – | ✅ ist schon so umgesetzt |

## 2. Farbgestaltung

| Folie | Was die Folie zeigt | Folgerung |
|---|---|---|
| **26** | „Farbe allein wird präattentiv wahrgenommen. Form allein wird präattentiv wahrgenommen. Kombination aus 2 Eigenschaften wird attentiv wahrgenommen.“ | Auf ruhigem blauem Grund springt ein einziges Signal (grün oder orange) sofort ins Auge. Wir nutzen Farbe **und** Form **redundant**: Jede trägt die Aussage allein, man muss sie nicht kombinieren. |
| **27** | Tafel präattentiver Merkmale, darunter **„Blinking“** und „Direction/Phase of motion“ | **Blinken ist präattentiv**: Es zieht die Aufmerksamkeit an, bevor man liest. Das belegt die v5-Entscheidung „Klima-Punkt leuchtet ruhig“. Blinken nur, wenn wirklich gehandelt werden muss. |
| **23** Farbenblindheit | „Häufig: Rot/Grün Schwäche, ca. 8 % der männlichen Bevölkerung, Simulationsmöglichkeiten in Photoshop und anderen Apps“ | Wir haben die Simulation gemacht (siehe unten): Bei Rot-Grün-Schwäche werden **unser Grün und Orange fast gleich**. Nur die **Form** (Kreis mit Haken vs. Dreieck mit „!“) und das **Wort** unterscheiden die Zustände. |
| **76** kulturelle Constraints | Stoppschild (Form + Farbe auch ohne lesbare Schrift), Recycling-Symbol | Warndreieck nach ISO 7010 und grüner Haken sind **kulturell gelernte Zeichen**: Man erkennt sie, ohne den Text zu lesen. |
| **66** Farbauflösung & Kontrast | „Wie wichtig ist der Bildschirmkontrast?“ | Kontraste nachgemessen (siehe unten): Weiße Schrift ist gut, **orange Schrift auf hellem Blau ist zu schwach**. |
| **82** Feedback | Ladekreis, Fortschrittsbalken, Sanduhr | Der Ring ist ein Fortschrittsbalken für einen Prozess, der Wochen dauert. |

**Simulation Rot-Grün-Schwäche** (Machado et al. 2009, volle Ausprägung):

| | Grün „Alles gut“ `#3fcf7f` | Orange „Warnung“ `#e69f00` | Helligkeitsunterschied |
|---|---|---|---|
| normal | grün | orange | 1,12 : 1 (fast gleich hell) |
| Deuteranopie (Grün-Schwäche) | `#bdb284` oliv | `#cab411` oliv-gelb | **1,02 : 1**, praktisch nicht unterscheidbar |
| Protanopie (Rot-Schwäche) | `#cfbe7a` | `#b9a200` | 1,37 : 1 |

→ Ohne Form und Text wäre der Status für ca. 8 % der Männer **nicht lesbar**. Die redundante Codierung ist also nicht nur Theorie, sie ist **notwendig**. Fürs Booklet ist das ein starkes Argument mit eigener Messung.

**Kontrast nach WCAG** (externe Quelle: Text braucht mindestens 4,5 : 1, große Schrift 3 : 1):

| Schrift | auf hellster Stelle `#2f45f5` | auf Fläche `#1525c4` |
|---|---|---|
| Weiß | 6,4 ✅ | 10,0 ✅ |
| Hellblau (Nebentexte) `#c7cfff` | **4,2** ⚠️ knapp unter 4,5 | 6,6 ✅ |
| Grün `#3fcf7f` | 3,2 (nur große Schrift) | 5,0 ✅ |
| Orange `#e69f00` | **2,8** ❌ | 4,5 knapp |

→ Der **orange Warntitel** („Wasser leer“) steht im hellen Bereich unter dem Ring und ist dort zu kontrastarm. Vorschlag: Titel weiß, Orange nur für Dreieck, Rahmen und Knopf.

## 3. Gamification

Die Folien (G 10) listen **24 Mechaniken**. Für eine ruhige Box ohne Spielfigur passen diese:

| Mechanik (G 10) | Wo bei uns | Für |
|---|---|---|
| **19 Progression** | Ring = Fortschritt bis zur Ernte | A, B |
| **9 Countdown** | „3 Tage bis zur Ernte“ in der Ringmitte | A, B |
| **2 Appointments** | Ernte-Termin, „Jetzt ernten“, nächste Welle | A |
| **1 Achievements** | erste Ernte (Ernte-Moment, in der App teilbar) | B |
| **6 Cascading Information Theory** | Information schrittweise freigeben: Box zeigt das Nötigste, Kacheln mehr, App alles | A, B |
| **17 Ownership** | „mein“ Pilz, eigene Sorte in der App | B |
| **11 Epic Meaning** (auch G 8, McGonigal) | aus Substrat wird Essen | A |
| **8 Community Collaboration / 24 Virality** | Ernte teilen in der App | B |

**Bewusst nicht:** Points, Levels, Lottery, **Loss Aversion** (Druck und Angst, etwas zu verlieren, passt nicht zu Ingrid), Leaderboards.

| Folie | Aussage | Folgerung |
|---|---|---|
| **G 4** Deterding | Gamification = Spieldesign-Elemente in Nicht-Spiel-Kontexten | Die Box bleibt ein Gerät, Spielelemente unterstützen nur. |
| **G 12** Flow | 4 Voraussetzungen: klare Ziele, Balance Herausforderung ↔ Können, klares sofortiges Feedback, Aktivität als intrinsisch erlebt | Ziel = Ring. **Balance = Schwierigkeit der Sorten** (Auster leicht, Shiitake schwer) für Einsteiger und Profis. Feedback = Rückmeldung nach jedem Knopf. |
| **G 14** Hexad (Marczewski) | Philanthropist (Purpose), Achiever (Mastery), Free Spirit (Autonomy), Socialiser (Relatedness) … | **A Ingrid = Philanthropist** (kümmert sich). **B Power-User = Achiever** (Mastery: optimieren) mit Zügen von **Free Spirit** (Autonomie: eigene Sorte, 1 Min lüften). |
| **G 15** Serious Games | „Balance“ zwischen ernstem Ziel (*Characterizing Goal*) und Spiel | Das ernste Ziel (Pilze erfolgreich züchten) bleibt vorne. |

## 4. Barrierefreiheit

Die Folien behandeln Barrierefreiheit **nur knapp**:

- **Folie 23**: Farbenblindheit, siehe oben (Simulation gemacht).
- **Folie 70**: „Barrierefreiheit“ und „Design for all“ sind nur als **Rechercheaufgaben** genannt, ohne Inhalt.
- **Folie 133**: Sehkraft und Alter als Merkmale bei der Auswahl von Testpersonen.

Was wir darüber hinaus tun, braucht für das Booklet eine **externe Quelle**, z. B. WCAG 2.2 für Kontrast oder ein Buch zu Design for all:

- Status dreifach codiert: Farbe + Form + Wort, dazu das Pilz-Gesicht (froh/besorgt)
- große Schrift, große Ziele, kein Zeitdruck, wichtige Aktionen mit Bestätigung

## Korrekturen an unseren Dokumenten

- **Folie 38** („Begrenzung des Kurzzeitgedächtnisses“) zeigt nur ein Bild, **keine Zahl**. „Höchstens 3–4 Elemente“ steht nicht auf der Folie. Für eine Zahl braucht es eine externe Quelle (Miller 1956: 7 ± 2; Cowan 2001: ca. 4). Sonst nur „begrenzt“ schreiben. In `04-evaluation/entscheidungen-folien.md` (E3) angepasst.
- **Folie 27** belegt Blinken als präattentives Merkmal und stützt damit E5. Ergänzt.

## Vorschläge (noch nicht umgesetzt)

1. **Warntitel weiß statt orange**: Kontrast 2,8 → 6,4. Orange bleibt bei Dreieck, Rahmen und Knopf.
2. **Nebentexte etwas heller** (`#c7cfff` → z. B. `#d8deff`), damit sie auch in der hellen Mitte über 4,5 : 1 liegen.
3. **3 Kacheln behalten**, Begründung wie oben (Folien 8, 50, 72–73, 80–81, 130).
4. **Folie 8 (Mikrowelle)** als Einstieg für die Präsentation: Unsere Box sieht aus wie eine Mikrowelle, und genau deshalb hat sie wenige Bedienelemente.
