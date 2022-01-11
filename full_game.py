import pygame
import random
# set size of game
pygame.init()
WIDTH, HEIGHT = 400, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# set window title
pygame.display.set_caption("Tic Tac Toe")
# set common colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
# set images for x and o with proper size scale
RED_X_IMAGE = pygame.image.load("/Users/richie/Documents/First_Code/games/tic_tac_toe/red_x.png")
RED_X = pygame.transform.scale(RED_X_IMAGE,(100,100))
BLUE_O_IMAGE = pygame.image.load("/Users/richie/Documents/First_Code/games/tic_tac_toe/blue_o.png")
BLUE_O = pygame.transform.scale(BLUE_O_IMAGE,(80,80))
# set frames per second
FPS = 60
pygame.font.init()
FONT = pygame.font.Font("freesansbold.ttf", 25)
j = 0
i = 0
positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
record = []
sel = [0, 1, 2, 3, 4, 5, 6, 7, 8]
winner = None
# opening menu
def menu_screen():
    WINDOW.fill((WHITE))
    pygame.draw.rect(WINDOW, BLUE, (0, 0, 200, 400))
    pygame.draw.rect(WINDOW, RED, (200, 0, 200, 400))
    multi1 = FONT.render("Play with", True, WHITE)
    multi2 = FONT.render("a Friend", True, WHITE)
    single1 = FONT.render("Play a", True, WHITE)
    single2 = FONT.render("Computer", True, WHITE)
    WINDOW.blit(multi1, (25,150))
    WINDOW.blit(multi2, (25,175))
    WINDOW.blit(single1, (225,150))
    WINDOW.blit(single2, (225,175))
    pygame.display.update()


# set the window with starting position
def set_window():
    global positions
    global j
    WINDOW.fill((WHITE))
    pygame.draw.line(WINDOW, BLACK, (25, 133), (375, 133), 5)
    pygame.draw.line(WINDOW, BLACK, (25, 266), (375, 266), 5)
    pygame.draw.line(WINDOW, BLACK, (133, 25), (133, 375), 5)
    pygame.draw.line(WINDOW, BLACK, (266, 25), (266, 375), 5)
    if positions[0] == 1:
        WINDOW.blit(RED_X,(20,20))
    if positions[1] == 1:
        WINDOW.blit(RED_X,(153,20))
    if positions[2] == 1:
        WINDOW.blit(RED_X,(286,20))
    if positions[3] == 1:
        WINDOW.blit(RED_X,(20,153))
    if positions[4] == 1:
        WINDOW.blit(RED_X,(153,153))
    if positions[5] == 1:
        WINDOW.blit(RED_X,(286,153))
    if positions[6] == 1:
        WINDOW.blit(RED_X,(20,286))
    if positions[7] == 1:
        WINDOW.blit(RED_X,(153,286))
    if positions[8] == 1:
        WINDOW.blit(RED_X,(286,286))
    if positions[0] == 2:
        WINDOW.blit(BLUE_O,(20,20))
    if positions[1] == 2:
        WINDOW.blit(BLUE_O,(153,20))
    if positions[2] == 2:
        WINDOW.blit(BLUE_O,(286,20))
    if positions[3] == 2:
        WINDOW.blit(BLUE_O,(20,153))
    if positions[4] == 2:
        WINDOW.blit(BLUE_O,(153,153))
    if positions[5] == 2:
        WINDOW.blit(BLUE_O,(286,153))
    if positions[6] == 2:
        WINDOW.blit(BLUE_O,(20,286))
    if positions[7] == 2:
        WINDOW.blit(BLUE_O,(153,286))
    if positions[8] == 2:
        WINDOW.blit(BLUE_O,(286,286))
    pygame.display.update()


