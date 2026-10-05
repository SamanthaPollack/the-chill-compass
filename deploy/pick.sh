#!/bin/sh
# Picks the newest uploaded copy of the site (whichever folder Samantha dragged in) and publishes it.
set -e
ROOT="$(cd .. && pwd)"
best=""; bestv=-1
for d in "$ROOT/The Chill Compass/chill-compass-upload/site" "$ROOT/chill-compass-upload/site"; do
  [ -d "$d" ] || continue
  v=$(cat "$d/version.txt" 2>/dev/null || echo 0)
  if [ "$v" -gt "$bestv" ]; then best="$d"; bestv="$v"; fi
done
[ -n "$best" ] || { echo "No site folder found"; exit 1; }
echo "Publishing: $best (version $bestv)"
rm -rf publish
cp -R "$best" publish
