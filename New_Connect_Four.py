import pygame
import numpy as np
import time

# constants:
WIDTH = 800
HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 180)
RED = (200, 0, 0)
YELLOW = (240, 240, 0)
GREEN =(0, 255, 0)
FPS = 60
CIRC = 40

# Functions:

# display game
def set_window(positions):
    WINDOW.fill(WHITE)
    # board:
    pygame.draw.rect(WINDOW, BLUE, (50, 50, (WIDTH - 100), (HEIGHT - 100)), width = 0)
    for col in range(7):
        for row in range(6):
            x, y = (col + 1) * 100, (row + 1) * 100
            if positions[row][col] == 0:
                pygame.draw.circle(WINDOW, WHITE, (x, y), CIRC)
            elif positions[row][col] == 1:
                pygame.draw.circle(WINDOW, RED, (x, y), CIRC)
            else:
                pygame.draw.circle(WINDOW, YELLOW, (x, y), CIRC)
    # update display
    pygame.display.update()


# check red pieces for win conditions
def check_red(positions):
    # check cols
    for row in range(0, 3):
        for col in range(0, 7):
            if positions[row][col] == 1 and positions[row + 1][col] == 1 and positions[row + 2][col] == 1 and positions[row + 3][col] == 1:
                return True
    #check rows
    for row in range(0, 6):
        for col in range(0, 4):
            if positions[row][col] == 1 and positions[row][col + 1] == 1 and positions[row][col + 2] == 1 and positions[row][col + 3] == 1:
                return True
    #check diags positive
    for row in range(0, 4):
        for col in range(3, 7):
            if positions[row][col] == 1 and positions[row + 1][col - 1] == 1 and positions[row + 2][col - 2] == 1 and positions[row + 3][col - 3] == 1:
                return True
    # check diags negative
    for row in range(0, 3):
        for col in range(0, 4):
            if positions[row][col] == 1 and positions[row + 1][col + 1] == 1 and positions[row + 2][col + 2] == 1 and positions[row + 3][col + 3] == 1:
                return True
    return False



# check yellow pieces for win conditions
def check_yellow(positions):
        # check cols
    for row in range(0, 3):
        for col in range(0, 7):
            if positions[row][col] == 2 and positions[row + 1][col] == 2 and positions[row + 2][col] == 2 and positions[row + 3][col] == 2:
                return True
    #check rows
    for row in range(0, 6):
        for col in range(0, 4):
            if positions[row][col] == 2 and positions[row][col + 1] == 2 and positions[row][col + 2] == 2 and positions[row][col + 3] == 2:
                return True
    #check diags positive
    for row in range(0, 4):
        for col in range(3, 7):
            if positions[row][col] == 2 and positions[row + 1][col - 1] == 2 and positions[row + 2][col - 2] == 2 and positions[row + 3][col - 3] == 2:
                return True
    # check diags negative
    for row in range(0, 3):
        for col in range(0, 4):
            if positions[row][col] == 2 and positions[row + 1][col + 1] == 2 and positions[row + 2][col + 2] == 2 and positions[row + 3][col + 3] == 2:
                return True
    return False


# check for any win conditions
def check_win(positions):
    if check_red(positions) or check_yellow(positions):
        return True
    else:
        return False


# get the lowest empty row for use in move function
def get_low_row(positions: list, col: int):
    lowest_empty = []
    for i in range(6):
        if positions[i][col] == 0:
            lowest_empty.append(i)
    if lowest_empty:
        return int(max(lowest_empty))
    else:
        return -1


# assign a move based on click
def move(positions: list, row: int, col: int, i: int):
    player = i % 2
    # if spot is empty, change to current player
    if positions[row][col] == 0:
        # player one
        if player == 0:
            positions[row][col] = 1
        # player two
        else:
            positions[row][col] = 2


# main function to execute game
def main():
    positions = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
    clock = pygame.time.Clock()
    run = True
    count, i = 42, 0
    while run:
        clock.tick(FPS)
        # loop through events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # register clicks as moves
            if event.type == pygame.MOUSEBUTTONDOWN:
                col = (pygame.mouse.get_pos()[0] - 60) // 100
                # make move on board
                if col >= 0 and col <= 6:
                    row = get_low_row(positions, col)
                    if row >= 0:
                        move(positions, row, col, i)
                        i += 1
                        count -= 1
                print(positions)
                if count == 0 and not check_win(positions):
                    print("Tie Game")
                    pygame.quit()
                elif check_win(positions):
                    print("Winner")
                    pygame.quit()
        set_window(positions)
    pygame.quit()


if __name__ == "__main__":
    main()
