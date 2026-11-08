# Bedienfeld (iPhone in der Box)

**Stand v7 vom 05.11.2026** (Präsentationsstand + Editor „Eigene Sorte“), eingefroren in [`../../04-final/bedienfeld-v7/`](../../04-final/bedienfeld-v7/). Live: https://claude.ai/artifact/NHS2mr5kJKUXR1yPjPjrXi · Begründungen: [`../../04-final/entscheidungen-folien.md`](../../04-final/entscheidungen-folien.md) (E1–E31)

## Dateien

| Datei | Was |
|---|---|
| [`index.html`](index.html) | **Aktuelles Bedienfeld**; läuft ohne Server im Browser |
| [`vorschau-praesentation.html`](vorschau-praesentation.html) | nur das Display im schwarzen Rahmen (Mac) bzw. bildschirmfüllend (Handy); **so veröffentlicht** auf dem Link oben |
| [`vorschau-iphone.html`](vorschau-iphone.html) | iPhone-13-mini-Rahmen, nur lokal zum Vergleich der Handy-Ansichten |
| [`iphone-server.sh`](iphone-server.sh) | Mac-Server: Bedienfeld auf dem iPhone als Web-App im Vollbild |
| [`screenshot.sh`](screenshot.sh) | erzeugt `bilder/vorschau-aktuell.png` (Bild in der Haupt-README) |
| [`verlauf/`](verlauf/) | ältere Stände v1–v5, Original, `vorschau-einzeln.html` (nicht mehr gepflegt). **Nicht löschen** (Booklet) |

## Spezifikation v7

### Startbild

```
┌──────────────────────────────────────┐
│ AUSTER        ◌            📱  ⚙     │  Kopfzeile, alles 44 pt
│                                      │
│              ╭──────╮                │  Ring = Fortschritt bis zur Ernte
│              │ 🍄 15│                │  Mitte: Pilz + Tage
│              ╰──────╯                │
│           ✓  Alles gut               │  Status (zwischen zwei Linien)
│  22,4°      89 %       62 % · 4 T    │  Werte: Zahl · Balken · Name
│  ▬▬▬▬       ▬▬▬▬       ▬▬▬▬          │
│ Temperatur  Luftfeuchte Wassertank   │
│ ┌────────┐ ┌──────────┐ ┌────────┐   │
│ │ KLIMA  │ │ MELDUNGEN│ │ SORTEN │   │  3 Kacheln (Rahmen = drückbar)
│ │ ● Auto │ │    0     │ │  Neu   │   │
│ └────────┘ └──────────┘ └────────┘   │
└──────────────────────────────────────┘
```

- **Kopfzeile:** Sorte in Großbuchstaben · **Warnpunkt** (dunkler Ring, ohne „!“) · Handy-Symbol + Zahnrad als gleich große Knöpfe · keine Uhr
- **Handy-Symbol:** Antippen → Code + Knopf **VERBUNDEN** → ausgeblendet; zurück über Einstellungen → Handy verbinden → Trennen; nach dem Neuladen wieder da (für die Vorführung)
- **Status:** nur drei Zustände, immer Form + Farbe + Text

  | Zustand | Zeichen |
  |---|---|
  | Alles gut | grüner Kreis mit Haken, ohne Satz darunter |
  | Warnung | gelbes Warndreieck (ISO 7010) + Handlung + ein großer Knopf |
  | Erntebereit | **beiger** Kreis mit Pilz (Beige = anfassen, wie an der Box) |

- **Pilz wächst** in drei Stufen (klein < ⅓ · mittel · groß > ⅔ des Fortschritts); bei jeder neuen Stufe federt er und **drei Striche sprühen** aus dem Hut (ca. 0,7 s, aus bei „Bewegung reduzieren“)
- **Werte:** einheitlich Zahl · Balken · Name; Tank als `62 % · 4 T` (vorgelesen „reicht ca. 4 Tage“); außerhalb des Bereichs mit Warndreieck
- **Kacheln:** KLIMA (klein „Auto“, ruhiger grüner Punkt) · MELDUNGEN (Zahl) · SORTEN (klein „Neu“)

### Grundsätze

