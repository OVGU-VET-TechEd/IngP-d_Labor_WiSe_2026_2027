<!--
author:    Hannes Tegelbeckers
email:     hannes.tegelbeckers@ovgu.de
version:   0.1.0
language:  de
narrator:  Deutsch Female
mode:      Textbook

title:     S03 – Pädagogische Materialentwicklung mit KI & LiaScript (Praxis)
comment:   Ingenieurpädagogisches Labor – Praxissitzung 3 (27.10.2026). Lernmaterial didaktisch begründet mit KI erzeugen, mit einem Prüfraster qualitätssichern, Ausgaben verschiedener Sprachmodelle kriteriengeleitet vergleichen und das Ergebnis als LiaScript-Material umsetzen.
tags:      Ingenieurpädagogisches Labor, Künstliche Intelligenz, HAWKI, LiaScript, Lernmaterial, Constructive Alignment, Qualitätssicherung, Modellvergleich
-->

# S03 – Pädagogische Materialentwicklung mit KI & LiaScript

<!-- didaktik="Praxissitzung S03 · Live 27.10.2026, 09:00–11:00 · 90 min · baut auf KI-Einführung I (13.10.) und II (20.10., Prompting-Auftrag) auf · Ergebnis fließt in die Ideenpräsentation am 03.11. und in den Studiennachweis" -->

> [!IMPORTANT] 🧭 Leitfrage
> Wie wird aus einer KI-Ausgabe **gutes** Lernmaterial – didaktisch begründet, fachlich geprüft – und welche Rolle spielt dabei die Wahl des Sprachmodells?

> [!TIP] 🧰 Mitbringen
> Ihren **Prompt und Ihr Lernmaterial aus dem Prompting-Auftrag (S02)**, Zugang zu **HAWKI** (OVGU-Account) und die [Vorlage LiaScript-Präsentation](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/IngP-d_Labor_WiSe_2026_2027/main/00_Organisation/KI/Vorlage_LiaScript_Praesentation.md).

**Ablauf (90 min)**

<!-- data-type="none" -->
| Schritt | Inhalt | Zeit |
| --- | --- | --- |
| 0 | Anknüpfen: Was hat Ihr Prompting-Auftrag gezeigt? | 5 min |
| 1 | Didaktik zuerst: vom Lernziel zum Prompt | 15 min |
| 2 | Material generieren: Prompt-Muster und Prompt-Ketten | 15 min |
| 3 | Qualität sichern: das Prüfraster | 15 min |
| 4 | Modelle vergleichen: dieselbe Aufgabe, verschiedene LLMs | 20 min |
| 5 | Praxis: Ihr Material, Version 2 | 15 min |
| 6 | Abschluss und Ausblick | 5 min |

**Lernziele – nach dieser Sitzung können Sie …**

1. Lernmaterial aus einem **Lernziel** heraus planen und didaktische Entscheidungen als **Vorgaben im Prompt** formulieren,
2. Prompt-Muster für typische Materialarten (Lernsituation, Arbeitsblatt, Quiz, gestufte Hilfen) **anwenden** und Prompts **verketten**,
3. KI-generiertes Material mit einem **Prüfraster** fachlich, sicherheitsbezogen, didaktisch, sprachlich, rechtlich und technisch **beurteilen**,
4. Ausgaben verschiedener Sprachmodelle **kriteriengeleitet vergleichen** und eine begründete Modellwahl treffen,
5. geprüftes Material in **LiaScript** umsetzen.

## 0 · Anknüpfen

<!-- didaktik="ca. 5 min · Blitzlicht zum Prompting-Auftrag aus S02" -->

**Ihr Prompting-Auftrag aus S02:** Was war das größte Problem in Ihrer Originalausgabe? (mehrere möglich)

- [[ ]] fachliche Fehler oder erfundene Normen/Quellen
- [[ ]] Sicherheitshinweise unvollständig oder falsch
- [[ ]] Niveau passte nicht zur Lerngruppe
- [[ ]] Aufgaben passten nicht zum Lernziel
- [[ ]] Format/Struktur unbrauchbar
- [[ ]] kaum Probleme
***
Fast alle Probleme in dieser Liste lassen sich auf zwei Ursachen zurückführen: **Dem Modell fehlte Kontext** (es kennt Ihren Aufbau, Ihre Lerngruppe und Ihr Lernziel nicht) oder **es fehlten Vorgaben** (es wusste nicht, woran gutes Material gemessen wird). Beides ist heute das Thema.
***

