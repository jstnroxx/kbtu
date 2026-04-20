# Wormy (a Nibbles clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, pygame, sys
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
PURPLE    = (180,   0, 255)
ORANGE    = (255, 140,   0)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # syntactic sugar: index of the worm's head

FOOD_TYPES = [
    {'color' : RED, 'points' : 1, 'timer' : None},
    {'color' : ORANGE, 'points' : 2, 'timer' : 90},
    {'color' : PURPLE, 'points' : 3, 'timer' : 60}
]

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

# Set a random start point.
startx = random.randint(5, CELLWIDTH - 6)
starty = random.randint(5, CELLHEIGHT - 6)
wormCoords = [
    {'x': startx,     'y': starty},
    {'x': startx - 1, 'y': starty},
    {'x': startx - 2, 'y': starty}
]

def runGame():
    global wormCoords
    direction = RIGHT

    # Start the apple in a random place.
    food = spawnFood()

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # check if the worm has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return # game over
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return # game over
            
        # remove expired food
        food = tickFood(food)

        # check if worm has eaten food
        if wormCoords[HEAD]['x'] == food['x'] and wormCoords[HEAD]['y'] == food['y']:
            for _ in range(food['points'] - 1):
                wormCoords.append(wormCoords[-1])
            
            food = spawnFood() # set a new food somewhere
        else:
            del wormCoords[-1] # remove worm's tail segment

        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawFood(food)
        drawScoreLevel(len(wormCoords) - 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
def spawnFood():
    foodType = random.choice(FOOD_TYPES)
    
    pos = getRandomLocation()
    
    return {
        'x' : pos['x'],
        'y' : pos['y'],
        'color' : foodType['color'],
        'points' : foodType['points'],
        'timer' : foodType['timer']
    }
    
def tickFood(food):
    if food['timer'] and food['timer'] > 0:
        food['timer'] -= 1
    elif food['timer'] == 0:
        return spawnFood()
        
    return food

def drawFood(food):
    x = food['x'] * CELLSIZE
    y = food['y'] * CELLSIZE
    pygame.draw.rect(DISPLAYSURF, food['color'], (x, y, CELLSIZE, CELLSIZE))
    
    if food['timer'] is not None:
        maxTimer = next(f['timer'] for f in FOOD_TYPES if f['points'] == food['points'])
        ratio = food['timer'] / maxTimer
        barW = int(CELLSIZE * ratio)
        pygame.draw.rect(DISPLAYSURF, WHITE, (x, y + CELLSIZE - 3, barW, 3))

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Snake!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Snake!', True, GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame


def terminate():
    pygame.quit()
    sys.exit()

# determine next apple position which is not wall or snake's body
def getRandomLocation():
    global wormCoords
    randomLocation = {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
    
    while randomLocation in wormCoords:
        randomLocation = {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
    
    return randomLocation


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    
    global wormCoords
    wormCoords = [
        {'x': startx,     'y': starty},
        {'x': startx - 1, 'y': starty},
        {'x': startx - 2, 'y': starty}
    ]
    
    global FPS
    FPS = 15

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        
# update FPS (affects game speed) according to level (15 + (1 for each level)) but not greater than 60
def speedupSnake(level):
    global FPS
    
    if not FPS >= 60:
    
        if level > 1:
            NEWFPS = 15 + level - 1
            
            if NEWFPS == FPS:
                return
            else:
                FPS = NEWFPS
        
# draw level and score info text
def drawScoreLevel(score):
    snakeLevel = score // 3 + 1
    
    levelSurf = BASICFONT.render('Level: %s' % (snakeLevel), True, WHITE)
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    
    levelRect = levelSurf.get_rect()
    scoreRect = scoreSurf.get_rect()
    
    levelRect.topleft = (WINDOWWIDTH - 120, 10)
    scoreRect.topleft = (WINDOWWIDTH - 120, levelSurf.get_height() + 10)
    
    DISPLAYSURF.blit(levelSurf, levelRect)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    
    speedupSnake(snakeLevel)


def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()