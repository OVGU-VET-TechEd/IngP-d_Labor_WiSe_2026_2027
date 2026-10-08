<!--
author: Hannes Tegelbeckers
language: de
-->

# Fachdidaktik II – Ingenieurpädagogisches Labor: Gruppen-Inputs

## Dashboard

_Generiert aus den Projektabschnitten unten. Nicht manuell bearbeiten._

**Aktueller Stand:** Session 2 (Sicherheit, Gesundheit, Arbeit) fertiggestellt – Material, Validierung (PASS with concerns) und Persona-Review (Lena: OK) abgeschlossen.

**Next Commands:**
1. [▶ Build session 1](agent:teaching/build-session?number=1&type=input) `:build-session 1 input` — Material für Session 1 fehlt
2. [▶ Build session 3](agent:teaching/build-session?number=3&type=input) `:build-session 3 input` — Material für Session 3 fehlt
3. [▶ Build session 4](agent:teaching/build-session?number=4&type=input) `:build-session 4 input` — Material für Session 4 fehlt

**Agents:**
- 🎓 __Teaching__ — weitere Sessions aufbauen · [▶ build-session](agent:teaching/build-session?number=1&type=input)
- 🧑‍🎓 __Learner__ — zweite Perspektive zu Session 2 · [▶ review-as-persona](agent:learner/review-as-persona?name=Lena&number=2&type=input)
- 🛠️ __Development__ — erst nach course-mode-PASS · [▶ switch](agent:development/switch)
- 🎨 __Artist__ — keine Bildgenerierung in diesem Projekt · [▶ switch](agent:artist/switch)

**Session Progress:**

| # | Title | Status | Next step |
|---|-------|--------|-----------|
| 1 | Lehren und Lernen im Labor | 🟡 skeleton | [▶ Build](agent:teaching/build-session?number=1&type=input) `:build-session 1 input` |
| 2 | Sicherheit, Gesundheit, Arbeit | ✅ done | – |
| 3 | Sicherheit in Schulen | 🟡 skeleton | [▶ Build](agent:teaching/build-session?number=3&type=input) `:build-session 3 input` |
| 4 | Gefährdung und Schutzziele | 🟡 skeleton | [▶ Build](agent:teaching/build-session?number=4&type=input) `:build-session 4 input` |

**Open Blockers:** None. (PRÜFEN-Punkte aus Session 2 sind in `agent_report.md` dokumentiert.)

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
| 2 | Sicherheit, Gesundheit, Arbeit | input | gagne | 30 min | ✅ |
| 3 | Sicherheit in Schulen | input | gagne | 30 min | ⬜ |
| 4 | Gefährdung und Schutzziele | input | gagne | 30 min | ⬜ |

## Sessions

| # | Titel | Type | Skeleton | Material | Validation |
|---|---|---|---|---|---|
| 1 | Lehren und Lernen im Labor | input | ✅ | ⬜ | ⬜ |
| 2 | Sicherheit, Gesundheit, Arbeit | input | ✅ | ✅ | ✅ |
| 3 | Sicherheit in Schulen | input | ✅ | ⬜ | ⬜ |
| 4 | Gefährdung und Schutzziele | input | ✅ | ⬜ | ⬜ |

### 1. Lehren und Lernen im Labor

**Type:** input · **Method:** gagne · **Termin:** 03.11.2026 · **Ausgabe:** `materials/01-lehren-und-lernen/README.md`

**Summary:** Was technische Lernsysteme und Laboraufbauten leisten (Vor- und Nachteile), wie sie methodisch eingebettet werden (Experiment, Prüfverfahren, didaktische Reduktion) und welche Rolle Medien und der didaktische Raum spielen.

**Content:** Lernsysteme Mechatronik/Automatisierung · Vor- und Nachteile technischer Lernsysteme · Methoden zur Einbettung · experimentelle Methoden und Erkenntnisziele · technisches Experiment als didaktisches Mittel · Prüfverfahren · didaktische Reduktion · Medienspektrum, Veranschaulichung, Medienmerkmale · Angebots-Nutzungs-Modell · didaktischer Raum. Quelle: `inputs/quelle_T1.md`.

