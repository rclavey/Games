import pygame
import random
import time
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
sel = [0, 1, 2, 3, 4, 5, 6, 7, 8]
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


# check wins for x
def check_x(move: int, positions: list):
    # get the col the previous move was in
    c = move % 3
    r = move // 3
    # check that col to see if they are all x
    if positions[c] == 1 and positions[c + 3] == 1 and positions[c + 6] == 1:
        return True
    # check rows to see if they are all x
    elif positions[r * 3] == 1 and positions[(r * 3) + 1] == 1 and positions[(r * 3) + 2] == 1:
        return True
    # check diags to see if they are all x
    elif positions[0] == positions[4] and positions[4] == positions[8] and positions[0] == 1:
        return True
    elif positions[2] == positions[4] and positions[4] == positions[6] and positions[2] == 1:
        return True
    return False


# check wins for o
def check_o(move: int, positions: list):
        # get the col the previous move was in
    c = move % 3
    r = move // 3
    # check all cols to see if they are o
    if positions[c] == 2 and positions[c + 3] == 2 and positions[c + 6] == 2:
        return True
    # check all rows to see if they are o
    elif positions[r * 3] == 2 and positions[(r * 3) + 1] == 2 and positions[(r * 3) + 2] == 2:
        return True
    # check diags to see if they are o
    elif positions[0] == positions[4] and positions[4] == positions[8] and positions[0] == 2:
        return True
    elif positions[2] == positions[4] and positions[4] == positions[6] and positions[2] == 2:
        return True
    return False


# check for a win condition
def check_win(move: int, positions: list):
    return check_x(move, positions) or check_o(move, positions)


# reset game when over
def reset_game():
    time.sleep(3)
    global positions
    global j
    global i
    global sel
    j = 0
    i = 0
    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sel = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# check for a tie
def check_tie(move: int, positions: list):
    if (positions[0] and positions[1] and positions[2] and positions[3] and positions[4] and positions[5] and positions[6] and positions[7] and positions[8] != 0) and not check_win(move, positions):
        #print("Tie Game")
        return True
    else:
        return False


