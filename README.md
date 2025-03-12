# py_epub2hoerbuch
Erstellt aus epub/rtf/txt Dateien unter Verwendung von TTS Hörbücher

Hinweise:
Das Programm erstellt ansich lediglich Text Dateien durch Umwandlung und/oder Scripte um diese mit anderen Tools konvertieren zu können. Was dafür erforderlich ist ist hier beschrieben:

Installation:
- Stelle sicher das pip installiert ist mit "python3 get-pip.py"
- Stelle sicher das git installiert ist https://git-scm.com/downloads
- Gehe zu "https://github.com/rhasspy/piper/releases" und lade das Windows Release herunter. Das entpackt man in ein Unterverzeichnis zb. c:\tts\piper
- Lade die .json und die .onyx Dateien herunter von "https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0/de/de_DE/thorsten/high" und lege sie direkt in das Verzeichnis
- Gehe in die Console oder Powershell und gib ein: "pip install ebooklib beautifulsoup4 pyperclip"
- Starte das Script mit "py epub2hoerbuch.py".

Nutzung:
Im grafischen Menü kann man nun eine .epub (eBook Datei), .rtf (Richtext Dokument) oder eine vorhandene .txt (Einfache Textdatei) auswählen.
-> Der Inhalt der Datei läßt sich dann direkt als Textdatei in das Clipboard kopiern, als Textdatei speichern oder in eine .bat (ausführbare Batch Datei) speichern.
- - > Beim kopieren in das Clipboard kann man nun mein Programm "zVorlesen" verwenden um den Inhalt direkt mit der Windows eingenen Stimme vorlesen zu lassen.
- - > Das Speichern als Textdatei dient lediglich zur Umwandlung in einen Plaintext sofern man den Inhalt anderweitig verwenden möchte.
- - > Das Speichern als .bat Datei sollte in dem Piper Verzeichnis erfolgen zb. als "hoerbuch_erstellen.bat" wenn man dieses Script dann ausführt dauert es je nach Textlänge recht lange (ggf. mehrere Stunden), allerdings hat man anschliessend ein professionel klingendes Audiobuch vom Inhalt.

Das dürfte klar sein aber ich sags trotzdem:
Bitte beachten das dies nur für eigene Dokumente gedacht ist und NICHT dazu um irgendwelche Copyright Verletzungen zu begehen, also bitte keine original Bücher zu Hörbüchern machen welche nicht frei zugänglich sind.h
Hier ist eine Beispiel Umwandlung in eine Audio Datei zu finden, welche eine Geschichte aus meinem Sci-Fi Geschichten Generator verwendet.
