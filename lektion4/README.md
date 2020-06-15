# Lektion 4: Externe Bibliotheken, Daten vorformatieren, Graphen zeichnen

Hallo,

mit deutlicher Verspätung hier die nächste Lektion. In der vorherigen Lektion haben wir gelernt
wie wir Daten aus CSV-Dateien einlesen und als Text ausgeben.

Wir werden in dieser Lektion lernen wie wir mit Python Daten aufbereiten können
und unter Zuhilfenahme einer externen Bibliothek einen einfachen Graphen aus diesen Daten
zeichnen können.

Wir benutzen weiterhin die Datensätze zu COVID-19 aus den letzten Beispielen, wenn Ihr mögt,
könnt Ihr diese gerne aktualisieren. Ihr findet die aktuellen Daten hier:

[https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)
[https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv)

## Externe Bibliotheken

### PIP

Python stellt zur Installation von extenen Bibliotheken ein "Repository" zur Verfügung. Dieses lässt sich mit dem
Befehl `pip` nutzen.

Wenn Ihr die Schritte aus Lektion 1 befolgt habt, solltet Ihr eine Ausgabe kriegen, wenn Ihr in der Eingabeaufforderung
(Windows: Suchfeld: “cmd”, Mac: Spotlight “Terminal”) folgendes eingebt:

```bash
pip --version
```

Ausgabe (zum Beispiel):
```bash
pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)
```

Alternaiv könnt Ihr das "Terminal" von Visual Studio Code nutzen um den Befehl einzugeben. Ein neues Terminal öffnet Ihr
über das Menü "Terminal" > "New Terminal" in Visual Studio Code.

### Installation externer Libraries

Wir nutzen für unsere Beispiele zwei Bibliotheken die uns die Arbeit etwas einfacher machen `pandas` und `matplotlib`,
diese müssen über "pip" installiert werden. Hierzu nutzen wir wieder die Eingabeaufforderung von oben, oder das Terminal
von Visual Studio Code:

```bash
pip install pandas
```

Ausgabe (zum Beispiel):
```bash
Collecting pandas
  Using cached https://files.pythonhosted.org/packages/db/83/7d4008ffc2988066ff37f6a0bb6d7b60822367dcb36ba5e39aa7801fda54/pandas-0.24.2-cp27-cp27mu-manylinux1_x86_64.whl
Collecting numpy>=1.12.0 (from pandas)
  Downloading https://files.pythonhosted.org/packages/3a/5f/47e578b3ae79e2624e205445ab77a1848acdaa2929a00eeef6b16eaaeb20/numpy-1.16.6-cp27-cp27mu-manylinux1_x86_64.whl (17.0MB)
    100% |████████████████████████████████| 17.0MB 89kB/s 
Collecting pytz>=2011k (from pandas)
  Downloading https://files.pythonhosted.org/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl (510kB)
    100% |████████████████████████████████| 512kB 2.4MB/s 
Collecting python-dateutil>=2.5.0 (from pandas)
  Using cached https://files.pythonhosted.org/packages/d4/70/d60450c3dd48ef87586924207ae8907090de0b306af2bce5d134d78615cb/python_dateutil-2.8.1-py2.py3-none-any.whl
Collecting six>=1.5 (from python-dateutil>=2.5.0->pandas)
  Downloading https://files.pythonhosted.org/packages/ee/ff/48bde5c0f013094d729fe4b0316ba2a24774b3ff1c52d924a8a4cb04078a/six-1.15.0-py2.py3-none-any.whl
Installing collected packages: numpy, pytz, six, python-dateutil, pandas
Successfully installed numpy-1.16.6 pandas-0.24.2 python-dateutil-2.8.1 pytz-2020.1 six-1.15.0
```

```bash
pip install matplotlib
```

