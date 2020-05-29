# **Lektion 2: Logik, Datentypen, Kontrollstrukturen**

Hallo,

nachdem wir in der letzten Lektion unsere Entwicklungsumgebung eingerichtet und unser erstes kleines Programm geschrieben haben, 
geht es dieses Mal etwas mehr in die Tiefe. Wir werden lernen wie Programmiersprachen es schaffen dem Computer zu befehlen was er 
machen soll und was wir tun müssen damit das funktioniert. Dafür müssen wir ein paar Sachen lernen: Syntax, Logik, Datenstrukturen. 

Aber der Reihe nach:

## **Syntax**

Die Syntax einer Programmiersprache sind die sprachlichen Regeln an die wir uns halten müssen um korrekte Anweisungen zu schreiben. 
Wir erinnern uns an unser erstes Programm:

```python
msg = "Hello World"
print(msg)
```

Was genau passiert hier? In der ersten Zeile weisen wir der *Variable* "msg" den *Wert* "Hello World" zu. In der zweiten Zeile rufen 
wir die *Funktion* "print" mit der *Variable* als *Parameter* auf. Doch was genau heissen diese ganzen Begriffe?

## **Variablen und Zuweisung**

In python, wie in fast jeder anderen Programmiersprache, können selbst gewählten Variablen Werte zugewiesen werden. Die Variable ist 
hierbei wie ein "Speicher" für den Wert. Der Inhalt von Variablen kann sich ändern und entspricht im Normalfall einem *Datentyp* 
(dazu später mehr, in diesem Fall ist der Datentyp ein "String", eine Zeichenkette).

Inhalte von Variablen können geändert werden, wir können mit Inhalten von Variablen rechnen oder Aussagen treffen über den Inhalt/Wert 
der Variable.

In unserem Beispiel können wir das verändern des Wertes einer Variable einfach testen:

```python
msg = "Hello World"
msg = "Hallo Welt"
print(msg)
```

Ausgabe:
```
Hallo Welt
```

Die Ausgabe dieses Programms wird "Hallo Welt" sein, da wir den initialen Wert der Variable "Hello World" in der zweiten Zeile direkt 
ändern und dann den geänderten Wert an "print" geben (welches eine *Funktion* ist, die für die Ausgabe auf dem BIldschirm zuständig ist).

Ein paar andere mögliche Variablenzuweisungen in Python sind die folgenden:

```python
x = 4.2
y = x / 2
x += 4
x, y = True, False
x = not x and y
a = ["hello", x, 3]
b = a[0]
c = b[4]
y = not a[1]
```

Wir kommen später zu den etwas "komplexeren" Zuweisungen. In den ersten drei Zeilen sehen wir, dass wir auch bestehende Werte von Variablen 
modifiziert an andere Variablen zuweisen können. Wenn wir unser Programm wie folgt modifizieren:

```python
x = 4
msg = x / 2
print(msg)
```

Ausgabe:
```
2.0
```

Erhalten wir eine Ausgabe von "2". Probieren sie aus, was hiermit möglich ist. Ändern sie den Wert von *x*, ändern sie die "2" in der 
zweiten Zeile in eine andere Zahl und führen Sie jeweils das Programm aus um die Ausgabe zu betrachten. Führen sie ggf eine dritte 
Variable ein, oder versuchen sie zwei Ausgaben zu erzeugen.

## **Imperative Programmierung**

Python folgt hier, wie die meisten populären Programmiersprachen, den Anweisungen Zeile für Zeile. Eine Anweisung die nach einer 
anderen kommt wird auch nach dieser ausgeführt. Wir sehen das daran, dass wir den Wert einer Variable überschreiben und ändern 
können. Ein kurzer versuch eine Variable nachträglich zu ändern wird fehlschlagen:

```python
x = "Hallo"
print(x)
x = "Auf Wiedersehen!"
```

Ausgabe:
```
Hallo
```

Wird weiterhin "Hallo" ausgeben, da die "print" Anweisung vor der Änderung der Variable stattfindet. Wir lernen später Möglichkeiten 
das etwas "aufzuweichen" aber der Ablauf eines Programms bleibt immer "von oben nach unten".

## **Logik**

In jeder Programmiersprache gibt es ein Konzept von "Wahrheit", welches sich im Normalfall in sogenannten "booleschen Ausdrücken" 
manifestiert. Python hat hierfür die Schlüsselwörter *True* und *False* reserviert mit denen wir die Richtigkeit bestimmter Überprüfungen 
feststellen können. Python bietet uns zum Vergleich von Variablenwerten verschiedene Vergleichsoperatoren, z.B.:

```python
== (gleich)
< (kleiner als)
\> (größer als)
=> (größer oder gleich)
<= (kleiner oder gleich)
```

Die Syntax dieser Vergleichsoperatoren sollte aus der Mathematik bekannt sein. Wichtig ist hier zu beachten, dass das "=" in den meisten 
Programmiersprachen für die Zuweisung von Werten zu Variablen benutzt wird, während zum Vergleich der Werte "==" zum Einsatz kommt.

