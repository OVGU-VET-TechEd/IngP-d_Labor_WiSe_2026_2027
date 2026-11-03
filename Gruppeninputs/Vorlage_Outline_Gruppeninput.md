# Vorlage: Outline für einen Gruppen-Input (Beispiel T1)

Ingenieurpädagogisches Labor · WiSe 2026/27 · OVGU

Diese Datei zeigt am **Gruppen-Input T1 „Lehren und Lernen in ingenieurpädagogischen Laboren“**, wie aus einer
Originalpräsentation eine quellentreue LiaScript-Präsentation geplant wird. Sie dient als **Vorlage für die
Gruppen-Inputs T2–T4**.

| Gruppe | Thema                          | Termin     | Grundlage                                                                 | Ordner                                       |
| ------ | ------------------------------ | ---------- | ------------------------------------------------------------------------- | -------------------------------------------- |
| T1     | Lehren und Lernen im Labor     | 03.11.2026 | Originalpräsentation (PDF, 23 Seiten)                                     | `Gruppeninputs/T1_Lehren_und_Lernen/`        |
| T2     | Sicherheit, Gesundheit, Arbeit | 24.11.2026 | Vorjahrespräsentation (Text: `_agent/package/inputs/quelle_T2.md`)        | `Gruppeninputs/T2_Sicherheit_Gesundheit_Arbeit/` |
| T3     | Sicherheit in Schulen          | 01.12.2026 | **keine** Vorjahrespräsentation – nur Stichworte (`quelle_T3.md`)          | `Gruppeninputs/T3_Sicherheit_in_Schulen/`    |
| T4     | Gefährdung und Schutzziele     | 08.12.2026 | Vorjahrespräsentation (Text: `_agent/package/inputs/quelle_T4.md`)        | `Gruppeninputs/T4_Gefaehrdung_und_Schutzziele/` |

Ergebnis für T1: [`T1_Lehren_und_Lernen_Praesentation.md`](T1_Lehren_und_Lernen/T1_Lehren_und_Lernen_Praesentation.md) ·
[in LiaScript öffnen](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/IngP-d_Labor_WiSe_2026_2027/main/Gruppeninputs/T1_Lehren_und_Lernen/T1_Lehren_und_Lernen_Praesentation.md) ·
passender Prompt: [`Beispiel_Prompt_Gruppeninput.md`](Beispiel_Prompt_Gruppeninput.md)

**So ist die Datei aufgebaut**

1. **Teil A – Outline** im Format des Teaching-Agent (`templates/course-outline.yaml`); lässt sich 1:1 in `journal.md` → `## Outline` übernehmen.
2. **Teil B – Folienplan:** jede LiaScript-Folie mit ihrer Originalfolie.
3. **Teil C – Regeln zur Quellentreue** – gelten für alle vier Gruppen-Inputs.
4. **Teil D – Blanko-Vorlage** für T2–T4 zum Ausfüllen.
5. **Teil E – Abnahme-Checkliste** vor dem Hochladen.

---

## Teil A – Outline (Beispiel T1)

<!-- Format: Teaching-Agent, tasks/create-outline.md – flache `* __Label:__`-Punkte, keine Unterüberschriften -->

* __Title:__
  Lehren und Lernen in ingenieurpädagogischen Laboren – Gruppen-Input T1
* __Target Audience:__
  Studierende Lehramt an berufsbildenden Schulen (gewerblich-technische Fachrichtungen: Metall-, Elektro-, Bau-,
  Informations-, Prozesstechnik), ca. 10–20 Personen, fachlich vorgebildet, didaktisch am Anfang. Ihr
  Studiennachweis: zu einem Ausbildungsberuf und Lernfeld einen domänenspezifischen Laboraufbau didaktisch einbinden.
* __Time Commitment:__
  Sitzung 4 am 03.11.2026, 09:00–11:00 Uhr: 70 Min. Input + 20 Min. Aktivierung (Organisationsüberblick,
  „Erwartungen an die Präsentationen“). Aktivierung als vier Kurzchecks à ca. 5 Min.
* __Abstract:__
  Der Input folgt der Originalpräsentation „Lehren und Lernen in ingenieurpädagogischen Laboren“
  (Ingenieurpädagogisches Labor, Dozent: M. Robra; Fassung 2023) Folie für Folie: Lernsysteme im Bereich
  Mechatronik und Automatisierung (Fachkenntnisse, Kompetenzen, Psychomotorik), Vor- und Nachteile technischer
  Lernsysteme, Methoden der schulischen Berufsbildung, Merkmale und Arten von Experimenten (Labor-/Feldexperiment,
  wissenschaftliches/technisches Experiment), das technische Experiment aus didaktischer Sicht, Experimente als
  didaktisches Mittel, Prüfverfahren, Planungsebenen für Experimente, didaktische Reduktion (Ebenen und Formen,
  Beispiel Hebel-/Momentgesetz), Medienspektrum, Formen der Veranschaulichung, Medienmerkmale, Formen
  wissenserwerbsbezogener Interaktivitäten, Angebot-Nutzungs-Modell und „didaktischer Raum“. Nutzen: Die
  Studierenden erhalten die Begriffe, mit denen sie ihren eigenen Laboraufbau didaktisch begründen.
