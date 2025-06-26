import time
import sys
from Brains import introduce, listen, Scearching, exit, clean_command
from VoicePartitions import talk 
from SpeechRec import listen_for_speech
import pywhatkit

# Optional: Only if you want to use 'q' to quit manually
import keyboard

introduce()

def activate_assistant():
    """
    Once "Hey Violet" is heard, enter command mode.
    """
    talk("Yes?")
    print("🤖 Waiting for your command...")

    while True:
        command = listen()
        if command == "":
            continue

        if 'play' in command and 'song' in command:
            song_name = command.replace('play', "")
            song_name = song_name.replace('song', "")
            clean_command(song_name)
            talk('playing song'+song_name)
            pywhatkit.playonyt(song_name)
            return True

        if command in ["exit", "quit", "goodbye", "stop"]:
            exit() #attribute to 'Brains'
            return False
        
        elif command in ["standby", "wait"]:
            talk("Going back to standby.")
            return True

        else:
            talk("Processing...")
            print(f"----------->Processing command: {command}")
            try:
                Scearching(command)
            except Exception as e:
                talk("I had trouble processing that.")
                print("[Error]", e)

def main():
    while True:
        spoken_text = listen_for_speech().lower()

        if spoken_text == "":
            continue

        if spoken_text in ["exit", "quit", "goodbye", "stop"]:
            exit() #attribute to 'Brains'
            return False
        
        if "hey violet" in spoken_text:
            print("🟢 Activated!")
            should_continue = activate_assistant()
            if not should_continue:
                break

        time.sleep(0.5)
    sys.exit()

if __name__ == "__main__":
    main()