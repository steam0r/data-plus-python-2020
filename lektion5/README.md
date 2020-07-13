# Lektion 5: Mehr Pandas, mehr matplotlib, mehr Graphen, Daten speichern

Hey,

in der letzten Lektion haben wir unter zuhilfenahme zweier externer Libraries (Pandas und matplotlib)
unseren COVID-19 Datensatz in einen (oder mehrere) einfache Graphen dargestellt.

Die Aufgabenverteilung der beiden Bibliotheken die wir benutzt haben ist im groben wie folgt:

Pandas ist für die Datenaufbereitung dar, damit wir brauchbare Datenstrukturen kriegen die
wir in Python weiterbenutzen können. Im Prinzip dass was wir in Lektion 3 noch "per Hand" mit
dem "csv.reader" gemacht haben.

matplotlib nimmt diese Daten an und kann dann über ein paar Parameter angewiesen werden hieraus
Graphen zu erstellen, also unsere Daten auszugeben. Im Prinzip haben wir auch das in Lektion 3
schon gemacht, indem wir die Daten einfach ge"print"ed haben.

Diese Aufteilung von Verantwortlichkeiten ist sinnvoll und wird in der Softwarearchitektur
allgemein als "seperation of concerns" bezeichnet. Wenn Pandas es schafft Daten irgendwie
aufzubereiten kann potentiell jede andere Bibliothek diese Daten annehmen und darstellen,
oder als PDF ausgeben, oder per Email verschicken...oder, oder, oder. Auch das haben wir
in Lektion 3 bereits gelernt als wir über "Datenformate" gesprochen haben.

Datenformate sind nicht nur Dateien die wir einlesen oder andere Daten, sondern eben auch
wie unterschiedliche Teile des Programmes miteinander sprechen. Mehr dazu aber in der nächsten
Lektion.

Die vorliegende Lektion könnt ihr für weitere Projekte gut als Basis zum Nachschlagen und
"rüberkopieren" Nutzen. Das meister hatten wir auch schonmal, daher etwas weniger Text.

## Mehr Pandas

Zum einfachen angucken der Daten, um herauszufinden was man überhaupt machen kann oder auch
und vor allem zum "debugging" (also der Fehlersuche) empfiehlt es sich immer wieder die
Daten einfach mal auszugeben und sich anzugucken. Dafür gibt es ein paar simple Funktionen in
Pandas.

### Die ersten fünf Datensätze

```python
import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
print(csv.head())
```

Ausgabe:
```bash
  Province/State Country/Region      Lat     Long  1/22/20  1/23/20  1/24/20  1/25/20  1/26/20  1/27/20  1/28/20  1/29/20  1/30/20  1/31/20  2/1/20  2/2/20  2/3/20  2/4/20  2/5/20  ...  5/9/20  5/10/20  5/11/20  5/12/20  5/13/20  5/14/20  5/15/20  5/16/20  5/17/20  5/18/20  5/19/20  5/20/20  5/21/20  5/22/20  5/23/20  5/24/20  5/25/20  5/26/20  5/27/20
0            NaN    Afghanistan  33.0000  65.0000        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...     502      558      558      610      648      691      745      745      778      801      850      930      938      996     1040     1075     1097     1128     1138
1            NaN        Albania  41.1533  20.1683        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...     627      650      654      682      688      694      705      714      715      727      742      758      771      777      783      789      795      803      812
2            NaN        Algeria  28.0339   1.6596        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...    2546     2678     2841     2998     3058     3158     3271     3409     3507     3625     3746     3968     4062     4256     4426     4784     4747     4918     5129
3            NaN        Andorra  42.5063   1.5218        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...     545      550      550      568      576      596      604      615      617      624      628      639      639      652      653      653      663      676      676
4            NaN         Angola -11.2027  17.8739        0        0        0        0        0        0        0        0        0        0       0       0       0       0       0  ...      13       13       13       13       14       14       17       17       17       17       17       17       17       17       18       18       18       18       18

[5 rows x 131 columns]
```

### Die letzten fünf Datensätze

```python
import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
print(csv.tail())
```

Ausgabe:
```bash
```

### Fünf zufällige Datensätze

```python
import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
print(csv.sample(5))
```

Ausgabe:
```bash
```

### Spalten einblenden und ausblenden

```python
import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
print(csv[['Lat', 'Long', '5/23/20']])
```