**Kurz erinnert:** In der [Beispiel-Prompt-Dokumentation](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/IngP-d_Labor_WiSe_2026_2027/main/00_Organisation/KI/Beispiel_Prompt_Dokumentation.md) sollte das Modell die Zeiten auf genau 180 Minuten summieren. Unter die Tabelle schrieb es „Summe der Zeiten: 180 Minuten“. Was ergab das Nachrechnen?

- [( )] 180 Minuten – die Vorgabe wurde eingehalten.
- [(X)] 160 Minuten – die Angabe des Modells stimmte nicht mit der eigenen Tabelle überein.
- [( )] Das Modell hat keine Summe angegeben.
***
Das Modell **behauptet**, die Vorgabe erfüllt zu haben – die Tabelle ergibt aber 160 Minuten. Merksatz für heute: **Die Selbstauskunft eines Modells ist keine Prüfung.** Alles Überprüfbare prüfen Sie selbst (oder per Skript).
***

## 1 · Didaktik zuerst: vom Lernziel zum Prompt

<!-- didaktik="ca. 15 min · Kernidee: Die didaktischen Entscheidungen trifft die Lehrkraft, nicht das Modell" -->

Ein Sprachmodell erzeugt das **wahrscheinlichste** Material zu Ihrer Anfrage – also durchschnittliches Material. Didaktische Qualität entsteht, wenn **Sie** vorher entscheiden, *was* gelernt werden soll und *woran* man es erkennt, und das Modell diese Entscheidungen umsetzen lassen.

```ascii
  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
  │ 1 Entscheiden│──►│ 2 Prompten   │──►│ 3 Generieren │──►│ 4 Prüfen     │──►│ 5 Umsetzen   │
  │ Lernziel,    │   │ Leitplanken  │   │ ein oder     │   │ Prüfraster,  │   │ LiaScript,   │
  │ Lerngruppe,  │   │ als Vorgaben │   │ mehrere      │   │ Primärquellen│   │ Kennzeichnung│
  │ Aufbau       │   │              │   │ Modelle      │   │              │   │              │
  └──────────────┘   └──────────────┘   └──────────────┘   └──────┬───────┘   └──────────────┘
         ▲                  ▲                                     │
         │                  └──────────── Iteration ◄─────────────┤
         └──────────────────── Lernziel unklar? ◄─────────────────┘
       Sie entscheiden                 KI unterstützt                Sie verantworten
```

### Constructive Alignment

Lernziel, Lernaktivität und Lernerfolgskontrolle müssen zueinander passen (Biggs, 1996). Für KI-Material heißt das: **Das Lernziel gehört in den Prompt** – mit seinem Operator.

<!-- data-type="none" -->
| Anforderungsbereich | Typische Operatoren | Aufgabe im Labor (Beispiel Elektropneumatik) |
| --- | --- | --- |
| **I** – Wiedergeben | nennen, beschreiben, benennen | Benennen Sie die Anschlüsse des 5/2-Wegeventils. |
| **II** – Anwenden, Zusammenhänge herstellen | erklären, vergleichen, anwenden, berechnen | Erklären Sie, warum der Zylinder nach dem Abschalten der Spule nicht zurückfährt. |
| **III** – Beurteilen, Probleme lösen | beurteilen, bewerten, entwickeln, gestalten | Beurteilen Sie, ob der Aufbau für eine Not-Halt-Funktion ausreicht, und entwickeln Sie eine Verbesserung. |

<small>Anforderungsbereiche in Anlehnung an die überarbeitete Lernzieltaxonomie (Anderson & Krathwohl, 2001); Operatorenlisten unterscheiden sich je nach Land und Schulform.</small>

**Ordnen Sie die Operatoren zu:**

[[I] [II] [III]]
[ (X)  ( )  ( ) ] nennen
[ ( )  (X)  ( ) ] erklären
[ ( )  ( )  (X) ] beurteilen
[ ( )  (X)  ( ) ] vergleichen
[ (X)  ( )  ( ) ] beschreiben
[ ( )  ( )  (X) ] entwickeln
***
Wichtig für KI-Material: Modelle **verschieben das Niveau gern nach unten**. Ein Lernziel mit „erklären“ wird oft mit Aufgaben „Nennen Sie …“ beantwortet, weil Wiedergabeaufgaben in Trainingsdaten häufiger sind. Deshalb steht im Prompt nicht nur das Thema, sondern das **Lernziel mit Operator** – und die Prüfung kontrolliert, ob die Aufgaben dazu passen.
***

