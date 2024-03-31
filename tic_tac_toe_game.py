"""
In this file it is created a terminal version of the Tic Tac Toe 
game (X and O) which can be played by two users. The players are 
asked successivelly in the terminal to input the location (row and
column) where they want their specific character to be inserted.
The game ends when one of them first satisfies one of the three
winning conditions.
"""

board = []
for n in range(2):
    board.append(["_"] * 3)
board.append([" "] * 3)


def print_board(board):
    for row in board:
        print(" | ".join(row))


def insert_symbol(board, symbol):
    print("Time for {S}:".format(S = symbol))
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))
    while row not in range(1,4) or col not in range(0,4):
        print("You missed the board! Enter a valid location for {S}:".format(S = symbol))
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
    while board[row-1][col-1] == "X" or board[row-1][col-1] == "O":
        print("Choose an empty box for {S}:".format(S = symbol))
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
    board[row-1][col-1] = symbol.upper()
    print_board(board)