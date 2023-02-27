# Gesichts-Emotionserkennung
Angaben von Benni (NICHT selbst getestet!)
- deepface 0.0.75
- Python 3.8.10

Tested also with:
- Python 3.9.13


1. Python muss installiert sein
2. Deepface per pip installieren
    ```
    pip install deepface==0.0.75
    ```
3. Den Ordner öffnen, in der Python die Deepface Bibliothek abgelegt hat. Anschließend in der realtime.py den Code durch "replace in realtime" ersetzen.
    1. Versions abhängiges überschreiben kann Fehler verursachen!
4. Ordner mit database erstellen und ein Bild reinziehen (Kann ein beliebiges Bild sein, es muss jedoch ein Bild im Ordner hinterlegt sein)
    1. Image muss unbedingt eine JPEG-Image sein!!!
5. emotionlist.txt muss in database vorhanden sein!!!
6. server.py starten
7. startFaceDetection.py starten, um die Gesichts- und Emotionserkennung zu starten 

# Windows 10
Installation path of deepface:
```
C:\Users\{current user}\AppData\Roaming\Python\Python39\site-packages\deepface
```

# MacOS
Installation path of deepface:
```
/Users/{current user}/opt/anaconda3/lib/python3.9/site-packages/deepface/
```