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

**Fest: 2 Minuten** (2026-11-04). Auf dem Bildschirm ist nur das Bedienfeld (`localhost:8000/vorschau-praesentation.html` im Vollbild oder der Hauptlink). Erzählt wird aus Sicht von **Ingrid**: Lesebrille, zitternde Hände, misstraut Technik. **Vorher:** Zahnrad → Admin-Modus → **Zurücksetzen**. Start: Austernpilz frisch angesetzt, **15 Tage bis zur Ernte**.

```
0:00  OBERFLÄCHE + KLIMA ─── ein Blick · Rahmen = drückbar, Trennstrich = Text
0:30  ZAHNRAD ────────────── Kontrast + Urlaub (je 1 Satz) → Admin-Modus
0:45  CASE 1 Tank leer ───── Blinken → Handlung → Wasser → AUFGEFÜLLT
1:15  CASE 2 Ernte ───────── Zeitraffer = Gamification → Neue Sorte → Starten
1:45  CASE 3 Handy ───────── kein Handy nötig → Übergabe an Anlin
2:00
```

**Leitsatz:** Jede Stelle zeigt *eine* Idee aus der Vorlesung. Die Kacheln und Einstellungen bekommen keinen eigenen Rundgang, sie kommen dort vor, wo der Ablauf sie braucht. Der **Admin-Modus ist kein Use Case**, sondern das Werkzeug für die Vorführung; so ansagen.

### 0:00 · Oberfläche + KLIMA (30 s)
- **Sagen:** „Ingrid will pflegen, ohne sich etwas zu merken. **Ein Blick genügt:** grüner Haken, ‚Alles gut‘, nichts zu tun.“ *(Wahrnehmen → Denken → Handeln · 16–17)*
- „**Nie nur Farbe**, immer Form + Farbe + Text.“ *(Rot-Grün-Schwäche · 23, präattentiv · 26–27)* „Drei große Kacheln trifft man auch mit zitternder Hand.“ *(Fitts · 50)*
- *KLIMA antippen:* „**Alles mit Rahmen kann man drücken, alles mit Trennstrich ist nur Text.**“ *(Affordance · 72–73, Konsistenz · 80)* „Ingrid sieht, *dass* und *wann* die Box regelt, kann aber nichts verstellen.“ *(Gulf of Evaluation · 59, Modusfehler · 60)* Der **beige Kreis** ist der echte Taster an der Box. *(Mapping · 77–79)* *Zurück.*

### 0:30 · Zahnrad: Kontrast + Urlaub (15 s)
- „Selten Gebrauchtes liegt hier, nicht auf dem Startbild.“ *(minimalist design · 130)*
- **Darstellung:** „Hoher Kontrast, schwarz und weiß, für schwache Augen. Schon der Standard hat mindestens 4,5 : 1.“ *(Kontrast · 66, Sehkraft · 133)*
- **Urlaub:** „Ein Tipp, dann spart die Box Wasser und Meldungen gehen aufs Handy. Oben steht dauerhaft **URLAUB ✕**: Man sieht immer, in welchem Modus die Box ist.“ *(Modusfehler · 60, user control · 130)* Nur zeigen, nicht einschalten.
- „Ganz unten der **Admin-Modus, nur für die Vorführung**.“ → *Wassertank leer*

### 0:45 · Case 1: Tank leer (30 s)
- **Standby:** Display schwarz, nur ein **oranger Punkt blinkt**. „Blinken sieht man, bevor man liest, auch im Augenwinkel.“ *(präattentiv · 27)*
- *Antippen* → **Problem + Handlung + Knopfwort**: „Tank auffüllen, dann AUFGEFÜLLT drücken.“ „Kein Fachwort, keine Schuld.“ *(Fehlermeldungen · 83–85)*
- „Wasser oben eingießen bis zur Linie im Sichtfenster; das Sichtfenster ist der Balken auf dem Display.“ *(Mapping · 77–79)* *AUFGEFÜLLT* → sofort Rückmeldung. *(Feedback · 82)*
- *Optional (+10 s):* MELDUNGEN zeigt den Fehler grün als „behoben“.

### 1:15 · Case 2: Ernte + neue Sorte (30 s)
*Zahnrad → Admin-Modus → **Pilze fertig***
- **Zeitraffer:** Ring läuft voll, 15 → 0 Tage, der Pilz wächst in drei Stufen. „**Gamification ohne Spielfigur:** Ingrid sieht ihren Fortschritt, hat ein klares Ziel und bekommt sofort Rückmeldung.“ *(Progression · G 10, Flow · G 12)*
- „Oben steht weiter ‚Alles gut‘: ein Hinweis, keine Warnung, denn nichts ist kaputt.“ → *Geerntet? Neue Sorte*
- *Sorte antippen:* „Schwierigkeit als 1–3 Pilze **wie ein Level**.“ *(Levels · G 10)* Detailseite → *Neu ansetzen* → **„Sicher?“** → *Starten* → **Tag 1**.
- „Die Kammer ist schon leer, also keine Rückfrage. Mitten im Wachstum müsste man 2 s gedrückt halten.“ *(Murphy · 61, Fehler vermeiden · 130)*

### 1:45 · Case 3: Handy verbinden (15 s)
- „Bis hier braucht Ingrid **kein Handy**.“ *Handy-Symbol* → Code → *VERBUNDEN* → **Symbol verschwindet**.
- „Wer mehr will, nutzt die App: gleiche Wörter, gleiche Farben.“ *(äußere Konsistenz · 80)* → **Übergabe an Anlin.**

**Zu lang?** Zuerst MELDUNGEN weglassen (falls drin), dann Urlaub (−10 s), dann bei der Oberfläche nur „ein Blick“ und „Rahmen = drückbar“ sagen. **Zweiter Durchlauf:** Zurücksetzen oder neu laden (das Handy-Symbol ist dann wieder da).

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
