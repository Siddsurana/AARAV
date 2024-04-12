import pyautogui
import time
import webbrowser
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
        query  = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def pizza():
    speak("Opening Dominos")
    webbrowser.open("https://www.dominos.co.in/")

    time.sleep(2)
    pyautogui.click(629,922)
    speak("Loading the page sir")
    time.sleep(5)
    pyautogui.click(2230,279)
    time.sleep(2)
    pyautogui.click(2230,279)
    time.sleep(2)
    speak("Please tell the address sir")
    location = takeCommand().lower()
    pyautogui.write(location)
    time.sleep(8)
    pyautogui.click(2372,1016)
    speak("Please add what you want to buy in the cart sir and say checkout when finished")
    while True:
        checkout = takeCommand().lower()
        if checkout == 'check out':
            speak("checking out sir!")
            pyautogui.click(2438,1301)
            break
    speak("Please do the transaction and enjoy the order sir!")



