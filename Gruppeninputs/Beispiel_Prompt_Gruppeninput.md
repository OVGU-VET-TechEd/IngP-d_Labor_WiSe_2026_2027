# Beispiel-Prompt: Gruppen-Input als quellentreue LiaScript-Präsentation

Ingenieurpädagogisches Labor · WiSe 2026/27 · OVGU

Zwei Varianten für dieselbe Aufgabe – aus einer Originalpräsentation wird eine LiaScript-Präsentation, die der
Originalgliederung folgt und **nichts erfindet**:

- **Variante A – HAWKI** (für Studierende): eine Prompt-Kette aus vier strukturierten Prompts.
- **Variante B – Teaching-Agent** (für Lehrende, Claude Code): Befehlsfolge plus Auftragsprompt.

Beide setzen die [Vorlage: Outline für einen Gruppen-Input](Vorlage_Outline_Gruppeninput.md) um (Teil C = Regeln).
Ausgefülltes Beispiel: [T1 – Lehren und Lernen in ingenieurpädagogischen Laboren](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/IngP-d_Labor_WiSe_2026_2027/main/Gruppeninputs/T1_Lehren_und_Lernen/T1_Lehren_und_Lernen_Praesentation.md).

> **Prompt-Dokumentation nicht vergessen:** Laut Kursregeln dokumentieren Sie die **ersten drei Prompts mit Iterationen
> und Originalausgaben** im Anhang ([Beispiel](../00_Organisation/KI/Beispiel_Prompt_Dokumentation.md)).

---

## Variante A – HAWKI (Studierende)

**Vorbereitung:** Kopieren Sie den Text der Originalpräsentation **folienweise** in ein Textdokument
(`Folie 1: …`, `Folie 2: …`). Notieren Sie zu jeder Abbildung Dateiname und Quelle. Bei T3 gibt es keine
Originalpräsentation – dort ersetzen die Stichworte aus `quelle_T3.md` den Folientext.

Arbeiten Sie die Prompts **nacheinander im selben Chat** ab und prüfen Sie jede Ausgabe, bevor Sie weitergehen.

### Prompt 1 – Quellen-Inventar und Folienplan

```text
ROLLE
Du bist Fachdidaktiker:in für die gewerblich-technische Berufsbildung und erfahren mit LiaScript.

KONTEXT
Wir halten im Seminar „Ingenieurpädagogisches Labor“ (OVGU, Lehramt an berufsbildenden Schulen) den
Gruppen-Input «Tn – Thema» am «Datum» (70 Min. Input + 20 Min. Aktivierung). Grundlage ist ausschließlich
die Originalpräsentation unten.

AUFGABE
1. Erstelle ein Quellen-Inventar: eine Zeile pro Originalfolie.
2. Erstelle daraus einen Folienplan für eine LiaScript-Präsentation.

VORGABEN
- Reihenfolge und Gliederung der Originalfolien bleiben unverändert. Keine Folie entfällt.
- Eine dichte Folie darf auf zwei LiaScript-Folien verteilt werden – begründe das.
- Plane 3–4 Kurzchecks, jeweils NACH einem inhaltlichen Block von ca. 15–20 Minuten; nenne die Folien, die sie prüfen.
- Am Ende: eine Folie „Zur Vertiefung: Videos“ und eine Folie „Quellen“.
- Erfinde keine Inhalte. Folien, die nicht zum Thema passen, markierst du mit PRÜFEN statt sie zu übernehmen.

AUSGABEFORMAT
Zwei Markdown-Tabellen:
1. | Original | Folientitel | Inhalt (Stichworte) | Abbildung? | Zitat / Quelle auf der Folie |
2. | # | LiaScript-Folie | Original | Darstellung | Interaktion / Animation |
Danach eine Liste „Offene Fragen“.

ORIGINALPRÄSENTATION
«Folientext hier einfügen: Folie 1: … Folie 2: …»
«Abbildungen: Dateiname – Folie – Quelle»
```

✅ **Prüfen Sie:** Hat jede Originalfolie eine Zeile? Stimmt die Reihenfolge? Steht etwas im Plan, das nicht im Original vorkommt?

### Prompt 2 – LiaScript-Präsentation erzeugen

