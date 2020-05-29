# Lektion 3: Einlesen von Daten zur weiteren Verarbeitung

Hallo,

in der letzten Lektion haben wir ein bisschen über unterschiedliche Datentypen, Kontrollstrukturen,
Syntax und Blöcke gelernt. Dieses Mal wollen wir das gelernte Wissen nutzen um ein paar Daten einzulesen,
auzugeben und ein bisschen zu manipulieren.

Wie werden dazu einen Datensatz zu der Ausbreitung von COVID-19 in der Welt nutzen. Die Daten werden vom
"COVID-19 Dashboard by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University"
zur Verfügung gestellt und sind "provided solely for non-profit public health, educational, and academic research purposes".
Sollte also passen.

[https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)

Im spezifischen werden wir uns mit diesem Datensatz beschäftigen:

[https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv)

## Arbeiten mit Daten

### Datenbeschaffung

Um irgendwelche Daten in welcher Art und Weise auch immer darzustellen oder zu bearbeiten müssen wir diese Daten erstmal
finden oder selber erstellen. Für unsere Zwecke sind öffentliche/offene Daten recht praktisch und hier gibt es einige
davon:

[https://www.google.com/publicdata/directory](https://www.google.com/publicdata/directory)

Für selbsterhobene Daten hilft auch ein Export aus Excel oder jedweder anderen Software in einem brauchbaren Datenformat.
Aber was sind diese Datenformate und welche sind brauchbar?

### Datenformate

Wie auch wir (gleich) muss jedes Programm dass "von aussen" Daten einliest irgendwie Wissen wie diese strukturiert sind.
Euer Excel muss wissen was eine Tabellenzeile ist, wieviele Spalten diese hat und was der Inhalt der jeweiligen Spalte ist.
Euer Computerspiel muss beim einlesen wissen wo sich die aktuelle Anzahl der "Leben" sowie der Punktestand befindet.

Stellt Euch das ungefähr so vor wie die Listen die wir in der letzten Lektion kennengelernt haben:

```python
spielstand = [2, 5711, 12, "Barde"]
```

Für Euer Computerspiel könnte dies ein Spielstand sein mit den Informationen. Wenn wir den Spielstand laden macht das Spiel
vielleicht folgendes:

```python
anzahlLeben = spielstand[0]
punkte = spielstand[1]
level = spielstand[2]
charakterKlasse = spielstand[3]
print "Leben: ", anzahlLeben
print "Punkte: ", punkte
print "Level: ", level
print "Klasse: ", charakterKlasse
```

Ausgabe:
```
Leben: 2
Punkte: 5711
Level: 12
Klasse: Barde
```

Das Spiel könnte nun diese eingelesenen Werte setzen und das Spiel kann bei Level 12 mit 2 Leben fortgesetzt werden.

Wir sehen, dass wir einzelnen Elemente einer liste mit `[0]` adressieren können und nicht, wie in der vorherigen Lektion
immer eine Schleife bauen müssen. Die `0` ist hierbei der **Index** des Datensatzes in der Liste. Listen beginnen immer
mit dem Index `0`.

Wir haben gerade, für unser fiktives Computerspiel, ein Datenformat für Spielstände festgelegt und dieses eingelesen.

Komplexere Programme benötigen komplexere Datenformate und das Ziel für das Spiel sollte ausserdem sein, dass nicht jeder
einfach das Level auf 120 oder seine Leben auf 9001 setzen kann. Daher haben viele/die meisten Programme eigene Datenstrukturen.
Viele davon sind "binär" und nicht "menschenlesbar" (wie z.B. docx von Word oder xlsx von Excel).

Wenn wir mit offenen Daten arbeiten oder Daten zwischen zwei Programmen austauschen wollen, ist es aber oft hilfreich
ein Format zu wählen, dass möglichst viele Parteien lesen können, inklusive des Menschen. Man einigt sich also oft
auf "strukturierten Text" und da dann ein paar Konventionen wie genau dieser strukturiert ist. 

Im folgenden wollen wir uns CSV und JSON als Datenformat angucken. Im weiteren werden wir (wie oben in der Datenbeschaffung
angedeutet) mit CSV arbeiten.

#### CSV

CSV steht für "Comma Seperated Values". Das Datenformat ist genau das: eine Textdatei die in Zielen aufgeteilt ist und
einzelne Zellen einer Tabelle durch Kommata (oder Semikolon) voneinander abtrennt. Das sieht dann für unseren
Spielstand ungefähr so aus:

```
2,5711,12,"Barde"
```

Sollten wir, z.b. für einen weiteren Spieler, einen weiteren Spielstand einlesen können/wollen, könnte das wie folgt aussehen:

```
2,5711,12,"Barde"
1,1337,12,"Koch"
```

Wir hätten dann zwei Zeilen die einzulesen wären und könnten dann die einzelnen Zellen pro Spieler durchgehen und
die entsprechenden Werte setzen.

Insbesondere Excel exportiert CSV gerne mit Semikolon als Zellentrennzeichen, das sähe dann so aus und wir müssten
"an Semikolon trennen" aber das Ergebnis wäre das gleiche:

```
2;5711;12;"Barde"
1;1337;12;"Koch"
```

Eine weitere Besonderheit von CSV ist, dass es manchmal eine Kopfzeile (den sogenannten Header) mitbringt, die die
Daten genauer beschreibt. Diese Zeile entspricht dem Format der darunterliegenden Zeilen aber meist/oft nicht den
**Datentypen** dieser. Das wäre dann im folgenden der Fall:

```
"Leben","Punkte","Level","Klasse"
2,5711,12,"Barde"
1,1337,12,"Koch"
```

Manchmal helfen diese "Metainformationen" den Datensatz besser zu verstehen. Wir werden das sehen, sobald wir mit
unserem COVID-19 Datensatz arbeiten.

#### JSON

Ein weiteres verbreitetes Datenformat auf das hier nur kurz eingegangen werden soll, ist JSON.

JSON steht für "JavaScript Object Notation" und hat sich vor allem im Web einen Namen gemacht, da die Programmiersprache
JavaScript diese Daten sehr einfach einlesen kann.

Unser Spielstand sähe in JSON etwa so aus:

```JSON
[2,5711,12,"Barde"]
```

Der Spielstand für zwei Spieler etwa so:

```JSON
[
    [2,5711,12,"Barde"],
    [1,1337,12,"Koch"]
]
```

Dem aufmerksamen Leser dieser Zeilen fällt, vielleicht, auf, dass hier eine "Liste von Listen" kontruiert wird.
Wir haben eine äussere Liste `[]` die als Elemente unsere zwei Spielstände als weitere Listen enthält.

Dieses Konzept ist nicht nur in JSON weitverbreitet und daher interessant zu verstehen. Später dazu mehr, aber
auch eine Excel-Tabelle ist beim einlesen eine Liste von Zeilen die jeweils eine Liste von Feldern enthält.
Guckt Euch mal ein Schachbrett an und versucht es Euch als Excel-Tabelle vorzustellen.

### Libraries

Um die Umwandung von unterschiedlichen Datenformaten nicht immer "per Hand" machen zu müssen, und auch um
so besonderheiten wie "Semikolon" oder "Header" nicht immer als Fehlerquelle zu haben, gibt es eine große
Menge an fertiger Software die diese Aufgabe erledigt.

In Python kann man dafür sogenannten **Libraries** oder **Bibliotheken** benutzen, die einem diese
Fleissarbeit abnehmen und ein paar **Funkionen** zur Verfügung stellen um sich das Leben etwas einfacher
zu machen.

Manche Libraries werden von Python bereits mitgeliefert und ein paar Funktionen dieser Libraries haben
wir auch schon genutzt (`print`, `len`), andere müssen installiert und importiert werden.

Wir nutzen vorerst die python eigene Library `csv` zur Verarbeitung von CSV Dateien.

## Daten einlesen und ausgeben

Um Daten einzulesen müssen wir drei Schritte erledigen:

- CSV Datei herunterladen (siehe oben)
- Library importieren
- CSV Datei einlesen

Das folgende Programm macht genau dies:

```python
import csv

csv_file = open('time_series_covid19_recovered_global.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
for row in csv_reader:
    if line_count == 0:
        cell_count = 0
        for col in row:
            print("Name Spalte:", cell_count, col)
            cell_count += 1
    line_count += 1
print("Zeilen in Datei:", line_count)
```

Ausgabe (gekürzt, unterer Teil):
```
...
Name Spalte: 114 5/11/20
Name Spalte: 115 5/12/20
Name Spalte: 116 5/13/20
Name Spalte: 117 5/14/20
Name Spalte: 118 5/15/20
Name Spalte: 119 5/16/20
Name Spalte: 120 5/17/20
Name Spalte: 121 5/18/20
Name Spalte: 122 5/19/20
Name Spalte: 123 5/20/20
Name Spalte: 124 5/21/20
Name Spalte: 125 5/22/20
Name Spalte: 126 5/23/20
Name Spalte: 127 5/24/20
Name Spalte: 128 5/25/20
Name Spalte: 129 5/26/20
Name Spalte: 130 5/27/20
Zeilen in Datei: 254
```

Wir `import`ieren das csv modul, lesen eine Datei mit dem angegebenen Namen `time_series_covid19_recovered_global.csv` im lokalen
Verzeichnis aus, setzen uns einen "Zähler" um die Zeilenanzahl zu zählen, machen eine Schleife über jede Zeile, überprüfen
ob es sich um die erste Zeile handelt (unsere "Header"-Zeile) und machen dann in der Schleife eine weitere Schleife über jede Spalte
um den "Namen" der Spalte auszugeben. Auch in der inneren Schleife halten wir einen Zähler vor, damit wir im nächsten Beispiel nicht
manuell zählen müssen. Am Ende kehren wir (über die Einrückung) zu unserem "Hauptblock" des Programmes zurück
und geben die gezähle Anzahl von Zeilen im Datensatz insgesamt aus.

Interessant bei den Zählern ist das `+= 1` Konstrukt, dass die Variable einfach um eins erhöht. Wir haben das vorher noch etwas
mühseliger mit `line_count = line_count + 1` gemacht. Das hier ist kürzer. Programmierer sind faule Menschen.

Wir haben Daten eingelesen! Und ausgegeben!

## Daten verarbeiten

Wenn wir uns die heruntergeladene CSV Datei jetzt angucken (in einem Texteditor (Visual Studio Code) oder Import nach Excel),
können wir uns den vorliegenden Datensatz genau angucken und werden, zusammen mit der Information aus den Headerspalten und dem Dateinamen 
herausfinden, dass es sich (vermutlich) um folgendes hält:

Anzahl der von COVID-19 geheilten Personen in `Province/State` und `Country/Region` pro Tag seit dem `1/22/20`. Zusätzlich
kriegen wir für die Region noch Positionsinformationen in der Form von **Latitude** und **Longitude** (Breiten- und Längengrad).

Wenn wir jetzt z.B. rausfinden möchten wieviele Leute von COVID-19 geheilt waren am 23.05.2020 in allen Regionen, würde
uns eine Modifikation des obigen Programmes weiterhelfen:

```python
import csv

csv_file = open('time_series_covid19_recovered_global.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
for row in csv_reader:
    if line_count > 0:
        print("Provice:", row[0], "Region:", row[1], "Number:", row[126])
    line_count += 1
print("Zeilen in Datei:", line_count)
```

Ausgabe (gekürzt, unterer Teil):
```
...
Provice: Anguilla Region: United Kingdom Number: 3
Provice: British Virgin Islands Region: United Kingdom Number: 6
Provice: Turks and Caicos Islands Region: United Kingdom Number: 10
Provice:  Region: MS Zaandam Number: 0
Provice:  Region: Botswana Number: 19
Provice:  Region: Burundi Number: 20
Provice:  Region: Sierra Leone Number: 241
Provice: Bonaire, Sint Eustatius and Saba Region: Netherlands Number: 6
Provice:  Region: Malawi Number: 28
Provice: Falkland Islands (Malvinas) Region: United Kingdom Number: 13
Provice: Saint Pierre and Miquelon Region: France Number: 1
Provice:  Region: South Sudan Number: 6
Provice:  Region: Western Sahara Number: 6
Provice:  Region: Sao Tome and Principe Number: 4
Provice:  Region: Yemen Number: 11
Provice:  Region: Comoros Number: 18
Provice:  Region: Tajikistan Number: 1223
Provice:  Region: Lesotho Number: 0
Zeilen in Datei: 254
```

Wir ändern den Vergleichsoperator `==` auf ein `>` und ignorieren damit die nicht mehr relevanten Headerzeilen.

Auch referenzieren wir die Datensätze der Zeile `row` direkt, da wir den Zähler für die Zellen nicht mehr brauchen.
Die `126` haben wir uns aus dem vorherigen Beispiel herausgesucht. Programmierer sind faule Menschen.

Wenn wir uns die Ausgabe dieses Programmes angucken, werden wir sehen, dass alle Datensätze eine `Region` aber nur
wenige eine `Province` haben. Damit müssen wir wohl leben und ändern unser Interesse dahingehend, dass uns nur noch
`Region`s interessieren. Dafür können wir in der Schleife, genau wie wir es mit line_count machen einen "Filter" einbauen.

```python
import csv

csv_file = open('time_series_covid19_recovered_global.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
for row in csv_reader:
    if line_count > 0:
        if not row[0]:
            print("Region:", row[1], "Number:", row[126])
    line_count += 1
print("Zeilen in Datei:", line_count)
```

Ausgabe (gekürzt, unterer Teil):
```
...
Region: Vietnam Number: 267
Region: Zambia Number: 336
Region: Zimbabwe Number: 18
Region: West Bank and Gaza Number: 348
Region: Laos Number: 14
Region: Kosovo Number: 782
Region: Burma Number: 120
Region: MS Zaandam Number: 0
Region: Botswana Number: 19
Region: Burundi Number: 20
Region: Sierra Leone Number: 241
Region: Malawi Number: 28
Region: South Sudan Number: 6
Region: Western Sahara Number: 6
Region: Sao Tome and Principe Number: 4
Region: Yemen Number: 11
Region: Comoros Number: 18
Region: Tajikistan Number: 1223
Region: Lesotho Number: 0
Zeilen in Datei: 254
```

Der Filter funktioniert weil der Wert für `row[0]` `False` ist wenn er leer oder nicht gesetzt ist, und damit der
Block im `if` nicht abgearbeitet wird...wie für `line_count == 0`.

Wir haben also erfolgreich einen Datensatz eingelesen, gefiltert auf die relevanten Informationen (aufbereitet) und
dann nur die relevanten Informationen ausgegeben.

## Fazit

Soviel für diese Lektion. Spielen sie mit dem `not` Operator in Zeile 8 des letzten Beispiels herum, probieren sie andere Tageswerte abzufragen, versuchen sie nur die ersten 20/30/100 Zeilen der Datei einzulesen und auszugeben, oder probieren sie eine andere/eigene
CSV Datei aus.

In der nächsten Lektion werden wir lernen mit diesen Daten oder anderen Daten zu rechnen und uns die Ergebnisse, wie unseren
Spielstand vom anfang, abzuspeichern und weiterzuverabeiten. Auf diese Weise erhalten wir aus den **Rohdaten** für uns brauchbare
**aggregierte Daten** mit denen wir dann irgendwas hübscheren anzeigen können sollten als einfach nur weissen Text auf schwarzem
Grund.

Bei Fragen, fragen!
