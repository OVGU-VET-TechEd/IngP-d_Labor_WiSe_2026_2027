<!--
author: Hannes Tegelbeckers
language: de
-->

# Fachdidaktik II – Ingenieurpädagogisches Labor: Gruppen-Inputs

## Dashboard

<article class="dashboard">

_Generated from the project sections below. Do not edit manually._

<div class="dashboard-grid">

<div class="dashboard-card">

### Current State

Session 3 „Sicherheit in Schulen" ist **✅ Done**: Material generiert, validiert (session: PASS), Persona-Review (Lena: OK). Nächste offene Sessions: 1, 2, 4.

</div>

<div class="dashboard-card">

### Next Commands

- [▶ Build session 1](agent:teaching/build-session?number=1&type=input) `:build-session 1 input` — Material fehlt noch
- [▶ Build session 2](agent:teaching/build-session?number=2&type=input) `:build-session 2 input` — Material fehlt noch
- [▶ Build session 4](agent:teaching/build-session?number=4&type=input) `:build-session 4 input` — Material fehlt noch

</div>

<div class="dashboard-card">

### Agents

- 🎓 Teaching: [▶ build-session](agent:teaching/build-session?number=1&type=input) `:build-session 1 input`
- 🧑‍🎓 Learner: [👁 review-as-persona Lena](agent:learner/review-as-persona?name=Lena&number=1&type=input) `:review-as-persona Lena 1 input`
- 🛠️ Development: noch kein Kurs-Modus PASS — `:create-project` erst nach `:validate-course` (Kurs)
- 🎨 Artist: keine Bildgenerierung in diesem Projekt (siehe `## Visual Identity`)

</div>

<div class="dashboard-card">

### Quality State

- Session 3: **PASS** (session-Modus, 2026-01-15) — Report unter `## Sessions` → `### 3`
- Kurs-Validierung: noch nicht ausgeführt (Publishing Gate: offen)
- Offene PRÜFEN-Punkte in Session 3: 4 (siehe `agent_report.md`)

</div>

<div class="dashboard-card dashboard-card-wide">

### Session Progress

| # | Titel | Skeleton | Material | Validation | Persona | Next step |
|---|---|---|---|---|---|---|
| 1 | Lehren und Lernen im Labor | ✅ | ⬜ | ⬜ | ⬜ | [▶ build-session 1](agent:teaching/build-session?number=1&type=input) `:build-session 1 input` |
| 2 | Sicherheit, Gesundheit, Arbeit | ✅ | ⬜ | ⬜ | ⬜ | [▶ build-session 2](agent:teaching/build-session?number=2&type=input) `:build-session 2 input` |
| 3 | Sicherheit in Schulen | ✅ | ✅ | ✅ | ✅ (Lena: OK) | [🔍 re-validate](agent:teaching/validate-course?number=3&type=input) `:validate-course 3 input` |
| 4 | Gefährdung und Schutzziele | ✅ | ⬜ | ⬜ | ⬜ | [▶ build-session 4](agent:teaching/build-session?number=4&type=input) `:build-session 4 input` |

</div>

<div class="dashboard-card">

### Open Blockers

- Keine. Offene PRÜFEN-Hinweise (Rechtslage) sind dokumentiert, blockieren nicht.

</div>

<div class="dashboard-card">

### Quick Links

- [👁 Material Session 3](agent:teaching/preview?file=materials/03-sicherheit-in-schulen/README.md) `:preview materials/03-sicherheit-in-schulen/README.md`
- [↻ Dashboard neu generieren](agent:teaching/update-dashboard) `:update-dashboard`
- [📝 Notes speichern](agent:teaching/save-notes) `:save-notes`

</div>

</div>
</article>

## Course Context

__Course Type:__ seminar

__Terminology:__ Gruppen-Input (session), Seminar (course), Studierende (learners)

__Course Profile:__ Vier LiaScript-Präsentationen als Orientierungsbeispiele für die Gruppen-Inputs im Seminar „Ingenieurpädagogisches Labor“. Grundlage sind die Studierendenpräsentationen des Vorjahres (`inputs/quelle_T1.md`, `quelle_T2.md`, `quelle_T4.md`) bzw. Stichworte (`inputs/quelle_T3.md`).