* __Learning Objectives:__
  <!-- aus den Folieninhalten abgeleitet – Operatoren vom Lehrenden zu bestätigen; sie stehen NICHT in der Präsentation -->
  1. Fachkenntnisse, Kompetenzen und Psychomotorik, die technische Lernsysteme fördern, sowie deren Vor- und Nachteile **nennen** (Folien 2–4).
  2. Labor- und Feldexperiment sowie wissenschaftliches und technisches Experiment **unterscheiden** und die Doppelfunktion des technischen Experiments **erläutern** (Folien 6–8).
  3. Zielstellungen von Experimenten (kausal, konditional, final) und Prüfverfahren **zuordnen** (Folien 9–11).
  4. Horizontale und vertikale didaktische Reduktion am Beispiel des Hebel-/Momentgesetzes **erläutern** (Folien 12–14).
  5. Medienspektrum, Formen der Veranschaulichung und Interaktionsformen **zuordnen** und das Angebot-Nutzungs-Modell **beschreiben** (Folien 15–20).

---

## Teil B – Folienplan (Beispiel T1)

Original: `Presentation_IngLab_2023_Lehren_Lernen_ingped_Labor_V_01.pdf` (23 Seiten). Spalte „Original“ = PDF-Seite.

| #  | LiaScript-Folie                                              | Original      | Darstellung                                  | Interaktion / Animation              |
| -- | ------------------------------------------------------------ | ------------- | -------------------------------------------- | ------------------------------------ |
| 1  | Lehren und Lernen in ingenieurpädagogischen Laboren (Titel)  | 1             | Titel, Grundlage                             | –                                    |
| 2  | Lernsysteme im Bereich Mechatronik und Automatisierung       | 2             | Abbildung + drei Listen                      | Fragmente 1–3                        |
| 3  | Vorteile von technischen Lernsystemen                        | 3             | zwei Listen                                  | Fragment 1                           |
| 4  | Nachteile von technischen Lernsystemen …                     | 4             | Liste mit Unterpunkten                       | Fragment 1                           |
| 5  | **Kurzcheck 1:** Vor- und Nachteile                          | Ergänzung → 3, 4 | –                                          | Multiple Choice, Single Choice       |
| 6  | Methoden der schulischen Berufsbildung                       | 5 (ohne Titel) | Satz + Auswahl von acht Methoden            | –                                    |
| 7  | Merkmale eines Experiments                                   | 6             | Liste + Tabelle Labor-/Feldexperiment        | Fragment 1                           |
| 8  | Experimente nach Erkenntniszielen                            | 7             | Gegenüberstellung + Zitat Pahl               | Fragment 1                           |
| 9  | Das technische Experiment aus didaktischer Sicht             | 8             | Liste                                        | Fragment 1                           |
| 10 | Experimente als didaktisches Mittel                          | 9             | Zitat Schweder + Schema + Liste              | Fragment 1                           |
| 11 | Prüfverfahren als Technisches Experiment                     | 10            | Liste + zwei Aussagen                        | Fragmente 1–2                        |
| 12 | Planungsebenen für den Einsatz von Experimenten              | 11            | Abbildung → Lesefassung                      | Abbildung wird durch Text ersetzt    |
| 13 | **Kurzcheck 2:** Experiment und Prüfverfahren                | Ergänzung → 6–10 | –                                          | 2 × Matrix-Quiz, Single Choice       |
| 14 | Didaktische Reduktion                                        | 12            | Zitat + Liste + ASCII-Diagramm               | Fragment 1                           |
| 15 | Ebenen und Formen der didaktischen Reduktion – „Mundus in gutta“ | 13        | Abbildung → Lesefassung                      | Abbildung wird durch Text ersetzt    |
| 16 | Beispiel „Hebel Gesetz“ und „Moment Gesetz“                  | 14            | Abbildung                                    | –                                    |
| 17 | Beispiel „Moment Gesetz“ – Lesefassung                       | 14            | Text der Abbildung (aus der PPTX)            | Fragmente 1–2                        |
| 18 | **Kurzcheck 3:** Didaktische Reduktion                       | Ergänzung → 12–14 | –                                         | 3 × Single Choice                    |
| 19 | Medienspektrum …                                             | 15            | Abbildung → Tabelle                          | Abbildung wird durch Tabelle ersetzt |
| 20 | Formen der Veranschaulichung                                 | 16            | Tabelle                                      | –                                    |
| 21 | Medienmerkmale – Darstellungsformen                          | 17            | Tabelle                                      | –                                    |
| 22 | Formen wissenserwerbsbezogener Interaktivitäten              | 18            | Tabelle                                      | –                                    |
| 23 | Angebot-Nutzungs-Modell der Wirkungsweise des Unterrichts    | 19            | Abbildung, Sprechertext beschreibt sie       | –                                    |
| 24 | „Didaktischer Raum“ – Medienunterstützte Lehr-/Lernarrangements | 20         | Abbildung, Sprechertext beschreibt sie       | –                                    |
| 25 | **Kurzcheck 4:** Medien                                      | Ergänzung → 15–19 | –                                         | Single Choice, Matrix-Quiz           |
| 26 | Zur Vertiefung: Videos                                       | Ergänzung     | Linktabelle (YouTube)                        | –                                    |
| 27 | Quellen                                                      | 2–20, 23      | nur auf den Folien genannte Quellen          | –                                    |

