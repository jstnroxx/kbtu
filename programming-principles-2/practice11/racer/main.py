#Imports
import pygame, sys
from pygame.locals import *
import random, time

from pathlib import Path

#Initialzing 
pygame.init()

BASE_DIR = Path(__file__).parent
MEDIA_DIR = BASE_DIR / "media"

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
COINS_COLLIDABLE = True

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(MEDIA_DIR / "AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(MEDIA_DIR / "Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(MEDIA_DIR / "Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        
        self.weight = random.randint(1, 3)
        weightSurf = font_small.render(str(self.weight), True, (0, 255, 0))
        weightRect = weightSurf.get_rect(center = self.image.get_rect().center)

        self.image.blit(weightSurf, weightRect)
        
    #Update coin's weight and appearance
    def redraw(self):
        self.image = pygame.image.load(MEDIA_DIR / "Coin.png")
        self.rect = self.image.get_rect()
        
        self.weight = random.randint(1, 3)
        weightSurf = font_small.render(str(self.weight), True, (0, 255, 0))
        weightRect = weightSurf.get_rect(center = self.image.get_rect().center)

        self.image.blit(weightSurf, weightRect)
        
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            global COINS_COLLIDABLE
            COINS_COLLIDABLE = True
            
            self.redraw()
        
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.image.set_alpha(255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(MEDIA_DIR / "Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    money = font_small.render("Coins: " + str(COINS), True, BLACK)
    
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(money, (10, scores.get_height() + 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(MEDIA_DIR / "crash.wav").play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()
          
    #Look for collision between Player and Coin
    coinHit = pygame.sprite.spritecollideany(P1, coins)
    
    #To be run if collision occurs between Player and Coin
    if coinHit and COINS_COLLIDABLE:
        COINS_COLLIDABLE = False
        coinHit.image.set_alpha(0)
        
        pygame.mixer.Sound(MEDIA_DIR / "deposit.wav").play()

        COINS += coinHit.weight
        SPEED = 5 + ((COINS // 3) * 0.5) 
                      
        
    pygame.display.update()
    FramePerSec.tick(FPS)