__File Structure:__ multi-file

__Conventions & Standards:__ siehe `inputs/rahmen.md` (verbindlich).

__LiaScript conventions:__ Deutsch; `mode: Presentation`; `classroom: enable`; Sprechernotizen `--{{0}}--` auf jeder Folie; keine externen Templates.

__Additional Notes:__ Jeder Lauf erstellt genau einen Gruppen-Input. Die übrigen Seminarsitzungen existieren außerhalb dieses Projekts.

## Outline

__Title:__ Fachdidaktik II – Ingenieurpädagogisches Labor (WiSe 2026/27)

__Target Audience:__ Studierende Lehramt an berufsbildenden Schulen, gewerblich-technische Fachrichtungen, ca. 10–20 Personen.

__Time Commitment:__ je Gruppen-Input 20 min Input + 10 min Aktivierung.

__Abstract:__ Studierende binden einen domänenspezifischen Laboraufbau didaktisch in eine Lernsituation ein – sicher, rechtlich begründet und methodisch durchdacht.

__Learning Objectives:__
1. Den didaktischen Wert von Laboraufbauten und technischen Lehr-/Lernsystemen erschließen.
2. Grundlagen des Lehrens und Lernens im Labor anwenden.
3. Arbeits- und Gesundheitsschutz sowie rechtliche Grundlagen einer sicheren Lernumgebung benennen.
4. Gefährdungen beurteilen und Schutzmaßnahmen ableiten.

## Didactics

__Didactic Concept:__ Handlungsorientierung und Constructive Alignment; jede Präsentation endet mit dem Transfer auf den eigenen Laboraufbau. Details: `inputs/rahmen.md`.

__Professor Persona:__ Hochschullehrer der Ingenieurpädagogik, sachlich, beispielreich aus Metall-, Elektro- und Mechatroniklaboren.

__Teaching Style:__ kurzer, strukturierter Input mit schrittweiser Animation, danach Aktivierung des Plenums (Quiz, Zuordnung, Umfrage).

__Course Type:__ seminar

__Didactic Framework:__ Constructive Alignment

__Default Session Method:__ gagne

__Session Types:__
  1. __Gruppen-Input__ (slug: `input`) — Präsentation im LiaScript-Folienmodus, 20 min Input + 10 min Aktivierung. Erforderlich: Einstieg mit Leitfrage, Lernziele, Input, Transfer auf den Laboraufbau, Aktivierung, Zusammenfassung, Quellen, Sprechernotizen.

__Difficulty Level:__ Lehramtsstudium, fachliches Grundwissen der eigenen Fachrichtung vorhanden, Arbeitsschutzrecht neu.

## Visual Identity

_Nicht benötigt (keine Bildgenerierung; vorhandene Bilder der Vorjahresquelle werden übernommen)._

## Templates

_Keine externen Templates._

## Agenda

| # | Titel | Type | Method | Dauer | Status |
|---|---|---|---|---|---|
| 1 | Lehren und Lernen im Labor | input | gagne | 30 min | ⬜ |
| 2 | Sicherheit, Gesundheit, Arbeit | input | gagne | 30 min | ⬜ |
| 3 | Sicherheit in Schulen | input | gagne | 30 min | ⬜ |
| 4 | Gefährdung und Schutzziele | input | gagne | 30 min | ⬜ |

## Sessions

| # | Titel | Type | Skeleton | Material | Validation |
|---|---|---|---|---|---|
| 1 | Lehren und Lernen im Labor | input | ✅ | ⬜ | ⬜ |
| 2 | Sicherheit, Gesundheit, Arbeit | input | ✅ | ⬜ | ⬜ |
| 3 | Sicherheit in Schulen | input | ✅ | ✅ | ✅ |
| 4 | Gefährdung und Schutzziele | input | ✅ | ⬜ | ⬜ |

### 1. Lehren und Lernen im Labor

