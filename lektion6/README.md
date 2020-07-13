# Lektion 6: Programme strukturieren, Variablen, Funktionen, Module

Hey,

bitte beachtet als allererstes, dass ich in Lektion 5ein Update vorgenommen habe, dass
Euch zeigt wie Ihr von Euch gefiltertet Daten wieder als CSV zurückspeichern könnt und
dann in andere Programme (z.b. Excel, R, SPSS) importieren könnt. Dies gibt Euch die Möglichkeit
Python nur zur Datenfilterung zu benutzen und dann zur Auswertung oder Visualisierung ein
Tool zu erwenden das ggf. besser geeignet ist oder Euch bereits besser liegt.

In dieser Lektion möchte ich Euch ein paar Möglichkeiten nahelegen größere Programme in
Python richtig zu strukturieren. Wir gehen dafür weg von unserem COVID-19 Datensatz und
springen wieder zu dem was wir in Lektion 2 gelernt haben. Ein paar der Konnzepte werden
Euch bekannt vorkommen, ein paar sind neu und auch erst hilfreich wenn man wirklich etwas
mehr Code schreibt oder sich einen "Werkzeugkasten" für unterschidliche Projekte zusammenbauen
möchte.

Ich hoffe es ist als "letzter Tip" hilfreich und erlaubt Euch in weitergehender Literatur
über Python zumindest nicht direkt in den ersten Beispielen abgehängt zu werden.


## Programme strukturieren

Generell versucht man in der Softwareentwicklung, wie auch schon erwähnt, soweit
es geht eine "seperation of concerns" zu erreichen. Einzelne Programmteile sollen möglichst
wenig tun, nur das tun und ihre Ergebnisse in einer weiterverarbeitbaren, maschinenlesbaren
Form zurückgeben.

Man versucht daher oft, mit unterschiedlichen Mitteln, "blackboxes" zu erzeugen in die man
Daten reingibt und innerhalb dieser diese dann verarbeitet, umgewandelt oder ausgegeben werden.
Wir haben dieses Konzept schon bei den Libraries die wir genutzt haben (z.B. Pandas und matplotlib)
gelernt.

Ein Aufruf einer solchen Library sah immer wie folgt aus:

```python
import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
print(csv.tail())
```

Hier nutzen wir die "blackboxes" `read_csv` und `tail` der Library `pandas` um Daten aus einer
Datei einzulesen und die letzten Zeilen auszugeben. Wie genau Pandas das macht bleibt uns
verborgen und interessiert uns nicht. Ebenfalls gibt uns Pandas unsere CSV Datei in einem Format
zur Verfügung mit dem wir weiterarbeiten können und `tails`aufrufen können. Pandas stellt
auch eine "blackbox" `read_excel` zur Verfügung. Diese bereitet eine Excel-Datei genauso auf
wie es hier mit der CSV-Datei passiert und wir können auf dem Rückgabewert ebenfalls `tails`
aufrufen.

Pandas selber sorgt also schon für eine "seperation of concerns" für die beiden Aufgaben
"Daten einlesen" und "Daten weiterverarbeiten". Dies macht es einfacher Programme zu ändern,
Datenformate umzustellen und trotzdem große Teile des Codes beibehalten zu können.

Python gibt uns einige Möglichkeiten, dass auch in unseren eigenen Programmen zu machen.
Im folgenden gucken wir uns nochmal den "Scope" von Variablen an, lernen Funktionen kennen und
schreiben eigene "Libraries". Aber los geht's...

## Variablen und Scope

Wie wir in der ersten Lektion schon gelernt haben, arbeitet Python mit "Blocks" die durch
unterschiedliche Einrückung definiert sind. Das folgende Programm definiert eine neue
Variable und gibt diese aus:

```python
name = "stephan"
print(name)
```

Ausgabe:
```bash
stephan
```

Wenn wir nun einen "Block" definieren können wir den Wert der Variable abhängig von einer
Überprüfung ändern:

```python
change = False
name = "stephan"
if(change):
    name = "stefan"
print(name)
```

Ausgabe:
```
stephan
```

