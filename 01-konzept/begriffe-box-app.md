# Begriffe Box ↔ App

Für das App-Teammitglied: Box-Display und App sind **zwei Ansichten auf denselben Zustand** (MVC, Folien 99–100). Damit Nutzer nichts doppelt lernen müssen, verwenden beide **dieselben Wörter, Symbole und Farben** (äußere Konsistenz, Folien 80–81). Stand: Bedienfeld v5 (`01-konzept/bedienfeld/index.html`).

Wenn die App einen Begriff anders braucht: bitte kurz absprechen und hier ändern, nicht still abweichen.

## Zustand (immer Form + Farbe + Text)

| Begriff | Bedeutung | Symbol / Farbe |
|---|---|---|
| **Alles gut** | Nichts zu tun. Hinweise wie „Ernte prüfen“ laufen trotzdem darunter. | grüner Kreis mit Haken, Grün `#3fcf7f` |
| **Warnung** (Titel der Meldung, z. B. „Wasser leer“) | Der Mensch muss etwas tun. | gelbes Warndreieck mit „!“ (ISO 7010), Orange `#e69f00` |
| **Klima regelt sich automatisch.** | Satz unter „Alles gut“ | – |
| **Pausiert** | Durchgang beendet, neues Zuchtset noch nicht drin | – |

Nur **zwei Stufen**. Keine dritte Farbe (z. B. Rot) in der App einführen.

## Hauptbereiche

| Box (Kachel) | App | Inhalt |
|---|---|---|
| **Klima** (Untertitel „Auto“, grüner Punkt leuchtet ruhig) | Klima | Lüfter, Nebler, Heizung, Licht mit Kennzeichen **AUTO** und „läuft gerade“ bzw. „nächstes Lüften in X Min“ |
| **Meldungen** (Zahl = offene Meldungen) | Meldungen | offene Meldungen mit „seit“, Verlauf (Beginn, „behoben um“ / „erledigt um“) |
| **Sorte & Neu** | Sorte & Neu | Sorten ansehen, neu ansetzen, Notfall „Zurück zu …“, Urlaub |
| Zahnrad = **Einstellungen** | Einstellungen | Handy verbinden, Ruhemodus, Urlaub, Über diese Box |
| – | **Advanced Analytics** (nur App) | Verläufe, CO₂, Vergleiche |

## Geräte und Werte

| Begriff | Nicht verwenden | Hinweis |
|---|---|---|
| **Lüfter** | Ventilator, Fan | Frischluft alle 30 Min und bei hohem CO₂ |
| **Nebler** | Befeuchter, Vernebler, Mister | macht Luftfeuchte |
| **Heizung** | Wärme | Kühlen gibt es nicht, nur den Hinweis „umstellen“ |
| **Licht** | LED, Lampe | 8–20 Uhr automatisch; Ausnahme per **Taster** oder App bis zum nächsten Wechsel |
| **Temperatur** | Temp | Anzeige `22,4°` (Komma, eine Nachkommastelle) |
| **Luftfeuchte** | Feuchtigkeit, RH | Anzeige `89 %` |
| **Wasser** / **Tank** | Reservoir | Anzeige `62 %` und „reicht ca. 4 Tage“ |
| **CO₂** | – | nur App (Analytics) und Admin-Modus, nicht auf dem Startbild der Box |

## Phasen und Sorten

| Begriff | Bedeutung |
|---|---|
| **Durchwachsen** | Pilzgeflecht wächst durchs Substrat, Licht aus |
| **Fruchtung** | Pilze wachsen sichtbar, Licht an |
| **Ruhephase** | Pause nach der Ernte bis zur nächsten Welle |
| **bis zur Ernte** | Ring und Zahl in der Mitte: „X Tage bis zur Ernte“ bzw. „Jetzt ernten“ |

Sorten (lang / kurz in der Kopfzeile): **Austernpilz / Auster**, **Shiitake / Shiitake**, **Kräuterseitling / Kräuter**, **Igel-Stachelbart / Igel**, **Eigene Sorte** (nur in der App anlegbar und änderbar).

## Knöpfe (Bestätigungswörter)

Meldungen sagen, was zu tun ist, und nennen das Wort auf dem Knopf in Großbuchstaben, z. B. „Tank auffüllen, dann AUFGEFÜLLT drücken.“

| Knopf | wann |
|---|---|
| **Aufgefüllt** | Wasser leer / bald leer |
| **Geerntet** | Ernte prüfen |
| **Fruchtung starten** | Durchwachsen? / Nächste Welle |
| **Umgestellt** | zu warm / zu kalt |
| **Geschlossen** | Tür offen |
| **Geprüft** | Sensor ausgefallen, viel zu trocken |
| **Gesehen** | zu trocken, zu nass, braucht Frischluft (die Box regelt selbst) |
| **Weiterlaufen** | Pausiert, versehentlich beendet |
| **Neu ansetzen** | nur mit **2 s gedrückt halten** |

## Modi (immer oben sichtbar)

| Begriff | Anzeige oben | Bedeutung |
|---|---|---|
| **Ruhemodus** | `RUHE` | Display schwarz, wacht bei Warnung, Berührung oder Taster |
| **Urlaub** | `URLAUB ✕` | Box spart Wasser, Meldungen nur aufs Handy |
| **Admin-Modus** | – | nur Vorführung, nicht Teil der normalen Bedienung |

## Nur in der App

- **1 Min lüften / 1 Min befeuchten** (Ausnahme für den Power-User; die Box zeigt dann „läuft noch X s (vom Handy)“)
- **Push-Mitteilungen** bei Warnungen (die Box schickt ihre Meldungen mit)
- **Eigene Sorte** anlegen und ändern
- **Advanced Analytics**, Ernte **teilen**

## Schnittstelle (technisch)

Die Box schreibt ihren Stand nach `boxes/<Code>`. Die App schreibt Befehle nach `boxes/<Code>/cmd/last` als `{id, at, type, arg}`. Erlaubte `type`: `power`, `burst` (1 Min lüften), `mist` (1 Min befeuchten), `away`, `sleep`, `do` (Knopf einer Meldung, `arg` = Meldungs-ID), `species`, `phase`, `custom`. Details: `01-konzept/bedienfeld/index.html`, Abschnitt „Verbindung Box und Handy-App“.
