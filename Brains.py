import pyttsx3
import Scearch
import VoicePartitions
import SpeechRec

def listen():
    inp = SpeechRec.listen_for_speech()
    return inp
def Scearching(x):
    reply = Scearch.ask(x)
    VoicePartitions.talk(reply)

def exit():
    VoicePartitions.talk("Goodbye")

def introduce():
    VoicePartitions.talk("Hey this is Violet, your personal assistent powered by gemini. You can ask me anything you need and ill try to help...")

def clean_command(text):
    text = text.lower()

    filler_words = [
        "please", "can you", "could you", "would you", "i want to", "i would like to", 
        "for me", "will you", "hey", "bot", "okay", "just", "to", "me", "play me"
    ]

    for i in filler_words:
        text = text.replace(i, "")

    return text