Der "Block" der mit `if(change):` startet und dann alle auf dem selben Level eingerückten Zeilen
darunter enthält wird nicht ausgeführt, und der Wert der Variable wird nicht verändert.

Wenn wir nun `change` auf `True` setzen und das Programm erneut ausführen, erhalten wir eine
andere Ausgabe:


```python
change = True
name = "stephan"
if(change):
    name = "stefan"
print(name)
```

Ausgabe:
```
stefan
```

Dies erlaubt uns schon eine einfache Strukturierung unserer Programme. So könnten wir am Anfang ein
paar sogenannte globale Variablen setzen mit der wir den Ablauf des Programmes beinflussen könnten:

```python
import random

male = False
maleNames = ["stephan", "daniel", "alexander", "philipp"]
femaleName = ["silke", "daniela", "maria", "bianca"]

if(male):
    name = random.choice(maleNames)
else:
    name = random.choice(femaleName)

print(name)
```

Wir nutzen Pythons eingebaute Zufallsrouting (ebenfalls eine "blackbox") um Anhand der Konfigurationsvariable
`male` einen zufälligen männlichen oder weiblichen Namen auszugeben. Probiert `male` von `False` auf `True`
zu ändern und führt das Programm mehrfach aus.

Wir arbeiten hier nun mit sogenannten `globalen Variablen`, die Konfigurationsvariable `male` steht allen
Teilen unseres Programmes zur Verfügung und kann geändert werden:

```python
import random

male = False
maleNames = ["stephan", "daniel", "alexander", "philipp"]
femaleName = ["silke", "daniela", "maria", "bianca"]

if(male):
    name = random.choice(maleNames)
else:
    name = random.choice(femaleName)

print(name)

male = not male

if(male):
    name = random.choice(maleNames)
else:
    name = random.choice(femaleName)

print(name)
```

Ausgabe:
```bash
daniela
stephan
```

Hier setzen wir den Wert von `male` mitten im Programm auf den "invertierten Wert" `male = not male` (dies macht
aus `True` dann `False` und aus `False` eben `True`) und führen das Programm nochmal aus. Etwas unschön ist hier
die doppelung unseres Codes für den zweiten Aufruf. Das ist genau wo `Funktionen` und das leben etwas vereinfachen
können.

## Funktionen

Wir haben bisher einige Funktionen genutzt die Python schon mitbringt, am häufigsten vermutlich `print`. Eine
Funktion sieht im Normalfall so aus, dass die einen Namen hat und keine, einen oder mehrere Parameter "übernimmt"
mit denen sie dann arbeiten kann. Diese Parameter sind nur in der Funktion verfügbar und auch neue Variablen
die wir in der Funktion nutzen sind nur dort Verfügbar, nicht im "global Scope". Dies stellt sicher, dass wir
in unserer "blackbox" nur das machen, wass von uns erwartet wird und nichts verändern was und nicht angeht.

### Definition

Funktionen in Python werden wie folgt definiert und aufgerufen:

```python
def printHallo():
  print("hallo")

def prefixPrint(text):
  print("AUSGABE: ", text)

printHallo()
prefixPrint("test")
```

Ausgabe:
```
hallo
AUSGABE: test
```

Hier definieren wir zwei Funktionen die einen beliebigen Namen haben können, wir entscheiden uns für `printHallo`
(welche keinen Parameter von "außen" übernimmt) und `prefixPrint` (welche einen Parameter von "außen" übernimmt
und den entsprechenden Wert in der Variable `text` zur Verfügung stellt). Danach rufen wir unsere Funktionen der
Reihe nach auf und erhalten unsere Ausgabe.

Beachtet, dass die Definition einer Funktion `def` ebenfalls einen "Block" eröffnet und alle Zeilen die darunter
eingerückt sind zur Funktion gehören. Beachtet ebenfalls, dass der Code in der Defintion nicht ausgeführt wird,
sondern dafür ein Aufruf der Funktion nötig ist. Probiert aus, wass passiert wenn ihr die Zeile `prefixPrint("test")`
entfernt.

Mit diesem Wissen können wir nun unser obiges Problem des doppelten Codes lösen:

