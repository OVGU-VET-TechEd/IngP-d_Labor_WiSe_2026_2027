# T3 Sicherheit in Schulen – Fixes durch Claude (2026-10-05)
Rohausgabe `raw/output.md` (472 Zeilen, 20 Folien). Lauf 12:47–13:35 (47 min, 29 Schritte). Grundlage: Stichwortliste von Claude (`quelle_T3.md`).

| # | Befund | Art | Fix |
|---|---|---|---|
| 1 | 68 Marker + 109 Zeilen eingerückt | Syntax | `lia_fix.py` |
| 2 | Doppelte Titelfolie (`#` + `## Titelfolie`) | Struktur | zusammengeführt |
| 3 | Ergänzung „Schulträger ist die Gemeinde oder das Land“ (nicht in Quelle, für BBS ungenau) | erfunden | gestrichen |
| 4 | Zuordnungsaufgabe als leere Tabelle („Haken Sie an“) – nicht interaktiv | Didaktik | 3 Single-Choice-Fragen |
| 5 | Quellenfolie behauptet „Stichwortliste der Vorjahresgruppe“ | falsch | korrigiert (Stichwortliste des Dozenten) |
| 6 | „Schläucheführung“ | Tippfehler | korrigiert |

Alle 5 PRÜFEN-Marker aus der Stichwortliste korrekt übernommen, keine neuen Normnummern.