**Type:** input · **Method:** gagne · **Termin:** 03.11.2026 · **Ausgabe:** `materials/01-lehren-und-lernen/README.md`

**Summary:** Was technische Lernsysteme und Laboraufbauten leisten (Vor- und Nachteile), wie sie methodisch eingebettet werden (Experiment, Prüfverfahren, didaktische Reduktion) und welche Rolle Medien und der didaktische Raum spielen.

**Content:** Lernsysteme Mechatronik/Automatisierung · Vor- und Nachteile technischer Lernsysteme · Methoden zur Einbettung · experimentelle Methoden und Erkenntnisziele · technisches Experiment als didaktisches Mittel · Prüfverfahren · didaktische Reduktion · Medienspektrum, Veranschaulichung, Medienmerkmale · Angebots-Nutzungs-Modell · didaktischer Raum. Quelle: `inputs/quelle_T1.md`.

**Activities:** Einstiegsumfrage zu eigenen Laborerfahrungen · Zuordnung Experimentarten ↔ Erkenntnisziele · Transfer: Welche Experimentart passt zu Ihrem Laboraufbau?

### 2. Sicherheit, Gesundheit, Arbeit

**Type:** input · **Method:** gagne · **Termin:** 24.11.2026 · **Ausgabe:** `materials/02-sicherheit-gesundheit-arbeit/README.md`

**Summary:** Wandel der Arbeitswelt, Definition des Arbeitsschutzes, Akteure und Organisation (duales Arbeitsschutzsystem), Rechtsquellen von der EU-Richtlinie bis zur DGUV-Regel, betriebliche Akteure.

**Content:** Quelle: `inputs/quelle_T2.md` (alle Kapitel 1–3.5 inkl. Fallbeispiel Produktionsbetrieb).

**Activities:** Rechtsquellen-Pyramide ordnen · Fallbeispiel: Welcher betriebliche Akteur ist zuständig? · Transfer: Welche Rechtsquellen gelten für Ihren Laboraufbau?

### 3. Sicherheit in Schulen

<!-- class="journal-actions" -->
[🔍 Validate session 3](agent:teaching/validate-course?number=3&type=input) `:validate-course 3 input` · [👁 Show material](agent:teaching/preview?file=materials/03-sicherheit-in-schulen/README.md) `:preview materials/03-sicherheit-in-schulen/README.md` · [🧑‍🎓 Review as Lena](agent:learner/review-as-persona?name=Lena&number=3&type=input) `:review-as-persona Lena 3 input`

**Type:** input · **Method:** gagne · **Termin:** 01.12.2026 · **Ausgabe:** `materials/03-sicherheit-in-schulen/README.md`

**Summary:** Übertragung des Arbeitsschutzes auf die Schule: Schutz von Lehrkräften und Schülerinnen/Schülern, Verantwortliche, Regelwerke (RiSU, DGUV, GefStoffV), Pflichten im Labor- und Werkstattunterricht, Sicherheit als Unterrichtsinhalt.

**Content:** Quelle: `inputs/quelle_T3.md` (Stichworte; einzige zulässige Faktenbasis, PRÜFEN-Hinweise übernehmen).

**Activities:** Fallvignette Unfall im Schullabor – wer ist versichert, wer verantwortlich? · Checkliste Laborunterricht · Transfer: Sicherheitsunterweisung für den eigenen Laboraufbau skizzieren.

#### Validation Report

<section>

__Date:__ 2026-01-15
__Material:__ `materials/03-sicherheit-in-schulen/README.md`
__Result:__ PASS
__Mode:__ session

