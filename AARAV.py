import cv2
import os
import face_recognition
import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import threading
from plyer import notification
from Automation.scroll import ScrollControl
import pygetwindow as gw
from GUI.GUI import GUI
import psutil


distance_threshold = 0.5  

def initialize_speech_recognition():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.setProperty("rate", 170)
    return engine


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


def get_system_status():
    ram_usage = psutil.virtual_memory().percent

    battery_health = None
    try:
        battery = psutil.sensors_battery()
        if battery is not None:
            battery_health = battery.percent
    except Exception as e:
        print("Failed to retrieve battery health:", e)

    cpu_usage = psutil.cpu_percent()

    return ram_usage, battery_health, cpu_usage

def system_status():
    ram_usage, battery_health, cpu_usage = get_system_status()
    status_message = f"System Status:\nRAM Usage: {ram_usage}%\nCPU Usage: {cpu_usage}%"
    if battery_health is not None:
        status_message += f"\nBattery Health: {battery_health}%"
    return status_message

def load_known_face(folder_name):

    known_face_image = face_recognition.load_image_file(f"sample/{folder_name}/sample_{folder_name}.jpg")
    known_face_encoding = face_recognition.face_encodings(known_face_image)[0]
    return known_face_encoding

def detect_and_recognize_faces(frame, folder_names):
    global engine  
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    for face_encoding in face_encodings:
        for folder_name in folder_names:
            known_face_encoding = load_known_face(folder_name)
            face_distance = face_recognition.face_distance([known_face_encoding], face_encoding)[0]

            if face_distance < distance_threshold:
                return folder_name

    return None

def greet_user(user_name):
    print(f"Welcome {user_name} Sir! Glad to see you.")
    speak(f"Welcome {user_name} Sir! Glad to see you.")

