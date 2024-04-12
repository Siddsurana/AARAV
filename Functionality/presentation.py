import webbrowser
import pyautogui
import time
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

def ppt():
    speak("Opening slidesgo Presentations")
    webbrowser.open("https://slidesgo.com/ai-presentations")
    time.sleep(3)
    pyautogui.click(495,1158)
    time.sleep(3)
    speak("Please tell me what topic you want presentation on")
    pyautogui.click(967,621)
    topic = takeCommand()
    pyautogui.write(topic)
    time.sleep(1)
    speak("Please mention the style of the sheet?, also choose your specific slide and say go ahead when done.")
    slides = takeCommand().lower()
    while True:
        if "go ahead" in slides:
            pyautogui.click(1426,1673)
            break
    speak("Please wait generating the presentation")
    time.sleep(50)
    speak("Presentation generated successfully")
    pyautogui.click(2554,301)
    time.sleep(1)
    pyautogui.click(2651,1204)
    speak("Downloading the pdf for the presentation")
    





