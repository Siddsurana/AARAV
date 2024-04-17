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
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def forms():
    print("Okay Sir, please answer the following order process.")
    speak("Okay Sir, please answer the following order process.")
    print("What should be the title of the form?")
    speak("What should be the title of the form?")
    title = takeCommand()
    print("What should be the description?")
    speak("What should be the description?")
    description = takeCommand()

    print("How many questions do you want, out of maximum 3?")
    speak("How many questions do you want, out of 3?")
    questions = int(input("How many questions: "))

    speak("You have selected " + str(questions) + " questions.")
    selected_type = []
    q = []
    for i in range(0, questions):
        speak("What type of question should it be for question " + str(i+1))
        print(" 1. Short answer \n 2. Paragraph \n 3. Multiple Choice \n 4. Checkbox \n 5. Drop Down \n 6. File upload \n 7. Linear Scale \n 8. Multiple choice grid \n 9. Checkbox grid \n 10. Date \n 11. Time")
        while True:
            try:
                selected_type.append(int(input("Enter the number corresponding to the question type: ")))
                if selected_type[i] < 1 or selected_type[i] > 11:
                    print("Invalid choice. Please enter a number between 1 and 11.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        print("Please enter the question of number " + str(i+1))
        speak("Please enter the question of number " + str(i+1))
        q.append(str(input("Please enter the question: ")))
    speak("Opening Google Forms")
    webbrowser.open("https://docs.google.com/forms/u/0/")
    time.sleep(5) 
    pyautogui.click(532,643)
    time.sleep(5)
    pyautogui.click(978,577)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(2)
    pyautogui.write(title)
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(description)
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    if questions == 1:
        time.sleep(1)
        pyautogui.write(q[0])
        time.sleep(1)
        if selected_type[0] == 1:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1952,680)
        elif selected_type[0] == 2:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(2055,791)
        elif selected_type[0] == 3:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(2044,914)
        elif selected_type[0] == 4:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1959,1014)
        elif selected_type[0] == 5:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1938,1101)
        elif selected_type[0] == 6:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1916,1242)
        elif selected_type[0] == 7:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1953,1362)
        elif selected_type[0] == 8:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1983,1467)
        elif selected_type[0] == 9:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1980,1559)
        elif selected_type[0] == 10:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1937,1695)
        elif selected_type[0] == 11:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1949,1786)
        time.sleep(1)
        speak("Enter the option and submit the form")      
    elif questions == 2:
        time.sleep(1)
        pyautogui.write(q[0])
        time.sleep(1)
        if selected_type[0] == 1:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1952,680)
        elif selected_type[0] == 2:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(2055,791)
        elif selected_type[0] == 3:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(2044,914)
        elif selected_type[0] == 4:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1959,1014)
        elif selected_type[0] == 5:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1938,1101)
        elif selected_type[0] == 6:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1916,1242)
        elif selected_type[0] == 7:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1953,1362)
        elif selected_type[0] == 8:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1983,1467)
        elif selected_type[0] == 9:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1980,1559)
        elif selected_type[0] == 10:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1937,1695)
        elif selected_type[0] == 11:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1949,1786)
        time.sleep(3)
        pyautogui.click(2346,932)
        time.sleep(1)
        pyautogui.write(q[1])
        time.sleep(1)
        if selected_type[1] == 1:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1952,680)
        elif selected_type[1] == 2:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1957,1166)
        elif selected_type[1] == 3:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(2044,914)
        elif selected_type[1] == 4:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1959,1014)
        elif selected_type[1] == 5:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1938,1101)
        elif selected_type[1] == 6:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1916,1242)
        elif selected_type[1] == 7:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1953,1362)
        elif selected_type[1] == 8:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1983,1467)
        elif selected_type[1] == 9:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1980,1559)
        elif selected_type[1] == 10:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1937,1695)
        elif selected_type[1] == 11:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1949,1786) 
        speak("Enter the option and submit the form")
    elif questions == 3:
        time.sleep(1)
        pyautogui.write(q[0])
        time.sleep(1)
        if selected_type[0] == 1:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1952,680)
        elif selected_type[0] == 2:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(2055,791)
        elif selected_type[0] == 3:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(2044,914)
        elif selected_type[0] == 4:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1959,1014)
        elif selected_type[0] == 5:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1938,1101)
        elif selected_type[0] == 6:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1916,1242)
        elif selected_type[0] == 7:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1953,1362)
        elif selected_type[0] == 8:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1983,1467)
        elif selected_type[0] == 9:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1980,1559)
        elif selected_type[0] == 10:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1937,1695)
        elif selected_type[0] == 11:
            pyautogui.click(1994,868)
            time.sleep(1)
            pyautogui.click(1949,1786)
        time.sleep(3)
        pyautogui.click(2346,932)
        time.sleep(1)
        pyautogui.write(q[1])
        time.sleep(1)
        if selected_type[1] == 1:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1952,680)
        elif selected_type[1] == 2:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(2055,791)
        elif selected_type[1] == 3:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(2044,914)
        elif selected_type[1] == 4:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1959,1014)
        elif selected_type[1] == 5:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1938,1101)
        elif selected_type[1] == 6:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1916,1242)
        elif selected_type[1] == 7:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1953,1362)
        elif selected_type[1] == 8:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1983,1467)
        elif selected_type[1] == 9:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1980,1559)
        elif selected_type[1] == 10:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1937,1695)
        elif selected_type[1] == 11:
            pyautogui.click(1957,1166)
            time.sleep(1)
            pyautogui.click(1949,1786) 
        time.sleep(3)
        pyautogui.click(2351,1112)
        time.sleep(1)
        pyautogui.write(q[2])
        time.sleep(1)    
        if selected_type[2] == 1:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(1952,680)
        elif selected_type[2] == 2:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(2055,791)
        elif selected_type[2] == 3:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(2044,914)
        elif selected_type[2] == 4:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(1959,1014)
        elif selected_type[2] == 5:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(1938,1101)
        elif selected_type[2] == 6:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(1916,1242)
        elif selected_type[2] == 7:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(1953,1362)
        elif selected_type[2] == 8:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(1983,1467)
        elif selected_type[2] == 9:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(1980,1559)
        elif selected_type[2] == 10:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(1937,1695)
        elif selected_type[2] == 11:
            pyautogui.click(1994,1466)
            time.sleep(1)
            pyautogui.click(1949,1786)
        speak("Enter the option and submit the form")     




