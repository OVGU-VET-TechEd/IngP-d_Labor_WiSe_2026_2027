#!/usr/bin/env python3
"""Erzeugt die Originalausgaben für Beispiel_Prompt_Dokumentation.md (3 Prompts × 2 Iterationen).
Modell: qwen3.8:27b lokal auf dem GX10 (Stellvertreter für HAWKI). Ausgaben werden unverändert gespeichert.
Aufruf: python3 run_prompts.py   (aus diesem Ordner)"""
import json, subprocess, os, time, pathlib

HERE = pathlib.Path(__file__).parent
MODEL = "qwen3.8:27b"
LINT = HERE.parents[4] / "XX_Teacher_Agent/GX10_Wiki/tools/lia_lint.py"


def chat(messages):
    req = json.dumps({"model": MODEL, "stream": False, "think": False, "messages": messages,
                      "options": {"num_ctx": 32768}})
    t = time.time()
    r = subprocess.run(["ssh", "-o", "BatchMode=yes", "ovgu-server", "curl -s http://127.0.0.1:11434/api/chat -d @-"],
                       input=req, capture_output=True, text=True, check=True)
    d = json.loads(r.stdout)
    return d["message"]["content"].strip(), {"s": round(time.time() - t), "in": d.get("prompt_eval_count"), "out": d.get("eval_count")}


def save(name, text):
    (HERE / name).write_text(text, encoding="utf-8")


def run(pid, prompt, iteration):
    meta = {}
    m = [{"role": "user", "content": prompt}]
    out1, meta["v1"] = chat(m); save(f"{pid}_v1.md", out1)
    m += [{"role": "assistant", "content": out1}, {"role": "user", "content": iteration(out1)}]
    out2, meta["v2"] = chat(m); save(f"{pid}_v2.md", out2)
    save(f"{pid}_prompt.md", prompt); save(f"{pid}_iteration.md", iteration(out1))
    print(pid, meta, flush=True)
    return out2, meta


P1 = """# Rolle
Du bist Fachdidaktiker:in für gewerblich-technische Berufsbildung und planst Laborunterricht an einer berufsbildenden Schule.

# Kontext
- Ausbildungsberuf: Mechatroniker/-in, 2. Ausbildungsjahr
- Laboraufbau: Elektropneumatik-Lernsystem (doppeltwirkende Zylinder, 5/2-Wegeventile mit Magnetspule, induktive Näherungsschalter, 24-V-Steuerung mit Netzteil, Druckluftversorgung 6 bar)
- Lerngruppe: 16 Auszubildende, heterogene Vorkenntnisse (einige aus der Metalltechnik, einige aus der Elektrotechnik)
- Zeit: 4 Unterrichtsstunden à 45 Minuten im Schullabor

# Aufgabe
Entwirf eine handlungsorientierte Lernsituation, in der die Auszubildenden am Laboraufbau eine elektropneumatische Steuerung für einen betrieblichen Auftrag planen, aufbauen und in Betrieb nehmen.

# Vorgaben
- Vollständige Handlung: Informieren, Planen, Entscheiden, Ausführen, Kontrollieren, Bewerten.
- Für jede Phase ein konkretes, überprüfbares Handlungsprodukt.
- Nenne keine Lernfeldnummer, keine Normnummern und keine Literatur. Wo eine Angabe aus dem Rahmenlehrplan nötig wäre, schreibe [PRÜFEN: …].

# Ausgabeformat (Markdown)
1. Titel der Lernsituation
2. Auftrag aus Kundensicht (3–5 Sätze)
3. Tabelle: Phase | Handlung der Lernenden | Handlungsprodukt | Zeit (min)
4. Drei Kompetenzen, jeweils mit Operator (z. B. „planen“, „prüfen“)
5. Offene Punkte für die Lehrkraft"""

I1 = lambda _: """Überarbeite deinen Entwurf:
a) Die Zeiten müssen sich auf genau 180 Minuten summieren – gib die Summe unter der Tabelle an.
b) Baue in den Auftrag eine Störung ein, die die Lernenden diagnostizieren müssen (Fehlersuche, nicht nur Aufbau).
c) Ergänze für jede Phase eine Differenzierung für Lernende mit wenig Vorwissen.
Gib nur die vollständige überarbeitete Fassung aus."""

