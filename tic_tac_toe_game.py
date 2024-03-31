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

# print(board)

def print_board(board):
    for row in board:
        print(" | ".join(row))