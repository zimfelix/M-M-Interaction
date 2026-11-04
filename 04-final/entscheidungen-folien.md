# Entscheidungen · Personen · Folien

Grundlage für **Präsentation (05.11.)** und **Booklet (08.11.)**. Jede Design-Entscheidung lässt sich auf eine der zwei Personen zurückführen und wird mit einer Vorlesungsfolie **ausdrücklich begründet**: Was sagt die Folie, und was folgt daraus für die Box?

- **Folie N** = Seitenzahl im PDF `WS26_HCI - Vorlesungsfolien.pdf`, **G N** = `HCI - Vorlesungsfolien_Gamification.pdf` (Sammlung aller Konzepte: [`../01-konzept/HCI-KONZEPTE.md`](../01-konzept/HCI-KONZEPTE.md))
- Verbindlicher Stand der Entscheidungen: [`../BRIEF.md`](../BRIEF.md), Tabelle „Entscheidungen“
- Geprüft gegen **Bedienfeld v6** (`01-konzept/bedienfeld/index.html`, 02.11.2026), live: https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi
- Gleiche Wörter in Box und App: [`../01-konzept/begriffe-box-app.md`](../01-konzept/begriffe-box-app.md)
- Was die Folien wörtlich zeigen, Farbsimulation, Kontrastmessung, Gamification-Mechaniken: [`../01-konzept/folien-recherche.md`](../01-konzept/folien-recherche.md)

## Die zwei Personen

Personas sind **Annahmen** (idealtypische Nutzer, Folie 118). Im Booklet benennen, was Tests bestätigt oder geändert haben.

| | **A · Ingrid** (wenig bedienen) | **B · Power-User, „der Nerd“** (App als Zusatz) |
|---|---|---|
| Quelle | [`../01-konzept/personas-storyboard.md`](../01-konzept/personas-storyboard.md), Persona 3 | **Entwurf**: technikaffiner „Nerd“, trackt alles (Präsentation ohne Altersangaben, 04.11.) |
| Nutzt | nur die Box: Display und Taster | Box im Vorbeigehen, **App** unterwegs und für Details |
| Motiv (Warum, Folie 139) | etwas Sinnvolles pflegen, ohne sich etwas merken zu müssen | Ernte optimieren, verstehen, was in der Kammer passiert |
| Fähigkeiten | Lesebrille, leicht zitternde Hände, misstraut Technik | technikaffin, liest Messwerte und Verläufe gern |
| Frustriert, wenn … | Schrift klein ist, Gesten versteckt sind, Fehler nach Schuld klingen | er nicht eingreifen kann oder Box und App Verschiedenes zeigen |
| Spielertyp (G 13–14) | Philanthropist: kümmert sich gern | Achiever: will Fortschritt messen und verbessern |

Leitfrage der Aufteilung: **Box für A, App als Zusatz für B, beide sehen denselben Zustand.**

```
Braucht die Aufgabe den Körper an der Box?   ── ja ──► Box  (A und B: nachfüllen, ernten, neu ansetzen, Licht)
        │ nein
Muss jeder es sofort sehen?                  ── ja ──► Box zeigt es, App pusht es  (Warnungen)
        │ nein
        └────────────────────────────────────────────► App  (B: Analytics, 1 Min lüften, eigene Sorte, teilen)
```

## Entscheidungen mit Begründung