### Didaktische Leitplanken im Prompt

Jede didaktische Entscheidung wird zu einer **Vorgabe im Prompt** – und zu einer **Prüffrage** danach.

| Didaktisches Prinzip | Vorgabe im Prompt | Prüffrage an die Ausgabe |
| --- | --- | --- |
| **Constructive Alignment** | „Lernziel: Die Auszubildenden *erklären* … Jede Aufgabe prüft dieses Lernziel.“ | Passt jeder Operator zum Lernziel? |
| **Handlungsorientierung / vollständige Handlung** | „Phasen: Informieren, Planen, Entscheiden, Ausführen, Kontrollieren, Bewerten – je ein Handlungsprodukt.“ | Gibt es für jede Phase ein überprüfbares Produkt? |
| **Lernfeldbezug** | „Ausgangspunkt ist ein betrieblicher Auftrag aus Kundensicht.“ | Ist die Situation beruflich realistisch? |
| **Differenzierung** | „Ergänze gestufte Hilfen (Hilfe 1: Hinweis, Hilfe 2: Teilschritt, Hilfe 3: Lösungsweg).“ | Führen die Hilfen zum Ziel, ohne die Lösung vorwegzunehmen? |
| **Sprachsensibilität** | „Kurze Sätze, Fachbegriffe beim ersten Auftreten erklären, Glossar mit 5 Begriffen.“ | Verstehen auch Auszubildende mit Deutsch als Zweitsprache die Aufgabe? |
| **Sicherheit** | „Sicherheitshinweise mit [PRÜFEN] markieren. Keine Normen nennen, die nicht im Material stehen.“ | Sind alle Hinweise mit Primärquellen abgeglichen? |
| **Fehlerkultur / Diagnose** | „Distraktoren aus typischen Fehlvorstellungen ableiten und jeweils benennen.“ | Sind die falschen Antworten plausibel und diagnostisch aussagekräftig? |

**Welche Vorgabe sorgt für Constructive Alignment?**

- [( )] „Schreibe ein abwechslungsreiches Quiz zur Elektropneumatik.“
- [(X)] „Lernziel: Die Auszubildenden erklären, warum vor dem Umstecken von Schläuchen entlüftet werden muss. Jede Frage prüft genau dieses Lernziel auf Anforderungsbereich II.“
- [( )] „Schreibe ein Quiz mit 10 Fragen, mittlerer Schwierigkeitsgrad.“
***
Nur die zweite Vorgabe nennt Lernziel **und** Operator **und** Anforderungsbereich – das Modell hat einen Maßstab, und Sie haben eine Prüffrage. „Mittlerer Schwierigkeitsgrad“ ist nicht überprüfbar.
***

## 2 · Material generieren: Prompt-Muster und Prompt-Ketten

<!-- didaktik="ca. 15 min · Prompt-Muster vorstellen, ein Muster gemeinsam ausfüllen" -->

### Ein Prompt-Muster für ein diagnostisches Quiz

Der Aufbau ist bekannt (Rolle · Kontext · Aufgabe · Vorgaben · Ausgabeformat). Neu ist: Die **Vorgaben** enthalten die didaktischen Leitplanken, das **Ausgabeformat** die LiaScript-Syntax.

````markdown
# Rolle
Du bist Fachlehrkraft für Mechatronik an einer berufsbildenden Schule und erstellst Lernmaterial für den Laborunterricht.

# Kontext
- Ausbildungsberuf: Mechatroniker/-in, 2. Ausbildungsjahr
- Laboraufbau: Elektropneumatik-Lernsystem (doppeltwirkende Zylinder, 5/2-Wegeventile mit Magnetspule, 24-V-Steuerung, Druckluft 6 bar)
- Lerngruppe: 16 Auszubildende, heterogene Vorkenntnisse, einige mit Deutsch als Zweitsprache

# Lernziel
Die Auszubildenden erklären, warum vor dem Umstecken von Schläuchen die Druckluft abgesperrt
und das System entlüftet werden muss (Anforderungsbereich II).

# Aufgabe
Erstelle ein diagnostisches Quiz mit 4 Single-Choice-Fragen zu diesem Lernziel.

# Vorgaben
- Jede Frage prüft das Lernziel auf Anforderungsbereich II – keine reinen Wissensfragen.
- Je 3 Distraktoren, abgeleitet aus typischen Fehlvorstellungen. Nenne die Fehlvorstellung im Lösungstext.
- Kurze Sätze, Fachbegriffe beim ersten Auftreten erklären.
- Nenne keine Normen, Vorschriften oder Quellen. Markiere jede sicherheitsrelevante Aussage mit [PRÜFEN].

