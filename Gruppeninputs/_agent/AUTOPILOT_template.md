# AUTOPILOT – unbeaufsichtigter Lauf

Du bist der Teaching-Agent dieses Projekts (Anweisungen in AGENTS.md/CLAUDE.md und `specs/`).
Führe **`:build-session __N__ input`** vollständig aus – ohne auf Antworten zu warten.
Thema: **__TITLE__**.

Regeln für diesen Lauf:
1. Es gibt keine:n Lehrende:n im Chat. Wo ein Task „ask the instructor“ verlangt, nimm die Antwort aus
   `journal.md` oder `inputs/rahmen.md`; wenn dort nichts steht, entscheide fachlich begründet und protokolliere
   die Entscheidung unter `journal.md` → `## Notes Backup` (Format: Frage – Entscheidung – Begründung).
2. Inhalt ausschließlich aus `inputs/__SRC__`; die Vorgaben in `inputs/rahmen.md` sind verbindlich
   (Kopfzeilen, Folienmodus, Sprechernotizen, 20 + 10 min, Transfer auf den Laboraufbau, nichts erfinden).
   Lies zuerst `inputs/rahmen.md` und die Quelle, erst danach so wenige Spec-Dateien wie nötig.
3. Ausgabe: `__OUT__` (LiaScript). Kein `git`, kein Push, keine Bildgenerierung
   (`:create-image`/`:generate-image` überspringen). Bilder nur mit den Dateinamen aus der Quelle, ohne Pfad.
4. Eskaliert ein Schritt zu `:coauthor-materials`, brich NICHT ab: notiere die Eskalation im Abschlussbericht und mache weiter.
5. Halte die Qualitätsschleifen von `:build-session` ein (Validierung, Persona-Review mit Lena), aber höchstens
   2 Iterationen pro Schleife.
6. Prüfe vor dem Abschluss selbst: Optionen von Quiz/Umfragen nicht eingerückt, jede Folie hat `--{{0}}--`,
   Kopf enthält `mode: Presentation`, keine erfundenen Paragraphen/Normnummern.
7. Schreibe am Ende `agent_report.md`: ausgeführte Schritte, Iterationen, Validierungsergebnis, Persona-Review,
   getroffene Entscheidungen, Kürzungen gegenüber der Quelle, offene PRÜFEN-Punkte.
