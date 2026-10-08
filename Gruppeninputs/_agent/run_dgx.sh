#!/bin/bash
# Erstellt die Gruppen-Inputs T1–T4 offline auf dem GX10 mit dem Teaching-Agent (XX_Teacher_Agent) und qwen3.8:27b.
# Laufzeit: fd2_agent_runner.py (nur Dateiwerkzeuge im Arbeitsordner, keine Shell), Ollama nativ, num_ctx 131072.
# Die Themen laufen nacheinander in EINEM abgekoppelten Job; laufende doc2md-Batches werden pausiert und immer fortgesetzt.
# Aufruf:    bash run_dgx.sh [1 2 3 4]      Abholen: bash pull_dgx.sh
set -euo pipefail
cd "$(dirname "$0")"
HOST=ovgu-server
TOPICS="${*:-1 2 3 4}"
R=ingpaed-agent

ssh -o BatchMode=yes $HOST "mkdir -p ~/$R"
rsync -a package/ "$HOST:$R/package/"
rsync -a AUTOPILOT_template.md "$HOST:$R/"
rsync -a "../../../../XX_Teacher_Agent/GX10_Wiki/tools/gx10_agent_runner.py" "$HOST:$R/"   # logs eval tokens

ssh -o BatchMode=yes $HOST "bash -s $(printf '%q' "$TOPICS")" <<'REMOTE'
set -euo pipefail
TOPICS=$1; A=~/ingpaed-agent; F=~/fd2-agent
[ -f $A/run.pgid ] && for g in $(cat $A/run.pgid); do kill -TERM -- -$g; done 2>/dev/null && sleep 3 || true
(cd $F/teaching-agent && git pull -q) || true
cat > $A/run.sh <<EOF
#!/bin/bash
export PATH=\$HOME/.local/bin:\$PATH
LOG=$A/run.log; : > \$LOG
echo \$\$ > $A/run.pgid
PIDS=\$(pgrep -f 'run_papers_batch.sh|run_books_batch.sh|doc2md.py|doc2md_fixtext.py' || true)
resume() { [ -n "\$PIDS" ] && kill -CONT \$PIDS 2>/dev/null; echo "##### ALLE ENDE \$(date '+%F %H:%M:%S')" >> \$LOG; touch $A/DONE; }
trap resume EXIT
[ -n "\$PIDS" ] && kill -STOP \$PIDS && echo "##### doc2md pausiert (\$PIDS)" >> \$LOG
for N in $TOPICS; do
  case \$N in
    1) T="Lehren und Lernen im Labor";      S=quelle_T1.md; O=materials/01-lehren-und-lernen/README.md;;
    2) T="Sicherheit, Gesundheit, Arbeit";  S=quelle_T2.md; O=materials/02-sicherheit-gesundheit-arbeit/README.md;;
    3) T="Sicherheit in Schulen";           S=quelle_T3.md; O=materials/03-sicherheit-in-schulen/README.md;;
    4) T="Gefährdung und Schutzziele";      S=quelle_T4.md; O=materials/04-gefaehrdung-und-schutzziele/README.md;;
  esac
  W=$A/T\$N/work; rm -rf $A/T\$N; mkdir -p \$W
  cp -a $F/teaching-agent/. \$W/ && cp -a $A/package/. \$W/ && rm -f \$W/README.md.bak
  sed -e "s|__N__|\$N|g" -e "s|__TITLE__|\$T|g" -e "s|__SRC__|\$S|g" -e "s|__OUT__|\$O|g" $A/AUTOPILOT_template.md > \$W/AUTOPILOT.md
  echo "##### T\$N START \$(date '+%F %H:%M:%S') – \$T" >> \$LOG
  timeout --foreground 2h python3 -u $A/gx10_agent_runner.py --workdir \$W --prompt-file \$W/AUTOPILOT.md --system-file \$W/AGENTS.md \\
    --model qwen3.8:27b --num-ctx 131072 --max-steps 120 --log $A/T\$N/run.jsonl < /dev/null >> $A/T\$N/run.log 2>&1
  echo "##### T\$N ENDE \$(date '+%F %H:%M:%S') Exit \$? – \$(ls \$W/materials/*/README.md 2>/dev/null | head -1)" >> \$LOG
done
EOF
chmod +x $A/run.sh; rm -f $A/DONE
nohup setsid $A/run.sh >/dev/null 2>&1 &
sleep 4; cat $A/run.log
REMOTE
