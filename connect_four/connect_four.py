import pygame
import time
WIDTH = 800
HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 180)
RED = (200, 0, 0)
YELLOW = (240, 240, 0)
FPS = 60
CIRC = 40
j = 0
i = 0
col1 = 0
col2 = 0
col3 = 0
col4 = 0
col5 = 0
col6 = 0
col7 = 0


class Rows:
    def __init__(self, row, pos1, state1, pos2, state2, pos3, state3, pos4, state4, pos5, state5, pos6, state6, pos7, state7):
        self.row = row
        self.pos1 = pos1
        self.state1 = state1
        self.pos2 = pos2
        self.state2 = state2
        self.pos3 = pos3
        self.state3 = state3
        self.pos4 = pos4
        self.state4 = state4
        self.pos5 = pos5
        self.state5 = state5
        self.pos6 = pos6
        self.state6 = state6
        self.pos7 = pos7
        self.state7 = state7
    def make_row(self):
        pygame.draw.circle(WINDOW, self.state1, (self.pos1, self.row), CIRC)
        pygame.draw.circle(WINDOW, self.state2, (self.pos2, self.row), CIRC)
        pygame.draw.circle(WINDOW, self.state3, (self.pos3, self.row), CIRC)
        pygame.draw.circle(WINDOW, self.state4, (self.pos4, self.row), CIRC)
        pygame.draw.circle(WINDOW, self.state5, (self.pos5, self.row), CIRC)
        pygame.draw.circle(WINDOW, self.state6, (self.pos6, self.row), CIRC)
        pygame.draw.circle(WINDOW, self.state7, (self.pos7, self.row), CIRC)


row6 = Rows(100, 100, WHITE, 200, WHITE, 300, WHITE, 400, WHITE, 500, WHITE, 600, WHITE, 700, WHITE)
row5 = Rows(200, 100, WHITE, 200, WHITE, 300, WHITE, 400, WHITE, 500, WHITE, 600, WHITE, 700, WHITE)
row4 = Rows(300, 100, WHITE, 200, WHITE, 300, WHITE, 400, WHITE, 500, WHITE, 600, WHITE, 700, WHITE)
row3 = Rows(400, 100, WHITE, 200, WHITE, 300, WHITE, 400, WHITE, 500, WHITE, 600, WHITE, 700, WHITE)
row2 = Rows(500, 100, WHITE, 200, WHITE, 300, WHITE, 400, WHITE, 500, WHITE, 600, WHITE, 700, WHITE)
row1 = Rows(600, 100, WHITE, 200, WHITE, 300, WHITE, 400, WHITE, 500, WHITE, 600, WHITE, 700, WHITE)


def set_window():
    WINDOW.fill(WHITE)
    # board:
    pygame.draw.rect(WINDOW, BLUE, (50, 50, (WIDTH - 100), (HEIGHT - 100)), width = 0)
    row6.make_row()
    row5.make_row()
    row4.make_row()
    row3.make_row()
    row2.make_row()
    row1.make_row()
    # update display
    pygame.display.update()


def check_hor():
    if row6.state1 == row6.state2 == row6.state3 == row6.state4 and row6.state1 != WHITE:
        if row6.state1 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row5.state1 == row5.state2 == row5.state3 == row5.state4 and row5.state1 != WHITE:
        if row5.state1 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row4.state1 == row4.state2 == row4.state3 == row4.state4 and row4.state1 != WHITE:
        if row4.state1 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row3.state1 == row3.state2 == row3.state3 == row3.state4 and row3.state1 != WHITE:
        if row3.state1 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row2.state1 == row2.state2 == row2.state3 == row2.state4 and row2.state1 != WHITE:
        if row2.state1 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row1.state1 == row1.state2 == row1.state3 == row1.state4 and row1.state1 != WHITE:
        if row1.state1 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row6.state2 == row6.state3 == row6.state4 == row6.state5 and row6.state5 != WHITE:
        if row6.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row5.state2 == row5.state3 == row5.state4 == row5.state5 and row5.state5 != WHITE:
        if row5.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row4.state2 == row4.state3 == row4.state4 == row4.state5 and row4.state5 != WHITE:
        if row4.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row3.state2 == row3.state3 == row3.state4 == row3.state5 and row3.state5 != WHITE:
        if row3.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row2.state2 == row2.state3 == row2.state4 == row2.state5 and row2.state5 != WHITE:
        if row2.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row1.state2 == row1.state3 == row1.state4 == row1.state5 and row1.state5 != WHITE:
        if row1.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row6.state3 == row6.state4 == row6.state5 == row6.state6 and row6.state5 != WHITE:
        if row6.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row5.state6 == row5.state3 == row5.state4 == row5.state5 and row5.state5 != WHITE:
        if row5.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row4.state6 == row4.state3 == row4.state4 == row4.state5 and row4.state5 != WHITE:
        if row4.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row3.state6 == row3.state3 == row3.state4 == row3.state5 and row3.state5 != WHITE:
        if row3.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row2.state6 == row2.state3 == row2.state4 == row2.state5 and row2.state5 != WHITE:
        if row2.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row1.state6 == row1.state3 == row1.state4 == row1.state5 and row1.state5 != WHITE:
        if row1.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row6.state3 == row6.state7 == row6.state5 == row6.state6 and row6.state5 != WHITE:
        if row6.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row5.state6 == row5.state7 == row5.state4 == row5.state5 and row5.state5 != WHITE:
        if row5.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row4.state6 == row4.state7 == row4.state4 == row4.state5 and row4.state5 != WHITE:
        if row4.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row3.state6 == row3.state7 == row3.state4 == row3.state5 and row3.state5 != WHITE:
        if row3.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row2.state6 == row2.state7 == row2.state4 == row2.state5 and row2.state5 != WHITE:
        if row2.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row1.state6 == row1.state7 == row1.state4 == row1.state5 and row1.state5 != WHITE:
        if row1.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    else:
        return False