Ausgabe:
```bash
           Lat        Long  5/23/20
0    33.000000   65.000000     1040
1    41.153300   20.168300      783
2    28.033900    1.659600     4426
3    42.506300    1.521800      653
4   -11.202700   17.873900       18
5    17.060800  -61.796400       19
6   -38.416100  -63.616700     3530
7    40.069100   45.038200     2936
8   -35.473500  149.012400      104
9   -33.868800  151.209300     2653
10  -12.463400  130.845600       29
..         ...         ...      ...
243 -13.254308   34.301525       28
244 -51.796300  -59.523600       13
245  46.885200  -56.315900        1
246   6.877000   31.307000        6
247  24.215500  -12.885800        6
248   0.186360    6.613081        4
249  15.552727   48.516388       11
250 -11.645500   43.333300       18
251  38.861034   71.276093     1223
252 -29.609988   28.233608        0

[253 rows x 3 columns]
```

### Filtern

Nur Datensätze die am 23.05.2020 eine Zahl über 0 COVID-19 Heilungen hatten (`'5/23/20' > 0`):

```python
import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
date = csv[csv['5/23/20'] > 0]
print(date[['Province/State', '5/23/20']])
```

Ausgabe:
```bash
                       Province/State  5/23/20
0                                 NaN     1040
1                                 NaN      783
2                                 NaN     4426
3                                 NaN      653
4                                 NaN       18
5                                 NaN       19
6                                 NaN     3530
7                                 NaN     2936
8        Australian Capital Territory      104
9                     New South Wales     2653
10                 Northern Territory       29
..                                ...      ...
243                               NaN       28
244       Falkland Islands (Malvinas)       13
245         Saint Pierre and Miquelon        1
246                               NaN        6
247                               NaN        6
248                               NaN        4
249                               NaN       11
250                               NaN       18
251                               NaN     1223

[249 rows x 2 columns]
```


### Sortieren

Alle Datensätze die die am 23.05.2020 eine Zahl über 0 COVID-19 Heilungen hatten (`'5/23/20' > 0`),
sortiert nach eben diesem Wert (`sort_values(by...)`), absteigend sortiert (`ascending=False`),
nur die ersten 10.

Quasi eine Top 10 der COVID Heilungen am 23.05.2020:

```python
import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
date = csv[csv['5/23/20'] > 0]
sorted = date.sort_values(by=['5/23/20'], ascending=False)
print(sorted[['Country/Region', 'Province/State', '5/23/20']].head(10))
```

Ausgabe:
```bash
    Country/Region Province/State  5/23/20
225             US            NaN   361239
112        Germany            NaN   159716
199          Spain            NaN   150376
29          Brazil            NaN   142587
131          Italy            NaN   138840
213         Turkey            NaN   117602
184         Russia            NaN   107936
127           Iran            NaN   104072
53           China          Hubei    63616
108         France            NaN    62893
```

## Mehr matplotlib

Auch matplotlib gibt uns ein paar mehr Möglichkeiten mit den Daten die Pandas für uns aufbereitet hat
zu arbeiten. Hier ein paar Beispiele.

### Graphen speichern

Bisher haben wir unsere Graphen immer nur angezeigt, matplotlib kann uns auch Bilder generieren:

```python
import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
x = csv['Lat']
y = csv['5/23/20']

plt.scatter(x, y)
plt.show()
```

### Styling

Wir möchsten einen größeren Graphen zeichnen (`fisize`), unsere Achsen benennen (`xlabel` und `ylabel`),
die Schriftgröße der Achsenbeschriftung ändern (`fontsize`), die Linie rot machen (`color="red"`) und
auch dicker (`linewidth=3`):

```python
import math
import matplotlib.pyplot as plt

daten = range(10)
plt.figure(figsize=(10,10))
plt.xlabel("Alle X", fontsize=20)
plt.ylabel("Alle Y", fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.plot(daten, [math.pow(x, 2) for x in daten], color="red", linewidth=3)
plt.show()
```

### Schleifen

Wenn wir unser Wissen aus Lektion 2 anwenden können wir uns ein Unterverzeichnis "images" anlegen
(`os.makedirs`) und darein für jedes einzelne Land jeweils ein Bild mit dem Graphen der Daten
von diesem Land ablegen. Das Programm generiert also ca. 250 Bilder, das dauert etwas...

```python
import os
import pandas
import matplotlib.pyplot as plt

os.makedirs('images', exist_ok=True)
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
countries = csv['Country/Region']
for country in countries:
    data = csv[csv['Country/Region'] == country]
    print("plotting " + country + "...")
    data.plot()
    plt.savefig("images/" + country + "_covid19.png")

```

## Mehr Graphen

### Scatterplot