| # | Entscheidung (Stand v6) | Für | Folie | Erklärung: Folie sagt … → deshalb … |
|---|---|---|---|---|
| E1 | Startbild hat nur **2 Zustände**: „Alles gut“ (grüner Kreis mit Haken) oder **Warnung** (gelbes Dreieck), immer **Form + Farbe + Text** | A | 26–27, 23 | Eine einzelne Farbe wird **präattentiv**, also ohne bewusstes Suchen, erkannt. Rot-Grün-Schwäche betrifft ca. 8 % der Männer. → Der Zustand ist über die Farbe sofort erkennbar und über Symbol und Wort trotzdem eindeutig (redundante Codierung). |
| E2 | Pro Bildschirm **eine Hauptaussage**, darunter ein Satz („Klima regelt sich automatisch.“) | A | 16–17 | Model Human Processor: Wahrnehmen → Denken → Handeln. Jede zusätzliche Information verlängert den Denk-Schritt. → Ingrid weiß nach einem Blick, ob sie etwas tun muss. |
| E3 | **3 große Kacheln** KLIMA · MELDUNGEN · SORTEN, jeweils großes Wort + kleine Zeile (Auto / Zahl / Neu); Ruhemodus und Urlaub unter dem Zahnrad | A | 8, 38, 50, 130 | Folie 8 „Die unbedienbare Mikrowelle“: wenige eindeutige Bedienelemente statt vieler Tasten. Das Kurzzeitgedächtnis ist begrenzt (38; eine konkrete Zahl steht nicht auf der Folie, dafür extern Cowan 2001: ca. 4). **Fitts' Law** (50): Große, nahe Ziele trifft man schneller und sicherer. Nielsen (130): *Aesthetic and minimalist design*. → Weniger und breitere Kacheln passen zu Ingrids zitternden Händen. Selten Genutztes (Ruhemodus) bekommt keinen Hauptplatz. |
| E4 | **Größere Schrift**, Beschriftungen ohne Großbuchstaben | A | 63 | Schriftgröße muss zu Sichtabstand und Auflösung passen (hier ca. 50–70 cm, 5,4″-Display). → Beschriftungen ca. 15 px statt 11 px, damit sie auch mit Lesebrille lesbar sind. |
| E5 | Klima-Punkt **leuchtet ruhig**; geblinkt wird **nur beim Warnpunkt** (E22) | A | 27, 45–47 | Folie 27 zählt **„Blinking“** zu den präattentiven Merkmalen: Blinken zieht die Aufmerksamkeit an sich, bevor man liest. Unnötige Reize sind **extrinsische kognitive Last** (47). → Für „läuft“ wäre Blinken falsch. Wir reservieren es für den einen Fall, in dem gehandelt werden muss. |
| E6 | **Automatik sichtbar**: Kachel Klima zeigt Lüfter, Nebler, Heizung, Licht mit **AUTO** und „nächstes Lüften in X Min“ | A, B | 56, 59 | Das **mentale Modell** des Nutzers entsteht aus dem, was das System zeigt. **Gulf of Evaluation**: Man muss erkennen können, was das System gerade tut. → Ingrid versteht, dass sie nichts regeln muss. Der Power-User sieht, *dass* und *wann* geregelt wird. |
| E7 | An der Box **kein Eingriff ins Klima**. „1 Min lüften/befeuchten“ gibt es **nur in der App** | A, B | 60, 61, 57–58 | Jede manuelle Ausnahme ist ein Zustand, den man vergessen kann (**Modusfehler**). Was schiefgehen kann, geht schief (**Murphy**). Mehrere Wege zum Ziel sind gut für Fortgeschrittene (**Flexibilität**). → Ingrid kann die Automatik nicht versehentlich stören. Der Power-User behält die Kontrolle in der App. |
| E8 | Jede Warnung nennt **eine konkrete Handlung** und das **Wort auf dem Knopf**: „Tank auffüllen, dann AUFGEFÜLLT drücken.“ | A | 83–85, 59 | Fehlermeldungen sollen **spezifisch, konstruktiv und höflich** sein. Der **Gulf of Execution** schließt sich, wenn klar ist, was zu tun ist. → Keine Schuld, kein Fachwort, ein Knopf. |
| E9 | Rückmeldung nach jeder Aktion („Tank voll · Nebler läuft wieder“, danach wieder „Alles gut“) | A, B | 82, 64–65 | **Feedback** visuell und, beim Taster, haptisch. Unter 100 ms wirkt eine Reaktion direkt, unter 1 s kausal. → Der Text erscheint sofort, auch wenn die Feuchte erst später steigt. |
| E10 | **Taster = nur Licht**, feste Bedeutung, haptisch. Das Ergebnis sieht man durchs Plexiglas. Licht hat deshalb **keine Kachel**; das Klima-Fenster verweist auf den „Taster unter dem Display“ | A | 33, 49, 72–74, 59, 57–58 | Finger sind besonders dicht mit Sinneszellen besetzt (33, Homunculus): Ein echter Knopf gibt spürbares Feedback. Touch braucht Zielgenauigkeit (49, Speed-Accuracy), einen großen Taster trifft man auch mit zitternder Hand. Ein Knopf hat eine eindeutige **Affordance** (72–74). Das Ergebnis ist direkt sichtbar (59). Licht geht zusätzlich per App (57–58). → Ingrid hat eine Funktion ohne Display, ohne Menü und ohne Modus. |
| E11 | **Neu ansetzen** nur nach Hinweis, was verloren geht, und **2 s gedrückt halten**; Notfall „Zurück zu …“ 14 Tage lang | A | 61, 130 | Kritisches nur mit Bestätigung oder rückgängig machbar (**Murphy**). Nielsen-Heuristiken: **Fehler vermeiden** und **Kontrolle und Freiheit** (Undo). → Ein versehentliches Tippen löscht keinen Durchgang. |
| E12 | Modi **Ruhemodus** und **Urlaub** stehen oben dauerhaft sichtbar (`RUHE`, `URLAUB ✕`) | A, B | 60 | Wenn ein Modus nötig ist, muss er **immer sichtbar** sein, sonst entstehen Modusfehler. → Man sieht, warum das Display dunkler ist, und kann Urlaub mit einem Tipp beenden. |
| E13 | **Ring = Fortschritt bis zur Ernte**, in der Mitte „X Tage“ bzw. „Jetzt ernten“ | A, B | G 10, G 12 | Gamification-Mechanik **Progression**. **Flow** braucht ein klares Ziel und sofortiges Feedback. → Beide sehen, wohin es geht, ohne Spielfigur oder Punkte. |
| E14 | Drei Werte **einheitlich**: Zahl mit Einheit, Balken, darunter nur der Name (**Temperatur · Luftfeuchte · Wassertank**). Temperatur und Feuchte mit hellem Zielbereich und Punkt, Tank als Füllstand mit Kurzangabe `60 % · 4 T`; ausgeschrieben „reicht ca. 4 Tage“ im Klima-Fenster | A, B | 45–47, 80, 86–87, G 10 | Rohzahlen erzeugen kognitive Last (47). **Syntaktische Konsistenz** (80): gleiche Elemente, gleicher Aufbau. **Physikanalogie** (86–87): Ein Füllstand wird ohne Erklärung verstanden. Details stufenweise zeigen (*Cascading Information*, G 10). → Ingrid liest „Punkt im hellen Bereich = passt“. Der Power-User hat zusätzlich die Zahl. |
| E15 | **Sichtfenster am Tank** mit Linie, passend zum Füllstandsbalken „Wassertank“ auf dem Display | A | 77–79 | **Mapping**: Anzeige und Gerät entsprechen sich räumlich und inhaltlich (Herdplatten-Beispiel). → Was das Display sagt, sieht Ingrid auch an der Box. |
| E16 | **Box ohne App vollständig bedienbar**, alles Nötige sichtbar, keine versteckten Gesten | A | 41–42 | Die Box wird nur alle paar Tage bedient, man **vergisst** dazwischen (Ebbinghaus). → Wiedererkennen statt Erinnern. Ingrid braucht kein Handy. |
| E17 | **Ein Zustand, zwei Ansichten**: Box und App lesen denselben Stand (Pi bzw. claude.ai-Speicher) | B | 99–100 | **Model View Controller**: ein Modell, mehrere Views. → Was der Power-User unterwegs in der App tut, zeigt die Box sofort („läuft noch 60 s (vom Handy)“). |
| E18 | **Gleiche Wörter, Symbole, Farben** in Box und App ([Begriffsliste](../01-konzept/begriffe-box-app.md)) | B | 80–81 | **Äußere Konsistenz** zwischen Produkten. → Der Power-User muss nichts doppelt lernen, und nichts widerspricht sich. |
| E19 | **App für Details**: Push, Advanced Analytics, eigene Sorte, 1 Min lüften, Ernte teilen | B | 101–102, 140, G 13–14 | **Zoomable UI**: erst Übersicht, dann Detail. Sheldon: **Autonomie und Kompetenz** als Bedürfnisse. → Die Box bleibt Übersicht. Wer mehr will, zoomt in der App hinein. |
| E21 | **Warntexte weiß**, Orange nur für Dreieck, Rahmen und Knopf; Nebentexte `#dfe4ff`; Werte außerhalb des Bereichs mit **Warndreieck** statt nur oranger Schrift | A | 66, 23, 26 | Folie 66 fragt nach Bildschirmkontrast: Orange auf hellem Blau erreichte nur 2,8 : 1 (WCAG-Ziel ≥ 4,5, externe Quelle), jetzt 6,4 : 1. Folie 23: Bei Rot-Grün-Schwäche sind unser Grün und Orange fast gleich (eigene Simulation). → Jede Abweichung braucht zusätzlich eine **Form** (26). Details: [`folien-recherche.md`](../01-konzept/folien-recherche.md). |
| E22 | **Warnpunkt** oben in der Mitte: orange mit „!“, **blinkt langsam**, sobald eine Warnung ansteht; sonst nur dunkler Ring | A | 26, 27, 23, 130, 63 | Ein einzelnes Signal auf ruhigem Grund wird **präattentiv** erkannt (26). Hell/dunkel, Blinken und „!“ funktionieren auch bei Rot-Grün-Schwäche (23). **Warnlicht bei dunklem Display** (04.11.): Im Regelfall ist das Display im Ruhemodus schwarz; bei Warnung leuchtet nur der Punkt, Antippen zeigt die Meldung. *Visibility of system status* (130). Die Box ist ein **Display im Raum**, kein Handy in der Hand: Aus 2–3 m kann man keinen Text lesen (Sichtabstand, 63), einen blinkenden Punkt aber schon (Blinken ist präattentiv, 27). Langsam (< 3 Blitze/s, WCAG, extern), nie ganz dunkel, bei „Bewegung reduzieren“ ruhig. |
| E23 | **Kopfzeile als eine Zeile, alles 44 pt hoch**: Sorte · Warnpunkt · Handy + Zahnrad als gleich große Knöpfe mit Rahmen; **Uhr entfernt** | A | 50, 72–73, 130 | Fitts' Law (50): Größere Ziele trifft man leichter. Die Folien nennen keine Zahl, die Mindestgröße 44 pt stammt aus Apples Human Interface Guidelines (externe Quelle). Der Rahmen zeigt, dass es ein Knopf ist (Affordance, 72–73). Die Uhr war für die Pilzpflege überflüssig: *minimalist design* (130). |
| E24 | **Handy-Symbol** rechts neben dem Zahnrad (Einrichtung gruppiert); nach VERBUNDEN ausgeblendet, über Einstellungen wieder erreichbar | A, B | 130, 41–42 | Einmaliger Einrichtungsschritt: Ist er erledigt, muss man ihn nicht mehr sehen (*minimalist design*, 130). Er bleibt über Einstellungen erreichbar und ist umkehrbar (*user control and freedom*, 130). |
| E25 | **Blauer Hintergrund** nur als Fläche; Schrift weiß; Grün/Orange exklusiv für den Status, kein Rot | A, B | 20, 22, 23, 26, 76 | Blau wird über eigene S-Zapfen gesehen (22) und eignet sich nicht für feine Details (20, extern: wenige Blau-Zapfen in der Fovea), deshalb nur als Fläche. Ein ruhiger Grund lässt Statusfarben präattentiv herausspringen (26). Die Blau-Gelb-Achse bleibt bei Rot-Grün-Schwäche erhalten (23, eigene Simulation). Blau ist kulturell neutral (76). |
| E26 | **Einstellungen** um **Sprache**, **Darstellung** (Standard / Hoher Kontrast) und **Fehler melden** ergänzt; gleiche Liste, gleich leicht zu finden | A, B | 75, 66, 130, 133 | Nicht verfügbare Sprachen sind **ausgegraut** statt scheinbar wählbar (logischer Constraint, 75). Hoher Kontrast (schwarz, alles weiß) für schwache Augen: Bildschirmkontrast (66), Sehkraft als Nutzermerkmal (133). Fehler melden mit einem Tippen: *help users recognize, diagnose, and recover from errors* (130). |
| E27 | **Meldungs-Verlauf grün mit Haken** („behoben · von – bis“), offene Meldungen orange mit Dreieck | A | 59, 76, 26 | Behobenes sah vorher wie eine Warnung aus (gelbes Dreieck): Man konnte nicht bewerten, ob noch etwas zu tun ist (**Gulf of Evaluation**, 59). Grün mit Haken = erledigt ist kulturell gelernt (76) und präattentiv unterscheidbar (26). |
| E28 | **SORTEN · Neu**: oben sichtbar „Neu ansetzen …“ (Sorte wählen, aktuelle zuerst), darunter Sorten ansehen | A, B | 130, 95, 61 | Das „Neu“ der Kachel muss man auch finden (*Visibility*, 130). Handeln (neu ansetzen) und Stöbern (Sorten ansehen) sind getrennt (Suchen vs. Stöbern, 95). Die Bestätigung mit 2 s Halten bleibt (Murphy, 61). |
| E29 | **Lesbarkeit und Treffsicherheit überall**: Schrift in Meldungen/Listen ≥ 15 pt, alle Touch-Ziele ≥ 44 pt (auch „Zurück“), Ruhemodus-Text lesbar | A | 63, 50 | Sichtabstand (63) und Fitts (50) gelten nicht nur fürs Startbild, sondern für jede Ebene. Zahlen extern: Apple HIG 44 pt, WCAG 4,5 : 1. |
| E30 | **Orange nur für Warnungen, auch an der Box**: Taster, Türgriff und Deckelgriff **beige**, Bedienfeld-Front schwarz glänzend, Taster mit eingeprägtem **Licht-Symbol** (Skizze `02-box-bau/zeichnungen/skizze-box-v3.html`) | A, B | 80, 72–74, 130, 26 | **Konsistenz** (80): Eine Farbe hat überall dieselbe Bedeutung. Auf dem Display heißt Orange „Warnung“ (E25), deshalb darf ein Bedienteil nicht orange sein. Beige hebt die Teile zum Anfassen vom schwarzen Rahmen ab, ohne eine Statusfarbe zu sein. Ein Taster zeigt, *dass* man ihn drücken kann (Affordance, 72–74), aber nicht, *was* er tut. Das Licht-Symbol macht ihn wiedererkennbar (*Recognition rather than recall*, 130). → Ein mögliches Warnlicht an der Box (Offen A1) wäre orange und damit konsistent. |
| E20 | **Admin-Modus** versteckt (Einstellungen → ganz unten) | – | 60 | Nicht personenbezogen, nur für die Vorführung. Er bleibt verborgen, damit kein Nutzer versehentlich hineingerät. |

