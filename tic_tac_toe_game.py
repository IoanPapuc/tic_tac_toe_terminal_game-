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


def full_row(board, symbol):    
    for i in range(3):
        if board[i] == [symbol] * 3:
            return True
    return False
        
def full_column(board, symbol):        
    for j in range(3):
        if [board[0][j], board[1][j], board[2][j]] == [symbol] * 3:
            return True
    return False
        
def full_diag(board, symbol):
    if [board[0][0], board[1][1], board[2][2]] == [symbol] * 3 \
        or [board[0][2], board[1][1], board[2][0]] == [symbol] * 3:
        return True
    return False

def winning_verification(board, symbol):
    if full_row(board, symbol) or full_column(board, symbol) or full_diag(board, symbol):
        return True
    return False