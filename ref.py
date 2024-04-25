import subprocess as sp
import os

programName = "notepad.exe"
folderPath = "C:/Users/shoun/OneDrive/Desktop/rough/notes"

# Ask the user for the file name
fileName = input("Enter the file name to save (without extension): ")
filePath = os.path.join(folderPath, fileName + ".txt")  # Adding .txt extension to the file name

# Open the Notepad application with the specified file path
process = sp.Popen([programName, filePath])

# Read input from the terminal and write to the file
with open(filePath, "w") as file:
    while True:
        user_input = input()  # Read input from the terminal
        if user_input.lower() == "exit":  # Exit loop if "exit" is entered
            break
        file.write(user_input + "\n")  # Write input to the file