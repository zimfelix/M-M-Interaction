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
| 1:45–3:30 | Felix | 5 Ingrid live | Bedienfeld am Mac, iPhone in der Box: Alles gut → Szenario **„Display aus · Warnung“**: Display schwarz, nur der Warnpunkt blinkt → antippen → Wasser leer → AUFGEFÜLLT → Taster drücken | 23, 26, 27, 63, 77–79, 33 |
| 3:30–4:30 | App-Teammitglied | 6 Der Nerd | Push mit denselben Wörtern → Analytics → 1 Min lüften, Box zeigt „läuft noch 60 s (vom Handy)“ | 80–81, 101–102, 57–58 |
| 4:30–5:00 | alle | 7 Fazit | Pointe, Nielsen 9 von 10, Lücke Hilfe mit Vorschlag Karte | 130 |

- **Zeitpuffer:** Bei Zeitnot in Szene 5 den Klima-Blick weglassen und in Szene 6 Analytics kürzen. Der Taster (Szene 5, Punkt 3) bleibt immer.
- **Stärkster Moment:** echter Taster, Licht geht an. Ist die Box nicht verkabelt, Taster im Admin-Modus auslösen und das offen sagen.
- **Nicht mehr drin** (aus der 7-Minuten-Fassung): Hoher Kontrast, Eigene Sorte, Werdegang Skizzen → Papier → Klick-Prototyp (gehört ins Booklet).

## Technik am Tag

```
 MacBook ──HDMI──► Whiteboard
   ├─ Folien (claude.ai, Präsentieren)
   ├─ Bedienfeld zum Erklären (claude.ai-Link oder localhost)
   └─ läuft: iphone-server.sh ──WLAN/Hotspot──► iPhone 13 mini in der Box (Vollbild)
 App: Gerät des App-Teammitglieds
```

- **iPhone in der Box (Vollbild):** auf dem Mac `sh 01-konzept/bedienfeld/iphone-server.sh`, die angezeigte Adresse auf dem iPhone in Safari öffnen → Teilen → „Zum Home-Bildschirm“ (Als Web-App öffnen) → Symbol „Growbox“ antippen. Am besten vorher zu Hause einrichten und den Mac in der Uni mit dem **iPhone-Hotspot** verbinden (Uni-WLAN trennt Geräte oft voneinander). Optional mit Geführtem Zugriff sperren.
- **Vollbild vor App-Sync (04.11.):** Das iPhone in der Box ist nicht mit der App verbunden. Szene 6 (Push, „läuft noch 60 s (vom Handy)“) deshalb am **Bedienfeld am Mac über den claude.ai-Link** zeigen und vorher dort mit der App koppeln (Handy-Symbol → Code).
- **Ein Link für Mac und iPhone:** https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi. Am Mac Display im Rahmen, am iPhone füllt das Bedienfeld den Bildschirm (oben bleibt die claude.ai-Leiste; ganz ohne Leiste nur über `iphone-server.sh`). Mac und iPhone haben jeweils ihren eigenen Stand: Demo dort starten, wo sie gezeigt wird.
- **Bedienfeld am Mac (Whiteboard):** `http://localhost:8000/vorschau-praesentation.html` im Browser-Vollbild (ctrl+cmd+F), solange `iphone-server.sh` läuft: nur das Display, keine claude.ai-Leiste. Ersatz ohne Server: https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi (dort mit claude.ai-Kopfzeile des Browsers).
- **Vorher:** Zahnrad → Admin-Modus → **Zurücksetzen**, auf Mac und iPhone.
- **Demo Display aus:** Zahnrad → Admin-Modus → **„Display aus · Warnung“**: Display wird schwarz, nach 4 s blinkt nur der Warnpunkt. Antippen zeigt „Wasser leer“. Danach Ruhemodus unter Einstellungen wieder ausschalten oder Zurücksetzen.
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