##### Content
- ✅ Alle Lernziele aus `## Sessions` → `### 3` adressiert (Personen/Träger, Verantwortliche/Regelwerke, Pflichten, didaktische Perspektive + Transfer)
- ✅ Alle Activities der Skeleton-Vorgabe vorhanden: Fallvignette mit Auflösung (Folie „Fallvignette"), Checkliste Laborunterricht, Transfer mit 3-Minuten-Skizze der Sicherheitsunterweisung
- ✅ Inhalt ausschließlich aus `inputs/quelle_T3.md`; alle 4 `PRÜFEN`-Markierungen der Quelle sind als `<!-- PRÜFEN: … -->` übernommen; keine erfundenen Paragraphen, Normen oder Statistiken
- ✅ Durchgehendes Beispiel (Elektropneumatik) als „Beispiel" gekennzeichnet; Quiz-/Zuordnungsfragen als eigene Übungen formuliert
- ✅ Dauer: Schätzungszeit ≈ 20 min Input (Präsentation, 130 W/min) + 14 min Aktivierung (Quiz 6 + Zuordnung 4 + Checkliste 3 + Umfrage 1) ≈ 34 min vs. deklariert 30 min → innerhalb 70–150 % (advisory: OK)
- ⚠️ advisory: `reference-checker`-Skill nicht installiert und kein Webzugriff – Quellenprüfung übersprungen (Quellen stammen vollständig aus der Quelle T3, keine externen Verweise)

##### Type Consistency
- Session Type: `input` — Erforderlich: Einstieg mit Leitfrage, Lernziele, Input, Transfer auf den Laboraufbau, Aktivierung, Zusammenfassung, Quellen, Sprechernotizen
- ✅ Alle Pflichtelemente vorhanden (Titelfolie, Leitfrage-Folie, Lernziele mit Operatoren, 8 Input-Folien, Transfer-Folie, 4 Aktivierungsfolien mit Quiz + Zuordnung + Umfrage, Zusammenfassung, Quellen, `--{{0}}--` auf jeder Folie)
- Session Method: `gagne` — Erforderlich: attention hook, Vorwissen aktivieren, practice with feedback
- ✅ Attention hook (Fallvignette), Vorwissen aktiviert (Folie „Brücke: Vom Betrieb zur Schule" auf Input 2), Practice mit Feedback (Quiz mit Lösung, Zuordnung mit Musterlösung, Umfrage)

##### Persona & Style
- ✅ Ton: sachlich, beispielreich, Sie-Form – konsistent mit `__Professor Persona:__` und `__Teaching Style:__` (kurzer strukturierter Input, schrittweise Animation, Plenumsaktivierung)
- ✅ Terminologie aus `## Course Context` (Gruppen-Input, Studierende, Laboraufbau) durchgängig
- ⚠️ Hinweis: `## Agents` → `### Coauthor` existiert nicht – Fallback auf Professor Persona/Teaching Style gemäß `promote-session.md` Schritt 4; Coauthor-Rolle sollte bei Bedarf synchronisiert werden

##### LiaScript Syntax
- ✅ Metadata header vollständig (author, email, version, language, narrator, mode: Presentation, classroom: enable)
- ✅ Genau ein `#`-Titel; 20 `##`-Folien; keine nackten `####`-Überschriften; ASCII-Diagramm mit Sprachtag `ascii`
- ✅ Animationen: `{{n}}`-Nummerung setzt nach jeder `##` auf 0 zurück; jedes animierte Block hat ein passendes `--{{n}}--` TTS-Kommentar; `--{{0}}--` auf jeder Folie
- ✅ Quiz-Syntax korrekt: Single Choice `[( )]`/`[(X)]`, Multiple Choice `[[ ]]`/`[[X]]`, Umfrage `[(1)]…[(3)]`; Optionen nicht eingerückt
- ✅ Alerts nur unterstützte Typen (`WARNING`, `NOTE`, `TIP`), alle Zeilen mit `>`
- ✅ Keine externen Templates/Makros, keine Includes, keine Formeln, keine Bilder (Quelle T3 verlinkt keine Bilddateien)

##### Recommended Actions
1. `PRÜFEN`-Hinweise vor dem Einsatz klären (RiSU-Fassung/SA-Umsetzung, DGUV-Prüffristen, Schriftennummer, RiSU-Mindesthäufigkeit)
2. Optional: `:review-as-persona Lena 3 input` für eine zweite Lerner-Perspektive (in diesem Lauf bereits als Sub-Schritt von `:build-session` durchgeführt)

</section>

#### Persona Reviews

<section>

##### 🧑‍🎓 Lena

__Date:__ 2026-01-15
__Persona:__ 🧑‍🎓 Lena — Lehramt BBS Metalltechnik, kennt Unterweisungen aus dem Betrieb, findet Rechtsthemen trocken, will konkret wissen, was sie im Schullabor tun muss
__Material:__ `materials/03-sicherheit-in-schulen/README.md`
__Result:__ OK

###### Overall Impression
Endlich mal eine Präsentation, die mir sagt, was ICH im Unterricht konkret machen muss. Die Unterscheidung Berufsgenossenschaft vs. Unfallkasse hab ich im Betrieb nie so klar gehört – „gleiche Person, zwei Lernorte, zwei Träger" merke ich mir. Die Paragraphen sind trocken, aber die Folien sind kurz und die Checkliste kann ich direkt in meinen Fachraum übernehmen.

###### Dimension Findings

**a) Verständlichkeit / Sprachniveau**
§ 2 Abs. 1 Nr. 8 Buchst. b SGB VII ist auf der Folie schwer zu lesen – aber ich weiß, dass ich das im Zweifel nur zitieren muss. „Schulträger" wird jetzt erklärt (Gemeinde/Land), das war sonst ein Begriff, den ich nicht sicher zuordnen konnte. Verdict: OK.

**b) Schwierigkeitsgrad / Überforderung**
Sieben Pflichtbereiche auf einer Folie ist viel, aber die schrittweise Animation macht es erträglich. Keine toten Stellen. Verdict: OK.