# check for a win condition
def check_win():
    global positions
    global j
    global winner
    # check rows for a win
    if positions[0] == positions[1] and positions[1] == positions[2] and positions[0] == 1:
        print("Game Over Row One")
        print("Player One Wins")
        winner = 1
        return True
    if positions[3] == positions[4] and positions[4] == positions[5] and positions[3] == 1:
        print("Game Over Row Two")
        print("Player One Wins")
        winner = 1
        return True
    if positions[6] == positions[7] and positions[7] == positions[8] and positions[6] == 1:
        print("Game Over Row Three")
        print("Player One Wins")
        winner = 1
        return True
    # check coloumns for a win
    if positions[0] == positions[3] and positions[3] == positions[6] and positions[0] == 1:
        print("Game Over Col One")
        print("Player One Wins")
        winner = 1
        return True
    if positions[1] == positions[4] and positions[4] == positions[7] and positions[1] == 1:
        print("Game Over Col Two")
        print("Player One Wins")
        winner = 1
        return True
    if positions[2] == positions[5] and positions[5] == positions[8] and positions[2] == 1:
        print("Game Over Col Two")
        print("Player One Wins")
        winner = 1
        return True
    # check diagnols for a win
    if positions[0] == positions[4] and positions[4] == positions[8] and positions[0] == 1:
        print("Game Over Diag One")
        print("Player One Wins")
        winner = 1
        return True
    if positions[2] == positions[4] and positions[4] == positions[6] and positions[2] == 1:
        print("Game Over Diag Two")
        print("Player One Wins")
        winner = 1
        return True

    # check rows for win
    if positions[0] == positions[1] and positions[1] == positions[2] and positions[0] == 2:
        print("Game Over Row One")
        print("Player Two Wins")
        winner = 2
        return True
    if positions[3] == positions[4] and positions[4] == positions[5] and positions[3] == 2:
        print("Game Over Row Two")
        print("Player Two Wins")
        winner = 2
        return True
    if positions[6] == positions[7] and positions[7] == positions[8] and positions[6] == 2:
        print("Game Over Row Three")
        print("Player Two Wins")
        winner = 2
        return True
    # check coloumns for a win
    if positions[0] == positions[3] and positions[3] == positions[6] and positions[0] == 2:
        print("Game Over Col One")
        print("Player Two Wins")
        winner = 2
        return True
    if positions[1] == positions[4] and positions[4] == positions[7] and positions[1] == 2:
        print("Game Over Col Two")
        print("Player Two Wins")
        winner = 2
        return True
    if positions[2] == positions[5] and positions[5] == positions[8] and positions[2] == 2:
        print("Game Over Col Three")
        print("Player Two Wins")
        winner = 2
        return True
    # check diagnols for a win
    if positions[0] == positions[4] and positions[4] == positions[8] and positions[0] == 2:
        print("Game Over Diag One")
        print("Player Two Wins")
        winner = 2
        return True
    if positions[2] == positions[4] and positions[4] == positions[6] and positions[2] == 2:
        print("Game Over Diag Two")
        print("Player Two Wins")
        winner = 2
        return True
    else:
        return False


# reset game when over
def reset_game():
    global positions
    global j
    global i
    global record
    global sel
    j = 0
    i = 0
    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    record = []
    sel = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# check for a tie
def check_tie():
    global positions
    if (positions[0] and positions[1] and positions[2] and positions[3] and positions[4] and positions[5] and positions[6] and positions[7] and positions[8] != 0) and not check_win():
        print("Tie Game")
        return True
    else:
        return False