# Ausgabeformat
LiaScript-Markdown. Verwende ausschließlich diese Syntax:
- [( )] falsche Antwort
- [(X)] richtige Antwort
***
Lösungstext
***
````

**Welcher Baustein des Musters bewirkt, dass falsche Antworten im Quiz *lehrreich* sind?**

- [( )] Rolle
- [( )] Kontext
- [(X)] Vorgaben: Distraktoren aus Fehlvorstellungen, Fehlvorstellung im Lösungstext benennen
- [( )] Ausgabeformat
***
Distraktoren wie „Weil die Schläuche sonst schmutzig werden“ sind sofort als falsch erkennbar und sagen nichts über das Denken der Lernenden. Distraktoren aus **Fehlvorstellungen** („Grundstellung des Ventils = drucklos“) zeigen Ihnen, *welcher* Fehler vorliegt – das Quiz wird diagnostisch.
***

### Muster für weitere Materialarten

| Material | Was das Modell gut kann | Was Sie vorgeben müssen |
| --- | --- | --- |
| **Lernsituation** | Kundenauftrag, Phasenstruktur, Ideen für Handlungsprodukte | Lernfeld, Aufbau, Zeit, vollständige Handlung, Lernziele |
| **Arbeitsblatt** | Gliederung, Aufgabenformulierungen, Tabellenvorlagen | Lernziel mit Operator, Sicherheitsrahmen, Niveau |
| **Quiz** | viele Varianten schnell, Lösungstexte | Lernziel, Distraktoren aus Fehlvorstellungen, LiaScript-Syntax |
| **Gestufte Hilfen** | Hinweise in Stufen formulieren | Lösung (von Ihnen geprüft!) als Material mitgeben |
| **Bewertungsraster** | Kriterien und Niveaustufen vorschlagen | Lernziele, Handlungsprodukte, Gewichtung |
| **Gefährdungsbeurteilung** | Strukturvorschlag, Gefährdungsgruppen abfragen | **nur Entwurf** – Prüfung gegen Gesetz, DGUV, RiSU, Hersteller |

### Prompt-Ketten

Großes Material entsteht nicht in einem Prompt. Die **geprüfte** Ausgabe eines Schritts wird Material des nächsten:

```ascii
  Lernsituation ──prüfen──► Arbeitsblatt ──prüfen──► Quiz + Hilfen ──prüfen──► LiaScript ──Prüfskript──► fertig
       │                         │                        │                         ▲
       └─────────────────────────┴────────────────────────┴── Vorlage + Lernziele ──┘
```

> [!WARNING] ⚠️ Fehler wandern mit
> Wird eine **ungeprüfte** Ausgabe weiterverwendet, übernimmt der nächste Prompt deren Fehler – und formuliert sie oft noch überzeugender. Prüfen Sie **zwischen** den Schritten, nicht erst am Ende.

## 3 · Qualität sichern: das Prüfraster

<!-- didaktik="ca. 15 min · Prüfraster einführen und an einem Beispiel anwenden" -->

KI-Material wird in **sechs Dimensionen** geprüft. Für jede gibt es einen geeigneten Prüfweg – und nicht jeder Prüfweg ist gleich zuverlässig.

| Dimension | Prüffragen | Prüfweg |
| --- | --- | --- |
| **1 Fachliche Richtigkeit** | Stimmen Werte, Abläufe, Begriffe, Schaltzeichen? | Datenblatt, Fachbuch, eigener Versuch am Aufbau |
| **2 Sicherheit** | Sind alle Gefährdungen erfasst, Maßnahmen richtig, Normen echt? | **Primärquellen**: Gesetz, DGUV, RiSU, Herstellerangaben |
| **3 Didaktische Passung** | Alignment Lernziel–Aufgabe, Niveau, vollständige Handlung, Differenzierung | Lernziele und Leitplanken aus Abschnitt 1 |
| **4 Sprache** | Verständlich für die Lerngruppe? Fachbegriffe erklärt? Einheitlich? | Lesen aus Sicht der Lernenden, ggf. Kolleg:in |
| **5 Recht und Transparenz** | Bildrechte, Lizenzen, Quellenangaben, KI-Kennzeichnung | Lizenz prüfen, APA 7, Prompt-Dokumentation |
| **6 Technik und Format** | Rendert das LiaScript? Funktionieren Quiz und Links? | LiaScript-Vorschau, Prüfskript |