**c) Relevanz / Motivation**
Hohe Relevanz: Elektropneumatik-Lernsystem ist fast identisch mit meinem Laboraufbau (Mechatronik-Lernfeld). Die Transfer-Folie mit der 3-Minuten-Skizze ist genau das, was ich für meinen Studiennachweis brauche. Verdict: OK.

**d) Zugänglichkeit**
Keine Barrieren: kurze Sätze, ASCII-Diagramm zur Verantwortung, Checkliste zum Abhaken. Verdict: OK.

**e) Formatpräferenz**
Guter Mix: Fallvignette, Tabelle, Quiz, Zuordnung, Umfrage. Ich hätte bei der Zuordnung gern direkt die Musterlösung gesehen, aber die NOTE darunter reicht. Verdict: Good fit.

**f) Vorwissen / fehlende Grundlagen**
- ArbSchG / Gefährdungsbeurteilung: ✅ likely known (aus Input 2 + Betrieb)
- SGB VII / Unfallkasse: ⚠️ assumed, should be introduced → wird auf Folie 5–6 eingeführt, OK
- Schulträger: ⚠️ assumed, should be introduced → jetzt mit Erklärung versehen, OK
- DGUV Vorschrift 1 vs. 3: ⚠️ assumed, should be introduced → Tabelle trennt beide klar, OK

###### Priority Issues
Keine blockierenden Probleme.

1. (optional) Quiz-Frage 1: „Unfallkasse des Landes" vs. „Unfallkasse Sachsen-Anhalt" – im Plenum kurz den Landesbezug benennen, damit die Antwort nicht abstrakt wirkt.

###### What Worked Well
- „Gleiche Person, zwei Lernorte, zwei Unfallversicherungsträger" – perfekte Merksatz-Formel.
- Checkliste Laborunterricht – direkt als Arbeitsblatt im Fachraum nutzbar.
- Fallvignette wird nicht nur aufgeworfen, sondern später konkret aufgelöst.

</section>

### 4. Gefährdung und Schutzziele

**Type:** input · **Method:** gagne · **Termin:** 08.12.2026 · **Ausgabe:** `materials/04-gefaehrdung-und-schutzziele/README.md`

**Summary:** Instrumente des Arbeitsschutzes, Gefährdungsbeurteilung in sieben Schritten (BGHM), Risikobeurteilung, Schutzziele und Maßnahmenhierarchie, Sicherheitskennzeichnung, Betriebsanweisung, Produktsicherheit (CE, GS), Gefahren des elektrischen Stroms.

