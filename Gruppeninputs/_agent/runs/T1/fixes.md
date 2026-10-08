# T1 Lehren und Lernen – Fixes durch Claude (2026-10-05)

Rohausgabe des Modells: `raw/output.md` (509 Zeilen, 27 Folien). Lauf 10:57–11:41 (44 min, 38 Schritte).

| # | Befund | Art | Fix |
|---|---|---|---|
| 1 | 36 Sprechernotizen + 74 Zeilen Text/Animationsblöcke mit 4 Leerzeichen eingerückt → würden als Codeblock erscheinen | Syntax (systematisch) | `lia_fix.py` |
| 2 | Umfrageoptionen eingerückt (Einstieg) | Syntax | `lia_fix.py` |
| 3 | Leere Sprechernotiz `--{{2}}--` (Didaktische Reduktion) | Syntax | `lia_fix.py` entfernt |
| 4 | 5 Quiz-Hinweise `[[?]]` durch Leerzeile vom Quiz getrennt | Syntax | `lia_fix.py` (Regel nachträglich ergänzt) |
| 5 | Umfrage nach `{{1}}` ohne `<section>` – nur die Überschrift wäre animiert | Syntax | manuell `<section>` |
| 6 | Bild `04_Ebenen der Reduktion.png` (Leerzeichen, Fehler aus Vorjahresquelle) | Bild | → `04_Ebenen_der_Reduktion.png` |
| 7 | Lernziele grammatisch falsch („können Sie: 1. **nennen** Sie …“) | Sprache | manuell umformuliert |
| 8 | `?[Kurzantwort …]` ist keine gültige LiaScript-Eingabe (wäre Audio-Einbettung) | Syntax | Freitext-Umfrage `[[___ ___ ___]]` |
| 9 | Lernfeld „Pneumatische Schaltkreise“ (kein belegter Lernfeldtitel) | erfunden | generisch „ein Lernfeld der Mechatroniker-Ausbildung“ |

Selbstauskunft des Agenten falsch: `agent_report.md` meldet „LiaScript Syntax: alle 13 Checks bestanden“ und Datum 2026-02-14.
Inhalt: alle Abschnitte der Quelle übernommen, englische Titel übersetzt, keine erfundenen Quellen; 2 PRÜFEN-Marker (APA-Angaben Pahl 2007, Schweder 2013) bleiben für Hannes.