- **Rahmen = drückbar, Trennstrich = nur Text.** Information steht **zwischen zwei Linien** (grün gut, orange Warnung, hell Hinweis); gerahmt ist nur der Knopf darin
- **Display schlank, Erweitertes in der App** (1 Min lüften/befeuchten, Analytics)
- **Blinken nur im Standby** (Warnpunkt), alles andere ruhig
- **Orange nur für Warnungen**, auch an der Box

### Ebenen

| Ebene | Inhalt |
|---|---|
| **KLIMA** | ein Satz („Die Box regelt Luft, Feuchte, Wärme und Licht selbst.“) + 4 Textzeilen mit Trennstrich: Lüfter · Nebler · Heizung · Licht, je **AUTO** + Bedingung je Sorte und Phase (z. B. „an unter 70 % Feuchte“, „8–20 Uhr“); Licht zusätzlich mit beigem Taster-Zeichen „Taster ↓ schaltet um“; **kein Eingriff, keine Live-Zustände** |
| **MELDUNGEN** | Stand mit Datum/Uhrzeit · offene Meldungen mit Handlung und „seit“ · Verlauf behoben **grün mit Haken** („behoben · von – bis“) · „Zu nass“/„Braucht Frischluft“ mit GESEHEN · nur **ein** Linienpaar |
| **Tank-Meldung** | einzeilig „Wasser leer · Tank im Technikraum auffüllen“, Knopf AUFGEFÜLLT |
| **SORTEN · Neu** | oben Stand des Durchgangs + **Neu ansetzen …**; darunter Sorten ansehen; Schwierigkeit als **1–3 kleine Pilze** (Level, keine Sterne); Detailseite: Schwierigkeit · Dauer · Temperatur · Luftfeuchte |
| **Einstellungen** (Zahnrad) | Handy verbinden · Urlaub · Sprache (nur Deutsch, Rest ausgegraut) · **Darstellung** (Standard Blau / Hoher Kontrast Schwarz / Individuell, nur angezeigt) · **Hilfe** (rote Flagge, Kategorie → App) · ganz unten Admin-Modus |
| **Urlaub** | nur unter Einstellungen; oben dann `URLAUB ✕` |

### Neu ansetzen: Hürde passt zum Risiko

```
mitten im Wachstum ──► Hinweis, was verloren geht ──► 2 s halten ──► Kammer leeren ──► Zuchtset ──► Tag 1
                                                                       (Notfall „Zurück zu …“ 14 Tage)
direkt nach Ernte ───► Sorte ──► Detailseite ──► Neu ansetzen ──► „Sicher?“ ──► Starten ──► Tag 1
                   └─► „Kleine Pause einlegen“ ──► oben „Kein Pilz“, Status „Pause“
```

### Eigene Sorte gestalten (seit 05.11.)

- **nur nach der Ernte:** NEU ANSETZEN → „Eigene Sorte gestalten …“ (in der App jederzeit)
- Name + Vorlage (Auster, Shiitake, Kräuter, Igel)
- eingeklappt unter **Erweitert**: Temperatur, Luftfeuchte, Licht pro Tag (0–14 h), Frischluft (wenig/normal/viel), in festen Schritten mit Grenzen
- gespeicherte Sorte nach der nächsten Ernte über „Werte ändern …“ anpassbar; **solange ein Pilz wächst, kein Editor**

### Standby und Admin-Modus (Vorführung)

- **Standby** nur im Fall „Tank leer“: Display schwarz, nur der **orange Punkt blinkt**; Antippen → normale Ansicht mit Meldung; nicht von Hand einschaltbar; **kein Ruhemodus**
- **Admin-Modus**, genau zwei Fälle + Zurücksetzen:
  - **1 · Tank leer** → Standby; AUFGEFÜLLT behebt es
  - **2 · Pilze fertig** → 5-s-Zeitraffer (Ring voll, Tage zählen herunter, Pilz wächst) → „Geerntet? Neue Sorte“ → Sortenwahl
- **Startzustand:** Austernpilz, Wachstumsphase, **15 Tage** bis zur Ernte
- übrige Fehler, Tag +1, Taster und Messwerte: nicht mehr erreichbar (Code bleibt)

### Details