<small>Ein zweites Modell kann als **Gegenprüfer** Hinweise liefern („Finde fachliche Fehler in diesem Arbeitsblatt“). Das ersetzt keine Prüfung: Auch Prüf-Modelle irren und bewerten z. B. längere Antworten systematisch besser (Zheng et al., 2023).</small>

### Übung 3: Ein KI-Quiz prüfen

Ein Modell hat zum Lernziel *„Die Auszubildenden **erklären**, warum vor dem Umstecken von Schläuchen die Druckluft abgesperrt und das System entlüftet werden muss“* diese Frage erzeugt:

> **Frage 2:** Was muss man tun, bevor man einen Schlauch umsteckt?
>
> - (a) Das Ventil in Grundstellung bringen, dann ist die Anlage drucklos. ✔
> - (b) Den Schlauch kräftig abziehen.
> - (c) Eine Pause machen.
> - (d) Nichts, Druckluft ist ungefährlich.
>
> *Lösung: (a) ist richtig, gemäß DGUV Vorschrift 3.*

In welchen Dimensionen des Prüfrasters fällt die Frage durch?

- [[X]] 1 Fachliche Richtigkeit
- [[X]] 2 Sicherheit
- [[X]] 3 Didaktische Passung
- [[ ]] 6 Technik und Format
***
- **Fachlich und Sicherheit:** Die als richtig markierte Antwort ist falsch – Grundstellung heißt **nicht** drucklos. Richtig wäre: Druckluft absperren und entlüften. Die zitierte DGUV Vorschrift 3 regelt **elektrische** Anlagen und Betriebsmittel, nicht die Pneumatik – ein echtes Regelwerk, falsch zugeordnet. Solche Fehler sind schwerer zu entdecken als frei erfundene Normen.
- **Didaktisch:** Das Lernziel verlangt **erklären** (AFB II), die Frage fragt nur eine Handlung ab (AFB I). Die Distraktoren (b)–(d) sind offensichtlich falsch und nicht diagnostisch.
- **Format:** Am Format ist nichts auszusetzen – gut formatiertes Material wirkt verlässlicher, als es ist.
***

**Welche Überarbeitung passt zum Lernziel?**

- [( )] „Nennen Sie die drei Schritte vor dem Umstecken eines Schlauchs.“
- [(X)] „Ein Kollege bringt das Ventil in Grundstellung und will dann den Schlauch abziehen. Erklären Sie, warum das gefährlich ist.“
- [( )] „Ist Druckluft gefährlich? Ja / Nein“
***
Die zweite Aufgabe greift die **Fehlvorstellung** („Grundstellung = drucklos“) als Situation auf und verlangt eine **Erklärung** – das ist Anforderungsbereich II und gleichzeitig diagnostisch.
***

## 4 · Modelle vergleichen: dieselbe Aufgabe, verschiedene LLMs

<!-- didaktik="ca. 20 min · theoretischer Vergleich mit konstruierten Ausgaben; Bewertung mit dem Prüfraster; Methodik eines fairen Vergleichs" -->

In HAWKI können Sie zwischen **mehreren Sprachmodellen** wählen (die Auswahl ändert sich laufend – die aktuelle Liste sehen Sie in HAWKI). Die Beispiel-Prompt-Dokumentation wurde mit einem offenen Modell auf dem Lehrstuhl-Server erzeugt. Woran unterscheiden sich Modelle – und was bedeutet das für Lernmaterial?

### Worin sich Modelle unterscheiden

| Merkmal | Was es bedeutet | Folge für Lernmaterial |
| --- | --- | --- |
| **Größe** (Parameter) | mehr gelerntes Wissen und Sprachvermögen, aber langsamer und teurer | kleine Modelle: mehr Fachfehler, flachere Aufgaben |
| **Trainingsdaten und Wissensstand** | Wissen endet am Trainingsstichtag; Deutsch und Fachsprache unterschiedlich stark vertreten | veraltete Normen; Anglizismen, ungewohnte Fachbegriffe |
| **Kontextfenster** | wie viel Material (Datenblatt, Vorlage, Lernsituation) gleichzeitig verarbeitet wird | lange Vorlagen werden teilweise „vergessen“ |
| **Reasoning-Modelle** („denkt nach“) | rechnen und planen Zwischenschritte, bevor sie antworten | besser bei Zeitbudgets, Berechnungen, Logik – aber langsamer |
| **Formattreue** | wie genau Vorgaben und Syntax eingehalten werden | LiaScript-Quiz rendert – oder eben nicht |
| **Offen vs. proprietär, Hosting** | wo die Daten verarbeitet werden, wer Zugriff hat | Datenschutz; lokal betriebene offene Modelle sind nachvollziehbarer |
| **Zufall (Sampling)** | dasselbe Modell gibt bei gleichem Prompt verschiedene Antworten | ein einzelner Lauf sagt wenig über ein Modell aus |

