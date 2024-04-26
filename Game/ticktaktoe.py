import random
import pyttsx3
#import speech_recognition
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
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

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def get_user_move(board):
    while True:
        try:
            print("Enter Row:")
            speak("Enter Row:")
            row = takeCommand().lower() #int(input("Enter row (0, 1, or 2): "))
            if "first" in row:
                row=0
            elif "second" in row:
                row=1
            elif "third" in row:
                row=2
            
            print("Enter Column:")
            speak("Enter coloumn:")
            col =takeCommand().lower() #int(input("Enter column (0, 1, or 2): "))
            if "first" in col:
                col=0
            elif "second" in col:
                col=1
            elif "third" in col:
                col=2
                
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                raise ValueError("Row and column must be between 1 and 3.")

            if board[row][col] != " ":
                raise ValueError("That position is already taken. Try again.")
            return row, col
        except ValueError as e:
            print(e)
            speak(e)

def get_computer_move(board):
    # Check if computer can win
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'
                if check_winner(board, 'O'):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "

    # Check if player can win and block
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'X'
                if check_winner(board, 'X'):
                    board[i][j] = "O"
                    return i, j
                board[i][j] = " "

    # Otherwise, make a random move
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            row, col = get_user_move(board)
        else:
            print("Computer's turn...")
            speak("Computer's turn")
            row, col = get_computer_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            if current_player == "X":
                print("Congratulations! You win!")
                speak("Congratulations! You win!")
            else:
                print("Computer wins!")
                speak("Computer wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

