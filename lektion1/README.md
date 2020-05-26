# Lektion 1: Setup Entwicklungsumgebung und "Hello World"

Hallo,

ich hoffe Ihr hattet einen angenehmen Start ins das Semester, seid gesund und wollt was lernen. In der ersten Woche wird die Aufgabe sein, 
sich die Entwicklungsumgebung und den Python-Interpreter zu installieren, einzurichten und dazu zu nutzen ein erstes Programm in Python 3 
zu schreiben, das “Hello World”. Aber vorher ein paar Begriffe:

## Warum Programmieren, warum Python?

Ihr habt mit dem Computer, Euren Handy, euren Tablet, Smartwatch, Spielkonsolen, Saugrobotern, Smart-Home-Devices oder auch nur 
Alltagsgeräten wie einem modernen Kühlschrank vermutlich die mächtigste Erfindung der Menschheit in der Hand: eine Maschine die 
tut was man Ihr sagt. Mit ein paar Einschränkungen: Es muss logisch sein, und es muss in einer Sprache sein welche die Maschine versteht. 
Da Maschinensprache zu schwer und kaum lesbar ist, suchen wir uns eine andere Sprache (eigentlich eher einen Dialekt) und lassen 
“irgendwen” übersetzen.

## Was ist eine Entwicklungsumgebung?

Als Entwicklungsumgebung bezeichnet man ein Programm dass beim Schreiben von Software hilft. In den meisten Fällen beinhaltet es einen 
Texteditor sowie ein paar Hilfsprogramme für den “Buildprozess” oder “Versionskontrolle”. Man kann sich eine Entwicklungsumgebung vorstellen wie 
“Word für Leute die Programme statt Bücher schreiben”. Wir werden in den nächsten Wochen “Visual Studio Code” von Microsoft benutzen, 
welches kostenlos für alle gängigen Betriebssysteme verfügbar ist und Unterstützung für eine Vielzahl an Programmiersprachen bereitstellt, 
unter anderem Python.

## Interpreter? Buildprozess? Versionskontrolle?

Weil Maschinensprache für den Menschen schwer zu lesen und zu schreiben ist, gibt es Programme die aus (etwas besser) lesbarer Sprache 
dann wieder Maschinensprache erstellen, quasi ein Übersetzer. Sogenannte Interpreter oder Compiler. Python ist dann nur noch ein “Dialekt” 
den wir uns als hübsch und recht einfach ausgesucht haben um ihn zu lernen. Dieser Übersetzungsjob ist Teil des “Buildprozesses”, 
zu Versionskontrolle kommen wir später...es geht im groben darum, dass man Dinge rückgängig machen kann.

Wer das alles etwas weniger langweilig erklärt haben möchte, kann sich ca. 30 Minuten (bei vorhandenem Netflix-Account) [“Explained - Programmieren”](https://www.netflix.com/watch/81097620) angucken. 

Aber jetzt geht’s los:

Für die Eiligen:

Wir folgen ziemlich genau diesem Vorgehen auf der “Visual Studio Code” (vscode) Seite

[https://code.visualstudio.com/docs/python/python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial) bis zu dem Punkt “Configure and run the debugger”.

Aber Schritt für Schritt:

Ladet Euch “Visual Studio Code” herunter (für Windows/OSX/Linux):

[https://code.visualstudio.com/](https://code.visualstudio.com/)

Startet den heruntergeladenen “Installer”, wartet ein paar Minuten und startet “Visual Studio Code”

Das sollte dann, in etwa, so aussehen:

![](<https://code.visualstudio.com/assets/docs/getstarted/tips-and-tricks/welcome_page.png>)

Jetzt brauchen wir einen Python-Interpreter von <https://www.python.org/downloads/> welchen wir ebenfalls installieren. 
Alternativ kann man unter Windows 10 den “Windows Store” nutzen um Python zu installieren. Wenn man nach einer Version gefragt wird, 
sollte immer “Python 3.8” gewählt werden (manchmal noch mit einer weiteren Nummer versehen, z.b. 3.8.2)

Nach der Installation sollten wir in einer Eingabeaufforderung (Windows: Suchfeld: “cmd”, Mac: Spotlight “Terminal”) 
folgendes eingeben können und eine vernünftige Ausgabe kriegen:

Windows: `py -3 --version`
OSX/Linux: `python3 --version`

Nun installieren wir die Python Unterstützung für “Visual Studio Code”: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>

Dazu sollte es ausreichen “vscode” zu öffnen, cmd/ctr/strg-p zu drücken, in das sich öffnende Eingabefeld folgendes einzufügen und auf Enter zu drücken:

`ext install ms-python.python`

Ungefähr so:

Nun legt Euch einen Ordner auf der Festplatte an in der Euer Code liegen soll und öffnet diesen in “vscode” über “File > Open Folder”.

Danach wählen wir noch den Python-Interpreter aus, indem wir cmd/ctrl/strg-shift-p drücken und “Python: Select Interpreter” eingeben, 
bzw. auswählen sobald die Option angezeigt wird.

Im darauffolgenden Feld wählen wir den gerade heruntergeladenen und installierten Python-Interpreter aus. Und können, hoffentlich, 
endlich anfangen zu programmieren:

![](<https://code.visualstudio.com/assets/docs/python/tutorial/toolbar-new-file.png>)

In der Dateianzeige klicken wir auf das Icon für “Neue Datei” und geben der neuen Datei einen Namen:

![](<https://code.visualstudio.com/assets/docs/python/tutorial/hello-py-file-created.png>)

Python-Dateien haben im Normalfall die Dateiendung .py und vscode hilft uns etwas beim schreiben von Python wenn es anhand der Endung
 erkennt, dass es sich um eine .py Datei handelt.

Nun fügen wir folgenden Inhalt in die neue Datei (geöffnet auf der rechten Seite) ein. Zwischendurch wird Euch vscode etwas “nerven” mit Vorschlägen 
und Hinweisen, einfach weitertippen...Ihr werdet das noch schätzen lernen.

```python
msg = "Hello World"
print(msg)
```

Nachdem wir die Datei mit cmd/ctrl/strg-s gespeichert haben können wir oben rechts im Editor auf das “Play”-Symbol klicken und es ausführen. 

![](<https://code.visualstudio.com/assets/docs/python/tutorial/run-python-file-in-terminal-button.png>)

Es wird sich ein “Terminal” öffnen, dass den Python-Interpreter aufruft, welcher unser neues Programm ausführt. Das sieht dann so aus:

![](<https://code.visualstudio.com/assets/docs/python/tutorial/output-in-terminal.png>)

Herzlichen Glückwunsch! Wenn das alles geklappt hat, habt ihr gerade der mächtigsten Erfindung der Menschheit gesagt was sie zu tun hat. 
Stark!

Sollte irgendwas nicht geklappt haben, Ihr irgendwas nicht verstehen oder ich irgendwo Mist geschrieben haben. Schreibt bitte hier im Forum. 
Ich versuche mir das einmal am Tag, vermutlich Abends, anzugucken und zu antworten...vielleicht kann aber ja auch bereits ein Kommilitone helfen.

Wer am Wochenende nichts zu tun hat, möchte vielleicht hier weitermachen:

<https://nealcaren.github.io/python-tutorials/>