Wir können nun unser kleines Programm weiter anpassen um ein paar Wahrheitswerte zu testen:

```python
x = 4
y = 5
msg = x == y
print(msg)
```

Ausgabe:
```
False
```

Die Ausgabe dieses Programms wird "False" sein, da "4 nicht gleich 5" ist. Versuchen Sie unterschiedliche Werte für die Variablen 
einzusetzen, probieren sie in Zeile drei andere Vergleichsoperatoren aus, führen Sie das Programm aus und gucken Sie ob die Ausgabe 
mit Ihren Erwartungen übereinstimmt.

## **Kontrollstrukturen**

Mit den gerade kennengelernten Wahrheitswerten können wir nun über ein paar einfache Kommandos den "Fluss" unseres Programms steuern. 
Das Programm wird weiterhin von "oben nach unten" ausgeführt, wir haben jedoch die Möglichkeit einzelne Befehle zu "überspringen" oder 
auch diese zu wiederholen. Hierzu benötigen wir ein paar weitere Kommandos und ein bisschen mehr wissen über die Syntax die Python 
von uns verlangt. Die Kommandos sind:

**if**
**elif**
**else**
**while**
**for**

Jeder dieser Befehlen öffnet in Python einen "Block" in dem etwas Ausgeführt wird, oder auch nicht. 

##### *Konditionen*

Wir verändern unser Programm minimal, die Einrückung des Aufrufs von "print" ist wichtig und kann über das drücken von "Tab" (die 
Taste links neben dem Q auf einer deutschen Tastatur).

```python
x = 4
y = 4
if (x == y):
    print("passt!")
```

Ausgabe:
```
passt!
```

Diese Programm wird "passt!" ausgeben. Probieren sie andere Werte für *x* und *y* sowie andere Vergleichsoperatoren in Zeile drei. 
Modifizieren sie danach das Programm wie folgt und probieren ebenfalls aus was mit unterschiedlichen Weten für *x* und *y* passiert:

```python
x = 4
y = 4
if (x == y):
    print("passt!")
else:
    print("passt nicht!")
```

Ausgabe (ohne Änderungen):
```
passt!
```

Über "if" und "else" haben wir Einfluss genommen in den Ablauf unseres Programmen, wir können Abzweigungen erschaffen und damit "Fälle" 
unterschiedlich behandeln wenn wir später Daten einlesen und verarbeiten wollen. Der Vollständigkeit halber sei hier auch noch "elif" 
(kurz für "else if") zum weiteren Ausprobieren vorgestellt:

```python
x = 4
y = 5
if (x == y):
  print("gleich")
elif (x > y):
  print("x größer")
else:
  print("y größer")
```

Ausgabe:
```
y größer
```

Achten Sie auf die Einrückung, probieren sie folgendes aus:

```python
x = 4
if (x == 5):
  print("hä?")
print("ende des programms")
```

Ausgabe (ohne Änderungen):
```
ende des programms
```

Hier wird, trotz der Abfrage in Zeile zwei, der Befehl in der letzten Zeile immer ausgeführt. Die Einrückung auf Zeile drei endet 
auch direkt wieder und damit "fällt die letzte Zeile nicht in die Überprüfung", das geht auch mit mehreren Befehlen, die alle 
gleich Eingerückt sind:

```python
x = 4
if (x == 5):
  print("hä?")
  print("irgendwas ist faul")
print("ende des programms")
```

Ausgabe (ohne Änderungen):
```
ende des programms
```

#### **Schleifen**

Auf die gleiche Weise können wir unserem Programm befehlen Dinge zu wiederholen. Hier unterscheiden wir in zwei Arten Dinge zu
 wiederholen. "Mache etwas solange eine Überprüfung wahr ist" und "mache etwas eine vorgegebene Anzahl häufig". 
 
 Hierfür gibt es zwei Befehle:

**while**
**for**

Beide Befehle arbeiten mit Wahrheitswerten (True und False) oben als "Abbruchbedingung" und wiederholen alles in ihrem entsprechenden 
*Block* bis diese False ist, danach wird das Programm normal weiter ausgeführt. 

Wenn wir das nun in unser Programm einbauen wollen, sähe das z.B. so aus:

```python
x = 0
while (x < 5):
  print(x)
  x = x + 1
print("fertig")
```

Ausgabe:
```
0
1
2
3
4
fertig
```

Der Befehl "while" funktioniert hier ähnlich wie das "if" oben und überprüft den Wahrheitswert des Vergleiches. Ist dieser "True", wird der 
Block ausgeführt. Ist dieser nicht (mehr) "True" (sondern "False") wird der Block übersprungen und mit dem Programm nach dem Block 
fortgefahren. Der Unterschied zu "if" besteht darin, dass der Block **solange** ausgeführt wird **bis** der Vergleich "False" ergibt.

In unserem Beispiel überprüfen wir, ob der Wert der Variable "x" kleiner als 5 ist. Solange das der Fall ist, wird der Block ausgeführt. 
Wir geben den aktuellen Wert von "x" aus und erhöhen diesen, in Zeile vier, um eins. Irgendwann wird also der Wert von "x" nicht mehr 
"kleiner als 5" sein, und der Block nicht mehr ausgeführt. Danach geben wir "fertig" aus.