## Entschieden am 04.11. (früher „Offen für Mittwoch“)

**A · Warnlicht:** Kein physisches Warnlicht an der Box. Die Warnung zeigt nur der Warnpunkt auf dem Display; im Ruhemodus bleibt das Display schwarz und nur der Punkt leuchtet (E22). Die Abwägung unten bleibt als Begründung stehen.

## Offen für Mittwoch (04.11.)

Zwei Fragen zum Taster und zur Warnung. Gemeinsamer Grundsatz für beide: **Eine Warnung muss immer sichtbar sein**, egal ob Ruhemodus, Licht aus oder Display schwarz.

### A · Warnung zusätzlich als physisches Licht?

| | **A1 Warnlicht an der Box** (z. B. Taster mit Leuchtring oder eigene LED, blinkt orange bei Warnung) | **A2 nur Display + App** |
|---|---|---|
| Display schwarz (Ruhemodus) oder ausgefallen | Warnung bleibt sichtbar ✅ | nur per Push, Ingrid hat **kein Handy** verbunden ❌ |
| Sichtbarkeit aus der Ferne | sehr gut, auch im Augenwinkel (Folie 27, Blinken präattentiv) | Warnpunkt auf dem Display, nur wenn es an ist |
| Folien | 59 Gulf of Evaluation, 130 *Visibility of system status*, 61 Murphy (Display kann ausfallen), 8 wenige physische Elemente | 130 *minimalist design* |
| Aufwand | LED + Vorwiderstand am Pi, evtl. Leuchttaster (Uni-Bestand prüfen, sonst Einkauf → Rückfrage) | keiner |
| Bedeutung des Tasters | bleibt **Licht**; das Warnlicht ist nur Ausgabe, keine zweite Funktion | unverändert |