P2_T = """# Rolle
Du bist Lehrkraft mit Zusatzqualifikation Arbeitssicherheit und bereitest eine Gefährdungsbeurteilung für Laborunterricht vor.

# Material
Lernsituation (Entwurf):
---
{ls}
---

# Aufgabe
Erstelle den Entwurf einer Gefährdungsbeurteilung für diese Unterrichtseinheit am Elektropneumatik-Lernsystem.

# Vorgaben
- Prüfe die 11 Gefährdungsgruppen (mechanisch, elektrisch, Gefahrstoffe, biologisch, Brand/Explosion, thermisch, spezielle physikalische Einwirkungen, Arbeitsumgebung, physische Belastung, psychische Faktoren, sonstige) und nimm nur die relevanten auf.
- Maßnahmen nach dem STOP-Prinzip (Substitution, Technisch, Organisatorisch, Personenbezogen) kennzeichnen.
- Risiko als gering / mittel / hoch mit einer kurzen Begründung.
- Rechtsgrundlagen nur allgemein benennen (z. B. Arbeitsschutzgesetz, Richtlinie zur Sicherheit im Unterricht, DGUV Vorschrift 3) – keine Paragraphen. Alles Unsichere mit [PRÜFEN: …] markieren.

# Ausgabeformat (Markdown)
1. Tabelle: Gefährdung | Gruppe | Risiko (Begründung) | Maßnahme | STOP
2. Fünf Inhalte für die Sicherheitsunterweisung der Auszubildenden
3. Rechtsgrundlagen (allgemein) mit [PRÜFEN]-Hinweisen"""

I2 = lambda _: """Prüfe deine Ausgabe selbst und überarbeite sie:
a) Steht bei jeder Gefährdung zuerst eine technische Maßnahme (T), bevor organisatorische (O) und personenbezogene (P) folgen? Korrigiere die Reihenfolge, wo nicht.
b) Entferne alle Paragraphen- oder Normnummern, die nicht in meiner Aufgabe stehen, und markiere die Stelle mit [PRÜFEN].
c) Formuliere die Sicherheitsunterweisung als 5-Minuten-Ablauf mit einer Aktivierung der Auszubildenden (z. B. Gefährdung am Aufbau selbst zeigen lassen).
Gib nur die vollständige überarbeitete Fassung aus."""

P3_T = """# Rolle
Du erstellst LiaScript-Präsentationen für Lehramtsstudierende. Halte dich exakt an die Anleitung im Kommentarblock der Vorlage.

# Aufgabe
Fülle die Vorlage unten vollständig aus. Thema: Elektropneumatik-Lernsystem im Laborunterricht für Mechatroniker/-innen. Gruppe: Gruppe 1, Datum: 03.11.2026. Es gibt keine Bilddateien – lass die Bildzeile weg und beschreibe den Aufbau in Text.

# Material
## Lernsituation
{ls}

## Gefährdungsbeurteilung
{gb}

## Vorlage
{vorlage}

# Ausgabe
Nur die vollständige Markdown-Datei, ohne umschließenden Codeblock und ohne Kommentar davor oder danach."""


def I3(out1):
    tmp = HERE / "_tmp_lint.md"; tmp.write_text(out1, encoding="utf-8")
    r = subprocess.run(["python3", str(LINT), str(tmp), "--presentation"], capture_output=True, text=True)
    tmp.unlink()
    report = "\n".join(l.replace(str(tmp), "praesentation.md") for l in r.stdout.splitlines())
    save("P3_lint_v1.txt", report)
    return f"""Ein Prüfskript hat deine Datei geprüft. Ergebnis:

{report}

Behebe alle FEHLER und alle WARNUNGEN, die Folien ohne Sprechernotiz betreffen. Ändere sonst nichts am Inhalt.
Gib nur die vollständige korrigierte Datei aus."""


if __name__ == "__main__":
    os.chdir(HERE)
    ls, m1 = run("P1", P1, I1)
    gb, m2 = run("P2", P2_T.format(ls=ls), I2)
    vorlage = (HERE.parent / "Vorlage_LiaScript_Praesentation.md").read_text(encoding="utf-8")
    pr, m3 = run("P3", P3_T.format(ls=ls, gb=gb, vorlage=vorlage), I3)
    save("meta.json", json.dumps({"model": MODEL, "P1": m1, "P2": m2, "P3": m3}, indent=1))