Anzahl der COVID-19 Heilungen am 23.05.2020 auf der Y-Achse und die "Latitude" auf
der X-Achse. Eine sehr simple Weise Geodaten zu visualisieren:

```python
import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
x = csv['Lat']
y = csv['5/23/20']

plt.scatter(x, y)
plt.show()
```

### Geodaten / Weltkarte

Hier nutzen wir "Longitude" und "Latitude" sowie ein Hintergrundbild als Weltkarte (könnt Ihr Euch aus
dem Verzeichnis zur Lektion bei github runterladen) um anzuzeigen welche Datensätze in der Datenbank
überhaupt vorkommen und wie diese verteilt sind. Die Werte für die "box" sind Minimal- und Maximalwerte
für Breiten und Längengrade. Die Daten passen nicht so ganz auf die Weltkarte, was vermutlich an der
Projektion der Karte liegt. Ein gutes Beispiel für andere Daten gibt es [hier](https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db).


```python
import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
data = csv[['Long', 'Lat']]

ruh_m = plt.imread('welt.png')
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(csv['Long'], csv['Lat'], zorder=1, alpha= 0.2, c='b', s=10)

box = (-180, +180, -90, 90)

ax.set_title('COVID-19 recoveries all over the worlds')
ax.imshow(ruh_m, zorder=0, extent = box, aspect= 'equal')
plt.show()

```

### Kuchendiagramm

Die Anzahl der COVID-19 Heilungen in Afganisten mit dem Stand von jedem Tag, als Kuchendiagramm.
Die Visualisierung ist recht "albern", da man sieht, dass die Daten scheinbar addiert sind, und
nicht die Heilungen an jedem einzelnen Tag. Eine gute Übung um zu sehen wie sich Daten aufbauen.
Vielleicht kriegt ihr es ja mit etwas Mathe hin nur den Anstieg pro Tag darzustellen.

```python
import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
country = csv[csv['Country/Region'] == 'Afghanistan']
keys = country.keys()
keys = keys.drop(['Province/State', 'Country/Region', 'Lat', 'Long'])
data = country[keys].transpose()
plt.pie(data,labels=keys,autopct='%1.1f%%')
plt.title('Afghanistan')
plt.axis('equal')
plt.show()
```

## Daten speichern

Wir können jederzeit die von uns verarbeiteten Daten auch wieder zurück in eine CSV-Datei speichern um sie dann
z.B. in Excel oder matplotlib einzulesen. Dazu nutzen wir einfach eine weitere Funktion von Pandas ``.

Für das Beispiel mit den "Top 10" oben, sieht das dann so aus:

```python
import pandas
csv = pandas.read_csv('time_series_covid19_recovered_global.csv')
date = csv[csv['5/23/20'] > 0]
sorted = date.sort_values(by=['5/23/20'], ascending=False)
data = sorted[['Country/Region', 'Province/State', '5/23/20']].head(10)
data.to_csv('top10.csv', index=False)  
```

Die Ausgabe ist eine Datei "top10.csv" die unsere gefilterten, sortierten Daten beinhaltet und
in Excel, R, SPSS oder auch in Python wieder eingelesen werden kann.

## Fazit

Wir haben gelernt Pandas und Matplotlib zu konfigurieren, Daten zu filtern, aufzubereiten und in unterschiedlichen
Formen und Farben auszugeben. Wenn Ihr in den letzten Lektionen meinen Aufforderungen zum "ausprobieren" gefolgt seid,
solltet Ihr in der Lage sein jeden Datensatz den Ihr irgendwie in das CSV Format konvertiert kriegt in irgendeinem
Graphen darzustellen. Nutzt hierfür die Pandas- und matplotlib-Dokumentation

Wir haben in diesem Kurs bisher recht wenig über Softwarearchitektur, Konzepte, Modelle und auch generell nicht
so viel Syntax gesprochen. In anderen Kursen fängt man damit an, relativ trockenes Thema und auch deutlich
abschreckend. Ich denke Ihr solltet in der Lage sein ein Python-Buch in die Hand zu nehmen und nicht komplett
unwissend zu sein wovon gesprochen wird. Auch hier: ausprobieren, Dinge kaputtmachen, Dinge reparieren.

Nichtsdestotroz wird die sechste (und letzte) Lektion sich ein bisschen mit diesen Dingen beschäftigen,
auch damit Dokumentation für Euch verständlicher ist. Das wird dann ein bisschen trocken, aber vieles von
dem was kommt haben wir (unwissend) schon genutzt.

Ich wünsche Euch bis dahin ein paar schöne Sommertage.

Und: Bei Fragen, fragen!