# easy mode computer with random moves played
def easy():
    # get global variables
    global positions
    global record
    global multi
    global winner
    # set variables
    clock = pygame.time.Clock()
    run = True
    # set infinite while loop
    while run:
        clock.tick(FPS)
        # loop through events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # accept mouseclicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if mouse is clicked get position of click as represented on tic tac toe board
                if pygame.mouse.get_pressed()[0]:
                    player = True
                    if player:
                        pos = (pygame.mouse.get_pos()[0] // 133), (pygame.mouse.get_pos()[1] // 133)
                        if pos == (0,0):
                            pos = 0
                        if pos == (1,0):
                            pos = 1
                        if pos == (2,0):
                            pos = 2
                        if pos == (0,1):
                            pos = 3
                        if pos == (1,1):
                            pos = 4
                        if pos == (2,1):
                            pos = 5
                        if pos == (0,2):
                            pos = 6
                        if pos == (1,2):
                            pos = 7
                        if pos == (2,2):
                            pos = 8
                        # if player one moves set corresponding position to 1 as long as move isnt already taken, for player to set to 2
                        if not record.count(pos) > 0:
                            positions[pos] = 1
                            record.append(pos)
                            sel.pop(sel.index(pos))
                            player = False
                        else:
                            print("Not a valid move")
                        if check_win() or check_tie():
                            run = False
                    if not player and not check_win() and not check_tie():
                        easy_move()
                        player = True
                        if check_win() or check_tie():
                            run = False
        set_window()
    reset_game()
    multi = False
    main()


# generate random moves for easy mode computer
def easy_move():
    global positions
    global sel
    global record
    move = random.choice(sel)
    index = sel.index(move)
    if not record.count(move) > 0:
        positions[move] = 2
        record.append(move)
        sel.pop(index)
    else:
        easy_move()


# generate hard move using min_max()
def hard_move():
    global positions
    global record
    # set best score absurdly low and set best move to a place holder
    best_score = -1000
    best_move = 0
    # iterate through all positions
    for k in range(len(positions)):
        # only calculate for positions that are empty
        if positions[k] == 0:
            # set position equal to computer move to evaluate strength of position
            positions[k] == 2
            # call min_max function in order to get score of current iteration
            score = min_max(positions, 0, True)
            # set position back to unoccupied so board is not changed prematurely
            positions[k] = 0
            # not reaching here, means k_score is not more than best score
            # if k_score is bigger than the previous best, this is now the best move, replace the two
            if score is not None:
                if score > best_score:
                    best_score = score
                    best_move = k
    
    # return best_move for use in hard() function
    print()
    print("Thinking Finished") 
    print() 
    return best_move
    


# recursive min_max function returns score of moves 
def min_max(board, depth, maxing):
    global winner
    global positions
    # base cases
    # if winner is x, which is the player, return -1
    if winner == 1:
        return -1
    # if winner is o, which is the computer, return 1
    if winner == 2:
        return 1
    # if game is a tie, return 0
    if check_tie():
        return 0
    # if trying to maximize score to find computers best move do the following:
    if maxing:
        # set the best score to an absurdly low number
        best_score = -1000
        # iterate through all the positions in the game
        for k in range(len(positions)):
            # only look at positions which are not alrady taken
            if positions[k] == 0:
                # set each of these positions to the computers move
                positions[k] = 2
                # recursively call this function with the new board, and set maxing to false so the next iteration will be minimizing
                score = min_max(positions, 0, False)
                # set position back to 0 as to not disturb the board before a move is played
                winner = None
                positions[k] = 0
                # if the score for k is better than the current best score, replace it
                if score is not None:
                    if score > best_score:
                        best_score = score
    # if trying to minimize score to find opponents best move do the following:
    else:
        # set the best score to an absurdly high number to be replaced by lower numbers
        best_score = 1000
        score = int
        # iterate through all positions in the game
        for k in range(len(positions)):
            # only do calculations for positions that are open
            if positions[k] == 0:
                # if position k is open, mark it as x
                positions[k] = 1
                # recursively call this function with the new board and set maxing to true so the next iteration will be maximizing
                score = min_max(positions, 0, True)
                # set position of k back to 0 so that it does not change the board prior to making a move
                winner = None
                positions[k] = 0
                # if the score of k is lower than the best score, replace the best score with k
                if score is not None:
                    if score < best_score:
                        best_score = score
        # after iterating through all the possible game states, return the best score
        return best_score


# hard mode computer with perfect moves via min_max
def hard():
    # get global variables
    global positions
    global record
    global multi
    global winner
    # set variables
    clock = pygame.time.Clock()
    run = True
    # set infinite while loop
    while run:
        clock.tick(FPS)
        # loop through events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # accept mouseclicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if mouse is clicked get position of click as represented on tic tac toe board
                if pygame.mouse.get_pressed()[0]:
                    player = True
                    if player:
                        pos = (pygame.mouse.get_pos()[0] // 133), (pygame.mouse.get_pos()[1] // 133)
                        if pos == (0,0):
                            pos = 0
                        if pos == (1,0):
                            pos = 1
                        if pos == (2,0):
                            pos = 2
                        if pos == (0,1):
                            pos = 3
                        if pos == (1,1):
                            pos = 4
                        if pos == (2,1):
                            pos = 5
                        if pos == (0,2):
                            pos = 6
                        if pos == (1,2):
                            pos = 7
                        if pos == (2,2):
                            pos = 8
                        # if player one moves set corresponding position to 1 as long as move isnt already taken, for player to set to 2
                        if player and not check_win() and not check_tie(): 
                            if not record.count(pos) > 0:
                                positions[pos] = 1
                                record.append(pos)
                                #sel.pop(sel.index(pos))
                                player = False
                            else:
                                print("Not a valid move")
                        else:
                            run = False
                    if not player and not check_win() and not check_tie():
                        pos = hard_move()
                        positions[pos] = 2
                        record.append(pos)
                        #sel.pop(sel.index(pos))
                        player = True
                        if check_win() or check_tie():
                            run = False
                    print(positions)
        set_window()
    reset_game()
    multi = False
    main()


# get response from player for easy mode or hard mode
def tic_tac_toe_single():
    clock = pygame.time.Clock()
    run = True
    global multi
    global single
    global FPS
    playing = True
    ez = False
    ai = False
    # set infinite while loop
    while playing:
        clock.tick(FPS)
        # loop through events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            # accept mouseclicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if mouse is clicked get position of click as represented on tic tac toe board
                if pygame.mouse.get_pressed()[0]:
                    # use integer division to determine if user picks left or right side of screen
                    choice = (pygame.mouse.get_pos()[0] // 200)
                    if choice == 0:
                        # if user clicks left side of screen, load multiplayer tic tac toe
                        ez = True
                        ai = False
                    else:
                        # if user does not click the left side, load single player menu screen
                        ai = True
                        ez = False
        single_screen()
        if ez:
            easy()
        elif ai:
            hard()
    pygame.quit()


# generate screen for tic_tac_toe_single()
def single_screen():
    WINDOW.fill((WHITE))
    pygame.draw.rect(WINDOW, BLUE, (0,0, 200, 400))
    pygame.draw.rect(WINDOW, RED, (200,0, 200, 400))
    easy = FONT.render("Easy Mode", True, WHITE)
    hard = FONT.render("Hard Mode", True, WHITE)
    WINDOW.blit(easy, (25,150))
    WINDOW.blit(hard, (225,150))
    pygame.display.update()


# pass and play tic tac toe
def tic_tac_toe_multi():
    # get global variables
    global positions
    global j
    global i
    global record
    global multi
    global winner
    # set variables
    clock = pygame.time.Clock()
    run = True
    
    # set infinite while loop
    while run:
        clock.tick(FPS)
        # loop through events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # accept mouseclicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if mouse is clicked get position of click as represented on tic tac toe board
                if pygame.mouse.get_pressed()[0]:
                    i += 1
                    j = i % 2
                    pos = (pygame.mouse.get_pos()[0] // 133), (pygame.mouse.get_pos()[1] // 133)
                    if pos == (0,0):
                        pos = 0
                    if pos == (1,0):
                        pos = 1
                    if pos == (2,0):
                        pos = 2
                    if pos == (0,1):
                        pos = 3
                    if pos == (1,1):
                        pos = 4
                    if pos == (2,1):
                        pos = 5
                    if pos == (0,2):
                        pos = 6
                    if pos == (1,2):
                        pos = 7
                    if pos == (2,2):
                        pos = 8
                    # if player one moves set corresponding position to 1 as long as move isnt already taken, for player to set to 2
                    if not record.count(pos) > 0:
                        if j:
                            positions[pos] = 1
                            record.append(pos)
                        if not j:
                            positions[pos] = 2
                            record.append(pos)
                    else:
                        i -= 1
                        print("Not a valid move")
                    if check_win() or check_tie():
                        run = False
        set_window()
    reset_game()
    multi = False
    main()


# display screen prompting choice for single or multiplayer
def main():
    clock = pygame.time.Clock()
    run = True
    global multi
    global single
    multi = False
    single = False
    global FPS
    # set infinite while loop
    while run:
        clock.tick(FPS)
        # loop through events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # accept mouseclicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if mouse is clicked get position of click as represented on tic tac toe board
                if pygame.mouse.get_pressed()[0]:
                    # use integer division to determine if user picks left or right side of screen
                    choice = (pygame.mouse.get_pos()[0] // 200)
                    if choice == 0:
                        # if user clicks left side of screen, load multiplayer tic tac toe
                        multi = True
                        single = False
                    else:
                        # if user does not click the left side, load single player menu screen
                        single = True
                        multi = False
        menu_screen()
        # if multiplayer is selected multi is true and tic_tac_toe_multi is called to pass and play
        if multi:
            tic_tac_toe_multi()
        # if multi is false and single is true then display options for single player
        elif single:
            tic_tac_toe_single()
    pygame.quit()


# execute main()
if __name__ == "__main__":
    main()