Ausgabe (zum Beispiel):
```bash
Collecting matplotlib
  Downloading https://files.pythonhosted.org/packages/9d/40/5ba7d4a3f80d39d409f21899972596bf62c8606f1406a825029649eaa439/matplotlib-2.2.5-cp27-cp27mu-manylinux1_x86_64.whl (12.8MB)
    100% |████████████████████████████████| 12.8MB 109kB/s 
Collecting cycler>=0.10 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Collecting numpy>=1.7.1 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/3a/5f/47e578b3ae79e2624e205445ab77a1848acdaa2929a00eeef6b16eaaeb20/numpy-1.16.6-cp27-cp27mu-manylinux1_x86_64.whl
Collecting backports.functools-lru-cache (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/da/d1/080d2bb13773803648281a49e3918f65b31b7beebf009887a529357fd44a/backports.functools_lru_cache-1.6.1-py2.py3-none-any.whl
Collecting subprocess32 (from matplotlib)
Collecting kiwisolver>=1.0.1 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/3d/78/cb9248b2289ec31e301137cedbe4ca503a74ca87f88cdbfd2f8be52323bf/kiwisolver-1.1.0-cp27-cp27mu-manylinux1_x86_64.whl
Collecting pytz (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl
Collecting six>=1.10 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/ee/ff/48bde5c0f013094d729fe4b0316ba2a24774b3ff1c52d924a8a4cb04078a/six-1.15.0-py2.py3-none-any.whl
Collecting python-dateutil>=2.1 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/d4/70/d60450c3dd48ef87586924207ae8907090de0b306af2bce5d134d78615cb/python_dateutil-2.8.1-py2.py3-none-any.whl
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/8a/bb/488841f56197b13700afd5658fc279a2025a39e22449b7cf29864669b15d/pyparsing-2.4.7-py2.py3-none-any.whl (67kB)
    100% |████████████████████████████████| 71kB 5.8MB/s 
Collecting setuptools (from kiwisolver>=1.0.1->matplotlib)
  Downloading https://files.pythonhosted.org/packages/e1/b7/182161210a13158cd3ccc41ee19aadef54496b74f2817cc147006ec932b4/setuptools-44.1.1-py2.py3-none-any.whl (583kB)
    100% |████████████████████████████████| 583kB 1.8MB/s 
Installing collected packages: six, cycler, numpy, backports.functools-lru-cache, subprocess32, setuptools, kiwisolver, pytz, python-dateutil, pyparsing, matplotlib
Successfully installed backports.functools-lru-cache-1.6.1 cycler-0.10.0 kiwisolver-1.1.0 matplotlib-2.2.5 numpy-1.16.6 pyparsing-2.4.7 python-dateutil-2.8.1 pytz-2020.1 setuptools-44.1.1 six-1.15.0 subprocess32-3.5.4
```

### Libraries nutzen

Wir können nun die beiden Biblotheken in unseren Programmen nutzen, und zum Beispiel das lesen und ausgeben der
CSV-Daten von letzter Woche etwas anders gestalten, indem wir `pandas` benutzen:

```python
import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
print(csv)
```

Ausgabe (Auszug):
```bash
                       Province/State          Country/Region        Lat        Long  1/22/20  1/23/20  1/24/20  1/25/20  1/26/20  1/27/20  1/28/20  1/29/20  1/30/20  1/31/20  2/1/20  2/2/20  ...  5/12/20  5/13/20  5/14/20  5/15/20  5/16/20  5/17/20  5/18/20  5/19/20  5/20/20  5/21/20  5/22/20  5/23/20  5/24/20  5/25/20  5/26/20  5/27/20
0                                 NaN             Afghanistan  33.000000   65.000000        0        0        0        0        0        0        0        0        0        0       0       0  ...      610      648      691      745      745      778      801      850      930      938      996     1040     1075     1097     1128     1138
1                                 NaN                 Albania  41.153300   20.168300        0        0        0        0        0        0        0        0        0        0       0       0  ...      682      688      694      705      714      715      727      742      758      771      777      783      789      795      803      812
2                                 NaN                 Algeria  28.033900    1.659600        0        0        0        0        0        0        0        0        0        0       0       0  ...     2998     3058     3158     3271     3409     3507     3625     3746     3968     4062     4256     4426     4784     4747     4918     5129
3                                 NaN                 Andorra  42.506300    1.521800        0        0        0        0        0        0        0        0        0        0       0       0  ...      568      576      596      604      615      617      624      628      639      639      652      653      653      663      676      676
4                                 NaN                  Angola -11.202700   17.873900        0        0        0        0        0        0        0        0        0        0       0       0  ...       13       14       14       17       17       17       17       17       17       17       17       18       18       18       18       18
5                                 NaN     Antigua and Barbuda  17.060800  -61.796400        0        0        0        0        0        0        0        0        0        0       0       0  ...       19       19       19       19       19       19       19       19       19       19       19       19       19       19       19       19
6                                 NaN               Argentina -38.416100  -63.616700        0        0        0        0        0        0        0        0        0        0       0       0  ...     1862     2266     2385     2497     2534     2569     2625     2872     2933     3032     3062     3530     3732     3999     4167     4349
...
```

