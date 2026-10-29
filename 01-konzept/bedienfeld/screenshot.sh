#!/bin/sh
# Erzeugt bilder/vorschau-3-screens.png aus vorschau-iphone.html (macOS-WebKit, keine Zusatzpakete).
# Aufruf: sh 01-konzept/bedienfeld/screenshot.sh  (läuft auch automatisch per pre-commit-Hook)
set -e
DIR=$(cd "$(dirname "$0")" && pwd)
PORT=8779
python3 -m http.server $PORT --bind 127.0.0.1 -d "$DIR" >/dev/null 2>&1 &
PID=$!
trap 'kill $PID 2>/dev/null' EXIT
sleep 1
swift "$DIR/screenshot.swift" "http://127.0.0.1:$PORT/vorschau-iphone.html" "$DIR/bilder/vorschau-3-screens.png" 1420 1150
sips --resampleWidth 1600 "$DIR/bilder/vorschau-3-screens.png" >/dev/null
echo "Bild aktualisiert: bilder/vorschau-3-screens.png"
