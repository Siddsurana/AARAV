import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

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
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                raise ValueError("Row and column must be between 0 and 2.")
            if board[row][col] != " ":
                raise ValueError("That position is already taken. Try again.")
            return row, col
        except ValueError as e:
            print(e)

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
            row, col = get_computer_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            if current_player == "X":
                print("Congratulations! You win!")
            else:
                print("Computer wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

play_tic_tac_toe()