Ihr seht hier schon, dass "pandas" uns selbst bei der einfachen Textausgabe schon ein paar Arbeitsschritte erleichtert.
So werden die Daten beispielsweise schon "bündig" dargestellt und sind etwas übersichtlicher. Auch die erste Zeile hat
"pandas" richtigerweise als Spaltenbezeichnungen erkannt und nutzt diese richtig.

Gleichzeitig erhalten wir eine Zeilennummer automatisch mitgeliefert. Wenn wir diese nicht brauchen oder die Daten anders
abfragen wollen, können wir "pandas" sagen, dass wir ein anderes Feld als den "Index" für diese Tabelle nutzen wollen.
Wir probieren das aus mit "Country/Region":

```python
import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv', index_col='Country/Region')
print(csv)
```
Ausgabe (Auszug):
```bash
                                          Province/State        Lat        Long  1/22/20  1/23/20  1/24/20  1/25/20  1/26/20  1/27/20  1/28/20  1/29/20  1/30/20  1/31/20  2/1/20  2/2/20  2/3/20  2/4/20  2/5/20  ...  5/10/20  5/11/20  5/12/20  5/13/20  5/14/20  5/15/20  5/16/20  5/17/20  5/18/20  5/19/20  5/20/20  5/21/20  5/22/20  5/23/20  5/24/20  5/25/20  5/26/20  5/27/20
Country/Region                                                                                                                                                                                                     ...                                                                                                                                                                  
Afghanistan                                          NaN  33.000000   65.000000        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...      558      558      610      648      691      745      745      778      801      850      930      938      996     1040     1075     1097     1128     1138
Albania                                              NaN  41.153300   20.168300        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...      650      654      682      688      694      705      714      715      727      742      758      771      777      783      789      795      803      812
Algeria                                              NaN  28.033900    1.659600        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...     2678     2841     2998     3058     3158     3271     3409     3507     3625     3746     3968     4062     4256     4426     4784     4747     4918     5129
Andorra                                              NaN  42.506300    1.521800        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...      550      550      568      576      596      604      615      617      624      628      639      639      652      653      653      663      676      676
Angola                                               NaN -11.202700   17.873900        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...       13       13       13       14       14       17       17       17       17       17       17       17       17       18       18       18       18       18
Antigua and Barbuda                                  NaN  17.060800  -61.796400        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...       19       19       19       19       19       19       19       19       19       19       19       19       19       19       19       19       19       19
Argentina                                            NaN -38.416100  -63.616700        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...     1757     1837     1862     2266     2385     2497     2534     2569     2625     2872     2933     3032     3062     3530     3732     3999     4167     4349
```

Hier sehen wir, dass die Daten entsprechend "umformatiert" wurden und jetzt "Country/Region" die erste Spalte ist. Dies kann praktisch sein um
ein bisschen Übersicht über die vorliegenden Daten zu erhalten.

Probiert andere Werte für `index_col` aus und schaut wie sich Eure Ausgabe ändert.

## Graphen zeichnen

Mit der installierten Bibliothek `matplotlib` können wir einfache Graphen, aber auch komplexere Visualisierungen von Daten zeichnen. Wir
versuchen das erstmal mit "zufälligen" Daten, um das Prinzip zu verstehen:

```python
import math
import matplotlib.pyplot as plt

daten = range(10)
plt.plot(daten, [math.pow(x, 2) for x in daten])
plt.show()
```

Die Ausgabe sollte der Graph einer quadratischen Funktion sein. Der Exponent der Funktion ist definiert mit 2, in der Zeile:

```python
plt.plot(X, [math.pow(x, 2) for x in daten])
```