**Activities:** Einstiegsumfrage zu eigenen Laborerfahrungen · Zuordnung Experimentarten ↔ Erkenntnisziele · Transfer: Welche Experimentart passt zu Ihrem Laboraufbau?

### 2. Sicherheit, Gesundheit, Arbeit

**Type:** input · **Method:** gagne · **Termin:** 24.11.2026 · **Ausgabe:** `materials/02-sicherheit-gesundheit-arbeit/README.md` · **Status:** ✅ Done (Autopilot-Lauf)

**Summary:** Wandel der Arbeitswelt, Definition des Arbeitsschutzes, Akteure und Organisation (duales Arbeitsschutzsystem), Rechtsquellen von der EU-Richtlinie bis zur DGUV-Regel, betriebliche Akteure.

**Content:** Quelle: `inputs/quelle_T2.md` (alle Kapitel 1–3.5 inkl. Fallbeispiel Produktionsbetrieb).

**Activities:** Rechtsquellen-Pyramide ordnen · Fallbeispiel: Welcher betriebliche Akteur ist zuständig? · Transfer: Welche Rechtsquellen gelten für Ihren Laboraufbau?

#### Validation Report

<section>

__Date:__ 2026-02-24
__Material:__ materials/02-sicherheit-gesundheit-arbeit/README.md
__Result:__ PASS with concerns
__Mode:__ session

##### Content
- ✅ Alle Lernziele (nennen/erläutern/ordnen/anwenden) im Material adressiert
- ✅ Erforderlich-Liste Session Type `input` erfüllt: Einstieg mit Leitfrage, Lernziele, Input, Transfer auf Laboraufbau, Aktivierung (Quiz + Zuordnung + Umfrage), Zusammenfassung, Quellen, Sprechernotizen
- ✅ Gagné-Methode: Aufmerksamkeit (Vorfall-Szene), Vorwissen aktiviert, Praxis mit Feedback (Quiz + Lösung)
- ✅ Inhalt ausschließlich aus `inputs/quelle_T2.md`; keine erfundenen Paragraphen/Normen/Statistiken; PRÜFEN-Hinweis für fehlende Jahreszahlen gesetzt
- ⚠️ [pedagogical] Detaillierungen aus Quelle 3.5 (Fachkraft für Arbeitssicherheit, Betriebsarzt) nur im Quiz/Feedback verankert, nicht als eigene Folie — Kürzung begründet in `agent_report.md`
- ⚠️ [pedagogical] Video „Staplerfahrer Klaus" (Quelle, YouTube-Embed) nicht übernommen — kein Embed in Offline-Lauf; in `agent_report.md` dokumentiert
- ⚠️ Dauer: Schätzung ≈ 25–32 Min. (ca. 900 Wörter Prosa @130 WPM ≈ 7 Min. + 3 Aktivierungsblöcke ≈ 10 Min. + Präsentationspuffer) vs. 30 Min. deklariert — innerhalb 70–150 %, OK (advisory)
- ✅ 19 Folien (16 Input + 3 Aktivierung) — Richtwert 12–18 Input + 1–3 Aktivierung erfüllt

##### Type Consistency
- Session Type: `input` — Erforderlich (from `## Didactics` → `__Session Types:__`): Einstieg mit Leitfrage, Lernziele, Input, Transfer auf Laboraufbau, Aktivierung, Zusammenfassung, Quellen, Sprechernotizen
- ✅ Alle Pflichtelemente vorhanden und in korrekter Reihenfolge

##### Persona & Style
- ✅ Ton sachlich, beispielreich (Professor Persona); Sie-Form konsistent
- ✅ Terminologie „Gruppen-Input" / „Laboraufbau" aus Course Context verwendet
- ✅ Coauthor-Rolle nicht in `## Agents` definiert → Fallback auf Professor Persona + Teaching Style (Hinweis: Rolle in `## Agents` synchronisieren)