**Empfehlung: A1.** Persona A (Ingrid) nutzt keine App. Ohne physisches Signal würde sie eine Warnung bei schwarzem Display nicht bemerken. Das physische Licht ist die Rückfallebene (*Fail-safe*).

### B · Taster schaltet Licht und Display gemeinsam?

| | **B1 gekoppelt:** Taster an = Licht + Display an, Taster aus = Licht aus + Display aus (Ruhe) | **B2 heute:** Taster = Licht, weckt das Display nur kurz |
|---|---|---|
| Mentales Modell (56) | einfach: „Box ansehen“ = Licht und Anzeige an, „Box schlafen lassen“ = alles aus | zwei getrennte Dinge: Licht und Ruhemodus |
| Modusfehler (60) | Display aus, obwohl man nur das Licht ausmachen wollte → abgefedert, weil Warnungen das Display ohnehin wecken | Ruhemodus muss man in den Einstellungen finden |
| Bedeutung des Tasters (72–73) | eine Handlung, zwei zusammengehörige Wirkungen | eine Handlung, eine Wirkung |
| Ruhemodus-Einstellung | wird fast überflüssig (Taster ersetzt ihn) | bleibt nötig |

**Empfehlung: B1, mit zwei Bedingungen:** (1) Warnungen wecken Display und Warnlicht **immer**, unabhängig von Taster, Licht und Ruhemodus. (2) Nach 30 s ohne Bedienung geht nur das Display aus, das Licht bleibt bis zum nächsten Tasterdruck bzw. 20 Uhr. So bleibt die Bedienung für Ingrid eine einzige Handlung.