if __name__ == "__main__":

    engine = initialize_speech_recognition()

    GUI()

    folder_names = [name for name in os.listdir("sample") if os.path.isdir(os.path.join("sample", name))]

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  
    cam.set(4, 480)  

    while True:
        ret, frame = cam.read()


        recognized_user_folder_name = detect_and_recognize_faces(frame, folder_names)

        if recognized_user_folder_name is not None:
            user_mapping = {"1": "sahil", "2": "loukik", "3": "siddharth", "4": "shounak"} 
            user_name = user_mapping.get(recognized_user_folder_name)
            if user_name:
                greet_user(user_name)
                break
        else:
            print("Face not recognized")
            speak("Face not recognized, Please run again!")
            break

    cam.release()
    cv2.destroyAllWindows()

    if recognized_user_folder_name is not None:
            scroll_control = ScrollControl()  
            while True:
                query = takeCommand().lower()
                if "wake up" in query or "aarav" in query:
                    from Functionality.GreetMe import greetMe
                    greetMe()

                    while True:
                        query = takeCommand().lower()
                        if "go to sleep" in query:
                            speak("Ok sir , You can call me anytime")
                            break 
                        elif "hello" in query:
                            speak("Hello Sir!, How are you?")
                        elif "who are you" in query:
                            speak("My name is AARAV as Advanced Artificial Response and Voice")
                        elif "what is your name" in query:
                            speak("My name is Aarav.")
                        elif "start scrolling up" in query:
                            speak("Scrolling up Sir!")
                            threading.Thread(target=scroll_control.start_scroll_up).start()
                        elif "start scrolling down" in query:
                            speak("Scrolling down Sir!")
                            threading.Thread(target=scroll_control.start_scroll_down).start()
                        elif "stop scrolling" in query:
                            speak("Stopped Scrolling Sir!")
                            threading.Thread(target=scroll_control.stop_scroll).start()
                        elif "pause" in query:
                            pyautogui.press("k")
                            speak("video paused")
                        elif "play" in query:
                            pyautogui.press("k")
                            speak("video played")
                        elif "mute" in query:
                            pyautogui.press("m")
                            speak("video muted")
                        elif "volume up" in query:
                            from keyboard import volumeup
                            speak("Turning volume up,sir")
                            volumeup()
                        elif "volume down" in query:
                            from keyboard import volumedown
                            speak("Turning volume down, sir")
                            volumedown()
                        elif "who is" in query:
                            import wikipedia
                            query = query.replace("who is", "")
                            try:
                                results = wikipedia.summary(query, sentences=2)
                                speak("According to Wikipedia..")
                                print(results)
                                speak(results)
                            except Exception as e:
                                speak("Can't perform the search at the moment")
                        elif "open web app" in query:
                            from Web.Dictapp import openappweb
                            openappweb(query)
                        elif "close" in query:
                            pyautogui.hotkey('alt','f4')
                        elif "google" in query:
                            from Web.SearchNow import searchGoogle
                            query = query.replace("search","")
                            query = query.replace("on","")
                            searchGoogle(query)
                        elif "youtube" in query:
                            from Web.SearchNow import searchYoutube
                            query = query.replace("search","")
                            query = query.replace("on","")
                            searchYoutube(query)
                        elif "wikipedia" in query:
                            from Web.SearchNow import searchWikipedia
                            query = query.replace("search","")
                            query = query.replace("on","")
                            searchWikipedia(query)
                        elif "make a note" in query:
                            speak("okay sir!!")
                            from Notes.notes import notes
                            notes()
                        elif "news" in query:
                            from Web.NewsRead import latestnews
                            latestnews()
                        elif "calculate" in query:
                            from Functionality.Calculatenumbers import WolfRamAlpha
                            from Functionality.Calculatenumbers import Calc
                            query = query.replace("calculate","")
                            query = query.replace("Aarav","")
                            Calc(query)
                        elif "whatsapp" in query:
                            from Functionality.Whatsapp import sendMessage
                            sendMessage()
                        elif "temperature" in query:
                            search = "temperature in pune"
                            url = f"https://www.google.com/search?q={search}"
                            r  = requests.get(url)
                            data = BeautifulSoup(r.text,"html.parser")
                            temp = data.find("div", class_ = "BNeawe").text
                            speak(f"current{search} is {temp}")
                        elif "weather" in query:
                            search = "temperature in pune"
                            url = f"https://www.google.com/search?q={search}"
                            r  = requests.get(url)
                            data = BeautifulSoup(r.text,"html.parser")
                            temp = data.find("div", class_ = "BNeawe").text
                            speak(f"current{search} is {temp}")
                        elif "the time" in query:
                            strTime = datetime.datetime.now().strftime("%H:%M")    
                            speak(f"Sir, the time is {strTime}")
                        elif "finally sleep" in query:
                            speak("Going to sleep,sir")
                            exit()
                        elif "copy" in query:
                            speak("copying")
                            pyautogui.hotkey('ctrl','c')
                        elif "paste" in query:
                            speak("Pasting")
                            pyautogui.hotkey('ctrl','v')
                        elif "select all" in query:
                            speak("Selecting all")
                            pyautogui.hotkey('ctrl', 'a')
                        elif "delete" in query:
                            speak("deleting")
                            pyautogui.hotkey('del')
                        elif "save" in query:
                            speak("saving")
                            pyautogui.hotkey('ctrl', 's')
                        elif "minimise" in query:
                            speak("okay Sir!")
                            pyautogui.hotkey('win', 'd')
                        elif "maximize" in query:
                            speak("okay Sir!")
                            pyautogui.hotkey('win', 'up')
                        elif "file explorer" in query:
                            speak("Opening File Explorer")
                            pyautogui.hotkey('win', 'e')
                        elif "switch window" in query:
                            speak("Okay Sir!")
                            pyautogui.hotkey('alt', 'tab')
                        elif "create a new folder" in query:
                            speak("creating a new folder")
                            pyautogui.hotkey('ctrl', 'shift', 'n')
                        elif "form" in query:
                            from Functionality.googleformgenerator import forms
                            forms()
                        elif "type" in query:
                            speak("Please tell me what should I write...")
                            while True:
                                writeNotepad = takeCommand().lower()
                                if writeNotepad == 'exit typing':
                                    speak("Done Sir.")
                                    break
                                else:
                                    pyautogui.typewrite(writeNotepad)
                                    pyautogui.press('enter')
                        elif "screenshot" in query:
                            im = pyautogui.screenshot()
                            im.save("ss.jpg")
                        elif "schedule my day" in query:
                            tasks = [] 
                            speak("Do you want to clear old tasks (Please speak YES or NO)")
                            query = takeCommand().lower()
                            if "yes please" in query:
                                if os.path.exists("TODO/tasks.txt"):
                                    os.remove("TODO/tasks.txt")  
                                no_tasks = int(input("Enter the number of tasks: "))
                                for i in range(no_tasks):
                                    tasks.append(input("Enter the task: "))
                                    with open("TODO/tasks.txt", "a") as file:
                                        file.write(f"{i}. {tasks[i]}\n")
                            elif "no thank you" in query:
                                no_tasks = int(input("Enter the number of tasks: "))
                                for i in range(no_tasks):
                                    tasks.append(input("Enter the task: "))
                                    with open("TODO/tasks.txt", "a") as file:
                                        file.write(f"{i}. {tasks[i]}\n")
                        elif "show my schedule" in query:
                            try:
                                with open("TODO/tasks.txt", "r") as file:
                                    tasks = file.readlines()
                                    if tasks:
                                        speak("Your schedule for today is as follows:")
                                        for task in tasks:
                                            print(task.strip())
                                            speak(task.strip()) 
                                    else:
                                        speak("Your schedule for today is empty.")
                            except FileNotFoundError:
                                speak("I couldn't find your schedule file.")
                        elif "open" in query:   
                            query = query.replace("open","")
                            query = query.replace("Aarav","")
                            pyautogui.press("super")
                            pyautogui.typewrite(query)
                            pyautogui.sleep(2)
                            pyautogui.press("enter")
                        elif "how far" in query:
                            query = query.replace("how far", "")
                            query = query.replace("is", "")
                            from Functionality.distance import distance
                            distance(query)
                        elif "email" in query:
                            print("To whom do you want to send the email")
                            speak("To whom do you want to send the email")
                            recipent_name = takeCommand().lower()
                            from Functionality.sendemail import recipent_mapping
                            recipent_email = recipent_mapping.get(recipent_name)
                            if recipent_email:
                                print("What is the subject of the email")
                                speak("What is the subject of the email")
                                subject =takeCommand().lower()
                                from Functionality.sendemail import send_email
                                from Functionality.sendemail import sender_email
                                from Functionality.sendemail import sender_password
                                print("what is the message in the email")
                                speak("what is the message in the email")
                                content = takeCommand().lower()
                                send_email(sender_email, sender_password, recipent_email, subject, content)
                            else:
                                print("Sorry! I am unable to find your contact details")
                                speak("Sorry! I am unable to find your contact details")
                        elif "system status" in query:
                            status_message = system_status()
                            print(status_message)
                            speak(status_message)
                        elif "shopping" in query:
                            print("Sure! Let's do some Shopping....")
                            speak("Sure! Let's do some Shopping....")
                            while True:
                                from Web.shopping import *
                                print("From where would you like to buy? We have Amazon, Flipkart, and Myntra.")
                                speak("From where would you like to buy? We have Amazon, Flipkart, and Myntra.")
                                website_choice = takeCommand().lower()
                                if "amazon" in website_choice:
                                    amazon()
                                    break
                                elif "flipkart" in website_choice:
                                    flipkart()
                                    break
                                elif "myntra" in website_choice:
                                    Myntra()
                                    break
                                else:
                                    print("Please choose a valid website.")
                                    speak("Please choose a valid website.")
                                    break  
                        elif "turn on light one" in query:
                            from HomeAutomation.homeautomation import onlight1
                            print("Turning on the Light 1")
                            speak("Turning on the Light 1")
                            onlight1()
                        elif "turn off light one" in query:
                            from HomeAutomation.homeautomation import offlight1
                            print("Turning off the Light 1")
                            speak("Turning off the Light 1")
                            offlight1()
                        elif "book a cab" in query:
                            print("Sure! lets book a cab for you")
                            speak("Sure! lets book a cab for you")
                            speak("I am marking to your current location")
                            from Web.olacabs import book_cab
                            book_cab()
                        elif "presentation" in query:
                            speak("sure sir lets make a presentation..")
                            print("sure sir lets make a presentation..")
                            from Functionality.presentation import ppt
                            ppt()
                        elif "ask gpt" in query:
                            query = query.replace("ask", "")
                            query = query.replace("gpt", "")
                            query = query.replace("chat", "")
                            from GPT.gpt import start_gpt_prompt
                            start_gpt_prompt(query)
                        elif "call me" in query:
                            from Call.callme import make_call
                            make_call()
                        elif "call" in query:
                            query = query.replace("call", "")
                            from Call.call import call
                            call(query)
                        elif "where is" in query:
                            query = query.replace("where", "")
                            query = query.replace("is", "")
                            url = f"https://www.google.com/maps/search/{query}"
                            import webbrowser
                            webbrowser.open_new_tab(url)
                            speak(f"Here is {query} on Google Maps")
                        elif "what can you see" in query or "what is this" in query:
                            from Functionality.lookaround import main
                            main()
                        elif "pizza" in query:
                            from Web.dominos import pizza
                            pizza()
                        elif "earth" in query:
                            import webbrowser
                            webbrowser.open_new_tab("https://earth.google.com/")
                        elif "shutdown the system" in query:
                            speak("Are You sure you want to shutdown")
                            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                            if shutdown == "yes":
                                os.system("shutdown /s /t 1")

                            elif shutdown == "no":
                                break
                        else:  
                           from Dataset.convo import convo
                           convo(query)