**Sie geben denselben Prompt zweimal in dasselbe Modell ein und erhalten zwei verschiedene Quizze. Was folgt daraus?**

- [( )] Das Modell ist defekt.
- [(X)] Antworten werden mit Zufallsanteil erzeugt – für einen Vergleich braucht es mehrere Läufe pro Modell.
- [( )] Die zweite Antwort ist besser, weil das Modell dazugelernt hat.
***
Sprachmodelle wählen das nächste Token mit Wahrscheinlichkeiten aus (KI-Einführung I). Das Modell lernt im Chat **nicht** dazu – es hat nur mehr Kontext. Wer Modelle vergleicht, muss diese Streuung berücksichtigen.
***

### Fallbeispiel: ein Prompt, drei Modelle

Der Prompt aus Abschnitt 2 (diagnostisches Quiz) wurde an drei Modelle gegeben. Hier jeweils die **erste Frage** der Ausgabe.

> [!NOTE] ℹ️ Hinweis
> Die drei Ausgaben sind **für diese Übung konstruiert** und typischen Mustern nachempfunden. Sie stehen nicht für bestimmte Produkte. Echte Ausgaben eines offenen Modells finden Sie in der [Beispiel-Prompt-Dokumentation](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/IngP-d_Labor_WiSe_2026_2027/main/00_Organisation/KI/Beispiel_Prompt_Dokumentation.md).

**Modell A** – großes Modell, schnell, sehr flüssige Sprache

````markdown
**Frage 1:** Was versteht man unter dem Entlüften einer pneumatischen Anlage?

- [( )] Das Öffnen aller Ventile
- [(X)] Das Ablassen der Druckluft aus dem System
- [( )] Das Reinigen der Schläuche
- [( )] Das Abschalten der 24-V-Versorgung
***
Richtig ist das Ablassen der Druckluft. Gemäß DGUV Vorschrift 3 ist dies vor
allen Arbeiten an der Anlage verpflichtend. Fehlvorstellung bei Antwort 4:
Die Lernenden verwechseln elektrische und pneumatische Energie.
***
````

**Modell B** – mittelgroßes offenes Modell, lokal betrieben, langsamer

````markdown
**Frage 1:** Lea hat das 5/2-Wegeventil in die Grundstellung geschaltet. Der Zylinder
ist eingefahren. Sie will jetzt den Schlauch am Zylinder abziehen. Warum ist das gefährlich?

- [x] Im Schlauch und im Zylinder steht noch Druck. Der Schlauch kann umherschlagen. 
- [ ] Die Grundstellung bedeutet, dass das System drucklos ist.
- [ ] Gefährlich ist nur die 24-V-Spannung am Ventil.
- [ ] Der Zylinder fährt sofort aus, weil die Feder fehlt.

Explanation: Fehlvorstellung 2 = "Grundstellung = drucklos". Fehlvorstellung 3 =
nur Elektrik ist gefährlich. [PRÜFEN] Verhalten des Zylinders bei Druckabfall.
````

**Modell C** – kleines Modell, sehr schnell

````markdown
**Frage 1:** Was macht man vor dem Umstecken?

- [(X)] Ventil in Grundstellung, dann ist alles drucklos
- [( )] Gar nichts
- [( )] Den Zylinder festhalten
- [( )] Musik hören
***
Lösung: Antwort 1.
***
````

**Bewerten Sie die drei Ausgaben mit dem Prüfraster** (3 = erfüllt, 2 = teilweise, 1 = kaum, 0 = nicht erfüllt). Ihre Einschätzung für **Modell A**:

[(3) (2) (1) (0)]
[               ] Fachliche Richtigkeit
[               ] Sicherheit
[               ] Didaktische Passung (Lernziel „erklären“, Distraktoren)
[               ] Sprache
[               ] Technik und Format (LiaScript)

Ihre Einschätzung für **Modell B**:

[(3) (2) (1) (0)]
[               ] Fachliche Richtigkeit
[               ] Sicherheit
[               ] Didaktische Passung (Lernziel „erklären“, Distraktoren)
[               ] Sprache
[               ] Technik und Format (LiaScript)