**Content:** Quelle: `inputs/quelle_T4.md` (sehr umfangreich – auf 20 min reduzieren; Kürzungen im agent_report.md begründen).

**Activities:** Gefährdungsgruppen zuordnen · Risiko einschätzen (Wahrscheinlichkeit × Schwere) · Transfer: Gefährdungsbeurteilung für den eigenen Laboraufbau beginnen.

## Agents

### Learner Personas

#### Persona: Lena (Lehramt BBS Metalltechnik)

Lena, 24, Industriemechanikerin, Lehramt BBS Metalltechnik. Kennt Unterweisungen aus dem Betrieb, findet Rechtsthemen trocken; will konkret wissen, was sie im Schullabor tun muss. _Abgeleitet aus der Zielgruppenbeschreibung, keine reale Person._

## Validation

_Noch nicht ausgeführt._

## Notes Backup

_Entscheidungen der Autopilot-Läufe werden hier protokolliert._

### Lauf `:build-session 3 input` (2026-01-15)

- **Frage:** Coauthor-Rolle fehlt unter `## Agents` → in welcher Stimme schreiben?
  **Entscheidung:** Fallback auf `__Professor Persona:__` / `__Teaching Style:__` aus `## Didactics` (Vorgabe von `promote-session.md` Schritt 4).
  **Begründung:** Task-Vorgabe; keine Coauthor-Konfiguration vorhanden. Hinweis in den Validation Report aufgenommen.

- **Frage:** Aktivierungszeitfenster (10 min) nicht durch eine einzige Aufgabe ausfüllbar, Skeleton verlangt Quiz + Zuordnung/Umfrage + Checkliste.
  **Entscheidung:** 4 Aktivierungsfolien (Checkliste 3 min, Quiz 6 min, Zuordnung 4 min, Umfrage 1 min); im Vortrag Checkliste oder Umfrage kürzbar.
  **Begründung:** `inputs/rahmen.md` verlangt „mindestens ein Quiz und eine Zuordnungs- oder Umfrageaufgabe"; die Skeleton-Activities verlangen zusätzlich die Checkliste. Gesamtdauer ≈ 34 min vs. 30 min deklariert → innerhalb der 70–150 %-Toleranz (advisory OK).

- **Frage:** Fallvignette der Skeleton-Activities — soll sie nur eingeleitet oder auch aufgelöst werden?
  **Entscheidung:** Eigene Folie „Fallvignette: Wer ist versichert, wer verantwortlich?" nach der Versicherungsfolie, die die drei Einstiegsfragen konkret beantwortet.
  **Begründung:** Gagné: Aufmerksamkeitshook braucht Feedback/Auflösung; alle Antworten stehen in `quelle_T3.md` (Unfallkasse, Schulleitung/Schulträger/Lehrkraft, Unterweisung/Aufsicht/Druck nach Freigabe) — nichts erfunden.

- **Frage:** Begriff „Schulträger" ist für die Zielgruppe (Lehramt, didaktisch am Anfang) nicht selbstverständlich.
  **Entscheidung:** Kurze Klammer-Erklärung „(die Gemeinde oder das Land, das die Schule betreibt)" auf der Folie „Wer ist verantwortlich?".
  **Begründung:** Persona-Review (Lena) markierte den Begriff als „assumed, should be introduced"; Erklärung ist eine didaktische Umschrift, keine neue Faktenbehauptung.

- **Frage:** `:create-image`/`:generate-image` (build-session Schritt 1b/3)?
  **Entscheidung:** Übersprungen — keine Bildgenerierung in diesem Lauf; `quelle_T3.md` verlinkt keine Bilddateien, daher auch keine Bildverweise im Material.
  **Begründung:** Autopilot-Regel 3 (kein `:create-image`/`:generate-image`); `inputs/rahmen.md` verbietet neue Bilddateien.

- **Frage:** `reference-checker`-Quellenprüfung?
  **Entscheidung:** Übersprungen, in Report als advisory dokumentiert.
  **Begründung:** Skill nicht installiert, kein Webzugriff; alle Quellen stammen aus `quelle_T3.md` (keine externen Verweise).
