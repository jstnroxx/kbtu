import pygame
import ball

# Game configurations
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BALL_COLOR = (255, 0, 0)
BG_COLOR = (255, 255, 255)
BALL_RADIUS = 25

CURRENT_COORDINATES = {    # Define the ball initial position here
    "X" : 250,
    "Y" : 250
} 

STEP = 20    # How many pixels the ball travels with one key press

FPS = 60

# Game logics
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressedKeys = pygame.key.get_pressed()
    CURRENT_COORDINATES = ball.ballMovement((WINDOW_WIDTH, WINDOW_HEIGHT), BALL_RADIUS, pressedKeys, CURRENT_COORDINATES, STEP)
    
    screen.fill(BG_COLOR)
    ball.drawBall(screen, BALL_COLOR, tuple(CURRENT_COORDINATES.values()), BALL_RADIUS)
            
    pygame.display.flip()
    clock.tick(FPS)