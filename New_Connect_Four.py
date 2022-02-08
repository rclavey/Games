# imports:
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
            x = (col + 1) * 100
            y = (row + 1) * 100
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
    height = len(positions)
    width = len(positions[0]) 
    # check cols
    for i in range(width):
        for j in range(height - 3):
            # animate (comment out next 5 lines for speed, keep for graphics)
            x = (i + 1) * 100
            y = (j + 1) * 100
            pygame.draw.circle(WINDOW, GREEN, (x, y), CIRC + 10, 15)
            pygame.display.update()
            time.sleep(.2)
            if positions[i][j] == 1 and positions[i - 1][j] == 1 and positions[i - 2][j] == 1 and positions[i - 3][j] == 1:
                print("Red Wins by col")
                return True
    return False
    # check rows
    for j in range(height):
        for i in range(width - 3):
            x = (i + 1) * 100
            y = (j + 1) * 100
            if positions[i][j] == 1 and positions[i][j + 1] == 1 and positions[i][j + 2] == 1 and positions[i][j + 3] == 1:
                print("Red Wins by row")
                return True
    # check diags negative
    for i in range(width - 3):
        for j in range(3, height):
            if positions[i][j] == 1 and positions[i + 1][j - 1] == 1 and positions[i + 2][j - 2] == 1 and positions[i + 3][j - 3] == 1:
                print("Red wins by positive diaganol")
                return True
    # check diags positive
    for i in range(width - 3):
        for j in range(height - 3):
            if positions[i][j] == 1 and positions[i + 1][j + 1] == 1 and positions[i + 2][j + 2] == 1 and positions[i + 3][j + 3] == 1:
                print("Red wins by negative diaganol")
                return True
    return False



# check yellow pieces for win conditions
def check_yellow(positions):
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
    i = 0
    positions = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
    clock = pygame.time.Clock()
    run = True
    count = 42
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
