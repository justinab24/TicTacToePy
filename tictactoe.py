import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
CROSS_SPACE = 55
BLUE = (0, 0, 255)
ORANGE = (237, 135, 45)
BACKGROUND_COLOR = (245, 224, 66)
GRID_COLOR = (141, 66, 245)
GRID_WIDTH = 12
BOARD_ROWS = 3
BOARD_COLS = 3


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BACKGROUND_COLOR)

board = np.zeros((BOARD_ROWS,BOARD_COLS))
#print(board)

#pygame.draw.line(screen, BLUE, (10,10), (300,300), 10)

def drawLines():
    pygame.draw.line(screen, GRID_COLOR, (0,200), (600,200), GRID_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, (0,400), (600,400), GRID_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, (200,0), (200,600), GRID_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, (400,0), (400,600), GRID_WIDTH)

def markSquare(row, col, pl):
    board[row][col] = pl

def openSquare(row, col):
    if board[row][col] == 0:
        return True
    else: 
        return False

def fullBoard():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def resetBoard():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

def drawShapes():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, BLUE, (int(col * 200 + 200//2), int(row * 200 + 200//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, ORANGE, (col * 200 + CROSS_SPACE , row * 200 + 200 - CROSS_SPACE), (col * 200 + 200 - CROSS_SPACE, row * 200 + CROSS_SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, ORANGE, (col * 200 + CROSS_SPACE , row * 200 + CROSS_SPACE), (col * 200 + 200 - CROSS_SPACE, row * 200 + 200 - CROSS_SPACE), CROSS_WIDTH)

def checkWin(pl):
    for col in range(BOARD_COLS):
        if board[0][col] == pl and board[1][col] == pl and board[2][col] == pl:
            vertVictoryLine(col, pl)
            return True
    
    for row in range(BOARD_ROWS):
        if board[row][0] == pl and board[row][1] == pl and board[row][2] == pl:
            horzVictoryLine(row, pl)
            return True
    
    if board[2][0] == pl and board[1][1] == pl and board[0][2] == pl:
        ascDiagVictoryLine(pl)
        return True

    if board[0][0] == pl and board[1][1] == pl and board[2][2] == pl:
        descDiagVictoryLine(pl)
        return True

    return False

def vertVictoryLine(col, pl):
    Xpos = col * 200 + 100
    if pl == 1:
         color = BLUE
    elif pl == 2:
        color = ORANGE
    
    pygame.draw.line(screen, color, (Xpos, 15), (Xpos, HEIGHT - 15), 15)

def horzVictoryLine(row, pl):
    Ypos = row * 200 + 100
    if pl == 1:
         color = BLUE
    elif pl == 2:
        color = ORANGE
    
    pygame.draw.line(screen, color, (15, Ypos), (WIDTH - 15, Ypos), 15)


def ascDiagVictoryLine(pl):
    if pl == 1:
         color = BLUE
    elif pl == 2:
        color = ORANGE

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)
    
def descDiagVictoryLine(pl):
    if pl == 1:
         color = BLUE
    elif pl == 2:
        color = ORANGE

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def playAgain():
    screen.fill(BACKGROUND_COLOR)
    drawLines()
    pl == 1
    resetBoard()

drawLines()

pl = 1
gameOver = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:

            mouseX = event.pos[0]
            mouseY = event.pos[1]


            rowClicked = int(mouseY // 200)
            colClicked = int(mouseX // 200)

            if openSquare(rowClicked, colClicked):
                if pl == 1:
                    markSquare(rowClicked, colClicked, 1)
                    if checkWin(pl):
                        gameOver = True
                    pl = 2
                elif pl == 2:
                    markSquare(rowClicked, colClicked, 2)
                    if checkWin(pl):
                        gameOver = True
                    pl = 1

                drawShapes()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                playAgain()
                pl = 1
                gameOver = False

    pygame.display.update()


