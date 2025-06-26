# Violet - A Python-Based Voice Assistant [STILL UNDER BUILD]

Violet is a lightweight, modular voice assistant built with Python that can listen, understand voice commands, and perform tasks like playing music, searching the web, or reading information aloud — similar to Alexa or Google Assistant.

---

##  Features

- Wake-word activation ("Hey bot")
- Speech recognition and natural command parsing
- Text-to-speech responses
- Music playback (via YouTube or local files)
- Modular command processing
- Easy to extend with new skills

---

##  Tech Stack

- Python 3
- `speech_recognition` + `pyaudio`
- `pyttsx3` / `gTTS` for speech output
- `pywhatkit`, `pafy`, `yt-dlp`, `vlc` for media
- `keyboard`, `threading` for control logic

---

##  Requirements

- Microphone (USB or 3.5mm)
- Speaker output
- Python environment with required libraries
- Internet connection (for online tasks)

---

##  Project Structure (Example)
│
├── main.py
├── Brains.py
├── VoicePartitions.py
├── SpeechRec.py
├── Scearch.py
├── requirements.txt
├── README.md

##  How It Works

1. Listens passively for "hey violet"
2. Activates voice recognition and parses the intent
3. Executes the command (e.g., play a song, speak a fact)
4. Responds via voice output

---

##  Notes

- API keys (e.g., for YouTube or Reddit) should be stored securely in `.env`
- Works best on a Raspberry Pi or local machine with mic/speaker
- Modular design makes it easy to add custom skills

---

##  Future Additions (Optional)

- GUI interface
- Visual feedback (LED ring)
- Offline mode with Vosk
- Integration with smart home devices
