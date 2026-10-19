<!--
author:    Hannes Tegelbeckers
email:     hannes.tegelbeckers@ovgu.de
version:   0.1.0
language:  de
narrator:  Deutsch Female
mode:      Textbook

title:     S02 – KI-Einführung II: Werkzeuge, Grenzen, Ethik (Selbstlerneinheit)
comment:   Ingenieurpädagogisches Labor – Selbstlerneinheit zu Sitzung 2 (Selbstlerntermin 20.10.2026). HAWKI und weitere KI-Werkzeuge nach Zweck einsetzen, fachliche und sicherheitsrelevante Fehler in KI-Lernmaterial erkennen, Datenschutz und Bildrechte beachten; erstes Lernmaterial für das eigene Lernfeld mit KI erstellen und prüfen.
tags:      Ingenieurpädagogisches Labor, Künstliche Intelligenz, HAWKI, Prompting, Lernmaterial, Arbeitsschutz, Halluzination, Selbstlernen
-->

# S02 – KI-Einführung II: Werkzeuge, Grenzen, Ethik

<!-- didaktik="Selbstlerneinheit S02 · Selbstlerntermin 20.10.2026 (Dozent nicht vor Ort) · ca. 75 min + Prompting-Auftrag · baut auf KI-Einführung I (13.10.2026) auf und bereitet die Praxissitzung am 27.10.2026 vor" -->

> [!IMPORTANT] 🧭 Leitfrage
> Wie erstelle ich mit KI Lernmaterial für mein Labor – und woran erkenne ich, dass es fachlich und sicherheitstechnisch nicht stimmt?

> [!WARNING] 📅 Selbstlerntermin am 20.10.2026
> An diesem Termin gibt es keine Präsenzveranstaltung. Bearbeiten Sie diese Einheit und danach den **Prompting-Auftrag** (Abschnitt 4). Ihr Ergebnis ist der Startpunkt für die Praxissitzung am 27.10. (Materialentwicklung mit KI & LiaScript).

