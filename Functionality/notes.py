import os
import pyautogui
import time
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

file_name = ""

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def create_notes_directory():
    directory = "Notes"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def stop_typing():
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite(file_name)
    pyautogui.press('enter')

def notes():
    print("Plese specify the file name")
    speak("Plese specify the file name")
    notes_directory = create_notes_directory()
    file_name = takeCommand()
    # Open Notepad
    os.system("start notepad")
    time.sleep(1)

    speak("Please tell me what should I write...")
    while True:
        writeNotepad = takeCommand().lower()
        if writeNotepad == 'exit typing':
            speak("Done Sir.")
            stop_typing()
            break
        else:
            pyautogui.typewrite(writeNotepad)
            pyautogui.press('enter')
    
    

notes()