```text
ROLLE
Du bist LiaScript-Autor:in und arbeitest streng quellentreu.

KONTEXT
Der Folienplan aus der vorherigen Antwort ist freigegeben. Die Präsentation wird im Präsentationsmodus von LiaScript
gezeigt; die Gruppe spricht frei, die Sprechertexte dienen als Notizen und Vorlesestimme.

AUFGABE
Schreibe die vollständige LiaScript-Präsentation nach dem Folienplan.

VORGABEN – Inhalt
- Folientext WÖRTLICH übernehmen. Nur offensichtliche Tippfehler korrigieren und im Kopfkommentar auflisten.
  Zitate und Namen in Quellen nie verändern.
- Nichts erfinden: keine neuen Fakten, Quellen, Paragraphen, Normnummern, Statistiken, Jahreszahlen.
  Fehlende Literaturangaben NICHT ergänzen.
- Unter jede Überschrift einen Herkunftsmarker: <!-- src: Folie N -->
- Abbildungen: ![Alternativtext, der den Inhalt beschreibt](dateiname.png "Quelle: …"). Ist eine Abbildung zu dicht,
  folgt mit {{0-1}} vor dem Bild und {{1}} vor dem Text eine „Lesefassung“, die nur den Text der Abbildung enthält.
- Kurzcheck- und Video-Folien beginnen mit:
  > [!NOTE] ✍️ Ergänzung
  > Nicht Teil der Originalfolien. Alle Antworten stehen auf den Folien «…».
- Quellenfolie: nur Quellen, die auf den Originalfolien stehen, mit Foliennummer.

VORGABEN – LiaScript-Syntax
- Kopf: author, email, version, language: de, narrator: Deutsch Female, mode: Presentation, classroom: enable, title, comment.
- Genau eine Überschrift mit #, danach jede Folie mit ##.
- Zu jedem Fragment {{n}} gehört ein Sprechertext in einer eigenen Zeile:
                  --{{n}}--
  darunter 1–3 Sätze, die NUR erklären, was auf der Folie steht. Zähler beginnen auf jeder Folie bei 0.
- Mehrere Absätze in einem Fragment: in <section> … </section> mit Leerzeilen innen.
- Quiz- und Umfrageoptionen beginnen am Zeilenanfang (nie 4 Leerzeichen einrücken).
- Keine runden Klammern in HTML-Kommentaren (LiaScript zeigt solche Kommentare sonst als Text an) und keine runden
  Klammern im Alternativtext von Bildern ![…] (LiaScript zeigt das Bild sonst womöglich nicht an).
- URLs innerhalb von <small> immer als Markdown-Link schreiben: [url](url).
- ASCII-Diagramme in einen Codeblock mit dem Sprachkürzel ascii.

AUSGABEFORMAT
Die vollständige Datei «Tn_Thema_Praesentation.md» in EINEM Markdown-Codeblock. Keine Erklärungen davor oder danach.

FOLIENTEXT
«Folientext erneut einfügen – das Modell soll nicht aus dem Gedächtnis arbeiten»
```

### Prompt 3 – Kurzchecks aus den Folien

```text
ROLLE
Du bist Fachdidaktiker:in und erstellst diagnostische Quizfragen.

AUFGABE
Erstelle für Kurzcheck «Nr.» 2–4 Fragen zu den Folien «von–bis».

VORGABEN
- Jede richtige Antwort steht wörtlich oder sinngemäß auf diesen Folien. Distraktoren stammen bevorzugt von
  anderen Folien – z. B. ein Nachteil als falscher „Vorteil“.
- Keine Gruppenarbeit: jede Frage ist allein im Plenum lösbar.
- Fragetypen mischen: Single Choice - [(X)], Multiple Choice - [[X]], Matrix-Quiz
  [[Spalte A] [Spalte B]]
  [   (X)        ( )   ] Aussage
- Nach jeder Frage ein Lösungsblock zwischen zwei Zeilen *** mit der VOLLSTÄNDIGEN Originalaussage und der Foliennummer.

AUSGABEFORMAT
Nur der LiaScript-Block für die Folie „## Kurzcheck «Nr.»: «Thema»“, beginnend mit dem Ergänzungs-Hinweis.
```

### Prompt 4 – Gegenprüfung

```text
ROLLE
Du bist kritische:r Gutachter:in. Du suchst Fehler, du lobst nicht.

AUFGABE
Vergleiche die LiaScript-Präsentation mit der Originalpräsentation Folie für Folie.

AUSGABEFORMAT
Eine Tabelle | Originalfolie | Befund | Fundstelle in der .md | Art |
mit Art = FEHLT · VERÄNDERT · ERFUNDEN · SYNTAX. Am Ende: Anzahl der Befunde je Art.

ORIGINAL
«Folientext»

PRÄSENTATION
«generierte .md»
```

> ⚠️ **Auch ein Prüf-Modell irrt.** Prüfen Sie die Befunde selbst und öffnen Sie die Präsentation in LiaScript
> (`https://liascript.github.io/course/?` + Raw-Link der Datei) – erst dort sehen Sie Darstellungsfehler.

---

## Variante B – Teaching-Agent (Lehrende, Claude Code)