**Entscheidungen, die im Folienplan stecken**

- Die Reihenfolge der Originalfolien bleibt unverändert; Kurzchecks stehen **nach** einem Block, nie mitten darin.
- Folie 14 (dichte Abbildung) wird auf zwei LiaScript-Folien verteilt: Abbildung, dann Lesefassung.
- Die Literaturliste der PDF-Seiten 21–23 gehört zu einem Arbeitsschutz-Foliensatz (DGUV, BMAS …) und wird **nicht**
  übernommen – nur Herzig & Aßmann (2009) passt zum Thema. ⚠️ **Für T2 prüfen:** Diese Liste stammt vermutlich aus der
  Vorjahrespräsentation „Sicherheit, Gesundheit, Arbeit“.
- Offensichtliche Tippfehler im Folientext werden korrigiert und im Kopfkommentar der Präsentation aufgelistet; Zitate bleiben wörtlich.

---

## Teil C – Regeln zur Quellentreue (für T1–T4)

1. **Gliederung der Originalpräsentation beibehalten.** Jede Originalfolie wird mindestens eine LiaScript-Folie (`##`),
   in derselben Reihenfolge. Nichts weglassen; Umordnen nur mit Begründung im Folienplan.
2. **Nichts erfinden.** Keine neuen Fakten, Quellen, Paragraphen, Normnummern, Statistiken oder Jahreszahlen.
   Fehlende bibliografische Angaben **nicht ergänzen**, sondern so übernehmen, wie sie auf der Folie stehen.
3. **Wortlaut übernehmen.** Folientext wörtlich; nur offensichtliche Tippfehler korrigieren und im Kopfkommentar
   dokumentieren. Zitate und Namen in Quellen nie „korrigieren“.
4. **Herkunft markieren:** unter jeder Überschrift `<!-- src: Folie N -->`.
   ⚠️ LiaScript-Stolperstein: **Keine runden Klammern in HTML-Kommentaren** – LiaScript zeigt solche Kommentare
   sonst als sichtbaren Text an. Erläuterungen gehören in den Kopfkommentar.
5. **Abbildungen:** Originalabbildung mit Quelle im Bildtitel und aussagekräftigem Alternativtext. Ist sie zu dicht,
   folgt eine **Lesefassung** mit dem Text *aus der Abbildung* (`{{0-1}}` Abbildung, `{{1}}` Lesefassung).
6. **Sprechertext** `--{{n}}--` zu jedem Fragment `{{n}}`: erklärt nur, was auf der Folie steht.
7. **Ergänzungen sichtbar kennzeichnen** (`> [!NOTE] ✍️ Ergänzung`): Kurzchecks und Video-Tipps.
   - Kurzcheck-Antworten stammen **nur** aus den Folien; jede Lösung (`***`-Block) gibt die vollständige Originalaussage
     mit Foliennummer wieder.
   - Keine Gruppenarbeit nötig – alle Kurzchecks lassen sich live im Plenum zeigen (`classroom: enable`).
   - Videos: Existenz und Titel prüfen (z. B. über `https://www.youtube.com/oembed?url=…`), Kanal angeben,
     Hinweis „vor dem Einsatz selbst ansehen“.