Ihre Einschätzung für **Modell C**:

[(3) (2) (1) (0)]
[               ] Fachliche Richtigkeit
[               ] Sicherheit
[               ] Didaktische Passung (Lernziel „erklären“, Distraktoren)
[               ] Sprache
[               ] Technik und Format (LiaScript)

**Mit welcher Ausgabe würden Sie weiterarbeiten?**

- [( )] Modell A – sie sieht am professionellsten aus und rendert sofort.
- [(X)] Modell B – didaktisch die beste Grundlage; Syntax und Sprache lassen sich gezielt korrigieren.
- [( )] Modell C – kurz und schnell, das reicht für ein Quiz.
***
<!-- data-type="none" -->
| | Modell A | Modell B | Modell C |
| --- | --- | --- | --- |
| Fachlich | Antwort richtig, aber **Regelwerk falsch zugeordnet** (DGUV V3 = Elektrik) | richtig, offene Stelle ehrlich mit [PRÜFEN] markiert | **falsch**: Grundstellung ≠ drucklos |
| Didaktik | **AFB I** statt „erklären“; ein Distraktor diagnostisch | **AFB II**, Situation, alle Distraktoren aus Fehlvorstellungen | AFB I, Distraktoren absurd |
| Vorgaben | Quelle genannt, obwohl verboten | [PRÜFEN] gesetzt, keine Quelle | Lösungstext ohne Fehlvorstellung |
| Format | **LiaScript korrekt** | **falsche Syntax** (`[x]`), Lösungstext fehlt im Block, „Explanation“ | korrekt |

**Die Lehre:** Die Ausgabe, die am besten *aussieht* (A), ist nicht die beste. Formatfehler (B) sind leicht und sicher zu beheben – mit der Vorlage im Prompt oder einem Prüfskript. Fachliche und didaktische Mängel (A, C) dagegen müssen Sie erst einmal *finden*. Wählen Sie deshalb nach **Inhalt und Didaktik**, nicht nach Glanz.
***

### Ein fairer Modellvergleich

Welche Regeln machen einen Vergleich von Modellen aussagekräftig? (mehrere richtig)

- [[X]] Bewertungskriterien **vor** dem Lesen der Ausgaben festlegen (Prüfraster).
- [[X]] Allen Modellen **denselben Prompt und dasselbe Material** geben.
- [[X]] Pro Modell **mehrere Läufe** betrachten, nicht nur einen.
- [[ ]] Das Modell mit der längsten Antwort nehmen – es hat sich am meisten Mühe gegeben.
- [[X]] Ausgaben möglichst **ohne Modellnamen** bewerten (blind), z. B. zu zweit.
- [[X]] Modell, Version und Datum **dokumentieren** – Modelle werden laufend geändert.
***
So wird aus „Modell X ist besser“ eine begründete Aussage: gleiche Bedingungen, vorher festgelegte Kriterien, mehrere Läufe, blinde Bewertung, Dokumentation. Länge ist kein Qualitätsmerkmal – Menschen **und** KI-Prüfer lassen sich davon aber leicht beeindrucken (Zheng et al., 2023).
***

> [!IMPORTANT] 🎯 Für die Modellwahl
> Es gibt nicht *das* beste Modell für Lernmaterial. Ein **großes Modell** für Entwurf und Struktur, ein **zweites Modell** als Gegenprüfer, ein **Prüfskript** für das Format – und **Sie** für Fachlichkeit, Sicherheit und Didaktik. Bei personenbezogenen oder internen Daten entscheidet ohnehin der **Datenschutz** über das Werkzeug: HAWKI mit OVGU-Account.

## 5 · Praxis: Ihr Material, Version 2

<!-- didaktik="ca. 15 min Arbeitsphase in der Sitzung, Fortsetzung bis zur Ideenpräsentation am 03.11." -->

> [!IMPORTANT] 📝 Auftrag
> Entwickeln Sie Ihr Lernmaterial aus dem Prompting-Auftrag (S02) zu einer **Version 2** weiter – didaktisch begründet, in zwei Modellen erzeugt, mit dem Prüfraster bewertet und als LiaScript umgesetzt.