Diese Zeile zeichnet alle Element der Liste `daten` (die Zahlen von 1 bis 10) auf die X-Achse eines Graphen, und berechnent `math.pow(x, 2)` 
für jedes `x` der Elemente der Liste `daten` um damit den entsprechenden Wert auf der Y-Achse abzutragen.

Probiert aus die Zahl in `range` zu ändern, oder den Exponenten in `pow(x, 2)` und schaut an wie sich euer Graph verhält.

Weitere einfache Beispiele, auch für anderen Visualisierungen, findet Ihr [hier](https://matplotlib.org/3.2.1/tutorials/introductory/sample_plots.html).

### Pandas und matplotlib

Unsere nächste Aufgabe ist es "pandas" und "matplotlib" zu verheiraten und unsere Daten aus dem COVID-19 Datensatz irgendwie
darzustellen.

Wir versuchen die COVID-19 Fälle im Datensatz für eine Region tageweise anzuzeigen, das geht im Prinzip so:

```python
import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
country = csv[csv['Country/Region'] == 'Germany']
keys = country.keys()
keys = keys.drop(['Province/State', 'Country/Region', 'Lat', 'Long'])
data = country[keys].transpose()
data.plot()
plt.show()
```

Die Ausgabe zeigt den Verlauf der COVID-19 "Genesungen" in Deutschland. Aber schrittweise:

1. Zeilen filtern:

```python
country = csv[csv['Country/Region'] == 'Germany']
```

Über pandas filtern wir unsere Datensätze auf alle Zeilen in denen das Feld "Country/Region" dem Wert "Germany" entspricht.
Hier können wir jeden Verleich anstellen, der einen `True` oder `False` Wert ausgibt, wir könnten auf "Province/State" filtern,
oder auf "Latitude" oder "Longitude". Probiert es aus, vor allem was passiert wenn der Vergleich mehr als eine Zeile ausgibt (`csv[csv['5/10/20'] > 500]`).

2. Spalten filtern

```python
keys = country.keys()
keys = keys.drop(['Province/State', 'Country/Region', 'Lat', 'Long'])
data = country[keys].transpose()
```

Für unsere Analyse interessieren uns nur die Daten der eigentlichen Tage, der Name sowie der Ort der Regions ist uns erstmal
egal. Wir filtern diese Spalten also aus dem Datensatz heraus und weisen die gefilterte Tabelle einer neuen Variable `data` zu.
`.transpose()` dreht unsere Daten einmal um 90°, damit wir eine Zeile pro Tag nachen, nicht eine Spalte pro Tag. Das macht
es "mathplotlib" einfacher die Daten abzuzeichnen. Probieren Sie aus, was passiert wenn die weniger Spalten filtern, oder mehr.

3. Daten anzeigen

```python
data.plot()
plt.show()
```

Wir zeichnen den Graph und weisen "matplotlib" an den letzten gezeichneten Graph anzuzeigen. Könnt Ihr die Werte von anderen
Ländern anzeigen? (Tip: guckt Euch den Vergleich in Zeile 5 an).

## Fazit

Soviel für diese Lektion. Guckt Euch die Hinweise und "Aufgaben" der einzelnen Codesschnipsel an, spielt einfach etwas
herum. Wenn Ihr glaubt es verstanden zu haben, guckt Euch [hier](https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot) um,
die Beispiele sind deutlich komplexer, aber versucht Euch vielleicht mit "copy paste" durchzuhangeln.

Wenn in den Beispielen die Rede ist von "Dataframes", dann ist das der Datentyp den wir in `csv` speichern, "Series" sind
das was wir am Ende in `data` speichern.

Guckt doch vielleicht auch mal, ob Ihr die Daten auf einen aktuellen Stand bringen könnt mit den Links in der Einleitung,
oder ob ihr statt den "Genesungen" den Datensatz für "Infektionen" oder "Todesfälle" so aufbereitet kriegt, dass Ihr auch
hiermit einen Graphen für ein ausgewähltes Land zu zeichnen.

In der nächsten Lektion versuchen wir mit den Daten zu rechnen (Durchschnittswerte ermitteln, ...) und die ein oder andere
weitere Datestellungsart für Daten zu finden.

Wie immer: Bei Fragen, fragen!