Umsetzung nach der Entscheidung: Bedienfeld (Taster-Logik, Ruhemodus) und, bei A1, Pi-Code und Verkabelung.

## Story für die Präsentation

Jede Szene zeigt eine Entscheidung „in Aktion“ (Storyboard, Folien 143–150). Die App-Szenen hängen vom Stand der App ab und sind mit dem App-Teammitglied abzustimmen.

### A · Ingrid, ein Morgen an der Box

| Szene | Was passiert | Entscheidung |
|---|---|---|
| 1 | Ingrid geht mit dem Kaffee vorbei. Grüner Haken, „Alles gut“, Ring: „3 Tage bis zur Ernte“. Sie geht weiter. | E1, E2, E13 |
| 2 | Zwei Tage später: gelbes Dreieck „Wasser leer“, darunter „Tank im Technikraum auffüllen, dann AUFGEFÜLLT drücken.“ | E1, E8 |
| 3 | Sie gießt oben Wasser ein, bis die Linie im Sichtfenster erreicht ist. | E15 |
| 4 | Sie drückt den großen Knopf **AUFGEFÜLLT**: „Tank voll · Nebler läuft wieder“, dann wieder „Alles gut“. | E8, E9 |
| 5 | Abends möchte sie die Pilze ansehen und drückt den Taster. Das Licht geht an, sichtbar durchs Plexiglas. | E10 |
| 6 | Ernte: „Jetzt ernten“, sie erntet und drückt **GEERNTET**. Klima hat sie nie anfassen müssen. | E6, E13, E16 |

