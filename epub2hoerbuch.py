# Installation:
# - Stelle sicher das pip installiert ist mit "python3 get-pip.py"
# - Stelle sicher das git installiert ist https://git-scm.com/downloads
# - Gehe zu "https://github.com/rhasspy/piper/releases" und lade das Windows Release herunter. Das entpackt man in ein Unterverzeichnis zb. c:\tts\piper
# - Lade die .json und die .onyx Dateien herunter von "https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0/de/de_DE/thorsten/high" und lege sie direkt in das Verzeichnis
# - Gehe in die Console oder Powershell und gib ein: "pip install ebooklib beautifulsoup4 pyperclip"
# - Starte das Script mit "py epub2hoerbuch.py".
# Nutzung:
# Im grafischen Menü kann man nun eine .epub (eBook Datei), .rtf (Richtext Dokument) oder eine vorhandene .txt (Einfache Textdatei) auswählen.
# Der Inhalt der Datei läßt sich dann direkt als Textdatei in das Clipboard kopiern, als Textdatei speichern oder in eine .bat (ausführbare Batch Datei) speichern.
# -> Beim kopieren in das Clipboard kann man nun mein Programm "zVorlesen" verwenden um den Inhalt direkt mit der Windows eingenen Stimme vorlesen zu lassen.
# -> Das Speichern als Textdatei dient lediglich zur Umwandlung in einen Plaintext sofern man den Inhalt anderweitig verwenden möchte.
# -> Das Speichern als .bat Datei sollte in dem Piper Verzeichnis erfolgen zb. als "hoerbuch_erstellen.bat" wenn man dieses Script dann ausführt dauert es je nach Textlänge
# recht lange (ggf. mehrere Stunden), allerdings hat man anschliessend ein professionel klingendes Audiobuch vom Inhalt.
# Bitte beachten das dies nur für eigene Dokumente gedacht ist und nicht dazu um irgendwelche Copyright Verletzungen zu begehen. Also bitte keine original Bücher zu Hörbüchern machen welche nicht frei zugänglich sind!
# In der Projektbeschreibung ist eine Beispiel Umwandlung in eine Audio Datei zu finden, welche eine Geschichte aus meinem Sci-Fi Geschichten Generator verwendet.

#Source: github.com/zeittresor/py_epub2hoerbuch
import tkinter as tk
from tkinter import filedialog, messagebox
from ebooklib import epub
from bs4 import BeautifulSoup
import pyperclip 
#pip install coqui-tts (to remember for next version)

class EpubApp:
    def __init__(self, master):
        self.master = master
        master.title("EPUB/Text Extractor")

        self.text = ''

        self.load_button = tk.Button(master, text="Datei öffnen (.epub/.txt/.rtf)", command=self.load_file)
        self.load_button.pack(pady=10)

        self.copy_button = tk.Button(master, text="In Zwischenablage kopieren", command=self.copy_text, state='disabled')
        self.copy_button.pack(pady=5)

        self.save_button = tk.Button(master, text="Als Textdatei speichern", command=self.save_text, state='disabled')
        self.save_button.pack(pady=5)

        self.hoerbuch_button = tk.Button(master, text="Hörbuch-Skript speichern", command=self.create_hoerbuch, state='disabled')
        self.hoerbuch_button.pack(pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[
            ("EPUB Dateien", "*.epub"),
            ("Textdateien", "*.txt"),
            ("RTF Dateien", "*.rtf")
        ])
        if file_path:
            if file_path.endswith('.epub'):
                self.text = self.extract_text_epub(file_path)
            else:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.text = file.read()

            self.copy_button.config(state='normal')
            self.save_button.config(state='normal')
            self.hoerbuch_button.config(state='normal')
            messagebox.showinfo("Geladen", "Datei erfolgreich geladen.")

    def copy_text(self):
        pyperclip.copy(self.text)
        messagebox.showinfo("Kopiert", "Text wurde in die Zwischenablage kopiert.")

    def save_text(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])
        if save_path:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(self.text)
            messagebox.showinfo("Gespeichert", f"Text wurde gespeichert unter:\n{save_path}")

    def create_hoerbuch(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".bat", filetypes=[("Batch Dateien", "*.bat")])
        if save_path:
            safe_text = self.text.replace('"', '\\"').replace('%', '%%')
            with open(save_path, 'w', encoding='utf-8-sig') as f:
                f.write('@echo off\n')
                f.write('chcp 65001 >nul\n')
                f.write(f'echo "{safe_text}" | piper -m ./de_DE-thorsten-high.onnx -f ausgabeFinal.wav\n')
            messagebox.showinfo("Gespeichert", f"Batch-Datei wurde gespeichert unter:\n{save_path}")

    def extract_text_epub(self, file_path):
        book = epub.read_epub(file_path)
        text = ""
        for item in book.get_items():
            if item.get_type() == epub.ITEM_DOCUMENT:
                soup = BeautifulSoup(item.get_body_content(), 'html.parser')
                text += soup.get_text()
        return text

if __name__ == "__main__":
    root = tk.Tk()
    app = EpubApp(root)
    root.geometry("400x220")
    root.mainloop()