8. **Quellenfolie** = nur die auf den Originalfolien genannten Quellen, mit Foliennummer.
9. **LiaScript-Syntax:** genau eine `#`-Überschrift; Quizoptionen nicht einrücken; Matrix-Quiz mit gleicher Spaltenzahl
   in Kopf und Zeilen; jeder `<section>`-Block geschlossen; ASCII-Diagramme als ` ```ascii `; URLs in `<small>` als
   Markdown-Link schreiben (`[url](url)`), sonst verschluckt der Autolink das `</small>`.

---

## Teil D – Blanko-Vorlage für T2–T4

> Kopieren, ausfüllen, als `Gruppeninputs/Tn_…/Tn_Outline.md` speichern. Alles in «…» ersetzen.

### D.1 Outline

* __Title:__
  «Titel der Originalpräsentation» – Gruppen-Input «Tn»
* __Target Audience:__
  Studierende Lehramt an berufsbildenden Schulen (gewerblich-technische Fachrichtungen), ca. 10–20 Personen,
  fachlich vorgebildet, didaktisch am Anfang.
* __Time Commitment:__
  Sitzung «Nr.» am «Datum», 09:00–11:00 Uhr: 70 Min. Input + 20 Min. Aktivierung.
* __Abstract:__
  Der Input folgt der Originalpräsentation «Titel» («Herkunft, Jahr») Folie für Folie: «Folientitel in Reihenfolge».
  Nutzen für den eigenen Laboraufbau: «ein Satz».
* __Learning Objectives:__
  <!-- aus den Folieninhalten ableiten, je Lernziel die Folien angeben -->
  1. «Inhalt» **nennen** (Folien «…»).
  2. «Inhalt» **erläutern** (Folien «…»).
  3. «Inhalt» **zuordnen / unterscheiden** (Folien «…»).
  4. «Inhalt» **beurteilen** (Folien «…»).

### D.2 Quellen-Inventar (zuerst ausfüllen, vor dem Folienplan)

| Original | Folientitel | Inhalt (Stichworte) | Abbildung? | Zitat / Quelle auf der Folie |
| -------- | ----------- | ------------------- | ---------- | ---------------------------- |
| 1        | «…»         | «…»                 | «ja/nein»  | «…»                          |
| 2        | «…»         | «…»                 | «…»        | «…»                          |

> **T3 (Sicherheit in Schulen):** Es gibt keine Vorjahrespräsentation. Das Inventar listet die Stichworte aus
> `quelle_T3.md`; sie sind die **einzige** zulässige Faktenbasis. Unsichere Angaben mit `<!-- PRÜFEN: … -->` markieren
> (ohne runde Klammern).

### D.3 Folienplan

| #  | LiaScript-Folie | Original | Darstellung | Interaktion / Animation |
| -- | --------------- | -------- | ----------- | ----------------------- |
| 1  | «Titel»         | 1        | Titel       | –                       |
| 2  | «…»             | «…»      | «…»         | «…»                     |
| …  | **Kurzcheck 1:** «Thema» | Ergänzung → «Folien» | – | «Quiztypen» |
| …  | Zur Vertiefung: Videos | Ergänzung | Linktabelle | – |
| …  | Quellen         | «Folien» | Liste       | –                       |

Richtwert: ein Kurzcheck nach jedem Block von ca. 15–20 Min., insgesamt ca. 20 Min. Aktivierung.

### D.4 Kurzchecks

| Kurzcheck | nach Folie | prüft Folien | Fragen (Typ) | Lösung belegt durch |
| --------- | ---------- | ------------ | ------------ | ------------------- |
| 1         | «…»        | «…»          | «…»          | Folie «…», wörtlich |

### D.5 Video-Tipps

| Zu Folie | Video-Titel (geprüft) | Kanal | URL | Sprache |
| -------- | --------------------- | ----- | --- | ------- |
| «…»      | «…»                   | «…»   | «…» | «de/en» |

### D.6 Entscheidungen und Abweichungen

| # | Entscheidung / Abweichung vom Original | Begründung |
| - | -------------------------------------- | ---------- |
| 1 | «z. B. Folie 7 auf zwei Folien verteilt» | «z. B. Abbildung zu dicht» |

---

## Teil E – Abnahme-Checkliste

- [ ] Jede Originalfolie ist im Folienplan einer LiaScript-Folie zugeordnet (`<!-- src: Folie N -->` vorhanden).
- [ ] Zeilenabgleich: Jeder Textbaustein der Originalfolien steht in der Präsentation.
- [ ] Keine neuen Fakten, Quellen oder Zahlen; Ergänzungen sind als „✍️ Ergänzung“ gekennzeichnet.
- [ ] Jeder Kurzcheck lässt sich mit den Folien beantworten; jede Lösung zitiert die Originalaussage.
- [ ] Alle Abbildungen haben Quelle und Alternativtext; dichte Abbildungen haben eine Lesefassung.
- [ ] Zu jedem `{{n}}` gibt es einen Sprechertext `--{{n}}--`.
- [ ] Keine runden Klammern in HTML-Kommentaren; keine nackten URLs in `<small>`.
- [ ] In LiaScript geöffnet und jede Folie angesehen (Präsentations- **und** Lehrbuchmodus).
- [ ] Video-Links geprüft und vorab angesehen.
- [ ] Quellenfolie enthält nur Quellen von den Originalfolien.
