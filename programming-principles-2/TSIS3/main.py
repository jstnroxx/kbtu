import pygame, sys, time

from pygame.locals import *

from racer import (
    Enemy, Coin, Player,
    font, font_small,
    BLACK, WHITE, RED,
    SCREEN_WIDTH, SCREEN_HEIGHT,
    MEDIA_DIR,
)

# Initialization
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

background = pygame.image.load(MEDIA_DIR / "AnimatedStreet.png")
game_over  = font.render("Game Over", True, BLACK)

# Game state
SPEED = 5
SCORE = 0
COINS = 0

# Initiate sprites
P1 = Player()
E1 = Enemy(SPEED)
C1 = Coin(SPEED)

enemies     = pygame.sprite.Group(E1)
coins       = pygame.sprite.Group(C1)
all_sprites = pygame.sprite.Group(P1, E1, C1)

# Main loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    scores_surf = font_small.render("Score: " + str(SCORE), True, BLACK)
    coins_surf = font_small.render("Coins: " + str(COINS),  True, BLACK)
    DISPLAYSURF.blit(scores_surf, (10, 10))
    DISPLAYSURF.blit(coins_surf, (10, scores_surf.get_height() + 10))

    # Move and draw all sprites
    P1.move()
    SCORE = E1.move(SPEED, SCORE)
    C1.move(SPEED)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Enemy collision
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(MEDIA_DIR / "crash.wav").play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
            
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Coin collision
    coin_hit = pygame.sprite.spritecollideany(P1, coins)
    if coin_hit and coin_hit.collidable:
        coin_hit.collidable = False
        coin_hit.image.set_alpha(0)

        pygame.mixer.Sound(MEDIA_DIR / "deposit.wav").play()

        COINS += coin_hit.weight
        SPEED  = 5 + ((COINS // 3) * 0.5)

    pygame.display.update()
    FramePerSec.tick(FPS)