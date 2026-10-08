# Vorgaben für die Gruppen-Inputs (IngPäd-Labor WiSe 2026/27)

Diese Vorgaben sind für alle vier Präsentationen verbindlich.

## Zweck
Jede Präsentation ist eine **Orientierungs- bzw. Musterpräsentation** für den Gruppen-Input im Seminar
„Fachdidaktik II – Ingenieurpädagogisches Labor“ (OVGU, Dienstag 09:00–11:00 Uhr).
Die Studierenden-Gruppen halten den Input selbst. Die Musterpräsentation zeigt ihnen Inhalt, Umfang und
LiaScript-Umsetzung, an der sie sich orientieren können.

| Nr. | Thema                              | Termin     | Quelle (Vorjahr)        |
| --- | ---------------------------------- | ---------- | ----------------------- |
| 1   | Lehren und Lernen im Labor         | 03.11.2026 | `inputs/quelle_T1.md`   |
| 2   | Sicherheit, Gesundheit, Arbeit     | 24.11.2026 | `inputs/quelle_T2.md`   |
| 3   | Sicherheit in Schulen              | 01.12.2026 | `inputs/quelle_T3.md` (nur Stichworte) |
| 4   | Gefährdung und Schutzziele         | 08.12.2026 | `inputs/quelle_T4.md`   |

## Zielgruppe
- Studierende Lehramt an berufsbildenden Schulen (gewerblich-technische Fachrichtungen: Metall-, Elektro-,
  Bau-, Informations-, Prozesstechnik), ca. 10–20 Personen, fachlich vorgebildet, didaktisch am Anfang.
- Ihr Studiennachweis: zu einem Ausbildungsberuf und Lernfeld einen **domänenspezifischen Laboraufbau**
  didaktisch einbinden, eine **Lernsituation** beschreiben, **Arbeits- und Gesundheitsschutz** samt rechtlicher
  Grundlagen benennen und ein **Ausbildungs-/Unterrichtsverfahren** begründet auswählen.
  Jede Präsentation soll zeigen, was das Thema für den eigenen Laboraufbau bedeutet.

## Zeitrahmen (aus dem Organisationsüberblick)
- **20 Minuten Input + 10 Minuten Aktivierung** (Übung oder Quiz für das Plenum).
- Richtwert: 12–18 Folien Input, dazu 1–3 Aktivierungsfolien.

## Aufbau jeder Präsentation
1. Titelfolie: Thema, Gruppe (Platzhalter „Gruppe N“), Termin.
2. Einstieg: Leitfrage oder Problem aus dem Laboralltag (z. B. ein Unfall oder eine Fehlbedienung im Schullabor).
3. Lernziele (3–4, mit Operatoren wie *nennen, erläutern, beurteilen, anwenden*).
4. Input-Teil: die Inhalte der Quelle, gegliedert, auf das Wesentliche reduziert.
5. **Transfer: „Was heißt das für Ihren Laboraufbau?“** mit einem durchgehenden Beispiel
   (z. B. Pneumatik-/Elektropneumatik-Lernsystem im Lernfeld einer Mechatroniker-Ausbildung).
6. Aktivierung (10 min): mindestens ein Quiz und eine Zuordnungs- oder Umfrageaufgabe.
7. Zusammenfassung (3–5 Kernaussagen).
8. Quellen (APA 7).

## Inhaltliche Pflichten
1. **Grundlage ist die Vorjahresquelle.** Alle Kernaussagen, Definitionen, Tabellen und Beispiele der Quelle
   bleiben inhaltlich erhalten. Kürzen ist erlaubt, Weglassen ganzer Abschnitte nur mit Notiz im `agent_report.md`.
2. **Nichts erfinden.** Keine neuen Quellen, Paragraphen, Normnummern, Statistiken oder Jahreszahlen,
   die nicht in der Quelle oder in `quelle_T3.md` stehen. Wo du eine Aktualisierung für nötig hältst
   (z. B. geänderte Rechtslage), schreibe einen Hinweis `<!-- PRÜFEN: … -->` statt einer erfundenen Angabe.
3. Ergänzungen ohne Quellenbeleg (Beispiele, Übungen) als „Beispiel“ oder „Übung“ kennzeichnen.
4. Fehler und Tippfehler der Vorjahresquelle korrigieren (z. B. „Arbeitsschutzssystem“, „Gesetzgebungesverfahren“).
   Die Quelle T1 enthält englische Folientitel („Slide 1: Introduction“) – alles auf Deutsch.
5. **Bilder:** Nur die Bilddateien verwenden, die in der Quelle verlinkt sind, mit genau demselben Dateinamen
   (sie liegen im Ausgabeordner neben der Präsentation, also Verweis `![Beschreibung](dateiname.png)` ohne Pfad).
   Keine neuen Bilddateien referenzieren. Für fehlende Abbildungen ein ASCII-Diagramm oder eine Tabelle.

## LiaScript-Format
- Eine Datei `README.md`, Kopf genau so (nur `title`/`comment` anpassen):

```
<!--
author:    Hannes Tegelbeckers
email:     hannes.tegelbeckers@ovgu.de
version:   0.1.0
language:  de
narrator:  Deutsch Female
mode:      Presentation
classroom: enable

title:     <Thema> – Gruppen-Input IngPäd-Labor
comment:   Orientierungsbeispiel für den Gruppen-Input im Ingenieurpädagogischen Labor, WiSe 2026/27.
-->
```

- Jede Folie ist eine `##`-Überschrift (`#` nur für den Titel und höchstens 4 Kapiteltrenner).
- Schrittweise Animation mit `{{1}}`, `{{2}}` … vor Absätzen oder `<section>`-Blöcken.
- **Sprechernotizen** zu jeder Folie: `                --{{0}}--` gefolgt von 1–3 Sätzen, die beim Vortrag gesagt werden.
- Quiz: Single Choice `- [( )]` / `- [(X)]`, Multiple Choice `- [[ ]]` / `- [[X]]`, Lückentext `[[Antwort]]`.
  Optionen **nicht einrücken**. Umfragen ohne richtige Antwort: `- [(1)] Text`.
- Tabellen in Markdown; Formeln mit `$…$`; Diagramme als ASCII-Art im Codeblock mit Sprachangabe `ascii`.
- Kein HTML außer `<section>`, `<small>`, `<!-- … -->`. Keine externen Templates oder Makros.
- Sprache: Deutsch.
