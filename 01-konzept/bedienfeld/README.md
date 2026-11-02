# Bedienfeld (iPhone in der Box)

| Datei | Was |
|---|---|
| [`index.html`](index.html) | **Aktuelles Bedienfeld** (v6, Stand 02.11.2026). Läuft ohne Server: im Browser öffnen oder vom Pi ausliefern. Original: https://claude.ai/artifact/EGmf5bvFTK16eYGfKWVkPE |
| [`vorschau-iphone.html`](vorschau-iphone.html) | iPhone-13-mini-Vorschau, nur der aktuelle Stand (v6); ältere Stände im Archiv `verlauf/`; Ansichten claude.ai-Link / Safari / Vollbild |
| [`vorschau-einzeln.html`](vorschau-einzeln.html) | Nur der aktuelle Entwurf im iPhone-Rahmen (eigener claude.ai-Link, siehe Haupt-README) |
| [`verlauf/`](verlauf/) | Ältere Stände fürs Booklet (Entwicklungsverlauf). Nicht löschen. |

## Verlauf

| Stand | Wo | Idee |
|---|---|---|
| Konzept-Skizzen, Blätter 01–14 | https://claude.ai/artifact/7MF2tG589SHFE4ghP35TE9 (privat, Canvas auf claude.ai) | Papier-/Skizzenphase mit Vorlesungsbezug; fürs Booklet als Bild/PDF exportieren |
| v1 „Kacheln“ (27.10.2026) | [`verlauf/v1-kacheln/`](verlauf/v1-kacheln/) | großer 3-Stufen-Zustand + Kacheln Licht · Klima · Hinweise; braucht den Server aus `03-software` |
| v2 „Panel“ (29.10.2026) | [`verlauf/v2-panel/`](verlauf/v2-panel/) | Wand-Bedienteil vom Kollegen: Pilz im Feuchte-Ring, wichtigste Meldung, Tasten Ein · Frischluft · Meldungen · Sorte |
| Original claude.ai, Live-Stand (29.10.2026, 12:15) | [`verlauf/claude-ai-live/`](verlauf/claude-ai-live/) | Weiterentwicklung des Kollegen: Name „FunghiLab“, Handy-Verbindung per Code (Box ↔ Handy-App); archiviert. Bei Änderungen am Link neu übernehmen |
| v3 (29.10.2026) | [`verlauf/v3/`](verlauf/v3/) | Ring = Fortschritt bis zur Ernte, Status-Symbole aus v1, Werte als Balken; 2 Status-Stufen; Tasten Lüften · Befeuchten (mit Empfehlung) · Meldungen (mit Verlauf) · Sorte & Neu (ansehen, bewusst neu ansetzen, Notfall-Rückweg, Urlaub); Admin-Modus; HANDY-Verbindung wie im Original |
| v4 (29.10.2026) | [`verlauf/v4/`](verlauf/v4/) | Automatik sichtbar: Kacheln Klima (Lüfter, Nebler, Heizung, Licht mit AUTO-Status) · Ruhemodus (Display weckt nur bei Warnung) · Meldungen · Sorte & Neu; grüner Punkt an Klima blinkt dauerhaft; „Alles gut“ ohne Zusatztext; oben nur Pilzname; simulierte Heizung; Vorführung im Admin-Modus |
| v5 (02.11.2026) | [`verlauf/v5/`](verlauf/v5/) | Nach Review mit den Folien: **3 größere Kacheln** Klima · Meldungen · Sorte & Neu (Ruhemodus unter dem Zahnrad); größere Beschriftungen ohne Großbuchstaben; Klima-Punkt leuchtet ruhig statt zu blinken; **„1 Min lüften/befeuchten“ nur noch in der App**, das Klima-Fenster zeigt nur, was die Box selbst tut; Meldungen „Zu nass“ und „Braucht Frischluft“ mit GESEHEN statt Eingriff; nach Folien-Recherche: Warntexte weiß (Kontrast), Nebentexte heller, Warndreieck bei Werten außerhalb des Bereichs, Klima-Fenster verweist auf den Licht-Taster; Kopfzeile als eine Zeile mit 44 pt: Sorte · Warnpunkt · Handy-Symbol (nach VERBUNDEN ausgeblendet) + Zahnrad; keine Uhr; Werte einheitlich beschriftet (Temperatur · Luftfeuchte · Wassertank), Reichweite in Tagen im Klima-Fenster |
| v6 aktuell (02.11.2026) | [`index.html`](index.html) | Kachel **SORTEN** (klein „Neu“) mit sichtbarem Knopf „Neu ansetzen …“; **Warnpunkt blinkt** langsam; Tank `62 % · 4 T` in gleicher Schrift; Klima-Fenster ohne Wassertank; **Meldungs-Verlauf grün mit Haken**; Einstellungen + **Sprache · Darstellung (Hoher Kontrast) · Fehler melden**; Urlaub nur unter Einstellungen; größere Schrift in Meldungen/Listen; Touch-Ziele ≥ 44 pt; Ruhemodus-Hinweis lesbar |