def check_vert():
    if row6.state1 == row5.state1 == row4.state1 == row3.state1 and row3.state1 != WHITE:
        if row3.state1 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row2.state1 == row5.state1 == row4.state1 == row3.state1 and row3.state1 != WHITE:
        if row3.state1 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row2.state1 == row1.state1 == row4.state1 == row3.state1 and row3.state1 != WHITE:
        if row3.state1 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    else:
        return False
    

def check_diag():
    # positive slopes
    if row6.state7 == row5.state6 == row4.state5 == row3.state4 and row6.state7 != WHITE:
        if row6.state7 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row6.state6 == row5.state5 == row4.state4 == row3.state3 and row6.state6 != WHITE:
        if row6.state6 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row6.state5 == row5.state4 == row4.state3 == row3.state2 and row6.state5 != WHITE:
        if row6.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row6.state4 == row5.state3 == row4.state2 == row3.state1 and row6.state4 != WHITE:
        if row6.state4 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row5.state7 == row4.state6 == row3.state5 == row2.state4 and row5.state7 != WHITE:
        if row5.state7 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row5.state6 == row4.state5 == row3.state4 == row2.state3 and row5.state6 != WHITE:
        if row5.state6 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row5.state5 == row4.state4 == row3.state3 == row2.state2 and row5.state5 != WHITE:
        if row5.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row5.state4 == row4.state3 == row3.state2 == row2.state1 and row5.state4 != WHITE:
        if row5.state4 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row4.state7 == row3.state6 == row2.state5 == row1.state4 and row4.state7 != WHITE:
        if row4.state7 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row4.state6 == row3.state5 == row2.state4 == row1.state3 and row4.state6 != WHITE:
        if row4.state6 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row4.state5 == row3.state4 == row2.state3 == row1.state2 and row4.state5 != WHITE:
        if row4.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row4.state4 == row3.state3 == row2.state2 == row1.state1 and row4.state4 != WHITE:
        if row4.state4 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    # negative slopes
    if row1.state7 == row2.state6 == row3.state5 == row4.state4 and row1.state7 != WHITE:
        if row1.state7 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row1.state6 == row2.state5 == row3.state4 == row4.state3 and row1.state6 != WHITE:
        if row1.state6 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row1.state5 == row2.state4 == row3.state3 == row4.state2 and row1.state5 != WHITE:
        if row1.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row1.state4 == row2.state3 == row3.state2 == row4.state1 and row1.state4 != WHITE:
        if row1.state4 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row2.state7 == row3.state6 == row4.state5 == row5.state4 and row2.state7 != WHITE:
        if row2.state7 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row2.state6 == row3.state5 == row4.state4 == row5.state3 and row2.state6 != WHITE:
        if row2.state6 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row2.state5 == row3.state4 == row4.state3 == row5.state2 and row2.state5 != WHITE:
        if row2.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row2.state4 == row3.state3 == row4.state2 == row5.state1 and row2.state4 != WHITE:
        if row2.state4 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row3.state7 == row4.state6 == row5.state5 == row6.state4 and row3.state7 != WHITE:
        if row3.state7 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row3.state6 == row4.state5 == row5.state4 == row6.state3 and row3.state6 != WHITE:
        if row3.state6 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row3.state5 == row4.state4 == row5.state3 == row6.state2 and row3.state5 != WHITE:
        if row3.state5 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True
    if row3.state4 == row4.state3 == row5.state2 == row6.state1 and row3.state4 != WHITE:
        if row3.state4 == RED:
            print("Red Wins!")
            return True
        else:
            print("Yellow Wins!")
            return True

    else:
        return False