# easy mode computer with random moves played
def easy():
    # get global variables
    global positions
    global multi
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
                        col, row = (pygame.mouse.get_pos()[0] // 133), (pygame.mouse.get_pos()[1] // 133)
                        # set move equal to the position of board clicked on, row is multiplied by three because moving one row down moves it three in list
                        move = col + 3 * row
                        # if player one moves set corresponding position to 1 as long as move isnt already taken, for player to set to 2
                        if positions[move] == 0:
                            positions[move] = 1
                            sel.pop(sel.index(move))
                            player = False
                        else:
                            print("Not a valid move")
                        if check_win(move, positions) or check_tie(move, positions):
                            run = False
                    if not player:
                        easy_move()
                        player = True
                        if check_win(move, positions) or check_tie(move, positions):
                            run = False
        set_window()
    reset_game()
    multi = False
    main()


# generate random moves for easy mode computer
def easy_move():
    global positions
    global sel
    move = random.choice(sel)
    index = sel.index(move)
    if positions[move] == 0:
        positions[move] = 2
        sel.pop(index)
    else:
        easy_move()


# generate hard move using min_max()
def hard_move(positions):
    # set best score absurdly low and set best move to a place holder
    best_score = -1000
    best_move = 9
    a: list = []
    names = ["top left", "top mid", "top right", "mid left", "mid mid", "mid right", "bottom left", "bottom mid", "bottom right"]
    # iterate through all positions
    print(positions)
    for k in range(len(positions)):
        # only calculate for positions that are empty
        if positions[k] == 0:
            # set position equal to computer move to evaluate strength of position
            positions[k] = 2
            # call min_max function in order to get score of current iteration
            score = min_max(positions, k, 1, True)
            print(score, "is the score of ", names[k])
            # set position back to unoccupied so board is not changed prematurely
            positions[k] = 0
            # not reaching here, means k_score is not more than best score
            # if k_score is bigger than the previous best, this is now the best move, replace the two
            if score > best_score:
                best_score = score
                best_move = k
                a: list = []
                a.append(best_move)
            elif score == best_move:
                a.append(k)
    # return best_move for use in hard() function
    print("list of all the best moves: ", a)
    print("Thinking Finished") 
    print() 
    return int(random.choice(a))


# recursive min_max function returns score of moves 
def min_max(positions: list, move: int, depth: int, maxing: bool):
    # base cases
    # if winner is x, which is the player, return -1
    if check_x(move, positions):
        #print("1 won after ", depth, "turns")
        return -1.0 * depth
    # if winner is o, which is the computer, return 1
    elif check_o(move, positions):
        #print("2 won after ", depth, "turns")
        return 1.0 / depth
    # if game is a tie, return 0
    elif check_tie(move, positions):
        #print("game is a tie after ", depth, "turns")
        return 0.0
    # if trying to maximize score to find computers best move do the following:
    if maxing:
        # set the best score to an absurdly low number
        best_score = 1000
        # iterate through all the positions in the game
        for k in range(len(positions)):
            # only look at positions which are not alrady taken
            if positions[k] == 0:
                # set each of these positions to the computers move
                positions[k] = 1
                # recursively call this function with the new board, and set maxing to false so the next iteration will be minimizing
                score = min_max(positions, k, (depth + 1), False)
                #print(positions)
                # set position back to 0 as to not disturb the board before a move is played
                positions[k] = 0
                # if the score for k is better than the current best score, replace it
                if score < best_score:
                    best_score = score
    # if trying to minimize score to find opponents best move do the following:
    else:
        # set the best score to an absurdly high number to be replaced by lower numbers
        best_score = -1000
        # iterate through all positions in the game
        for k in range(len(positions)):
            # only do calculations for positions that are open
            if positions[k] == 0:
                # if position k is open, mark it as x
                positions[k] = 2
                # recursively call this function with the new board and set maxing to true so the next iteration will be maximizing
                score = min_max(positions, k, (depth + 1), True)
                #print(positions)
                # set position of k back to 0 so that it does not change the board prior to making a move
                positions[k] = 0
                # if the score of k is lower than the best score, replace the best score with k
                if score > best_score:
                    best_score = score
    # after iterating through all the possible game states, return the best score
    return best_score


# hard mode computer with perfect moves via min_max
def hard():
    # get global variables
    global positions
    global multi
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
                        col, row = (pygame.mouse.get_pos()[0] // 133), (pygame.mouse.get_pos()[1] // 133)
                        # set move equal to the position of board clicked on, row is multiplied by three because moving one row down moves it three in list
                        move = col + 3 * row
                        # if player one moves set corresponding position to 1 as long as move isnt already taken, for player to set to 
                        if positions[move] == 0:
                            positions[move] = 1
                            if check_win(move, positions) or check_tie(move, positions):
                                run = False
                                break
                            player = False
                        else:
                            print("Not a valid move")
                    if not player:
                        comp = hard_move(positions)
                        positions[comp] = 2
                        if check_win(comp, positions) or check_tie(comp, positions):
                            run = False
                            break
                        player = True
                        print("this is the computer move: ", comp)
                        
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
    global multi
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
                    col, row = (pygame.mouse.get_pos()[0] // 133), (pygame.mouse.get_pos()[1] // 133)
                    # set move equal to the position of board clicked on, row is multiplied by three because moving one row down moves it three in list
                    move = col + 3 * row
                    # if player one moves set corresponding position to 1 as long as move isnt already taken, for player to set to 2
                    if positions[move] == 0:
                        if j:
                            positions[move] = 1
                        if not j:
                            positions[move] = 2
                    else:
                        i -= 1
                        print("Not a valid move")
                    #if check_win() or check_tie():
                    if check_win(move, positions) or check_tie(move, positions):
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
