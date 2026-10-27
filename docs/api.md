# Schnittstelle der Growbox – für die App

Der Raspberry Pi hält den **einzigen Zustand** der Box. Display, App und Taster sind nur Ansichten bzw. Eingaben dazu. Ändert jemand etwas, bekommen alle verbundenen Ansichten sofort den neuen Zustand.

```text
App ──POST /api/light──► Pi (Zustand) ──WebSocket /ws──► Display, App, Demo-Panel
```

- **Adresse:** `http://<pi-adresse>:8000` (im selben WLAN bzw. Handy-Hotspot)
- **Interaktive Doku:** `http://<pi-adresse>:8000/docs`
- **Kein Login** – nur für den Prototyp im lokalen Netz gedacht.

## Live-Zustand: `WS /ws`

Direkt nach dem Verbinden kommt der aktuelle Zustand, danach bei jeder Änderung ein neuer, vollständiger Zustand (immer dasselbe Format wie `GET /api/state`). Die App muss selbst nichts senden.

## Zustand: `GET /api/state`

```json
{
  "status":  { "level": "now", "title": "Jetzt handeln", "message": "Es ist zu trocken." },
  "light":   { "on": true, "source": "taster" },
  "climate": { "level": "now", "humidity": 68, "humidity_label": "zu trocken",
               "temperature": 21.0, "temperature_label": "angenehm",
               "humidity_trend": null, "temperature_trend": null },
  "hints":   [ { "id": "zu-trocken", "level": "now", "title": "Es ist zu trocken.",
                 "action": "Bitte Wasser in die Schale füllen – bis zur Linie.", "resolving": false } ],
  "growth":  { "day": 6, "harvest_day": 14, "progress": 0.429, "harvest_ready": false },
  "scenario": "zu-trocken",
  "hardware": "simuliert"
}
```

| Feld | Bedeutung |
|---|---|
| `status.level` | `ok` = Alles gut · `soon` = Bald kümmern · `now` = Jetzt handeln |
| `light.source` | wer zuletzt geschaltet hat: `display`, `app`, `taster`, `demo` |
| `climate.*_label` | fertige Texte zum Anzeigen – bitte diese statt eigener Formulierungen verwenden |
| `*_trend` | `rising` / `falling`, solange sich ein Wert nach „Erledigt“ ändert, sonst `null` |
| `hints[].resolving` | `true`, nachdem jemand „Erledigt“ gedrückt hat und der Wert sich erholt |

## Aktionen

| Aufruf | Body | Wirkung |
|---|---|---|
| `POST /api/light` | `{"on": true, "source": "app"}` | Licht an/aus |
| `POST /api/hints/{id}/done` | – | Hinweis als erledigt bestätigen |

Jede Aktion antwortet mit dem neuen Zustand.

## Nur für die Vorführung

| Aufruf | Wirkung |
|---|---|
| `GET /api/demo/scenarios` | Liste der Szenarien |
| `POST /api/demo/scenario` mit `{"name": "zu-trocken"}` | Szenario einstellen: `alles-gut`, `bald-trocken`, `zu-trocken`, `zu-warm`, `erntezeit` |
| `POST /api/demo/button` | physischen Taster simulieren |

## Gemeinsame Gestaltung (äußere Konsistenz)

Damit Display und App wie ein Produkt wirken, gelten auf beiden dieselben:

- **Begriffe:** „Alles gut“, „Bald kümmern“, „Jetzt handeln“, „Licht“, „Klima“, „Hinweise“, „Erledigt“
- **Symbole:** Kreis mit Haken (ok), Dreieck mit ! (bald), Achteck mit !! (jetzt) – Farbe nie allein
- **Farben:** siehe `box/ui/style.css` (`--ok`, `--soon`, `--now`, `--light-on`)
