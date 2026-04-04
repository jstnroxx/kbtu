import pygame
import clock
import utility

pygame.init()

# Game configurations
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BG_COLOR = (255, 255, 255)
FONT_PREFERENCES = ["Comic Sans MS"]
WATCHFACE_RADIUS = 175

FPS = 1

# Preload numbers to blit
one = utility.createText("1", FONT_PREFERENCES, 32, (0, 0, 0))
two = utility.createText("2", FONT_PREFERENCES, 32, (0, 0, 0))
three = utility.createText("3", FONT_PREFERENCES, 32, (0, 0, 0))
four  = utility.createText("4", FONT_PREFERENCES, 32, (0, 0, 0))
five = utility.createText("5", FONT_PREFERENCES, 32, (0, 0, 0))
six = utility.createText("6", FONT_PREFERENCES, 32, (0, 0, 0))
seven = utility.createText("7", FONT_PREFERENCES, 32, (0, 0, 0))
eight = utility.createText("8", FONT_PREFERENCES, 32, (0, 0, 0))
nine = utility.createText("9", FONT_PREFERENCES, 32, (0, 0, 0))
ten = utility.createText("10", FONT_PREFERENCES, 32, (0, 0, 0))
eleven = utility.createText("11", FONT_PREFERENCES, 32, (0, 0, 0))
twelve = utility.createText("12", FONT_PREFERENCES, 32, (0, 0, 0))

# Preload number positions
centerX = WINDOW_WIDTH // 2
centerY = WINDOW_HEIGHT // 2

numbers = [twelve, one, two, three, four, five, six, seven, eight, nine, ten, eleven]
numberPositions = []

for num in range(12):
    hour = num if num != 0 else 12
    position = utility.getClockPosition(hour, numbers[num], WATCHFACE_RADIUS, centerX, centerY)
    numberPositions.append(position)

# Game logics
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mickey's Clock")
pyClock = pygame.time.Clock()

minuteHand = utility.getImage("images/rightHand.png")
secondHand = utility.getImage("images/leftHand.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(BG_COLOR)
    
    currentTime = clock.getCurrentTime()
    
    secondAngle = 150 - ((currentTime["seconds"] + currentTime["milliseconds"] / 1000) * 6)
    screen.blit(*utility.rotateHand(secondHand, (centerX, centerY), (0, 0), secondAngle))
    
    minuteAngle = 215 - ((currentTime["minutes"] + currentTime["seconds"] / 60) * 6)
    screen.blit(*utility.rotateHand(minuteHand, (centerX, centerY), (86, 0), minuteAngle))
    
    for number in enumerate(numbers):
        screen.blit(number[1], numberPositions[number[0]])
   
    pygame.display.flip()
    pyClock.tick(FPS)
    