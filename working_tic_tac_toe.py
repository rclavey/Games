# imports
from stdio import write
from stdio import writeln
from sys import exit
# set up board
row1 = ["_", "|", "_", "|", "_"]
row2 = ["_", "|", "_", "|", "_"]
row3 = ["_", "|", "_", "|", "_"]
# make a spot for a record of moves
record = []


def board():
    # print the board 
    global row1
    global row2 
    global row3
    global record
    write(row1[0])
    write(row1[1])
    write(row1[2])
    write(row1[3])
    writeln(row1[4])
    write(row2[0])
    write(row2[1])
    write(row2[2])
    write(row2[3])
    writeln(row2[4])
    write(row3[0])
    write(row3[1])
    write(row3[2])
    write(row3[3])
    writeln(row3[4])


def player_one():
    global row1
    global row2 
    global row3
    global record
    # accept a value to represent a move
    turn = (input("Choose a position 1-9: "))
    try:
        turn = int(turn)
    except:
        print("Please enter a number 1-9")
        player_one()
    try:
        # if the turn has already been made, ask for another input
        if turn in record:
            turn = int(input("Choose a position 1-9 which has not been taken yet: "))
            # change inputs into the correct move on board
            if turn == 1:
                row1[0] = "x"
            elif turn == 2:
                row1[2] = "x"
            elif turn == 3:
                row1[4] = "x"
            elif turn == 4:
                row2[0] = "x"
            elif turn == 5:
                row2[2] = "x"
            elif turn == 6:
                row2[4] = "x"
            elif turn == 7:
                row3[0] = "x"
            elif turn == 8:
                row3[2] = "x"
            elif turn == 9:
                row3[4] = "x"
            else:
                # if input isn't 1-9 call this function again to get a proper input
                print("Not a valid entry")
                player_one()
        else:
            # accept input for move
            if turn == 1:
                row1[0] = "x"
            elif turn == 2:
                row1[2] = "x"
            elif turn == 3:
                row1[4] = "x"
            elif turn == 4:
                row2[0] = "x"
            elif turn == 5:
                row2[2] = "x"
            elif turn == 6:
                row2[4] = "x"
            elif turn == 7:
                row3[0] = "x"
            elif turn == 8:
                row3[2] = "x"
            elif turn == 9:
                row3[4] = "x"
            else:
                print("Not a valid entry")
                player_one()
    except:
        # if there is an error this will mark where the error is
        print("Player one error")
        player_one()
    # add this move to the record so that moves will not be repeated        
    record.append(turn)


def player_two():
    # see comments for player one, should be identical except x's are o's
    global row1
    global row2 
    global row3
    global record
    turn = (input("Choose a position 1-9: "))
    try:
        turn = int(turn)
        if turn in record:
            turn = int(input("Choose a position 1-9 which has not been taken yet: "))
            if turn == 1:
                row1[0] = "o"
            elif turn == 2:
                row1[2] = "o"
            elif turn == 3:
                row1[4] = "o"
            elif turn == 4:
                row2[0] = "o"
            elif turn == 5:
                row2[2] = "o"
            elif turn == 6:
                row2[4] = "o"
            elif turn == 7:
                row3[0] = "o"
            elif turn == 8:
                row3[2] = "o"
            elif turn == 9:
                row3[4] = "o"
            else: 
                print("Not a valid entry")
                player_two()
        else:
            if turn == 1:
                row1[0] = "o"
            elif turn == 2:
                row1[2] = "o"
            elif turn == 3:
                row1[4] = "o"
            elif turn == 4:
                row2[0] = "o"
            elif turn == 5:
                row2[2] = "o"
            elif turn == 6:
                row2[4] = "o"
            elif turn == 7:
                row3[0] = "o"
            elif turn == 8:
                row3[2] = "o"
            elif turn == 9:
                row3[4] = "o"
            else: 
                print("Not a valid entry")
                player_two()
    except:
        print("Player two error")
        player_two()
    record.append(turn)


def check_win():
    global row1
    global row2 
    global row3
    global record
    # check rows coloumns and diagnols for a win
    check_row_win()
    check_col_win()
    check_diag_win()
    if check_row_win() == False and check_col_win == False and check_diag_win == False:
        return False


def check_row_win():
    global row1
    global row2 
    global row3
    global record
    # check to see if one player controls all three parts of a row
    if row1[0] == "x" and row1[2] == "x" and row1[4] == "x":
        print("Player one wins by row 1!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row2[0] == "x" and row2[2] == "x" and row2[4] == "x":
        print("Player one wins by row 2!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row3[0] == "x" and row3[2] == "x" and row3[4] == "x":
        print("Player one wins by row 3!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row1[0] == "o" and row1[2] == "o" and row1[4] == "o":
        print("Player two wins by row 1!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row2[0] == "o" and row2[2] == "o" and row2[4] == "o":
        print("Player two wins by row 2!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row3[0] == "o" and row3[2] == "o" and row3[4] == "o":
        print("Player two wins by row 3!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    else:
        return False

    
def check_col_win():
    global row1
    global row2 
    global row3
    global record
    # check to see if one player controls all three parts of a coloumn
    if row1[0] == "x" and row2[0] == "x" and row3[0] == "x":
        print("Player one wins by coloumn 1!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row1[2] == "x" and row2[2] == "x" and row3[2] == "x":
        print("Player one wins by coloumn 2!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row1[4] == "x" and row2[4] == "x" and row3[4] == "x":
        print("Player one wins by coloumn 3!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row1[0] == "o" and row2[0] == "o" and row3[0] == "o":
        print("Player two wins by coloumn 1!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row1[2] == "o" and row2[2] == "o" and row3[2] == "o":
        print("Player two wins by coloumn 2!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row1[4] == "o" and row2[4] == "o" and row3[4] == "o":
        print("Player two wins by coloumn 3!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    else:
        return False


def check_diag_win():
    global row1
    global row2 
    global row3
    global record
    # check to see if one player controls all three parts of a diagnol
    if row1[0] == "x" and row2[2] == "x" and row3[4] == "x":
        print("Player one wins by diagnol 1!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row1[4] == "x" and row2[2] == "x" and row3[0] == "x":
        print("Player one wins by diagnol 2!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row1[0] == "o" and row2[2] == "o" and row3[4] == "o":
        print("Player two wins by diagnol 1!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    elif row1[4] == "o" and row2[2] == "o" and row3[0] == "o":
        print("Player two wins by diagnol 2!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()
        return True
    else:
       return False


def check_tie():
    global row1
    global row2 
    global row3
    global record
    # check to see if there is no win at the end of game
    if check_row_win() == False and check_col_win() == False and check_diag_win() == False:
        print("Tie Game!")
        again = input("Do you want to play again? y/n ")
        if again == "y":
            row1 = ["_", "|", "_", "|", "_"]
            row2 = ["_", "|", "_", "|", "_"]
            row3 = ["_", "|", "_", "|", "_"]
            record = []
            game()
        else:
            print("See you again soon!")
            exit()


def game():
    global row1
    global row2 
    global row3
    global record
    # call each function to create a playable game
    board()
    player_one()
    board()
    player_two()
    board()
    player_one()
    board()
    player_two()
    board()
    player_one()
    board()
    check_win()
    player_two()
    board()
    check_win()
    player_one()
    board()
    check_win()
    player_two()
    board()
    check_win()
    player_one()
    board()
    check_win()
    check_tie()


game()