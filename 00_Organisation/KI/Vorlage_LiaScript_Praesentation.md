<!--
author:    Vorname Nachname; Vorname Nachname
email:     vorname.nachname@st.ovgu.de
version:   0.1.0
language:  de
narrator:  Deutsch Female
mode:      Presentation
classroom: enable

title:     «Titel der Präsentation»
comment:   «Ein Satz: Worum geht es, für welchen Ausbildungsberuf und welchen Laboraufbau?»
-->

<!--
================================================================================
ANLEITUNG FÜR DAS KI-MODELL (z. B. in HAWKI) – dieser Block bleibt im Ergebnis stehen
================================================================================
Du füllst diese Vorlage zu einer LiaScript-Präsentation aus. Regeln:
1. Struktur, Überschriften-Ebenen und Reihenfolge der Folien beibehalten. Folien dürfen
   ergänzt werden (je eine `##`-Überschrift), aber keine Pflichtfolie entfällt.
2. Alles in «Winkelklammern» ersetzen. Kommentare `<!-- KI: … -->` nach dem Ausfüllen löschen.
3. Jede Folie bekommt eine Sprechernotiz: Zeile `                --{{0}}--`, darunter 1–3 Sätze.
4. Text NIE mit 4 oder mehr Leerzeichen einrücken (sonst erscheint er als Codeblock).
   Quiz- und Umfrageoptionen beginnen am Zeilenanfang mit `- [( )]`, `- [(X)]`, `- [[ ]]`, `- [[X]]`.
5. `{{1}}`, `{{2}}` … steht in einer eigenen Zeile direkt vor dem Block, der nacheinander erscheinen soll.
   Soll mehr als ein Absatz zusammen erscheinen: in `<section>` … `</section>` einschließen.
6. Nichts erfinden: keine Paragraphen, Normnummern, Statistiken, Literatur oder Lernfeldnummern,
   die nicht im mitgelieferten Material stehen. Unsichere Angaben mit `<!-- PRÜFEN: … -->` markieren.
7. Bilder nur mit Dateinamen, die im Material genannt sind, und immer mit Quelle/Lizenz im Titel.
8. Sprache: Deutsch, Fachbegriffe korrekt, Sie-Form gegenüber dem Plenum.
================================================================================
-->

# «Titel der Präsentation»

**«Gruppe N»** · «Datum» · Ingenieurpädagogisches Labor, OVGU

                --{{0}}--
«Begrüßung in einem Satz und worum es heute geht.»

## Einstieg: «kurzer Titel»

<!-- KI: Problem oder Situation aus dem Laboralltag, die neugierig macht (Fall, Foto, Frage). -->

> «Situation in 2–3 Sätzen»

                --{{0}}--
«Situation erzählen, Frage an das Plenum stellen.»

{{1}}
**Leitfrage:** «Eine Frage, die am Ende der Präsentation beantwortet wird.»

## Lernziele

Nach dieser Präsentation können Sie …

                --{{0}}--
«Lernziele kurz vorlesen und an den Studiennachweis anbinden.»

{{1}}
1. «Inhalt» **nennen**,
2. «Inhalt» **erläutern**,
3. «Inhalt» **beurteilen**,
4. «Inhalt» auf den eigenen Laboraufbau **anwenden**.

## Ausbildungsberuf und Lernfeld

                --{{0}}--
«Beruf, Lernfeld und warum der Laboraufbau dazu passt.»

| Merkmal | Angabe |
| --- | --- |
| Ausbildungsberuf | «staatlich anerkannter Ausbildungsberuf» |
| Lernfeld | «Nummer und Titel laut Rahmenlehrplan» <!-- PRÜFEN: Rahmenlehrplan --> |
| Ausbildungsjahr | «Jahr» |
| Zeitrichtwert | «Stunden laut Rahmenlehrplan» |

## Der Laboraufbau

<!-- KI: Aufbau beschreiben: Komponenten, was Lernende daran tun, welche Kompetenz entsteht. -->

![«Beschreibung des Aufbaus»](«dateiname.png» "Foto: «Urheber», «Lizenz»")

                --{{0}}--
«Aufbau in 2 Sätzen erklären.»

{{1}}
<section>

**Komponenten:** «Liste»

**Was die Lernenden tun:** «Handlung, z. B. aufbauen, messen, Fehler suchen»

</section>

## Lernsituation

                --{{0}}--