def check_win():
    check_hor()
    check_diag()
    check_vert()
    if check_hor() or check_diag() or check_vert():
        return True
    else:
        return False


def check_tie():
    if not check_win() and row6.state1 != WHITE and row6.state2 != WHITE and row6.state3 != WHITE and row6.state4 != WHITE and row6.state5 != WHITE and row6.state6 != WHITE and row6.state7 != WHITE:
        return True
    return False


def main():
    global j
    global i
    global col1
    global col2
    global col3
    global col4
    global col5
    global col6
    global col7
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        # loop through events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # register clicks as moves
            if event.type == pygame.MOUSEBUTTONDOWN:
                j = i % 2
                pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                # click on first col
                if pos[0] > 60 and pos[0] < 140:
                    col1 += 1
                    if j == 0:
                        if col1 == 1:
                            row1.state1 = RED
                            i += 1
                        if col1 == 2:
                            row2.state1 = RED
                            i += 1
                        if col1 == 3:
                            row3.state1 = RED
                            i += 1
                        if col1 == 4:
                            row4.state1 = RED
                            i += 1
                        if col1 == 5:
                            row5.state1 = RED
                            i += 1
                        if col1 == 6:
                            row6.state1 = RED
                            i += 1
                    if j == 1:
                        if col1 == 1:
                            row1.state1 = YELLOW
                            i += 1
                        if col1 == 2:
                            row2.state1 = YELLOW
                            i += 1
                        if col1 == 3:
                            row3.state1 = YELLOW
                            i += 1
                        if col1 == 4:
                            row4.state1 = YELLOW
                            i += 1
                        if col1 == 5:
                            row5.state1 = YELLOW
                            i += 1
                        if col1 == 6:
                            row6.state1 = YELLOW
                            i += 1
                # click on second col
                if pos[0] > 160 and pos[0] < 240:
                    col2 += 1
                    if j == 0:
                        if col2 == 1:
                            row1.state2 = RED
                            i += 1
                        if col2 == 2:
                            row2.state2 = RED
                            i += 1
                        if col2 == 3:
                            row3.state2 = RED
                            i += 1
                        if col2 == 4:
                            row4.state2 = RED
                            i += 1
                        if col2 == 5:
                            row5.state2 = RED
                            i += 1
                        if col2 == 6:
                            row6.state2 = RED
                            i += 1
                    if j == 1:
                        if col2 == 1:
                            row1.state2 = YELLOW
                            i += 1
                        if col2 == 2:
                            row2.state2 = YELLOW
                            i += 1
                        if col2 == 3:
                            row3.state2 = YELLOW
                            i += 1
                        if col2 == 4:
                            row4.state2 = YELLOW
                            i += 1
                        if col2 == 5:
                            row5.state2 = YELLOW
                            i += 1
                        if col2 == 6:
                            row6.state2 = YELLOW
                            i += 1
                # click on third col
                if pos[0] > 260 and pos[0] < 340:
                    col3 += 1
                    if j == 0:
                        if col3 == 1:
                            row1.state3 = RED
                            i += 1
                        if col3 == 2:
                            row2.state3 = RED
                            i += 1
                        if col3 == 3:
                            row3.state3 = RED
                            i += 1
                        if col3 == 4:
                            row4.state3 = RED
                            i += 1
                        if col3 == 5:
                            row5.state3 = RED
                            i += 1
                        if col3 == 6:
                            row6.state3 = RED
                            i += 1
                    if j == 1:
                        if col3 == 1:
                            row1.state3 = YELLOW
                            i += 1
                        if col3 == 2:
                            row2.state3 = YELLOW
                            i += 1
                        if col3 == 3:
                            row3.state3 = YELLOW
                            i += 1
                        if col3 == 4:
                            row4.state3 = YELLOW
                            i += 1
                        if col3 == 5:
                            row5.state3 = YELLOW
                            i += 1
                        if col3 == 6:
                            row6.state3 = YELLOW
                            i += 1
                # click on fourth col
                if pos[0] > 360 and pos[0] < 440:
                    col4 += 1
                    if j == 0:
                        if col4 == 1:
                            row1.state4 = RED
                            i += 1
                        if col4 == 2:
                            row2.state4 = RED
                            i += 1
                        if col4 == 3:
                            row3.state4 = RED
                            i += 1
                        if col4 == 4:
                            row4.state4 = RED
                            i += 1
                        if col4 == 5:
                            row5.state4 = RED
                            i += 1
                        if col4 == 6:
                            row6.state4 = RED
                            i += 1
                    if j == 1:
                        if col4 == 1:
                            row1.state4 = YELLOW
                            i += 1
                        if col4 == 2:
                            row2.state4 = YELLOW
                            i += 1
                        if col4 == 3:
                            row3.state4 = YELLOW
                            i += 1
                        if col4 == 4:
                            row4.state4 = YELLOW
                            i += 1
                        if col4 == 5:
                            row5.state4 = YELLOW
                            i += 1
                        if col4 == 6:
                            row6.state4 = YELLOW
                            i += 1
                # click on fifth col
                if pos[0] > 460 and pos[0] < 540:
                    col5 += 1
                    if j == 0:
                        if col5 == 1:
                            row1.state5 = RED
                            i += 1
                        if col5 == 2:
                            row2.state5 = RED
                            i += 1
                        if col5 == 3:
                            row3.state5 = RED
                            i += 1
                        if col5 == 4:
                            row4.state5 = RED
                            i += 1
                        if col5 == 5:
                            row5.state5 = RED
                            i += 1
                        if col5 == 6:
                            row6.state5 = RED
                            i += 1
                    if j == 1:
                        if col5 == 1:
                            row1.state5 = YELLOW
                            i += 1
                        if col5 == 2:
                            row2.state5 = YELLOW
                            i += 1
                        if col5 == 3:
                            row3.state5 = YELLOW
                            i += 1
                        if col5 == 4:
                            row4.state5 = YELLOW
                            i += 1
                        if col5 == 5:
                            row5.state5 = YELLOW
                            i += 1
                        if col5 == 6:
                            row6.state5 = YELLOW
                            i += 1
                # click on fifth col
                if pos[0] > 560 and pos[0] < 640:
                    col6 += 1
                    if j == 0:
                        if col6 == 1:
                            row1.state6 = RED
                            i += 1
                        if col6 == 2:
                            row2.state6 = RED
                            i += 1
                        if col6 == 3:
                            row3.state6 = RED
                            i += 1
                        if col6 == 4:
                            row4.state6 = RED
                            i += 1
                        if col6 == 5:
                            row5.state6 = RED
                            i += 1
                        if col6 == 6:
                            row6.state6 = RED
                            i += 1
                    if j == 1:
                        if col6 == 1:
                            row1.state6 = YELLOW
                            i += 1
                        if col6 == 2:
                            row2.state6 = YELLOW
                            i += 1
                        if col6 == 3:
                            row3.state6 = YELLOW
                            i += 1
                        if col6 == 4:
                            row4.state6 = YELLOW
                            i += 1
                        if col6 == 5:
                            row5.state6 = YELLOW
                            i += 1
                        if col6 == 6:
                            row6.state6 = YELLOW
                            i += 1
                # click on sixth col
                if pos[0] > 660 and pos[0] < 740:
                    col7 += 1
                    if j == 0:
                        if col7 == 1:
                            row1.state7 = RED
                            i += 1
                        if col7 == 2:
                            row2.state7 = RED
                            i += 1
                        if col7 == 3:
                            row3.state7 = RED
                            i += 1
                        if col7 == 4:
                            row4.state7 = RED
                            i += 1
                        if col7 == 5:
                            row5.state7 = RED
                            i += 1
                        if col7 == 6:
                            row6.state7 = RED
                            i += 1
                    if j == 1:
                        if col7 == 1:
                            row1.state7 = YELLOW
                            i += 1
                        if col7 == 2:
                            row2.state7 = YELLOW
                            i += 1
                        if col7 == 3:
                            row3.state7 = YELLOW
                            i += 1
                        if col7 == 4:
                            row4.state7 = YELLOW
                            i += 1
                        if col7 == 5:
                            row5.state7 = YELLOW
                            i += 1
                        if col7 == 6:
                            row6.state7 = YELLOW
                            i += 1
                check_win()
                if check_win() or check_tie():

                    pygame.quit()

        
        set_window()

    pygame.quit()


if __name__ == "__main__":
    main()
