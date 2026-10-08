#!/usr/bin/env python3
"""Baut ../Beispiel_Prompt_Dokumentation.md aus den Rohdaten (Prompts und Originalausgaben unverändert)."""
import json, pathlib, re, subprocess

H = pathlib.Path(__file__).parent
LINT = H.parents[4] / "XX_Teacher_Agent/GX10_Wiki/tools/lia_lint.py"
r = lambda n: (H / n).read_text(encoding="utf-8").strip()
meta = json.loads(r("meta.json"))


def block(text):
    return "````markdown\n" + text + "\n````"


def stats(pid, v):
    m = meta[pid][v]
    return f"{m['s']} s · {m['in']} Token Eingabe · {m['out']} Token Ausgabe"


def lint(name):
    tmp = H.parent / f"_lint_{name}"; tmp.write_text(r(name), encoding="utf-8")
    out = subprocess.run(["python3", str(LINT), str(tmp), "--presentation"], capture_output=True, text=True).stdout
    tmp.unlink()
    return out.splitlines()[0].split(": ", 1)[1] if out else "?"


def minutes(text):
    """Summe der Spalte, deren Kopf „Zeit“ enthält (Spaltenposition egal)."""
    rows = [[c.strip() for c in row.split("|")] for row in re.findall(r"^\|(.+)\|\s*$", text, re.M)]
    head = next((r_ for r_ in rows if any("Zeit" in c for c in r_)), None)
    if not head:
        return 0
    k = next(i for i, c in enumerate(head) if "Zeit" in c)
    return sum(int(m.group(1)) for r_ in rows if len(r_) > k
               for m in [re.match(r"^\**(\d{1,3})\**(\s*min)?$", r_[k])] if m)


def prompt_view(pid):
    """Prompt wie gesendet; eingefügtes Material durch Verweis ersetzt (vollständig in _rohdaten/)."""
    t = r(f"{pid}_prompt.md")
    rep = {"P1_v2.md": "[… hier vollständig eingefügt: Originalausgabe 1.2 …]",
           "P2_v2.md": "[… hier vollständig eingefügt: Originalausgabe 2.2 …]"}
    for f, ph in rep.items():
        t = t.replace(r(f), ph)
    v = (H.parent / "Vorlage_LiaScript_Praesentation.md").read_text(encoding="utf-8").strip()
    return t.replace(v, "[… hier vollständig eingefügt: Vorlage_LiaScript_Praesentation.md …]")


STEPS = [
    ("P1", "Lernsituation entwerfen",
     "Eine handlungsorientierte Lernsituation für den eigenen Laboraufbau als Ausgangspunkt für den Studiennachweis.",
     "Der erste Entwurf wird gezielt nachgeschärft: Zeitbudget prüfbar machen, Fehlersuche statt nur Aufbau "
     "(höherer Anspruch), Differenzierung für heterogene Lerngruppen. Jede Rückmeldung ist **konkret und prüfbar** – "
     "nicht „mach es besser“.",
     lambda: f"Zeitsumme in der Tabelle nachgerechnet: v1 = {minutes(r('P1_v1.md'))} min, v2 = {minutes(r('P1_v2.md'))} min (Vorgabe: 180 min)."
             + (" **Achtung:** Das Modell schreibt unter v2 selbst „Summe der Zeiten: 180 Minuten“ – die Tabelle ergibt etwas anderes. "
                "Typischer Fehler: Modelle behaupten, eine Vorgabe erfüllt zu haben. Immer nachrechnen!"
                if "180" in r('P1_v2.md') and minutes(r('P1_v2.md')) != 180 else "")),
    ("P2", "Gefährdungsbeurteilung vorbereiten",
     "Ein Entwurf der Gefährdungsbeurteilung für die Lernsituation aus Prompt 1 – die Ausgabe von Prompt 1 (v2) wird als Material mitgegeben (Prompt-Verkettung).",
     "Die Iteration lässt das Modell die eigene Ausgabe gegen Regeln prüfen (STOP-Reihenfolge, keine unbelegten "
     "Paragraphen) und macht aus einer Liste einen unterrichtstauglichen Ablauf.",
     lambda: f"[PRÜFEN]-Hinweise: v1 = {r('P2_v1.md').count('PRÜFEN')}, v2 = {r('P2_v2.md').count('PRÜFEN')} · "
             f"Paragraphenzeichen (§): v1 = {r('P2_v1.md').count('§')}, v2 = {r('P2_v2.md').count('§')}."),
    ("P3", "LiaScript-Präsentation aus Vorlage erzeugen",
     "Aus Lernsituation (P1 v2) und Gefährdungsbeurteilung (P2 v2) entsteht mit der "
     "[LiaScript-Vorlage](Vorlage_LiaScript_Praesentation.md) eine Präsentation.",
     "Die Iteration gibt dem Modell die **echte Ausgabe eines Prüfskripts** (`lia_lint.py`) zurück – "
     "Fehler werden nicht beschrieben, sondern belegt. In diesem Lauf meldete das Skript schon für v1 **0 Fehler**: "
     "Die mitgegebene Vorlage mit Syntaxregeln wirkt. Ohne Vorlage hatten Modelle im Test regelmäßig eingerückte "
     "Quizoptionen und Sprechernotizen erzeugt. Die Iteration lohnt sich dann trotzdem als Kontrollschritt.",
     lambda: f"Prüfskript: v1 → {lint('P3_v1.md')}; v2 → {lint('P3_v2.md')}."),
]

