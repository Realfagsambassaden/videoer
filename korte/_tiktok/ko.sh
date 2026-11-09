#!/bin/bash
# kø: legg mappenavn i _tiktok/ko.txt; kjører dem en etter en
cd "$(dirname "$0")/.."
while true; do
  m=$(head -1 _tiktok/ko.txt 2>/dev/null); [ -z "$m" ] && { sleep 5; continue; }
  sed -i '1d' _tiktok/ko.txt
  mkdir -p "$m/tmp"; python3 _tiktok/lag.py "$m" > "$m/tmp/logg.txt" 2>&1; echo "$m $(date +%T) $(tail -1 $m/tmp/logg.txt)" >> _tiktok/ko_ferdig.txt
done