Das obige Programm zählt also von 0 bis 4 und gibt dann "fertig" aus. Probieren sie andere Vergleiche (insbesondere "==" ... das Programm 
kann mit Strg/Ctrl/Cmd-C abgebrochen werden), andere Startwerte für "x" und andere Werte für "+ 1" und gucken was passiert.

Die oben vorgestellte "while schleife" wird häufig benutzt um Daten zu verarbeiten. Übliche Anwendungsfälle sind z.B. das zeilenweise 
Einlesen einer Datei ("solange es eine weitere Zeile in der Datei gibt, lese diese ein und mache was mit den eingelesenen Daten").

Wenn uns die *Elemente* einer *Liste* einzeln interessieren, bietet uns Python die "for schleife" um über diese zu "iterieren". Dies kann 
bei der Datenverarbeitung praktisch sein um z.B. einzelne Zellen aus einer Tabelle auszulesen.

Wir modifizieren unser Programm also wieder mal ein bisschen (Sie haben auch die Möglichkeit sich für jedes dieser Beispiele eine eigene 
Datei (if.py, while.py, test.py, ...) anzulegen und diese jeweils separat auszuführen):

```python
for i in ["montag", "dienstag", "mittwoch"]:
  print(i)
print("fertig")
```

Ausgabe:
```
montag
dienstag
mittwoch
fertig
```

Diese Programm wird in der Ausgabe von "montag" bis "mittwoch" und danach "fertig" ausgeben. Warum?

"["montag", "dienstag", "mittwoch"]" erstellt uns eine *Liste* (mehr dazu gleich) mit den *Werten* "montag", "dienstag" und "mittwoch". 
"for i" führt den Block aus und speichert in "i" das aktuelle *Element* der *Liste*. Bei jedem Durchlauf wird das nächste Element der Liste in "i" 
gespeichert und in "print(i)" ausgegeben. Hat die *Liste* kein *Element* mehr wird der Block nicht ausgeführt und das Programm in der nächsten 
Zeile fortgesetzt.

Probieren Sie die Liste zu erweitern, zu verkürzen, andere Werte einzubauen...

## **Datentypen**

Zum Schluss ein kleiner Exkurs zum Thema "Datentypen" als Vorgriff auf die nächste Lektion.

Python ist eine typisierte Sprache, aber "dynamisch typisiert". Was sind diese Typen und warum interessiert uns das?

Wir haben die drei wichtigsten Datentypen für uns bereits kennengelernt: String, Integer, List. Was ist der Unterschied?

### **String**

Ein "String" ist eine "Zeichenkette" die Buchstaben enthält und auf die man bestimmte Operatoren für Zeichenketten anwenden kann. Ein paar Beispiele:

Ausgabe der Anzahl der Buchstaben in einem Wort:

```python
print(len("hund"))
```

Verbinden zweier Zeichenketten:

```python
print("hund" + "katze")
```

Vergleich zweier Zeichenketten:

```python
print("hund" == "katze")
```

Ausgabe:
```
4
hundkatze
False
```

Was Zeichenketten nicht "können" sind mathematisch Operationen oder Vergleiche:

```python
print("hund" < 5)
```

```python
print("hund" / 2)
```

### **Integer**

Ein "Integer" ist eine mathematische "Ganzzahl", also ohne Nachkommastellen, und erlaubt mathematische Operationen und Vergleiche:

```python
print(4 / 2)
```

```python
print(4 == 4)
```

Ausgabe:
```
2.0
True
```

Auch hier geht, wie oben schon dargestellt, ein Vergleich und Operationen mit "Strings" nicht.

```python
print("hund" + 4)
```

### **Listen**

Wie oben kennengelernt besteht eine Liste aus unterschiedlichen Elementen die, idealerweise, den gleichen Datentyp haben (also z.B. String oder Integer). 

Über Listen kann man "iterieren":

```python
for i in [1, 2, 3, 4]:
  print(i + i)
```

Ausgabe:
```
2
4
6
8
```

```python
for i in ["hund", "katze", "maus", "elefant"]:
  print(i)
  print(len(i))
```

Auch hier sind mathematische Operationen und Vergleiche, aber auch Operationen die für Zeichenketten gehen nicht zugelassen. 
Der Computer weiss einfach nicht, was er machen soll:

```python
print(["hund", "katze", "maus", "elefant"] / 2)
```
```python
print(["hund", "katze", "maus", "elefant"] + "test")
```

## **Fazit**

Soviel für diese Lektion. Wir haben Datentypen und Kontrollstrukturen kennengelernt und uns etwas mit Logik bekanntgemacht. 
Diese Lektion ist im Groben und Ganzen eine Überstzung von diesen Slides, auf denen es (zum weiterarbeiten) ein paar Übungen gibt:

<http://www.cltl.nl/files/2014/10/04_control_structures.pdf>

In der nächsten Lektion lernen wir Funktionen kennen und lesen ein paar vorgegebene Daten ein und spielen damit rum.

Bei Fragen, fragen!
