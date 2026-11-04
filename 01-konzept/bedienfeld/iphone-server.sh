#!/bin/sh
# Zeigt das Bedienfeld im Vollbild auf dem iPhone in der Box (bis der Pi das übernimmt).
# Aufruf auf dem Mac: sh 01-konzept/bedienfeld/iphone-server.sh   (Beenden: ctrl+c)
#
# 1. Mac und iPhone ins selbe Netz. Sicherster Weg: Mac mit dem Hotspot des iPhones verbinden
#    (Uni-WLAN trennt Geräte oft voneinander).
# 2. Auf dem iPhone in Safari die angezeigte Adresse öffnen.
# 3. Teilen → „Zum Home-Bildschirm“ → „Als Web-App öffnen“ an → Hinzufügen.
# 4. Growbox-Symbol auf dem Home-Bildschirm antippen → Vollbild ohne Leisten.
# 5. Optional sperren: Einstellungen → Bedienungshilfen → Geführter Zugriff, dann 3× Seitentaste.
# Der Mac muss laufen, solange das Bedienfeld neu geladen wird; einmal geladen läuft es weiter.
DIR=$(cd "$(dirname "$0")" && pwd)
PORT=8000
IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null)
echo "Auf dem iPhone öffnen:  http://${IP:-<IP-des-Macs>}:$PORT/index.html"
exec python3 -m http.server $PORT --bind 0.0.0.0 -d "$DIR"
