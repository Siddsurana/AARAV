import subprocess as sp
import os
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


def notes():
    programName = "notepad.exe"
    folderPath = "Notes"

    print("Please enter the file name")
    speak("Please enter the file name")
    fileName = input("Enter the file name to save (without extension): ")
    filePath = os.path.join(folderPath, fileName + ".txt")  
    print("Please write the note you want to write and type exit/enter when done")
    speak("Please write the note you want to write and type exit/enter when done")
    with open(filePath, "w") as file:
        while True:
            user_input = input()  
            if user_input.lower() == "exit":  
                break
            file.write(user_input + "\n")  
    speak("Done sir!!")
