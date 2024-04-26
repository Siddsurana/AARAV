import gspread
from google.oauth2.service_account import Credentials
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


scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("Automation\credentials.json", scopes=scopes)
client = gspread.authorize(creds)
sheet_id = "1GNfUsP0bzZ9f8fTT_7mmjFAKkNJYY-Dt-c-Jo-HRZxM"
workbook = client.open_by_key(sheet_id)



def get_text_input(prompt):
    return input(prompt)
            
def perform_addition(values):
    return sum(values)

def perform_subtraction(values):
    return values[0] - sum(values[1:])

def perform_multiplication(values):
    result = 1
    for val in values:
        result *= val
    return result

def perform_division(values):
    result = values[0]
    for val in values[1:]:
        if val != 0:
            result /= val
        else:
            raise ValueError("Division by zero is not allowed.")
    return result

def main():
    while True:
        speak("Please enter the cell where you want to input or say 'stop' to exit: ")        
        print("Please enter the cell where you want to input (e.g., A1) or say 'stop' to exit: ")
        cell = takeCommand()
        if cell.lower() == "stop":
            break
        speak("Please enter the value you want to input: ")
        print("Please enter the value you want to input: ")
        value = takeCommand()
        try:
            sheet = workbook.sheet1
            sheet.update(cell, [[value]])  # Wrap the value in a list before passing to update method
            print(f"Updated value in cell {cell}")
            speak("value updated")
        except Exception as e:
            print(f"Error updating value in cell {cell}: {e}")
            speak(f"Error updating value in cell {cell}: {e}")
# Perform operations and store result in a cell provided by the user
def operations():
    while True:
        speak("Please select an operation")
        print("Please select an operation (addition/subtraction/multiplication/division): ")
        operation =  takeCommand().lower()
        if operation.lower() not in ["addition", "subtraction", "multiplication", "division"]:
            print("Invalid operation. Please select from 'addition', 'subtraction', 'multiplication', or 'division'.")
            speak("Invalid operation")
            continue
        speak("How many cells do you want to perform the operation on? please type it down")
        num_cells = int(get_text_input("How many cells do you want to perform the operation on? "))
        
        if num_cells < 1:
            print("Invalid number of cells. Please enter a positive integer.")
            continue
        values = []
        for i in range(num_cells):
            speak(f"Please enter the cell location {i+1}")
            print(f"Please enter the cell location {i+1}")
            cell_location = takeCommand()
            
            try:
                sheet = workbook.sheet1
                cell_value = sheet.acell(cell_location).value
                if not cell_value:
                    cell_value = 0
                values.append(int(cell_value))
            except Exception as e:
                print(f"Error retrieving value from cell {cell_location}: {e}")
                continue
        speak("Please select cell you want to store result in")
        print("Please select cell you want to store result in")
        result_cell = takeCommand()
        
        try:
            if operation.lower() == "addition":
                result = perform_addition(values)
            elif operation.lower() == "subtraction":
                result = perform_subtraction(values)
            elif operation.lower() == "multiplication":
                result = perform_multiplication(values)
            elif operation.lower() == "division":
                result = perform_division(values)
            sheet.update(result_cell, [[result]])  # Wrap the result in a list before passing to update method
            print(f"Result of {operation.lower()} stored in cell {result_cell}")
            speak(f"Result of {operation.lower()} stored in cell {result_cell}")
        except ValueError as ve:
            print(ve)
        speak("do you want to perform more operation please say yes or no")
        print("do you want to perform more operation")
        final = takeCommand().lower()
        if final == "no":
            break

def sheets():
    webbrowser.open("https://docs.google.com/spreadsheets/d/{sheet_id}".format(sheet_id="1GNfUsP0bzZ9f8fTT_7mmjFAKkNJYY-Dt-c-Jo-HRZxM"))
    while True:
        print("Instructions")
        print("say exit to end the program")
        speak("Do you want to perform an operation or feed data")
        print("Do you want to perform an operation or feed data")
        command = takeCommand().lower()
        if "operation" in command:
            operations()
        elif "data" in command:
            main()
        else:
            break




