

def new_board():
    empty_board = []
    for n in range(2):
        empty_board.append(["_"] * 3)
    empty_board.append([" "] * 3)
    return empty_board

quit_game = False

def print_board(board):
    for row in board:
        print(" | ".join(row))


def insert_symbol(board, symbol):
    print("Time for {S}:".format(S = symbol))
    while True:
        row = input("Enter row: ")
        col = input("Enter column: ")
        
        try:
            row_int = int(row)
            col_int = int(col)
            if row_int not in range(1,4) or col_int not in range(1,4):
                print("Outside of board! Enter a valid location.")
            elif board[row_int-1][col_int-1] == "X" or board[row_int-1][col_int-1] == "O":
                print("Choose an empty box!")
            else:
                board[row_int-1][col_int-1] = symbol.upper()
                print_board(board)
                break
        except ValueError:
            if row.upper() == "Q" or col.upper() == "Q":
                global quit_game
                quit_game = True 
                break
            else:
                print("If you want to quit game enter 'Q'. Otherwise, enter a valid location (1, 2 or 3 for row/ column).")

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


def play_game():
    
    board = new_board()
    print_board(board)

    global quit_game
    quit_game = False

    counter = 0
    while True:
        insert_symbol(board,"X")
        counter += 1
        if winning_verification(board, "X"):
            print("Game Over! X is the winner!")
            break
        elif counter == 9:
            print("Game Over! We have a draw!")
            break 
        elif quit_game == True:
            break      
        
        insert_symbol(board,"O")
        counter += 1
        if winning_verification(board, "O"):
            print("Game Over! O is the winner!")
            break
        elif counter == 9:
            print("Game Over! We have a draw!")
            break
        elif quit_game == True:
            break



def game_menu():
    print("-------------------------------------------------")
    print("     Welcome to Tic Tac Toe terminal game!")
    print("Insert the row and column (1, 2 or 3) for X or O.")
    print("The game starts with X.")

    while True:
        print("-----------------------------------------------------------------")
        print("Menu: [S] Start Game   [E] Exit   [Q] Quit Game / Return to Menu") 
        option = input("Insert an option: ")

        if option.upper() == "S":
            play_game()    
        elif option.upper() == "E":
            exit()
        else:
            continue


game_menu()