##### LiaScript Syntax
- ✅ Metadata header vollständig (author, email, version, language, narrator, mode: Presentation, classroom: enable)
- ✅ Genau ein `#`-Titel; jede Folie eine `##`; keine nackten `####`+
- ✅ Alle animierten Blöcke `{{n}}` haben passende `--{{n}}--` TTS-Kommentare; Nummerierung setzt pro Folie auf 0 zurück; jede Folie hat `--{{0}}--`
- ✅ Quiz-Syntax korrekt: Single Choice `- [( )]`/`- [(X)]`, Lückentext `[[Antwort]]`, Umfrage `- [(1)]…` — Optionen nicht eingerückt
- ✅ Alerts nur unterstützte Typen (NOTE/TIP/IMPORTANT), alle Zeilen mit `>`
- ✅ Zitate mit `>` + leere `>`-Zeile + `--`-Quellenzeile
- ✅ Alle Bilder mit Alt-Text, nur Dateinamen aus Quelle ohne Pfad; keine neuen Bilddateien
- ✅ Keine ungeschlossenen HTML-Blöcke; kein HTML außer `<section>`/Kommentaren
- ⚠️ Skill `liascript-syntax` nicht installiert — Validierung allein nach `specs/data/liascript-cheat-sheet.md`

##### Recommended Actions
1. PRÜFEN-Hinweis in Quellen-Folie vor Veröffentlichung auflösen (aktuelle Fassung ArbSchG/SGB VII/TFEU-288 prüfen)
2. Optional: Video „Staplerfahrer Klaus" bei Bedarf als `!?[...]`-Embed ergänzen (entspricht Quelle)
3. `:agent development` → `:create-project` erst nach course-mode-PASS aller vier Sessions

</section>

#### Persona Reviews

<section>

##### 🧑‍🎓 Lena

__Date:__ 2026-02-24
__Persona:__ 🧑‍🎓 Lena — Lehramt BBS Metalltechnik, 24, Industriemechanikerin, kennt Unterweisungen aus dem Betrieb, findet Rechtsthemen trocken
__Material:__ materials/02-sicherheit-gesundheit-arbeit/README.md
__Result:__ OK

###### Overall Impression
„Endlich mal klar, WAS ich im Schullabor tun muss – der Transfer mit dem Pneumatik-Beispiel hat mir direkt gezeigt, wo ich das ansetzen muss. Die Rechtsquellen-Pyramide war anfangs trocken, aber die Quiz-Fragen haben mir gezeigt, was ich wirklich mitnehmen muss."

###### Dimension Findings

**a) Verständlichkeit / Sprachniveau**
Sprache ist klar und direkt; Fachbegriffe (Vermutungswirkung, Selbstverwaltung) werden jeweils erklärt, bevor sie verwendet werden. Verdict: OK

**b) Schwierigkeitsgrad / Überforderung**
Die EU-Ebene (Richtlinie/Verordnung/Beschluss) ist der dichteste Block, aber die Schritt-Animation und die Merkhilfe „Ziel verbindlich, Mittel frei = Richtlinie" halten die Last in Grenzen. Verdict: OK

**c) Relevanz / Motivation**
Hohe Relevanz: Einstiegsszene (Werkstück im Schullabor), Pneumatik-Transfer und die Betriebspraxis-Bezüge (Unterweisungen, Sifa) sprechen direkt ihre Erfahrung an. Verdict: OK

**d) Zugänglichkeit**
Bilder mit Alt-Text, kurze Sätze, Alerts heben Kernpunkte visuell hervor; keine Barrieren identifiziert. Verdict: OK

**e) Formatpräferenz**
Guter Mix aus Folien, Bildern, Quiz und Umfrage; die Lückentext-Zuordnung (Aktivierung 2) ist genau ihr Ding – aktiv statt nur zuhören. Verdict: Good fit

**f) Vorwissen / fehlende Grundlagen**
- ⚠️ „ASiG (Arbeitssicherheitsgesetz)" – im Quiz-Feedback genannt, aber nicht vorher eingeführt → akzeptabel, da nur im Feedback-Kontext
- ✅ Unterweisungen, Betriebspraxis, PSA – aus ihrer Berufserfahrung bekannt
- ✅ ArbSchG, SGB VII – werden mit Kontext erklärt

