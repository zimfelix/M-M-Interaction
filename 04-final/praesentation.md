# Präsentation 05.11.2026 · 5 Minuten

**Folien:** https://claude.ai/artifact/DcLZePjqNpwgHBrxHGHFha (7 Folien, Sprechtext in den Notizen jeder Folie). Leitidee: **Dieselbe Box, zwei Menschen.** Ingrid nutzt nur die Box, der Nerd zusätzlich die App. Personas ohne Altersangabe.

Begründungen im Detail: [`entscheidungen-folien.md`](entscheidungen-folien.md) (E1–E30). Folienbelege: [`../01-konzept/folien-recherche.md`](../01-konzept/folien-recherche.md).

## Bewertungskriterien (Folie 5) – wo wir sie erfüllen

| Kriterium (Folie 5) | Wo in der Präsentation |
|---|---|
| Bezug zu Theorien und Konzepten der Vorlesung | Foliennummern in der Fußzeile jeder Folie und an jeder Szene |
| Beachtung der HCI-Grundprinzipien | Norman: Affordance, Mapping, Feedback (72–87); Barrierefreiheit (23, 63); **Nielsen (130):** [Nielsen-Check](entscheidungen-folien.md#nielsen-check-folie-130), 9 von 10, Lücke Hilfe offen benannt |
| Einbezug und Beschreibung verwendeter Technologien | Folie 4: iPhone als Display, Raspberry Pi, Taster/LED, ein Zustand für Box und App (MVC) |

## Ablauf (5:00)

| Zeit | Wer | Folie im Deck | Inhalt | Vorlesung |
|---|---|---|---|---|
| 0:00–0:20 | Felix | 1 Titel | „Dieselbe Box, zwei Menschen.“ Farbsystem: Beige anfassen, Grün gut, Orange Warnung | – |
| 0:20–0:45 | Felix | 2 Aufgabe | Mikrowelle für Pilze: Box regelt selbst, Mensch macht 3 Dinge | 5, 8, 56 |
| 0:45–1:15 | Felix | 3 Zwei Menschen | Ingrid (nur Box) und der Nerd (Box + App); Regel: Körper an der Box, Details in der App | 118, 139, G 13–14 |
| 1:15–1:45 | Felix | 4 Prototyp | Box-Skizze v3, auf die echte Box zeigen; Technik in einem Satz | 72–74, 80–81, 99–100 |
| 1:45–3:30 | Felix | 5 Ingrid live | Bedienfeld am Mac, iPhone in der Box: Alles gut → Admin-Modus **1 · Wassertank leer**: Display schwarz, nur der Warnpunkt blinkt → antippen → Wasser leer → AUFGEFÜLLT → Taster drücken → wenn Zeit: **2 · Tag 6 der Fruchtung** → GEERNTET → SORTEN → Neu ansetzen | 23, 26, 27, 63, 77–79, 33 |
| 3:30–4:30 | App-Teammitglied | 6 Der Nerd | Push mit denselben Wörtern → Analytics → 1 Min lüften, Box zeigt „läuft noch 60 s (vom Handy)“ | 80–81, 101–102, 57–58 |
| 4:30–5:00 | alle | 7 Fazit | Pointe, Nielsen 9 von 10, Lücke Hilfe mit Vorschlag Karte | 130 |

- **Zeitpuffer:** Bei Zeitnot in Szene 5 den Klima-Blick weglassen und in Szene 6 Analytics kürzen. Der Taster (Szene 5, Punkt 3) bleibt immer.
- **Stärkster Moment:** echter Taster, Licht geht an. Ist die Box nicht verkabelt, Taster im Admin-Modus auslösen und das offen sagen.
- **Nicht mehr drin** (aus der 7-Minuten-Fassung): Hoher Kontrast, Eigene Sorte, Werdegang Skizzen → Papier → Klick-Prototyp (gehört ins Booklet).

## Bedienfeld-Vorführung (ca. 2:15, nur Bildschirm)

Auf dem Bildschirm ist nur das Bedienfeld zu sehen (`localhost:8000/vorschau-praesentation.html` im Vollbild oder der Hauptlink). Wir erzählen aus Sicht von **Ingrid** (Persona A, ohne Altersangabe). **Vorher:** Zahnrad → Admin-Modus → **Zurücksetzen**. Die *kursiven* Zeilen beschreiben, was getippt wird.

| Zeit | Teil | Folien |
|---|---|---|
| 0:00–0:15 | Einstieg: Ingrid | 118 |
| 0:15–0:50 | Oberfläche und warum sie so aussieht | 16–17, 8, 50, 27, 63, G 10 |
| 0:50–1:05 | Handy verbinden | 99–100, 41–42 |
| 1:05–1:25 | Einstellungen | 60, 23, 63 |
| 1:25–1:55 | Warnmeldung: Wassertank leer | 27, 83–85, 77–79, 82 |
| 1:55–2:20 | Neuer Pilz: Ernte und neue Sorte | 61, 130 |
| 2:20–2:25 | Schluss | 41–42 |

**0:00 · Einstieg**
„Das ist das Display unserer Box. Wir zeigen es aus Sicht von Ingrid. Sie hat eine Lesebrille, leicht zitternde Hände und misstraut Technik. Sie will ihre Pilze pflegen, ohne sich etwas merken zu müssen.“

**0:15 · Oberfläche**
„Ingrid soll nach einem Blick wissen, ob sie etwas tun muss. Deshalb gibt es oben nur eine große Aussage: grüner Haken, ‚Alles gut‘. Der Ring zeigt, wie viele Tage es noch bis zur Ernte sind. Darunter stehen drei Werte, alle gleich aufgebaut: Zahl, Balken, Name. Ganz unten gibt es nur drei große Kacheln: KLIMA, MELDUNGEN, SORTEN. Wenige große Flächen trifft man auch mit zitternder Hand (Fitts' Law). Status zeigen wir nie nur über Farbe, sondern immer mit Form, Farbe und Text. Geblinkt wird nur, wenn Ingrid handeln muss.“
*Kurz auf KLIMA tippen:* „Hier sieht sie, dass die Box selbst regelt. Eingreifen kann sie hier bewusst nicht. Das Licht schaltet sie nur über den echten Taster an der Box.“ *Zurück.*

**0:50 · Handy verbinden**
*Handy-Symbol oben rechts antippen.*
„Wer will, verbindet sein Handy mit einem vierstelligen Code. Danach verschwindet das Symbol. Für Ingrid ist das freiwillig: Die Box ist ohne App vollständig bedienbar. Die App ist für den Power-User, der mehr Details möchte.“
*Zurück, ohne zu verbinden.*

**1:05 · Einstellungen**
*Zahnrad antippen.*
„Alles, was man selten braucht, liegt hier und nicht auf dem Startbild: Ruhemodus, Urlaub, Sprache, Hoher Kontrast für schlechtere Augen und ‚Fehler melden‘. Ist ein Modus aktiv, steht er dauerhaft oben, zum Beispiel RUHE. So wundert sich niemand, warum das Display dunkel ist. Ganz unten gibt es den Admin-Modus. Den brauchen wir nur für die Vorführung.“
*Admin-Modus → 1 · Fehler im Alltag → **Wassertank leer**.*

**1:25 · Warnmeldung**
„Im Alltag ist das Display meist schwarz, das ist der Ruhemodus. Bei einem Problem leuchtet nur der orange Warnpunkt und blinkt langsam. Blinken nimmt man wahr, bevor man liest, auch im Augenwinkel.“
*Display antippen.*
„Die Meldung nennt das Problem, eine konkrete Handlung und das Wort auf dem Knopf: ‚Tank im Technikraum auffüllen, dann AUFGEFÜLLT drücken.‘ Kein Fachwort, keine Schuld. Der Balken auf dem Display entspricht dem Sichtfenster am Tank (Mapping).“
*AUFGEFÜLLT drücken.*
„Die Rückmeldung kommt sofort, danach wieder ‚Alles gut‘.“

**1:55 · Neuer Pilz**
*Zahnrad → Admin-Modus → 2 · **Tag 6 der Fruchtung · Ernte fertig**.*
„Die Pilze sind reif. Ingrid erntet und drückt GEERNTET.“ *GEERNTET → Kachel SORTEN → **Neu ansetzen …** → Sorte wählen.*
„Neu ansetzen löscht den alten Durchgang. Deshalb steht vorher da, was verloren geht, und man muss den Knopf zwei Sekunden gedrückt halten. Ein versehentliches Tippen löscht also nichts.“ *2 s halten → Kammer leeren → Zuchtset einsetzen → Tag 1.*
„Und 14 Tage lang kommt sie noch zurück zur alten Sorte.“

**2:20 · Schluss**
„Ingrid braucht also kein Handy und muss sich nichts merken. Alles, was sie tun muss, steht auf dem Display.“

**Bei Zeitnot:** Klima-Blick und Sprache/Kontrast weglassen, dann etwa 1:55. **Bei mehr Zeit (bis 2:30):** in den Einstellungen Hoher Kontrast kurz an- und wieder ausschalten.

## Technik am Tag

```
 MacBook ──HDMI──► Whiteboard
   ├─ Folien (claude.ai, Präsentieren)
   ├─ Bedienfeld zum Erklären (claude.ai-Link oder localhost)
   └─ läuft: iphone-server.sh ──WLAN/Hotspot──► iPhone 13 mini in der Box (Vollbild)
 App: Gerät des App-Teammitglieds
```

- **iPhone in der Box (Vollbild):** auf dem Mac `sh 01-konzept/bedienfeld/iphone-server.sh`, die angezeigte Adresse auf dem iPhone in Safari öffnen → Teilen → „Zum Home-Bildschirm“ (Als Web-App öffnen) → Symbol „Growbox“ antippen. Am besten vorher zu Hause einrichten und den Mac in der Uni mit dem **iPhone-Hotspot** verbinden (Uni-WLAN trennt Geräte oft voneinander). Optional mit Geführtem Zugriff sperren.
- **Keine App-Kopplung am 05.11.:** Der Hauptlink zeigt das Bedienfeld ohne Verbindung zur App. Szene 6 zeigt die App allein; die Reaktion der Box („läuft noch 60 s (vom Handy)“) als Konzept erzählen und so benennen.
- **Ein Link für Mac und iPhone:** https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi. Am Mac Display im Rahmen, am iPhone füllt das Bedienfeld den Bildschirm (oben bleibt die claude.ai-Leiste; ganz ohne Leiste nur über `iphone-server.sh`). Mac und iPhone haben jeweils ihren eigenen Stand: Demo dort starten, wo sie gezeigt wird.
- **Bedienfeld am Mac (Whiteboard):** `http://localhost:8000/vorschau-praesentation.html` im Browser-Vollbild (ctrl+cmd+F), solange `iphone-server.sh` läuft: nur das Display, keine claude.ai-Leiste. Ersatz ohne Server: https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi (dort mit claude.ai-Kopfzeile des Browsers).
- **Vorher:** Zahnrad → Admin-Modus → **Zurücksetzen**, auf Mac und iPhone.
- **Admin-Modus (Zahnrad → ganz unten):** **1 · Fehler im Alltag**: eine Situation antippen → Display aus, nur der Warnpunkt blinkt → Display antippen → Meldung mit Knopf → Knopf drücken = behoben. **2 · Ernte und neue Sorte**: „Tag 6 der Fruchtung“ → GEERNTET → Kachel SORTEN → Neu ansetzen … → Sorte wählen → 2 s halten → Kammer leeren → Zuchtset einsetzen → Tag 1. Zwischen zwei Durchläufen: Zurücksetzen.
- **Probe mit Stoppuhr.**

## Risiken

| Risiko | Gegenmittel |
|---|---|
| iPhone erreicht den Mac nicht | Mac mit iPhone-Hotspot verbinden; sonst iPhone im Ruhemodus lassen und nur am Mac erklären |
| claude.ai auf dem Mac nicht angemeldet | Bedienfeld über `localhost:8000`; Folien als PDF vorher exportieren |
| App-Funktion aus Szene 6 fehlt noch | als Mockup zeigen und so benennen |
| Frage nach Hilfe/Anleitung (Nielsen Nr. 10) | Lücke offen benennen, Vorschlag Karte an der Box |
| Frage: Warum ist das Display meistens aus? | Ruhemodus ist der Regelfall. Bei Warnung leuchtet nur der Warnpunkt (Form „!“ + Helligkeit + Blinken, auch bei Rot-Grün-Schwäche erkennbar); Antippen zeigt, was zu tun ist (E22) |
| Fragen zu offenen Punkten | Warnlicht (A) und Taster-Kopplung (B): Stand vom 04.11. nennen, siehe [`entscheidungen-folien.md`](entscheidungen-folien.md#offen-für-mittwoch-0411) |