```python
import random

def randomName(male):
    maleNames = ["stephan", "daniel", "alexander", "philipp"]
    femaleName = ["silke", "daniela", "maria", "bianca"]
    if(male):
        name = random.choice(maleNames)
    else:
        name = random.choice(femaleName)
    print(name)

randomName(True)
randomName(False)
```

Ausgabe:
```bash
alexander
bianca
```

Wir haben die Doppelung des Codes aufgelöst indem wir uns eine "blackbox" geschrieben haben, die
einfach nur von aussen wissen muss ob sie einen männlichen oder einen weiblichen Vornamen ausgeben
soll. Die neue Funktion rufen wir zweimal auf, mit unterschiedlichen Parametern, und erhalten
das gleiche Ergebnis wie im alten Beispiel.

Gleichzeitig haben wir alle "globalen Variablen" `male`, `maleNames` und `femaleNames` entfernt und
diese sind jetzt nur noch in der Funktion selber Verfügbar. Dies können wir testen wenn wir folgendes
Programm ausführen:

```python
import random

def randomName(male):
    maleNames = ["stephan", "daniel", "alexander", "philipp"]
    femaleName = ["silke", "daniela", "maria", "bianca"]
    if(male):
        name = random.choice(maleNames)
    else:
        name = random.choice(femaleName)
    print(name)

print(name)
print(maleNames)
```

Ausgabe:
```bash
Traceback (most recent call last):
  File "/home/stephan/Projects/others/python/lektion6/05_functions_randomname.py", line 12, in <module>
    print(name)
NameError: name 'name' is not defined
```

Python gibt uns einen Fehler aus und weist uns darauf hin, dass die Variable `name` nicht definiert ist.
Dies ist der Fall, weil wir diese in unsere "blackbox" verschoben haben und damit der globale "Block"
nichts mehr von dieser Variable weiß. Das ist eine gute Sache...

### Rückgabewerte

Das obige Beispiel ist noch nicht wirklich sauber im Sinne der "seperation of concerns", unsere Funktion
sucht nicht nur einen zufälligen Namen aus den Listen, sondern gibt diesen auch noch aus. Das sind,
strenggenommen zwei Aufgaben die wir besser trennen wollen. Dazu hat Python die Möglichkeit Werte
aus einer Funktion zurückzugeben, sogenannte Rückgabewerte. Diese können dann weiterverarbeitet werden.

```python
import random

def prefixPrint(text):
  print("NAME:", text)

def randomName(male):
    maleNames = ["stephan", "daniel", "alexander", "philipp"]
    femaleName = ["silke", "daniela", "maria", "bianca"]
    if(male):
        name = random.choice(maleNames)
    else:
        name = random.choice(femaleName)
    return name

eins = randomName(True)
print(eins)
prefixPrint(randomName(False))
```

Ausgabe:
```bash
daniel
NAME: daniela
```

Man beachte das `return` als letzte Zeile der Funktion. Hier findet nun keine Ausgabe über `print` mehr
statt, sondern es wird der ermittelte Wert zurückgegeben und dem Aufrufer der Funktion überlassen
irgendwas damit anzufangen. Wir nutzen das direkt aus, indem wir einmal eine neue Variable damit befüllen
und diese über `print` ausgehen, und im zweiten Aufruf das Ergebnis direkt an unsere `prefixPrint`
Funktion übergeben um dort für die Ausgabe zu sorgen.

## Module / Libraries

Vielleicht benötigen wir jetzt ich mehreren Programmen immer wieder die `randomName` oder die `prefixPrint`
Funktion und haben keine Lust diese in jede Datei zu kopieren (oder Änderungen und Verbesserungen in jeder
Datei vorzunehmen). Hier bietet uns Python die Möglichkeit eine Library (bzw. ein Modul) zu schreiben, so
wie es die Entwickler von Pandas und matplotlib gemacht haben. Hierfür legen wir einfach eine seprate
Datei an und importieren diese in unserem Programm, dass die Funktionen nutzen soll:

helpers.py:
```python
import random

def prefixPrint(text):
  print("NAME:", text)

def randomName(male):
    maleNames = ["stephan", "daniel", "alexander", "philipp"]
    femaleName = ["silke", "daniela", "maria", "bianca"]
    if(male):
        name = random.choice(maleNames)
    else:
        name = random.choice(femaleName)
    return name
```