###### Priority Issues
1. (nicht blockierend) ASiG-Kürzel im Quiz-Feedback kurz ausgeschrieben – ist bereits erledigt („Arbeitssicherheitsgesetz")
2. (nicht blockierend) Keine weiteren blockierenden Punkte

###### What Worked Well
- Transfer-Folie mit Pneumatik-Beispiel: direkt übertragbar auf ihren Laboraufbau
- Aktivierung 2 (Zuordnung) als Lückentext: schnell, aktiv, prüfbar
- Merksätze in Alerts (z. B. „Staat = Gesetze · UV-Träger = Prävention")

</section>

### 3. Sicherheit in Schulen

**Type:** input · **Method:** gagne · **Termin:** 01.12.2026 · **Ausgabe:** `materials/03-sicherheit-in-schulen/README.md`

**Summary:** Übertragung des Arbeitsschutzes auf die Schule: Schutz von Lehrkräften und Schülerinnen/Schülern, Verantwortliche, Regelwerke (RiSU, DGUV, GefStoffV), Pflichten im Labor- und Werkstattunterricht, Sicherheit als Unterrichtsinhalt.

**Content:** Quelle: `inputs/quelle_T3.md` (Stichworte; einzige zulässige Faktenbasis, PRÜFEN-Hinweise übernehmen).

**Activities:** Fallvignette Unfall im Schullabor – wer ist versichert, wer verantwortlich? · Checkliste Laborunterricht · Transfer: Sicherheitsunterweisung für den eigenen Laboraufbau skizzieren.

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

### Lauf: `:build-session 2 input` (2026-02-24)

- **Frage:** Welche Rechtsquellen gilt es für den Transfer auf den Laboraufbau zu benennen? – **Entscheidung:** Arbeitsschutzgesetz, Arbeitsstättenverordnung, Betriebssicherheitsverordnung, Technische Regeln, DIN-Normen – **Begründung:** Alle in `inputs/quelle_T2.md` (Übersicht Rechtsvorschriften, Normen/Regeln) belegt; Pneumatik-Beispiel gemäß `inputs/rahmen.md` als „Beispiel" gekennzeichnet.
- **Frage:** Jahreszahlen für APA-7-Quellen? – **Entscheidung:** „(o. J.)" verwenden + PRÜFEN-Hinweis in der Quellen-Folie – **Begründung:** `inputs/rahmen.md` verbietet erfundene Jahreszahlen; Quelle nennt keine; APA 7 verlangt ein Datumsfeld, daher „o. J." als neutrale Lösung.
- **Frage:** Video „Staplerfahrer Klaus" (YouTube-Embed in Quelle) übernehmen? – **Entscheidung:** nicht übernehmen – **Begründung:** Offline-Lauf ohne externe Embeds; in `agent_report.md` als Kürzung dokumentiert.
- **Frage:** Detailblöcke Fachkraft für Arbeitssicherheit / Betriebsarzt (Quelle 3.5, `<details>`-Kästen) als eigene Folien? – **Entscheidung:** nur im Quiz-Feedback (Fachkraft für Arbeitssicherheit) verwenden, Betriebsarzt weglassen – **Begründung:** 20-Min-Input-Limit; Kerninformation (Beratung des Arbeitgebers, Mitverantwortung für Sicherheitsniveau) bleibt erhalten; Kürzung in `agent_report.md` dokumentiert.
- **Frage:** Welche Bilder aus der Quelle verwenden? – **Entscheidung:** 10 der 14 Quelldateien (alle zu den behandelten Themen), 4 Duplikate/Überschneidungen (z. B. zweites „Bestandteile"-Bild `b6d1a6f8…`, `9482ea2c…`, `56a2d3c4…`, `4b1c73b6…`) bewusst weggelassen – **Begründung:** Folienanzahl-Richtwert 12–18; Inhalte identisch/überlappend; keine neuen Bilddateien referenziert.
- **Frage:** Umfrage als Single-Choice-Vector oder Multi-Choice? – **Entscheidung:** Single-Choice-Vector `- [(1)]…` – **Begründung:** `inputs/rahmen.md` definiert Umfragen explizit als `- [(1)] Text`; Verteilung wird im Classroom als Diagramm sichtbar.