**Agent:** [OVGU-VET-TechEd/teaching-agent](https://github.com/OVGU-VET-TechEd/teaching-agent)
(lokal: `~/GitHub/Research/AI_Tools/2026/teaching-agent`, mit dem lokalen Kurs-Input `specs/course-input/ingpaed-labor/`,
der nie veröffentlicht wird).

**1. Arbeitskopie anlegen** – nicht im veröffentlichten Agent-Repo arbeiten, denn `journal.md` und das Material sind Kursarbeit.
Bei einer einzelnen Lektion schreibt der Agent das Material in die `README.md` im Wurzelordner; deshalb die Agent-README vorher umbenennen:

```bash
git clone https://github.com/OVGU-VET-TechEd/teaching-agent.git ~/Arbeit/teaching-agent-T2
cp -R ~/GitHub/Research/AI_Tools/2026/teaching-agent/specs/course-input ~/Arbeit/teaching-agent-T2/specs/
cd ~/Arbeit/teaching-agent-T2 && git mv README.md AGENT_README.md && claude
```

**2. Befehlsfolge** (Stand LiaScript-`main`, 03.11.2026: Sitzungsbefehle nehmen nur noch die Nummer)

| Schritt | Befehl | Eingabe / Entscheidung |
| ------- | ------ | ---------------------- |
| 1 | `:init-course` | Kurstyp **single-lesson** (ein Gruppen-Input = eine Lektion; Dateistruktur ist dann fest „eine Datei“) |
| 2 | `:create-outline` | Teil A der [Outline-Vorlage](Vorlage_Outline_Gruppeninput.md) für «Tn» |
| 3 | `:create-didactics` | Session Type „Gruppen-Input“ (siehe unten) |
| 4 | `:create-session 1 «Titel»` | Folienplan aus Teil D.3 als Gliederung |
| 5 | `:build-session 1` | Schleife: Material → Prüfung → Persona-Review |
| 6 | `:validate-syntax 1` | muss PASS ergeben |
| 7 | — | `README.md` der Arbeitskopie nach `Gruppeninputs/Tn_…/Tn_…_Praesentation.md` kopieren, Bilder mitnehmen, in LiaScript ansehen |

Session Type für Schritt 3:

```text
__Gruppen-Input__ (slug: `gruppeninput`) — Quellentreue LiaScript-Präsentation einer Originalpräsentation, 70 Min. Input + 20 Min. Aktivierung.
Required: je Originalfolie ein `<!-- src: Folie N -->`-Marker in Originalreihenfolge; nach jedem Block ein als Ergänzung markierter Kurzcheck mit Lösungen aus den Folien; Quellenfolie nur mit Quellen der Originalfolien.
```

**3. Auftragsprompt** (als erste Nachricht nach der Aktivierung):

```text
Wir erstellen den Gruppen-Input «Tn – Thema» für das Ingenieurpädagogische Labor (WiSe 2026/27, Termin «Datum»).
Lies zuerst specs/course-input/ingpaed-labor/README.md und halte die dort genannte Lesereihenfolge ein.

Grundlage ist ausschließlich die Originalpräsentation in specs/course-input/ingpaed-labor/01_quellen/«Tn»_Folientext.md
(bei T3: die Stichworte aus quelle_T3.md).

Verbindlich:
1. Gliederung und Reihenfolge der Originalfolien beibehalten; keine Folie weglassen.
2. Nichts erfinden – keine neuen Fakten, Quellen, Normen, Zahlen. Fehlende Literaturangaben nicht ergänzen.
3. Folientext wörtlich; Tippfehler nur korrigieren und im Kopfkommentar dokumentieren.
4. Ergänzungen (Kurzchecks, Video-Tipps) sichtbar als „✍️ Ergänzung“ kennzeichnen; Kurzcheck-Lösungen zitieren die Originalfolie.
5. Video-Tipps nur mit geprüftem Titel und Kanal (YouTube oEmbed), mit Hinweis „vor dem Einsatz selbst ansehen“.
6. Keine runden Klammern in HTML-Kommentaren und im Alternativtext von Bildern; URLs in <small> als Markdown-Link.

Starte mit :create-outline und nutze dafür Teil A der Vorlage Gruppeninputs/Vorlage_Outline_Gruppeninput.md als Muster.
Frage nach, wenn eine Originalfolie nicht zum Thema passt, statt sie zu übernehmen oder zu ersetzen.
```

> **Hinweis:** Der Agent fragt als „kritischer Sparringspartner“ nach. Beantworten Sie die Fragen mit Bezug auf die
> Originalfolien. Prüfen Sie das Ergebnis vor dem Veröffentlichen mit der Abnahme-Checkliste (Teil E der Vorlage).