> [!TIP] ✍️ Übung in Moodle
> Bearbeiten Sie diese Einheit als Übung im Moodle-Kurs (dort wird Ihr Bearbeitungsstand gespeichert) bis **26.10.2026, 23:59 Uhr**: [Übung in Moodle öffnen](https://elearning.ovgu.de/mod/scorm/view.php?id=702172)

**Ablauf (ca. 75 min + Prompting-Auftrag)**

<!-- data-type="none" -->
| Schritt | Inhalt | Zeit |
| --- | --- | --- |
| 0 | Wo stehen Sie? | 5 min |
| 1 | Werkzeuge nach Zweck auswählen | 10 min |
| 2 | Grenzen erkennen: ein KI-Arbeitsblatt prüfen | 25 min |
| 3 | Ethik und Recht | 15 min |
| 4 | Prompting-Auftrag: erstes Lernmaterial | 15 min Planung + Bearbeitung |
| 5 | Abschluss | 5 min |

**Lernziele – nach dieser Einheit können Sie …**

1. für eine Aufgabe der Materialentwicklung ein passendes KI-Werkzeug **auswählen**,
2. einen strukturierten Prompt (Rolle · Kontext · Aufgabe · Vorgaben · Ausgabeformat) **formulieren** und iterativ **überarbeiten**,
3. fachliche und sicherheitsrelevante Fehler in KI-generiertem Lernmaterial **erkennen** und mit Primärquellen **korrigieren**,
4. Datenschutz, Urheber- und Bildrechte bei der Nutzung von KI **beachten**,
5. Ihre KI-Nutzung nachvollziehbar **dokumentieren**.

## 0 · Wo stehen Sie?

**Wie sicher fühlen Sie sich?** (1 = gar nicht, 4 = sehr sicher)

Ich kann mit KI ein brauchbares Arbeitsblatt für mein Lernfeld erstellen.

- [(1)] 1
- [(2)] 2
- [(3)] 3
- [(4)] 4

**Kurz erinnert (KI-Einführung I):** Sie laden in HAWKI das Datenblatt Ihres Laboraufbaus hoch. Wo befindet sich der Text jetzt für das Modell?

- [( )] In den Trainingsdaten
- [(X)] Im Kontextfenster
- [( )] In den Parametern des Modells
***
Hochgeladenes Material verändert das Modell nicht – es steht nur im **Kontextfenster** dieses Chats. Deshalb lohnt es sich, Datenblätter und Vorgaben mitzugeben: Das Modell muss dann weniger „raten“.
***

## 1 · Werkzeuge nach Zweck auswählen

<!-- didaktik="ca. 10 min" -->

| Zweck | Werkzeug | Worauf Sie achten |
| --- | --- | --- |
| Lernsituation, Arbeitsblatt, Quiz, LiaScript-Material entwerfen | **HAWKI** (OVGU-Zugang, für alle) | Vorlage und Kontext mitgeben; Ausgabe ist ein Entwurf |
| Aktuelles recherchieren | Such-Assistent mit Quellen (z. B. Perplexity) | Quellen öffnen und lesen |
| Fachliteratur finden | Literatur-Assistent (z. B. Consensus) | jeden Titel im Katalog prüfen |
| Bilder, Skizzen erzeugen oder beschreiben | multimodale Modelle | Technische Darstellungen sind oft fehlerhaft (Symbole, Beschriftungen) |
| Vorschriften, Normen, Herstellerangaben | **keine KI** – Primärquelle | Gesetz, DGUV, RiSU, Datenblatt des Herstellers |

<small>Werkzeuge nach der Kurswebseite des Ingenieurpädagogischen Labors.</small>

**Ein strukturierter Prompt hat fünf Bausteine.** Ordnen Sie zu:

[[Rolle] [Kontext] [Aufgabe] [Vorgaben] [Ausgabeformat]]
[  (X)      ( )       ( )        ( )           ( )       ] „Du bist Fachlehrkraft für Elektrotechnik an einer berufsbildenden Schule.“
[  ( )      (X)       ( )        ( )           ( )       ] „Lernfeld 3, 1. Ausbildungsjahr, 16 Auszubildende, Laboraufbau: Elektropneumatik-Lernsystem, 6 bar.“
[  ( )      ( )       (X)        ( )           ( )       ] „Erstelle ein Arbeitsblatt zur Inbetriebnahme einer Zylindersteuerung.“
[  ( )      ( )       ( )        (X)           ( )       ] „Erfinde keine Normen. Markiere unsichere Angaben mit [PRÜFEN].“
[  ( )      ( )       ( )        ( )           (X)       ] „Gib das Ergebnis als LiaScript-Markdown nach der beigefügten Vorlage aus.“
***
Das ist der Aufbau aus der [Beispiel-Prompt-Dokumentation](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/IngP-d_Labor_WiSe_2026_2027/main/00_Organisation/KI/Beispiel_Prompt_Dokumentation.md). Besonders wichtig für das Labor: die **Vorgaben** – sie verbieten Erfundenes und erzwingen Markierungen, die Sie danach prüfen.
***

## 2 · Grenzen erkennen: ein KI-Arbeitsblatt prüfen

<!-- didaktik="ca. 25 min · Kernübung der Einheit" -->

| Grenze | Im Labor typisch |
| --- | --- |
| **Halluzination** | plausible, aber falsche technische Werte und Abläufe |
| **Erfundene Quellen** | Normen, DGUV-Regeln oder Paragrafen, die es nicht gibt oder die etwas anderes regeln |
| **Veraltetes Wissen** | zurückgezogene Normen, alte Fassungen von Vorschriften |
| **Bias** | einseitige Beispiele, stereotype Darstellung von Lernenden und Berufen |
| **Fehlender Kontext** | das Modell kennt Ihren Laboraufbau und Ihre Lerngruppe nicht |

### Übung 2a: Fehler finden

Ein Modell hat auf Anfrage diesen Ausschnitt eines Arbeitsblatts zum Elektropneumatik-Lernsystem erstellt:

> *„**Sicherheitshinweise:** 1. Die Steuerung arbeitet mit 24 V Gleichspannung. Deshalb sind bei diesem Versuch keine weiteren Schutzmaßnahmen nötig. 2. Bevor Sie Schläuche umstecken, bringen Sie das Ventil in Grundstellung – dann ist die Anlage sicher. 3. Beachten Sie die DIN 4711-P „Pneumatik im Unterricht“. 4. Stellen Sie den Betriebsdruck auf 6 bar ein.“*

Welche Hinweise sind falsch oder nicht belegt?

- [[X]] Hinweis 1
- [[X]] Hinweis 2
- [[X]] Hinweis 3
- [[ ]] Hinweis 4
***
- **Hinweis 1:** Kleinspannung senkt die elektrische Gefährdung, aber nicht die **mechanische**: Bewegte Zylinder können quetschen, lose Schläuche können umherschlagen. Die Gefährdungen ergeben sich aus dem ganzen Aufbau, nicht nur aus der Spannung.
- **Hinweis 2:** Grundstellung des Ventils heißt nicht drucklos. Vor dem Umstecken wird die **Druckluft abgesperrt und das System entlüftet**.
- **Hinweis 3:** Diese Norm gibt es nicht – ein typisches **erfundenes Zitat**. Maßgeblich sind z. B. die Betriebsanleitung des Herstellers, die DGUV-Regelwerke und die *Richtlinie zur Sicherheit im Unterricht* (RiSU) der KMK.
- **Hinweis 4:** plausibel und passend zu Ihrem Kontext (6 bar) – aber auch hier gilt: Maßgeblich ist die **Herstellerangabe** für Ihr Lernsystem.
***

> [!WARNING] ⚠️ Regel für das IngPäd-Labor
> KI-generierte Inhalte zu **Arbeitsschutz und Gefährdungen** gleichen Sie **immer** mit Primärquellen ab (Gesetz, DGUV, RiSU, Herstellerangaben). Ein falscher Sicherheitshinweis auf einem Arbeitsblatt ist kein Schönheitsfehler.

### Übung 2b: Wie hätte der Prompt den Fehler verhindert?

Welche Vorgaben im Prompt hätten geholfen? (mehrere richtig)

- [[X]] „Nenne nur Normen und Vorschriften, die im beigefügten Material stehen. Erfinde keine.“
- [[X]] „Markiere jeden Sicherheitshinweis mit [PRÜFEN].“
- [[ ]] „Antworte besonders überzeugend.“
- [[X]] „Hier ist die Betriebsanleitung des Lernsystems: …“
***
Vorgaben und Kontext verringern Fehler, verhindern sie aber nicht. Die Prüfung bleibt Ihre Aufgabe – die Markierung [PRÜFEN] zeigt Ihnen, wo Sie anfangen.
***

## 3 · Ethik und Recht

<!-- didaktik="ca. 15 min" -->

| Thema | Regel für das IngPäd-Labor |
| --- | --- |
| **Sicherheit** | Sicherheitsrelevante Inhalte immer selbst prüfen – Sie verantworten das Material. |
| **Datenschutz** | Keine personenbezogenen Daten von Lernenden oder Kolleg:innen, keine Betriebsinterna. Werkzeug für alle: HAWKI mit OVGU-Account. |
| **Urheber- und Bildrechte** | Keine fremden Abbildungen, Datenblätter oder Lehrbuchseiten ohne Prüfung der Nutzungsrechte hochladen oder übernehmen. Bildquellen und Lizenzen angeben. |
| **Transparenz** | KI-Nutzung im Studiennachweis kennzeichnen (Werkzeug, Zweck, Prompt; APA 7) und die ersten drei Prompts mit Iterationen und Originalausgaben im Anhang dokumentieren. |

**Ist das in Ordnung?**

[[ok] [nicht ok]]
[ (X)    ( )    ] das öffentlich zugängliche Datenblatt eines Ventils als Kontext hochladen
[ ( )    (X)    ] eine Notenliste der Lerngruppe hochladen, damit die KI Aufgaben differenziert
[ ( )    (X)    ] ein Lehrbuchbild abfotografieren und im eigenen Arbeitsblatt ohne Quelle verwenden
[ (X)    ( )    ] die Lerngruppe allgemein beschreiben („16 Auszubildende, heterogene Vorkenntnisse“)
***
Allgemeine Beschreibungen und öffentliche Dokumente sind unproblematisch. Daten über einzelne Personen und fremde Abbildungen ohne geklärte Rechte gehören nicht in Ihr Material.
***

## 4 · Prompting-Auftrag: erstes Lernmaterial

<!-- didaktik="Planung ca. 15 min, Bearbeitung bis 26.10.2026" -->

> [!IMPORTANT] 📝 Auftrag
> Erstellen Sie mit HAWKI ein **erstes Lernmaterial** (z. B. Arbeitsblatt oder Quiz) für ein Lernfeld Ihrer Fachrichtung und prüfen Sie es kritisch.

1. **Prompt:** strukturiert mit Rolle · Kontext · Aufgabe · Vorgaben · Ausgabeformat. Beruf und Lernfeld dürfen vorläufig sein (festgelegt wird am 10.11.).
2. **Originalausgabe:** unverändert speichern – auch wenn sie Fehler enthält.
3. **Iteration:** mindestens eine Überarbeitung mit konkreter, überprüfbarer Rückmeldung im selben Chat.
4. **Prüfung:** Tabelle mit mindestens fünf geprüften Stellen:

<!-- data-type="none" -->
| Stelle im Material | Primärquelle | Ergebnis | Änderung |
| --- | --- | --- | --- |
| Sicherheitshinweis 2 | Betriebsanleitung Lernsystem | ❌ falsch | „Druckluft absperren und entlüften“ |
| … | … | ✅ / ⚠️ / ❌ | … |

5. **Kennzeichnung:** Werkzeug, Modell, Datum (APA 7).

Orientieren Sie sich an der [Beispiel-Prompt-Dokumentation](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/IngP-d_Labor_WiSe_2026_2027/main/00_Organisation/KI/Beispiel_Prompt_Dokumentation.md).

> [!TIP] ✍️ Ergebnisse direkt hier eintragen
> Tragen Sie Ihre Ergebnisse in die Felder unten ein und schicken Sie jedes Feld ab. In Moodle wird Ihr Bearbeitungsstand gespeichert. Die Übung gilt als erledigt, wenn Sie diese Einheit in Moodle bis **26.10.2026, 23:59 Uhr** vollständig bearbeitet haben – eine Datei-Abgabe ist nicht nötig. Bewahren Sie Prompt und Material trotzdem auf: Sie arbeiten am 27.10. damit weiter.

**1 · Ihr Prompt** (Rolle · Kontext · Aufgabe · Vorgaben · Ausgabeformat):

[[___ ___ ___ ___]]

**2 · Originalausgabe** (Auszug, unverändert):

[[___ ___ ___ ___ ___]]

**3 · Iteration:** Welche Rückmeldung haben Sie gegeben – und was hat sich verbessert?

[[___ ___ ___]]

**4 · Prüftabelle** – mindestens fünf Stellen, je Zeile: *Stelle im Material – Primärquelle – Ergebnis (✅/⚠️/❌) – Änderung*

[[___ ___ ___ ___ ___ ___]]

**5 · Kennzeichnung** (Werkzeug, Modell, Datum nach APA 7):

[[___ ___]]

## 5 · Abschluss

**Noch einmal: Wie sicher fühlen Sie sich jetzt?**

Ich kann mit KI ein brauchbares Arbeitsblatt für mein Lernfeld erstellen.

- [(1)] 1
- [(2)] 2
- [(3)] 3
- [(4)] 4

**Was nehmen Sie mit in die Praxissitzung am 27.10.?** Welche Frage zu KI und LiaScript möchten Sie dort klären?

[[___ ___]]

## Quellen

- Kultusministerkonferenz. (2019). *Richtlinie zur Sicherheit im Unterricht (RiSU)* (Empfehlung der KMK vom 09.09.1994 i. d. F. vom 14.06.2019). KMK.
- Lo, L. S. (2023). The CLEAR path: A framework for enhancing information literacy through prompt engineering. *The Journal of Academic Librarianship, 49*(4), 102720. https://doi.org/10.1016/j.acalib.2023.102720
- McAdoo, T. (2023, 7. April). *How to cite ChatGPT*. APA Style. https://apastyle.apa.org/blog/how-to-cite-chatgpt
- UNESCO. (2023). *Guidance for generative AI in education and research*. UNESCO. https://doi.org/10.54675/EWZM9535
- Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports, 13*, 14045. https://doi.org/10.1038/s41598-023-41032-5