1. **Lernziel schärfen:** Formulieren Sie *ein* Lernziel mit Operator und Anforderungsbereich.
2. **Leitplanken ergänzen:** Ergänzen Sie Ihren S02-Prompt um mindestens **drei didaktische Vorgaben** aus Abschnitt 1 und um die LiaScript-Syntax (bzw. die [Vorlage](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/IngP-d_Labor_WiSe_2026_2027/main/00_Organisation/KI/Vorlage_LiaScript_Praesentation.md)) im Ausgabeformat.
3. **Zwei Modelle:** Führen Sie den Prompt in HAWKI mit **zwei verschiedenen Modellen** aus. Originalausgaben unverändert speichern.
4. **Bewerten:** Bewerten Sie beide Ausgaben mit dem Prüfraster – zu zweit und möglichst blind (Ausgaben vertauschen).
5. **Umsetzen:** Arbeiten Sie mit der besseren Ausgabe weiter, korrigieren Sie sie und prüfen Sie die LiaScript-Vorschau.

**Mini-Referenz LiaScript** – die Syntax, die Ihr Modell einhalten soll:

````markdown
Single Choice:              Multiple Choice:           Lückentext:
- [( )] falsch              - [[X]] richtig            Der Druck beträgt [[6]] bar.
- [(X)] richtig             - [[ ]] falsch
***                                                    Freitext (Umfrage):
Lösungstext                 Hinweis-Box:               [[___ ___ ___]]
***                         > [!WARNING] ⚠️ Titel
                            > Text
````

**1 · Ihr Lernziel** (mit Operator und Anforderungsbereich):

[[___ ___]]

**2 · Ihre didaktischen Vorgaben im Prompt** (mindestens drei):

[[___ ___ ___ ___]]

**3 · Modellvergleich:** Welche zwei Modelle (Name, Datum)? Wie haben Sie die Ausgaben mit dem Prüfraster bewertet – und warum haben Sie sich für eine entschieden?

[[___ ___ ___ ___ ___]]

**4 · Wichtigste Korrektur:** Welchen Fehler haben Sie gefunden, mit welcher Primärquelle geprüft und wie korrigiert?

[[___ ___ ___]]

> [!TIP] 📎 Für den Studiennachweis
> Prompt (v1 aus S02, v2 von heute), beide Originalausgaben und Ihre Prüftabelle gehören zu den **ersten drei Prompts mit Iterationen** im Anhang. Kennzeichnen Sie Werkzeug, Modell und Datum nach APA 7.

## 6 · Abschluss und Ausblick

**Wie sicher fühlen Sie sich jetzt?**

Ich kann KI-Lernmaterial didaktisch begründet erstellen und seine Qualität prüfen.

- [(1)] 1
- [(2)] 2
- [(3)] 3
- [(4)] 4

**Exit-Ticket:** Welche Prüfdimension unterschätzen Sie bisher am meisten – und warum?

[[___ ___]]

> [!NOTE] 📅 Nächste Sitzung: Dienstag, 03.11.2026 (live)
> **Input „Lehren und Lernen im Labor“ (Gruppe 1)** und **Ideenpräsentation**. Bringen Sie Ihre erste Idee für Beruf, Lernfeld und Laboraufbau mit – gern mit Ihrem Material aus heute als Beispiel.

## Quellen

- Anderson, L. W., & Krathwohl, D. R. (Hrsg.). (2001). *A taxonomy for learning, teaching, and assessing: A revision of Bloom's taxonomy of educational objectives*. Longman.
- Biggs, J. (1996). Enhancing teaching through constructive alignment. *Higher Education, 32*(3), 347–364. https://doi.org/10.1007/BF00138871
- Dietrich, A. (o. J.). *LiaScript-Dokumentation*. https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md
- Kasneci, E., Seßler, K., Küchemann, S., Bannert, M., Dementieva, D., Fischer, F., … Kasneci, G. (2023). ChatGPT for good? On opportunities and challenges of large language models for education. *Learning and Individual Differences, 103*, 102274. https://doi.org/10.1016/j.lindif.2023.102274
- Kultusministerkonferenz. (2019). *Richtlinie zur Sicherheit im Unterricht (RiSU)* (Empfehlung der KMK vom 09.09.1994 i. d. F. vom 14.06.2019). KMK.
- Kultusministerkonferenz. (2021). *Handreichung für die Erarbeitung von Rahmenlehrplänen der Kultusministerkonferenz für den berufsbezogenen Unterricht in der Berufsschule und ihre Abstimmung mit Ausbildungsordnungen des Bundes für anerkannte Ausbildungsberufe*. KMK.
- UNESCO. (2023). *Guidance for generative AI in education and research*. UNESCO. https://doi.org/10.54675/EWZM9535
- Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., … Stoica, I. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. *Advances in Neural Information Processing Systems, 36*. https://arxiv.org/abs/2306.05685
