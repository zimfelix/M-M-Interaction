# Präsentation 05.11.2026 · ca. 5 Minuten, ohne Folien

**Keine Folien** (2026-11-04): Wir zeigen live, was es gibt: den 3D-Entwurf, das Bedienfeld und die App. Leitidee: **Dieselbe Box, zwei Menschen.** Ingrid nutzt nur die Box, der Power-User zusätzlich die App. Personas ohne Altersangabe. Der frühere Foliensatz (https://claude.ai/artifact/DcLZePjqNpwgHBrxHGHFha) wird nicht gezeigt.

Begründungen im Detail: [`entscheidungen-folien.md`](entscheidungen-folien.md) (E1–E30). Folienbelege: [`../01-konzept/folien-recherche.md`](../01-konzept/folien-recherche.md).

## Ablauf

| Zeit | Wer | Was auf dem Bildschirm | Inhalt |
|---|---|---|---|
| 0:00–ca. 1:15 | Teammitglied | 3D-Entwurf der Box | Das Haptische: Taster, Griffe, Tank mit Sichtfenster, Farbprinzip (Beige = anfassen) |
| ca. 1:15–3:15 | **Felix** | **Bedienfeld** | Oberfläche und Begründung, dann 3 Fälle (unten) |
| ca. 3:15–4:45 | Anlin | App | Übernimmt nach „Handy verbinden“ |

## Bedienfeld · Spickzettel für 2:00

**Vorher:** Bedienfeld im Vollbild. Zahnrad, Admin-Modus, Zurücksetzen, Zurück. Start bei 15 Tagen bis zur Ernte.

**Tempo:** ruhig sprechen. Der Text hat rund 210 Wörter, das sind etwa 1:45. Der Rest ist Luft für das Tippen. Beim Zeitraffer einfach schweigen.

```
0:00  Oberfläche
0:30  Zahnrad
0:40  Fall 1 · Tank leer
1:10  Fall 2 · Ernte
1:45  Fall 3 · Handy
2:00
```

### 0:00 · Oberfläche
*Tippen: KLIMA, dann Zurück.*

„Das ist Ingrid. Sie sieht schlecht, und ihre Hände zittern.

Ein Blick genügt. Grüner Haken, Alles gut. Sie muss nichts tun.

Wir haben bewusst minimalistisch gestaltet. Wenig auf dem Bildschirm, dafür große Knöpfe. Farbe steht nie allein, immer auch ein Symbol und ein Wort.

*KLIMA* Hier sieht sie: Die Box regelt alles selbst.

Was einen Rahmen hat, kann man drücken. Was zwischen Linien steht, ist nur Information. Das ist Affordance: Man sieht, was man drücken kann.“

### 0:30 · Zahnrad
*Tippen: Zahnrad, Admin-Modus, Fehlermeldung.*

„Selten Gebrauchtes liegt hinter dem Zahnrad. Zum Beispiel hoher Kontrast für schwache Augen und der Urlaub. Unten der Admin-Modus, nur für die Vorführung.“

### 0:40 · Fall 1: Tank leer
*Tippen: Punkt, dann Aufgefüllt.*

„Fall eins: Der Tank ist leer.

Das Display ist schwarz, nur ein oranger Punkt blinkt. Den sieht man sofort.

*Punkt* Jetzt steht da: Wasser leer, Tank im Technikraum auffüllen. Ein Satz, ein Knopf.

Sie gießt oben Wasser ein, bis zur Linie im Sichtfenster.

*Aufgefüllt* Sofort steht wieder Alles gut da.“

### 1:10 · Fall 2: Ernte
*Tippen: Zahnrad, Admin-Modus, Ernte fertig. Dann Geerntet? Neue Sorte, eine Sorte, Neu ansetzen, Starten.*

„Fall zwei: Die Pilze sind reif. Wir spulen kurz vor.

*5 Sekunden schweigen*

Der Ring füllt sich, der Pilz wächst. Das ist unsere Gamification. Jetzt steht da: Erntebereit.

*Geerntet? Neue Sorte* Sie wählt eine neue Sorte. Die kleinen Pilze zeigen, wie schwer sie ist.

*Neu ansetzen* Die Kammer ist schon leer. Darum reicht eine kurze Frage. *Starten* Tag eins.“

### 1:45 · Fall 3: Handy
*Tippen: Handy-Symbol, dann Verbunden.*

„Bis hierhin braucht Ingrid kein Handy. Wer mehr will, verbindet sein Handy. Das zeigt euch jetzt Anlin.“

### Probelauf mit Stoppuhr

| ✓ | Marke | Bin ich hier spätestens? |
|---|---|---|
| ☐ | 0:30 | Zurück aus KLIMA |
| ☐ | 0:40 | Fehlermeldung angetippt |
| ☐ | 1:10 | Aufgefüllt gedrückt |
| ☐ | 1:45 | Starten gedrückt |
| ☐ | 2:00 | Übergabe an Anlin |

**Zu lang?** Zuerst den Satz zur Affordance weglassen. Dann beim Zahnrad nur „Selten Gebrauchtes liegt hier“ sagen. **Zweiter Durchlauf:** Zurücksetzen oder neu laden.

**Nachfragen zu Folien:** Begründungen mit Foliennummern stehen in `entscheidungen-folien.md`, E1 bis E31.

## Technik am Tag

```
 MacBook ──HDMI──► Whiteboard
   ├─ 3D-Entwurf (Teammitglied)
   ├─ Bedienfeld (localhost oder claude.ai-Link)
   └─ läuft: iphone-server.sh ──WLAN/Hotspot──► iPhone 13 mini in der Box (Vollbild)
 App: am MacBook bzw. Gerät von Anlin
```

- **iPhone in der Box (Vollbild):** auf dem Mac `sh 01-konzept/bedienfeld/iphone-server.sh`, die angezeigte Adresse auf dem iPhone in Safari öffnen → Teilen → „Zum Home-Bildschirm“ (Als Web-App öffnen) → Symbol „Growbox“ antippen. Am besten vorher zu Hause einrichten und den Mac in der Uni mit dem **iPhone-Hotspot** verbinden (Uni-WLAN trennt Geräte oft voneinander). Optional mit Geführtem Zugriff sperren.
- **Keine App-Kopplung am 05.11.:** Der Hauptlink zeigt das Bedienfeld ohne Verbindung zur App. „Handy verbinden“ zeigt nur den Ablauf; danach zeigt Anlin die App allein.
- **Ein Link für Mac und iPhone:** https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi. Am Mac Display im Rahmen, am iPhone füllt das Bedienfeld den Bildschirm (oben bleibt die claude.ai-Leiste; ganz ohne Leiste nur über `iphone-server.sh`). Mac und iPhone haben jeweils ihren eigenen Stand: Demo dort starten, wo sie gezeigt wird.
- **Bedienfeld am Mac (Whiteboard):** `http://localhost:8000/vorschau-praesentation.html` im Browser-Vollbild (ctrl+cmd+F), solange `iphone-server.sh` läuft: nur das Display, keine claude.ai-Leiste. Ersatz ohne Server: der Hauptlink.
- **Probe mit Stoppuhr.**

## Risiken

| Risiko | Gegenmittel |
|---|---|
| iPhone erreicht den Mac nicht | Mac mit iPhone-Hotspot verbinden; sonst nur am Mac zeigen |
| claude.ai auf dem Mac nicht angemeldet | Bedienfeld über `localhost:8000` |
| App-Funktion fehlt noch | als Mockup zeigen und so benennen |
| Frage nach Hilfe/Anleitung (Nielsen Nr. 10) | Lücke offen benennen, Vorschlag Karte an der Box |
| Frage: Warum war das Display schwarz? | Standby in der Box: Bei einem Problem leuchtet nur der orange Punkt und blinkt (Helligkeit + Blinken auf Schwarz, auch bei Rot-Grün-Schwäche erkennbar); Antippen zeigt, was zu tun ist (E22). Einen Ruhemodus zum Einstellen gibt es nicht. |
| Frage: Warum schaltet der Taster nicht auch das Display? | Der Taster hat **eine feste Bedeutung: Licht an/aus** (kein Modus, Ergebnis sichtbar durchs Plexiglas, Folie 60 und 72–73). Einen Ruhemodus gibt es nicht. |
| Frage nach HCI-Grundprinzipien | Norman: Affordance (Taster), Mapping (Sichtfenster), Feedback (AUFGEFÜLLT); Nielsen-Check 9 von 10 ([Nielsen-Check](entscheidungen-folien.md#nielsen-check-folie-130)) |
