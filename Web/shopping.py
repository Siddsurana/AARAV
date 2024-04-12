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
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def amazon():
    speak("Opening Amazon")
    webbrowser.open("https://www.amazon.com/")
    speak("Loading the page sir")
    time.sleep(5)
    pyautogui.click(762, 300)
    time.sleep(2)
    speak("Please tell what do you want to buy sir")
    stock = takeCommand().lower()
    pyautogui.write(stock)
    time.sleep(3)
    pyautogui.press('enter')  
    time.sleep(2)
    speak("Please add what you want to buy in the cart sir and say check out when finished")
    while True:
        checkout = takeCommand().lower()
        if checkout == 'check out':
            pyautogui.click(2861 ,368)
            time.sleep(3)
            break
    speak("Please do the transaction and place the order")


def flipkart():
    speak("Opening Flipkart")
    webbrowser.open("https://www.flipkart.com/")
    speak("Loading the page sir")
    time.sleep(4)
    pyautogui.click(691,312)
    time.sleep(2)
    speak("Please tell what do you want to buy sir")
    stock = takeCommand().lower()
    pyautogui.write(stock)
    time.sleep(3)
    pyautogui.press('enter') 
    time.sleep(2)
    speak("Please add what you want to buy in the cart and come back to the main page sir, say check out when finished")
    while True:
        checkout = takeCommand().lower()
        if checkout == 'check out':
            pyautogui.click(2606,294)
            time.sleep(3)
            break
    speak("Please do the transaction and place the order")

def Myntra():
    speak("Opening Myntra")
    webbrowser.open("https://www.myntra.com/")
    speak("Loading the page sir")
    time.sleep(4)
    pyautogui.click(1592,325)
    time.sleep(2)
    speak("Please tell what do you want to buy sir")
    stock = takeCommand().lower()
    pyautogui.write(stock)
    time.sleep(3)
    pyautogui.press('enter') 
    time.sleep(2)
    speak("Please add what you want to buy in the bag and come back to the main page sir, say check out when finished")
    while True:
        checkout = takeCommand().lower()
        if checkout == 'check out':
            pyautogui.click(2832,324)
            time.sleep(3)
            break
    speak("Please do the transaction and place the order")


    
