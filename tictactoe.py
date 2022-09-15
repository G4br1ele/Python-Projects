def assign_marker():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1 choose your marker (X/O): ").upper()
    if marker == "X":
        marker = ("X", "O")
    else: 
        marker = ("O", "X")
    return marker

import random  
def choose_first():
    if random.randint(1,2) == 1:
        print("Player 1 goes first")
        return "player1"
    else:
        print("Player 2 goes first")
        return "player2"

def display_board(board):

    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])

def place_marker(board, turn):
    position = ""
    while position not in [1,2,3,4,5,6,7,8,9]:
        try:
            position = int(input("Choose where to place your marker (1-9): "))
        except:
            print("Only integers are allowed!")
    if board[position] == " ":
        if turn == "player1":
            board[position] = player1
        else:
            board[position] = player2
    else:
        print("Invalid selection!")
        place_marker(board, turn)

def win_check(board, turn, player1, player2):
    if turn == "player1":
        return ((board[1] == board[2] == board[3] == player1) or
        (board[4] == board[5] == board[6] == player1) or
        (board[7] == board[8] == board[9] == player1) or
        (board[1] == board[4] == board[7] == player1) or
        (board[2] == board[5] == board[8] == player1) or
        (board[3] == board[6] == board[9] == player1) or
        (board[1] == board[5] == board[9] == player1) or
        (board[3] == board[5] == board[7] == player1))
    else :
        return ((board[1] == board[2] == board[3] == player2) or
        (board[4] == board[5] == board[6] == player2) or
        (board[7] == board[8] == board[9] == player2) or
        (board[1] == board[4] == board[7] == player2) or
        (board[2] == board[5] == board[8] == player2) or
        (board[3] == board[6] == board[9] == player2) or
        (board[1] == board[5] == board[9] == player2) or
        (board[3] == board[5] == board[7] == player2))

def tie_check(board):
    return " " not in board[1:10]

def replay():
    answer = ""
    while answer != "Y" and answer != "N":
        answer = input("Would you like to play again? (Y/N): ").upper()
    if answer == "Y":
        return True
    else:
        return False


# Game logic
if __name__ == "__main__":
    
    while True:
    
        game_on = True
        board = [" "] * 10
        player1, player2 = assign_marker()
        turn = choose_first()

        while game_on:
            if turn == "player1":
                display_board(board)
                place_marker(board, turn)
                if win_check(board, turn, player1, player2) == True:
                    display_board(board)
                    print("Player 1 has won!")
                    game_on = False
                    break
                elif tie_check(board) == True:
                    display_board(board)
                    print("There was a tie!")
                    game_on = False
                    break
                else:
                    turn = "player2"

            elif turn == "player2":
                display_board(board)
                place_marker(board, turn)
                if win_check(board, turn, player1, player2) == True:
                    display_board(board)
                    print("Player 2 has won!")
                    game_on = False
                    break
                elif tie_check(board) == True:
                    display_board(board)
                    print("There was a tie!")
                    game_on = False
                    break
                else:
                    turn = "player1"

        if not replay():
            print("Thanks for playing!")
            break
        else:
            game_on = True