### B · Power-User, unterwegs und zu Hause

| Szene | Was passiert | Entscheidung |
|---|---|---|
| 1 | In der Bahn: Push „Zu nass“. Die App zeigt dieselbe Meldung mit denselben Worten wie die Box. | E17, E18 |
| 2 | In **Advanced Analytics** sieht er im Feuchte-Verlauf, dass die Kammer seit dem Morgen über dem Zielbereich liegt. Der Lüfter arbeitet schon. | E19 |
| 3 | Er startet in der App **1 Min lüften**. Die Box zeigt unter Klima: „läuft noch 60 s (vom Handy)“. | E7, E17 |
| 4 | Er legt in der App eine **eigene Sorte** an. An der Box erscheint sie unter SORTEN, ändern lässt sie sich nur in der App. | E19 |
| 5 | Zu Hause ein Blick auf die Box: gleicher Zustand, Automatik sichtbar, nichts zu tun. | E6, E17 |

Pointe für die Präsentation: **Dieselbe Box, zwei Nutzungen.** Ingrid braucht nur das Display. Der Power-User bekommt in der App mehr Kontrolle, ohne dass die Box für Ingrid komplizierter wird.

## Nielsen-Check (Folie 130)

Analytische Selbstprüfung von Bedienfeld v6 und Box-Skizze v3 gegen die 10 Heuristiken (Stand 02.11.2026). Das ist der Maßstab, an dem sich die Präsentation messen lassen muss; in der Präsentation verlinkt. Die App-Spalte prüft das App-Teammitglied vor der Probe gegen [`begriffe-box-app.md`](../01-konzept/begriffe-box-app.md).