```python
import helpers

eins = helpers.randomName(True)
print(eins)
helpers.prefixPrint(helpers.randomName(False))
```

Ausgabe:
```bash
daniel
NAME: silke
```

Unser eigentliches Programm ist damit auf vier Zeilen geschrumpft und wir sind sogar das `import random` "losgeworden",
die Aufgabe (der "concern") irgendwie einen zufälligen männlichen oder weiblichen Namen zu finden ist jetzt vollends
an unsere Library übergegangen. Um diese zu Nutzen müssen wir die Datei (mit Ihrem namen ohne Erweiterung) `import`ieren
und jedem Aufruf einer Funktion den Namen der Library mit einem Punkt vorranstellen.

Auf diese weise könnt Ihr Euch für unterschiedliche Aufgaben einen "Werkzeugkasten" zusammenbauen der, zum Beispiel,
die Funktionen aus Lektion 5 enthält und als Library zur Verfügung stellt. Wenn Euch irgendwann eine bessere Methode
einfällt, Ihr einen Fehler findet oder einfach nur die Liste der möglichen Vornamen erweitern möchtet, könnt ihr das
in der `helper.py` machen und sofort in allen anderen Programmen die diese Library importieren nutzen.

Unser eigentliches Programm hat damit nur noch sehr wenige "concerns" und die "blackboxes" arbeiten im Hintergrund, 
nachvollziehbar und mit definierten Übergabewerten.

## Fazit

Wir haben in den letzten Wochen gelernt unsere Entwicklungsumgebung einzurichten, Python zu installieren,
externe Module über "pip" zu installieren. Wir haben einen kurzen Einblick in die Syntax von Python erhalten,
gelernt wie man "Blöcke" definiert und Abzweigungen und Schleifen erstellt. Ein paar Dateiformate und
Datenstrukturen haben wir kennengelernt und können mithilfe von Pandas diese ineinander umwandeln und
rudimentär verarbeiten und filtern. Mit matplotlib konnten wir dann einige Visualisierungen unseres
COVID-19 Datensatzes realisieren und die Daten mit Pandas auf unterschiedliche Weise filtern oder
modifizieren. In dieser Lektion haben wir noch ein bisschen "harte" Programmierung gelernt, um unsere
Programme besser zu strukturieren und für weitere Lektüre vorbereitet sein.

Eine völlig andere Art von Daten und Visualisierung habe ich kürzlich hier gefunden. Auch hier
wird Python nur zur Datenaufbereitung für ein anderes Vistualiserungstool genutzt:

[Creating Song Lyrics Graphs](https://onehundredairports.com/2020/06/13/creating-song-lyrics-graphs/)

Dieser Kurs kratzt sehr an der Oberfläche von dem was möglich ist und mein oberstes Ziel war es,
Euch als allererstes Ergebnisse zu präsentieren die mit sehr wenigen Zeilen Code auskommen, und dann
danach die Konzepte. Ich verweise nochmal auf die angesammelte Literatur auf der Hauptseite und
hoffe, dass ihr damit klarkommt.

In erster Linie hoffe ich Euch gezeigt zu haben, dass Programmierung kein Hexenwerk ist und Python
auch einfach eine weitere Sprache die man lernen kann. Vielleicht helfen euch die rudimentären
Erfahrungen aus diesem Kurs bei Eurem weiterem Studium, im Idealfall habt Ihr Lust auf mehr gekriegt
und bleibt am Ball.

Gerne hätte ich Euch alle persönlich kennengelernt und wäre etwas individueller auf Eure Fragen und
Probleme eingegangen...aber das hat wohl dieses Jahr einfach nicht sollen sein. Sollte sich, wider
erwarten, doch noch ein Termin für einen Termin vor Ort finden, melde ich mich umgehend bei Euch.
Dieser wäre dann selbstverständlich fakultativ und nur zur "Festigung" des gelernten.

Bis dahin freue ich mich auf Eure weiteren Fragen (bitte per Mail) und Eure Programme zum
Scheinerwerb.

Macht es gut, bleibt gesund!
