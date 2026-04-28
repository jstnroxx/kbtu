import pygame
import random

from pygame.locals import *
from pathlib import Path

pygame.init()

BASE_DIR = Path(__file__).parent
MEDIA_DIR = BASE_DIR / "assets"

# Screen constants
SCREEN_WIDTH  = 400
SCREEN_HEIGHT = 600

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.image.load(MEDIA_DIR / "Enemy.png")
        self.rect  = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self, speed, score):
        score += 0
        self.rect.move_ip(0, speed)
        
        if self.rect.bottom > SCREEN_HEIGHT:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            
        return score


class Coin(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self._load_image()
        self.collidable = True

    def _load_image(self):
        self.image = pygame.image.load(MEDIA_DIR / "Coin.png")
        self.rect  = self.image.get_rect()
        self.weight = random.randint(1, 3)
        
        weight_surf = font_small.render(str(self.weight), True, (0, 255, 0))
        weight_rect = weight_surf.get_rect(center=self.image.get_rect().center)
        self.image.blit(weight_surf, weight_rect)

    def move(self, speed):
        self.rect.move_ip(0, speed)
        
        if self.rect.bottom > SCREEN_HEIGHT:
            self.collidable = True
            self._load_image()
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.image.set_alpha(255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(MEDIA_DIR / "Player.png")
        self.rect  = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if keys[K_LEFT] or keys[K_a]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if keys[K_RIGHT] or keys[K_d]:
                self.rect.move_ip(5, 0)