| Heuristik | Umsetzung an der Box | | App |
|---|---|---|---|
| Visibility of system status | Warnpunkt blinkt nur bei Warnung, „Alles gut“, KLIMA zeigt AUTO (E1, E6, E22) | ✅ | Push mit derselben Meldung |
| Match between system and real world | Füllstand ↔ Sichtfenster, Ring = Wachstum bis zur Ernte (E13–E15) | ✅ | gleiche Symbole |
| User control and freedom | „Zurück zu …“ 14 Tage, `URLAUB ✕`, Handy trennen (E11, E12, E24) | ✅ | – |
| **Consistency and standards** | gleiche Wörter, Symbole und Farben in Box und App (E18); **Orange nur für Warnungen**, auch an Taster und Griff (E30) | ✅ seit v3 | ⚠️ prüfen: dieselben Wörter, kein Rot, Orange nur für Warnungen |
| Error prevention | Neu ansetzen nur mit 2 s halten; kein Eingriff ins Klima an der Box (E7, E11) | ✅ | – |
| Recognition rather than recall | Symbol + Wort auf jeder Kachel; Taster mit Licht-Symbol (E3, E30) | ✅ | – |
| Flexibility and efficiency of use | Licht über Taster **oder** App; 1 Min lüften nur in der App (E7, E10) | ✅ | Kern der App |
| Aesthetic and minimalist design | 3 Kacheln, keine Uhr, Handy-Symbol nach dem Koppeln weg (E3, E23, E24) | ✅ | – |
| Help users recognize, diagnose, and recover from errors | Warnung nennt Handlung und Knopfwort; Fehler melden (E8, E26) | ✅ | – |
| **Help and documentation** | **fehlt**: keine Hilfe am Display, keine Anleitung an der Box | ❌ | – |

**Offene Lücke Hilfe:** Vorschlag (noch nicht entschieden): kleine gedruckte Karte an der Box („Wasser · Licht · Ernte“ mit den drei Handgriffen) oder Eintrag „So geht’s“ unter dem Zahnrad. Die Karte passt besser zu Ingrid (ohne Menü, Folie 41–42 Vergessen), der Eintrag ist ohne Bau umsetzbar.

## Evaluation (Plan)

| Methode | Folie | Mit wem / was | Ergebnis |
|---|---|---|---|
| **Cognitive Walkthrough** (3 Fragen: Ist das Ziel klar? Ist die Aktion erkennbar? Gibt es Rückmeldung?) | 129 | A: Zustand ablesen, Wasser nachfüllen und bestätigen, Licht an, ernten. B: Meldung in App und Box vergleichen, 1 Min lüften per App | offen |
| **Nielsen-Heuristiken** als Checkliste | 130 | Bedienfeld v6 und App | **Box erledigt** (9 von 10, Lücke „Help and documentation“), siehe [Nielsen-Check](#nielsen-check-folie-130); App offen |
| **Kurzer Nutzertest** (Labor, formativ) | 126, 133, 136 | 3–5 Personen, bewusst über Altersgruppen gestreut; mindestens eine Person im Alter von Ingrid | offen |
| **AttrakDiff-Kurzform** nach dem Test | 141–142 | pragmatische vs. hedonische Qualität | offen |

## Ehrliche Grenzen (fürs Booklet)

- Personas sind Annahmen. Persona B ist noch ein Entwurf (Name und Details offen, siehe `BRIEF.md` → Offen).
- **Meldungs-Verlauf** und **Sorten-Katalog** sind noch auf der Box. Nach der Aufteilungsregel gehören sie eher in die App. Das ist bewusst offen gelassen.
- Im Ruhemodus ist das Display schwarz und könnte wie „aus“ wirken. Ein kleines Lebenszeichen fehlt noch.
- Messwerte sind simuliert. Echt sind nur Taster und LED.
