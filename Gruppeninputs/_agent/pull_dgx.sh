#!/bin/bash
# Holt die Ergebnisse vom GX10: Präsentation -> ../Tn_*/README.md, Bericht/Journal/Log -> runs/Tn/ (auch während des Laufs).
set -euo pipefail
cd "$(dirname "$0")"
HOST=ovgu-server
ssh -o BatchMode=yes $HOST "cat ~/ingpaed-agent/run.log; test -f ~/ingpaed-agent/DONE && echo 'Status: fertig' || echo 'Status: läuft'"
for N in 1 2 3 4; do
  D=$(ls -d ../T${N}_* | head -1)
  mkdir -p runs/T$N
  rsync -a "$HOST:ingpaed-agent/T$N/run.log" "runs/T$N/" 2>/dev/null || continue
  for f in agent_report.md journal.md; do rsync -a "$HOST:ingpaed-agent/T$N/work/$f" "runs/T$N/" 2>/dev/null || true; done
  M=$(ssh -o BatchMode=yes $HOST "ls ~/ingpaed-agent/T$N/work/materials/*/README.md 2>/dev/null | head -1" || true)
  if [ -n "$M" ]; then rsync -a "$HOST:$M" "$D/README.md"; echo "T$N -> $D/README.md ($(wc -l < "$D/README.md") Zeilen)"; else echo "T$N: noch kein Material"; fi
done