«Lernsituation als Kundenauftrag oder betriebliches Problem vorstellen.»

> **Auftrag:** «Lernsituation in 3–5 Sätzen aus Sicht eines Betriebs/Kunden»

{{1}}
| Phase | Handlung der Lernenden | Handlungsprodukt |
| --- | --- | --- |
| Informieren | «…» | «…» |
| Planen | «…» | «…» |
| Entscheiden | «…» | «…» |
| Ausführen | «…» am Laboraufbau | «…» |
| Kontrollieren | «…» | «…» |
| Bewerten | «…» | «…» |

## Sicherheit: Gefährdungen und Maßnahmen

<!-- KI: Gefährdungen nach Gefährdungsgruppen, Maßnahmen nach STOP-Prinzip (Substitution, Technisch,
Organisatorisch, Personenbezogen). Rechtsgrundlagen nur nennen, wenn im Material belegt. -->

                --{{0}}--
«Wichtigste Gefährdung des Aufbaus und die wirksamste Maßnahme nennen.»

{{1}}
| Gefährdung (Gruppe) | Risiko | Maßnahme | STOP |
| --- | --- | --- | --- |
| «z. B. umherschlagender Druckluftschlauch (mechanisch)» | «hoch/mittel/gering» | «…» | «T» |
| «…» | «…» | «…» | «…» |

{{2}}
**Rechtliche Grundlagen:** «nur belegte Angaben» <!-- PRÜFEN: aktuelle Fassung -->

## Ausbildungs- bzw. Unterrichtsverfahren

                --{{0}}--
«Gewähltes Verfahren nennen und begründen.»

{{1}}
**Verfahren:** «z. B. technisches Experiment, Leittextmethode, Projekt»

{{2}}
**Begründung:** «Warum passt es zu Lernziel, Laboraufbau und Lerngruppe? 2–3 Punkte»

## Ablauf (Grobplanung)

                --{{0}}--
«Ablauf der Unterrichtseinheit kurz erklären.»

``` ascii
 Einstieg ──► Information ──► Laborarbeit ──► Auswertung ──► Reflexion
  «5 min»      «15 min»        «45 min»       «15 min»       «10 min»
```

## Aktivierung: Quiz

                --{{0}}--
«Quiz ankündigen.»

**«Frage 1 – eine richtige Antwort»**

- [( )] «falsch»
- [(X)] «richtig»
- [( )] «falsch»
[[?]] «Hinweis, falls die Antwort falsch war»

**«Frage 2 – mehrere richtige Antworten»**

- [[X]] «richtig»
- [[ ]] «falsch»
- [[X]] «richtig»

**«Frage 3 – Lückentext»** «Satz mit Lücke:» [[«Lösungswort»]]

## Aktivierung: Umfrage

                --{{0}}--
«Umfrage ankündigen, Ergebnis im Plenum besprechen.»

**«Umfragefrage ohne richtige Antwort»**

- [(1)] «Option»
- [(2)] «Option»
- [(3)] «Option»

**«Offene Frage an das Plenum»**

[[___ ___ ___]]

## Zusammenfassung

                --{{0}}--
«Kernaussagen vorlesen, Leitfrage beantworten.»

{{1}}
1. «Kernaussage»
2. «Kernaussage»
3. «Kernaussage»

**Antwort auf die Leitfrage:** «ein Satz»

## Quellen

                --{{0}}--
Hier finden Sie alle Quellen und Bildnachweise.

- «Autor:in» («Jahr»). *«Titel»*. «Verlag/URL»  <!-- APA 7 -->
- «Ausbildungsordnung / Rahmenlehrplan mit Jahr»
- Bildnachweise: «Datei – Urheber – Lizenz»

## KI-Nutzung

                --{{0}}--
Für diese Präsentation haben wir KI-Werkzeuge so genutzt, wie in der Tabelle angegeben.

| Werkzeug (Modell) | Zweck | Prompt (Kurzform, vollständig im Anhang) | Was wir geprüft/geändert haben |
| --- | --- | --- | --- |
| HAWKI («Modellname») | «z. B. Entwurf Lernsituation» | «…» | «z. B. Lernfeld im Rahmenlehrplan geprüft, Zeitangaben angepasst» |
| «…» | «…» | «…» | «…» |

<small>Zitierbeispiel (APA 7): «Anbieter» («Jahr»). *«Modellname»* [Large language model]. Zugriff über HAWKI, OVGU, am «Datum».</small>
