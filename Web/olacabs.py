import webbrowser
import time
import pyautogui

import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


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
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def book_cab():
    print("Opening Ola Cabs website...")
    speak("Opening Ola Cabs website...")
    webbrowser.open("https://book.olacabs.com")
    speak("Loading the page sir")    
    time.sleep(3)  
    pyautogui.click(370,642)
    print("What is the destination sir")
    speak("What is the destination sir")
    destination = takeCommand().lower()
    pyautogui.write(destination)
    time.sleep(2)
    pyautogui.click(443,486)
    time.sleep(2)
    speak("Please select the vehicle and book the ride")

book_cab()