- **Fenstergrößen:** Klima, Meldungen, Sorten, Neu ansetzen, Sorte und Handy verbinden so groß wie die Einstellungen
- **Handy verbinden** zeigt zuerst nur „Meldungen aufs Handy“, den Code erst nach dem Antippen; „Verbunden“ grün zwischen Linien; „Über diese Box“ entfällt
- **Sortenlisten:** nur Dauer („20 Tage“) und Schwierigkeit; **Igel-Stachelbart** mit zwei Weißtönen (Hut reinweiß, Stiel creme), damit er sich vom Austernpilz abhebt
- **Pause:** offene Fenster werden nicht abgedunkelt; „Alles gut“ steht mittig zwischen Ring und Werten
- **Licht** nur über Taster und App (Ausnahme bis zum nächsten Wechsel 8/20 Uhr); **Heizung** simuliert; **Kühlen** nur als Hinweis

### Barrierefreiheit

| Regel | Wert |
|---|---|
| Kontrast Text | ≥ 4,5 : 1 (Warntexte weiß, Nebentexte `#dfe4ff`) |
| Touch-Ziele | ≥ 44 pt; Einstellungen/Admin ca. 1,5× hohe Balken |
| Schrift | für 50–70 cm Sichtabstand |
| Status | nie nur über Farbe |
| Blinken | langsam, aus bei „Bewegung reduzieren“ |

## 📘 Booklet S5 · Verlauf v1 → v7

```
Skizzen ─► v1 Kacheln ─► v2 Panel ─► v3 Ring ─► v4 Automatik ─► v5 Folien-Review ─► v6 ─► v7 Präsentation
27.10.     27.10.        29.10.      29.10.     29.10.          02.11.               02.11.  05.11.
```

| Stand | Wo | Was neu war |
|---|---|---|
| Konzept-Skizzen 01–14 | https://claude.ai/artifact/7MF2tG589SHFE4ghP35TE9 (privat) | Papier-/Skizzenphase mit Vorlesungsbezug |
| v1 „Kacheln“ (27.10.) | [`verlauf/v1-kacheln/`](verlauf/v1-kacheln/) | 3-Stufen-Zustand + Kacheln Licht · Klima · Hinweise; braucht den Server aus `03-software` |
| v2 „Panel“ (29.10.) | [`verlauf/v2-panel/`](verlauf/v2-panel/) | Panel vom Kollegen: Pilz im Feuchte-Ring, Tasten Ein · Frischluft · Meldungen · Sorte |
| Original claude.ai (29.10.) | [`verlauf/claude-ai-live/`](verlauf/claude-ai-live/) | „FunghiLab“, Handy-Verbindung per Code |
| v3 (29.10.) | [`verlauf/v3/`](verlauf/v3/) | **Ring = Fortschritt** bis zur Ernte, Werte als Balken, 2 Status-Stufen, Admin-Modus |
| v4 (29.10.) | [`verlauf/v4/`](verlauf/v4/) | **Automatik sichtbar** (Kachel Klima mit AUTO), Ruhemodus, simulierte Heizung |
| v5 (02.11.) | [`verlauf/v5/`](verlauf/v5/) | **Review mit den Folien:** 3 größere Kacheln · „1 Min lüften“ nur in der App · Warntexte weiß (Kontrast 2,8 → 6,4) · Nebentexte heller (≥ 5,1 : 1) · Warndreieck bei Werten außerhalb · Kopfzeile 44 pt ohne Uhr |
| v6 (02.11.) | [`verlauf/v6/`](verlauf/v6/) | Kachel SORTEN mit „Neu ansetzen …“ · Warnpunkt blinkt · Verlauf grün mit Haken · Einstellungen mit Sprache, Darstellung, Fehler melden · Schrift in Listen größer, Touch-Ziele ≥ 44 pt |
| **v7 (05.11.)** | [`../../04-final/bedienfeld-v7/`](../../04-final/bedienfeld-v7/) | **Ruhemodus gestrichen → Standby** nur bei Tank leer · **Rahmen = drückbar, Linien = Info** · Klima als Textzeilen mit Bedingungen · Meldung einzeilig · „Hilfe“ statt „Fehler melden“ · Erntebereit beige · Pilz wächst in 3 Stufen · Admin auf 2 Fälle + Zeitraffer · abgestufte Bestätigung + Kleine Pause · **Eigene Sorte gestalten** |

Belege mit Folien zu v5/v6: [`../folien-recherche.md`](../folien-recherche.md)
