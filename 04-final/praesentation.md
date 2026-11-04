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

Auf dem Bildschirm ist nur das Bedienfeld (`localhost:8000/vorschau-praesentation.html` im Vollbild oder der Hauptlink). Erzählt wird aus Sicht von **Ingrid**: Lesebrille, zitternde Hände, misstraut Technik. **Vorher:** Zahnrad → Admin-Modus → **Zurücksetzen**. Start: Austernpilz frisch angesetzt, **15 Tage bis zur Ernte**.

```
0:00  OBERFLÄCHE + KLIMA ──────── ein Blick genügt, Box regelt selbst
0:35  CASE 1 Tank leer ─────────── Zahnrad (Settings) → Admin → Warnung → MELDUNGEN
1:15  CASE 2 Pilze fertig ──────── Zeitraffer → „Geerntet? Neue Sorte“
1:45  CASE 3 Handy verbinden ───── Übergabe an Anlin
2:00
```

Die **drei Kacheln** (KLIMA · MELDUNGEN · SORTEN) und die **Einstellungen** bekommen keinen eigenen Rundgang. Jede kommt dort vor, wo sie im Ablauf ohnehin gebraucht wird.

### 0:00 · Oberfläche + KLIMA (35 s)
- **Ingrid** will pflegen, ohne sich etwas zu merken.
- **Ein Blick:** grüner Haken „Alles gut“ = nichts zu tun. *(Ein Zustand, ein Satz · Folie 16–17)*
- **Ring** = Tage bis zur Ernte. **3 große Kacheln**: trifft man auch mit zitternder Hand. **Nie nur Farbe**: immer Form + Farbe + Text. *(Fitts · 50, Barrierefreiheit · 23, 63)*
- *Kachel KLIMA:* vier Zeilen, alle **AUTO**, mit Bedingung (Nebler an unter 70 % Feuchte …). Ingrid sieht, *dass* und *wann* geregelt wird, kann aber nichts verstellen. Licht: Zeitplan, und der **beige Kreis** zeigt den echten Taster, mit dem sie umschaltet (Mapping · 77–79). *(Gulf of Evaluation · 59, Modusfehler · 60)* *Zurück.*

### 0:35 · Case 1: Tank leer + MELDUNGEN (40 s)
*Zahnrad:* „Selten Gebrauchtes liegt hier: Urlaub, Sprache, Kontrast und Hilfe mit der roten Flagge. Ganz unten der Admin-Modus für die Vorführung.“ *Admin-Modus → **Wassertank leer***
- **Standby:** Display schwarz, kein Text, **nur ein oranger Punkt blinkt**. Blinken sieht man, bevor man liest, auch im Augenwinkel. *(präattentiv · 27)*
- *Antippen* → Blinken aus, normale Ansicht mit **Problem + Handlung + Knopfwort**: „Tank auffüllen, dann AUFGEFÜLLT drücken.“ Kein Fachwort, keine Schuld. *(83–85)*
- **Haptisch:** oben Wasser eingießen bis zur Linie im Sichtfenster; Sichtfenster = Balken auf dem Display. *(Mapping · 77–79)* *AUFGEFÜLLT* → sofort Rückmeldung. *(Feedback · 82)*
- *Kachel MELDUNGEN:* Der Fehler steht jetzt **grün als „behoben“** im Verlauf. Ingrid sieht, dass alles erledigt ist. *Zurück.*

### 1:15 · Case 2: Pilze fertig → SORTEN (30 s)
*Zahnrad → Admin-Modus → **Tag 6 der Fruchtung · Ernte fertig***
- **5 s Zeitraffer:** Ring läuft voll, Tage zählen 15 → 0, der Pilz wächst sichtbar (klein → mittel → groß). Das ist die leichte Gamification: Fortschritt sehen, ohne Punkte oder Spielfigur. *(Progression, Flow · G 10, G 12)*
- Der Ring ist voll, oben steht weiter **„Alles gut“**, darunter der Knopf **„Geerntet? Neue Sorte“**: ein Hinweis, keine Warnung, denn nichts ist kaputt. → *antippen* → öffnet **direkt die Sortenwahl**.
- *Sorte wählen* (Schwierigkeit als ●○○, Dauer in Tagen): Vorher steht da, **was verloren geht**, dann **2 s gedrückt halten**. Versehen ist ausgeschlossen. *(Murphy · 61, Fehler vermeiden · 130)*
- *Kammer leeren → Zuchtset einsetzen* → **Tag 1, es geht von vorn los.**

### 1:45 · Case 3: Handy verbinden (15 s)
- „Bis hier braucht Ingrid **kein Handy**.“ *Handy-Symbol* → Code → *VERBUNDEN* → **Symbol verschwindet**.
- „Wer mehr will, nutzt die App.“ → **Übergabe an Anlin.**

**Zu lang?** Zuerst die MELDUNGEN-Kachel weglassen (−10 s), dann bei der Oberfläche nur „ein Blick“ und „nie nur Farbe“ sagen. **Zweiter Durchlauf:** Zurücksetzen oder neu laden (das Handy-Symbol ist dann wieder da).

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
| Frage zur Taster-Kopplung (B) | Stand vom 04.11. nennen, siehe [`entscheidungen-folien.md`](entscheidungen-folien.md#offen-für-mittwoch-0411) |
| Frage nach HCI-Grundprinzipien | Norman: Affordance (Taster), Mapping (Sichtfenster), Feedback (AUFGEFÜLLT); Nielsen-Check 9 von 10 ([Nielsen-Check](entscheidungen-folien.md#nielsen-check-folie-130)) |
