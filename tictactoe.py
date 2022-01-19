"""
Developer: Sean Walker
Description: Create a tic tac toe game.
Date: 1/14/2022
"""

#def main function
def main():
    #call create board function
    board = create_board()

    #create needed variables
    winner = None
    user = 'X'

    #Create a loop to recieve, validate, and use input.
    while True:
        #print the board
        print_board(board)

        #ask user for input
        user_input = input("Please enter a position number (1 - 9) or"
                           "\"quit\" to end program: ")
        
        #Call the quit function
        if quit(user_input):
            break

        #call  the check input function
        if not check_input(user_input, board):
            print('Please try again.')
            continue
        user_input = int(user_input)
        #call update board function
        board = update_board(user_input, board, user)

        #call the check for winner function
        if not check_for_winner(board):
            print('Thanks for playing!')
            break

        #call user trade function
        user = change_user(user)

        continue


def create_board():
    board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
    return board

def change_user(user):
    if user == 'O':
        return 'X'
    else:
        return 'O'

def print_board(board):
    print(" " + board[0] + "  /  " + board[1] + "  /  " + board[2])
    print("----------------")
    print(" " + board[3] + "  /  " + board[4] + "  /  " + board[5])
    print("----------------")
    print(" " + board[6] + "  /  " + board[7] + "  /  " + board[8])
    print()

def quit(user_input):
        if user_input == "quit":
            print('Thanks for playing!')
            return True
        else:
            return False

def check_input(user_input, board):
    if not check_for_number(user_input):
        return False
    user_input = int(user_input)
    if not check_bounds(user_input):
        return False
    if not check_available(user_input, board):
        return False
    else:
        return True

def check_for_number(user_input):
    if not user_input.isnumeric():
        print('This is not an integer.')
        return False
    else:
        return True

def check_bounds(user_input):
    if user_input > 9 or user_input < 1:
        print('This number is not between 1 and 9.')
        return False
    else:
        return True

def check_available(user_input, board):
    if board[user_input - 1] != "-":
        print('This spot is already taken.')
        return False
    else:
        return True

def update_board(user_input, board, user):
    board[user_input - 1] = user
    return board

def check_for_winner(board):
    if check_horizontal(board) or check_virtical(board) or check_diagonal(board):
        print_board(board)
        print(f'The winner is {winner}\'s!')
        return False
    if check_tie(board):
        print_board(board)
        print('There is no winner. We have a tie.')
        return False
    else:
        return True

def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[7]
        return True
    else:
        return False

def check_virtical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    else:
        return False

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    else:
        return False

def check_tie(board):
    global winner
    if "-" not in board:
        winner = "Tie"
        return True
    else:
        return False

main()