doc = [f"""<!--
author:    Hannes Tegelbeckers
email:     hannes.tegelbeckers@ovgu.de
version:   0.1.0
language:  de
narrator:  Deutsch Female

title:     Beispiel: Prompt-Dokumentation für den Studiennachweis
comment:   Drei aufeinander aufbauende Prompts mit je einer Iteration und den unveränderten Originalausgaben – Muster für den Anhang des Studiennachweises im Ingenieurpädagogischen Labor.
-->

# Beispiel: Prompt-Dokumentation

So dokumentieren Sie im Anhang Ihres Studiennachweises die **ersten drei Prompts** – mit Iterationen und
**Originalausgaben** (unverändert, auch wenn sie Fehler enthalten). Ihre Korrekturen gehören in die Spalte
„geprüft/geändert“, nicht in die Originalausgabe.

> **Hinweis zu diesem Beispiel:** Die Ausgaben wurden am 05.10.2026 mit dem offenen Modell *{meta['model']}* auf dem
> Lehrstuhl-Server erzeugt. In HAWKI stehen andere Modelle zur Verfügung – Ihre Ausgaben sehen daher anders aus.
> Das Vorgehen ist dasselbe.

## Aufbau eines fortgeschrittenen Prompts

Kein Chat („Kannst du mir mal …“), sondern ein **strukturierter Auftrag**:

| Baustein | Wozu | Beispiel aus Prompt 1 |
| --- | --- | --- |
| Rolle | Perspektive und Fachsprache festlegen | „Du bist Fachdidaktiker:in für gewerblich-technische Berufsbildung …“ |
| Kontext | Alles, was das Modell nicht wissen kann | Beruf, Laboraufbau, Lerngruppe, Zeit |
| Aufgabe | Ein klares Ergebnis | „Entwirf eine handlungsorientierte Lernsituation …“ |
| Vorgaben | Qualitätskriterien und Verbote | vollständige Handlung, nichts erfinden, [PRÜFEN] |
| Ausgabeformat | Prüfbare Struktur | nummerierte Abschnitte, Tabelle mit festen Spalten |

**Iterieren** heißt: die Ausgabe prüfen und **konkrete, überprüfbare Rückmeldungen** geben – im selben Verlauf,
damit das Modell seinen Entwurf kennt. **Verketten** heißt: die geprüfte Ausgabe eines Prompts wird Material des nächsten.

```ascii
 Prompt 1 ──► Ausgabe v1 ──► Iteration ──► Ausgabe v2 ─┐
 (Lernsituation)                                       │ Material
 Prompt 2 ◄────────────────────────────────────────────┘
 (Gefährdungen) ──► v1 ──► Iteration ──► v2 ─┐
 Prompt 3 ◄──────────────────────────────────┘ + Vorlage
 (LiaScript) ──► v1 ──► Prüfskript ──► Iteration ──► v2
```
"""]

for i, (pid, title, goal, why, measure) in enumerate(STEPS, 1):
    doc.append(f"""
## Prompt {i}: {title}

**Ziel:** {goal}

### Prompt {i} (Version 1)

{block(prompt_view(pid))}

### Originalausgabe {i}.1

<small>{meta['model']} · {stats(pid, 'v1')}</small>

{block(r(f'{pid}_v1.md'))}

### Iteration {i}.2

**Warum diese Iteration?** {why}

{block(r(f'{pid}_iteration.md'))}

### Originalausgabe {i}.2

<small>{meta['model']} · {stats(pid, 'v2')}</small>

{block(r(f'{pid}_v2.md'))}

### Prüfung durch die Gruppe

- Messbar: {measure()}
- Fachlich zu prüfen: <!-- Gruppe trägt hier ihre Prüfung ein: was stimmt, was wurde geändert, welche Quelle -->
  Angaben mit [PRÜFEN] gegen Rahmenlehrplan, RiSU, DGUV-Vorschriften und Herstellerangaben abgleichen.
""")

doc.append(f"""
## Kennzeichnung im Studiennachweis

| Werkzeug (Modell) | Zweck | Prompt | Was geprüft/geändert wurde |
| --- | --- | --- | --- |
| {meta['model']} (lokal) | Entwurf Lernsituation | Prompt 1 + Iteration 1.2 (Anhang) | Zeitsumme, Lernfeld im Rahmenlehrplan nachgeschlagen, Störung fachlich geprüft |
| {meta['model']} (lokal) | Entwurf Gefährdungsbeurteilung | Prompt 2 + Iteration 2.2 (Anhang) | jede Maßnahme gegen RiSU/DGUV geprüft, [PRÜFEN]-Stellen geklärt |
| {meta['model']} (lokal) | LiaScript-Präsentation | Prompt 3 + Iteration 3.2 (Anhang) | Syntax mit Prüfskript, Inhalte gegen P1/P2 abgeglichen |

<small>APA 7 (Beispiel für HAWKI): Anbieter (Jahr). *Modellname* [Large language model]. Zugriff über HAWKI, OVGU, am TT.MM.JJJJ.</small>

Die erzeugte Präsentation (Ausgabe 3.2, unverändert): [Beispiel_Praesentation_KI_generiert.md](Beispiel_Praesentation_KI_generiert.md)
""")

(H.parent / "Beispiel_Prompt_Dokumentation.md").write_text("\n".join(doc), encoding="utf-8")
(H.parent / "Beispiel_Praesentation_KI_generiert.md").write_text(r("P3_v2.md") + "\n", encoding="utf-8")
print("ok")
