#!/bin/sh
# Erzeugt bilder/vorschau-aktuell.png aus vorschau-praesentation.html (gleiche Ansicht wie der claude.ai-Link) (macOS-WebKit, keine Zusatzpakete).
# Aufruf: sh 01-konzept/bedienfeld/screenshot.sh  (läuft auch automatisch per pre-commit-Hook)
set -e
DIR=$(cd "$(dirname "$0")" && pwd)
PORT=8779
python3 -m http.server $PORT --bind 127.0.0.1 -d "$DIR" >/dev/null 2>&1 &
PID=$!
trap 'kill $PID 2>/dev/null' EXIT
sleep 1
swift "$DIR/screenshot.swift" "http://127.0.0.1:$PORT/vorschau-praesentation.html?v=$(date +%s)" "$DIR/bilder/vorschau-aktuell.png" 600 900
sips --resampleWidth 700 "$DIR/bilder/vorschau-aktuell.png" >/dev/null
echo "Bild aktualisiert: bilder/vorschau-aktuell.png"
