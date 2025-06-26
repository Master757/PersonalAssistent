import win32com.client
import pythoncom
import keyboard
import time
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def stop():
    speaker.Skip("Sentence", 99999999)
    pythoncom.CoUninitialize()
    
def speak(text):
    """Speak text using Windows SAPI and listen for 'q' key"""
    pythoncom.CoInitialize()

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    print("---------->>>>> Speaking started...")
    # Start speech asynchronously
    speaker.Speak(text, 1)  # 1 = asynchronous mode
   

    try:
        while True:
            if speaker.Status.RunningState == 1:  # 1 = Done
                break
            if keyboard.is_pressed('q'):
                stop()
                break
            time.sleep(0.05)
    except Exception as e:
        print(f"[Error during speech] {e}")
    pythoncom.CoUninitialize()
     

def talk(text):
    print("Assistant says:", text)
    speak(text)
    print(" --------------------- Speech Part ended. -------------------------- \n")

