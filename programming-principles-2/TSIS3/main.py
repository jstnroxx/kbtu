import pygame
import sys

from pygame.locals import *

from racer import (
    Player, Enemy, Coin, Obstacle, NitroPowerUp, ShieldPowerUp,
    PowerUpManager, get_difficulty_cfg,
    font, font_small,
    BLACK, WHITE, RED, GREEN, YELLOW, CYAN,
    SCREEN_WIDTH, SCREEN_HEIGHT, MEDIA_DIR,
)
from persistence import add_entry, calculate_score
from ui import (
    load_settings, save_settings,
    main_menu_screen, settings_screen,
    game_over_screen, leaderboard_screen,
    username_entry_screen,
)

# Pygame init 
pygame.init()
pygame.mixer.init()

FPS           = 60
FramePerSec   = pygame.time.Clock()
DISPLAYSURF   = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Road Racer")

background  = pygame.image.load(MEDIA_DIR / "AnimatedStreet.png").convert()
game_over_s = font.render("Game Over", True, BLACK)

# Sound helpers (respect settings)
def play_sound(path, settings: dict) -> None:
    if settings.get("sound", True):
        try:
            pygame.mixer.Sound(path).play()
        except Exception:
            pass


#  One full game session
def run_game(settings: dict, username: str) -> dict:
    cfg        = get_difficulty_cfg(settings.get("difficulty", "Normal"))
    base_speed = cfg["base_speed"]
    obs_interval = cfg["obstacle_interval"] # ms between new obstacles

    SPEED      = float(base_speed)
    SCORE      = 0
    COINS      = 0
    DISTANCE   = 0.0 # accumulated as float; cast to int for display/saving
    pup_mgr    = PowerUpManager()

    # Sprites 
    P1 = Player()

    # Variable number of enemies based on difficulty
    enemy_list = [Enemy(P1.rect) for _ in range(cfg["enemy_count"])]
    C1         = Coin(P1.rect)
    nitro_pup  = NitroPowerUp(P1.rect)
    shield_pup = ShieldPowerUp(P1.rect)

    enemies    = pygame.sprite.Group(*enemy_list)
    coins      = pygame.sprite.Group(C1)
    powerups   = pygame.sprite.Group(nitro_pup, shield_pup)
    obstacles  = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(P1, *enemy_list, C1, nitro_pup, shield_pup)

    # Obstacle spawn timer
    obstacle_timer    = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, obs_interval)

    # Difficulty scaling tracker
    last_scale_coins = 0 # scale speed every 3 coins collected

    clock = pygame.time.Clock()

    # Game loop 
    while True:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                return {"score": 0, "distance": int(DISTANCE), "coins": COINS, "action": "menu"}

            # Spawn a new obstacle on timer
            if event.type == obstacle_timer:
                obs = Obstacle(P1.rect)
                obstacles.add(obs)
                all_sprites.add(obs)

        # Speed: nitro boost or base
        pup_mgr.update()
        effective_speed = SPEED * 1.8 if pup_mgr.nitro_active else SPEED

        # Move sprites
        P1.move()
        P1.shield = pup_mgr.shield_active

        for enemy in enemy_list:
            SCORE = enemy.move(effective_speed, SCORE, P1.rect)

        C1.move(effective_speed, P1.rect)

        for obs in obstacles:
            obs.move(effective_speed, P1.rect)

        nitro_pup.move(effective_speed, P1.rect)
        shield_pup.move(effective_speed, P1.rect)

        # Distance accumulates proportional to speed each frame
        DISTANCE += effective_speed * 0.05

        # Difficulty scaling 
        if COINS - last_scale_coins >= 3:
            last_scale_coins = COINS
            SPEED = base_speed + (COINS // 3) * 0.5
            
            # Tighten obstacle spawn interval (floor: 800 ms)
            new_interval = max(800, obs_interval - (COINS // 3) * 100)
            
            pygame.time.set_timer(obstacle_timer, new_interval)

        # Draw 
        DISPLAYSURF.blit(background, (0, 0))

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)

        # Shield ring around player
        P1.draw_shield_ring(DISPLAYSURF)

        # HUD 
        hud_y = 10
        lines = [
            f"Score:    {SCORE}",
            f"Coins:    {COINS}",
            f"Dist:     {int(DISTANCE)} m",
            f"Speed:    {effective_speed:.1f}",
        ]
        for line in lines:
            surf = font_small.render(line, True, BLACK)
            DISPLAYSURF.blit(surf, (10, hud_y))
            hud_y += surf.get_height() + 2

        pup_mgr.draw_hud(DISPLAYSURF, hud_y + 4)

        # Collisions: enemy / obstacle 
        hit_enemy = pygame.sprite.spritecollideany(P1, enemies)
        hit_obs   = pygame.sprite.spritecollideany(P1, obstacles)

        if hit_enemy or hit_obs:
            if pup_mgr.shield_active:
                pup_mgr.consume_shield()
                
                # Move the colliding sprite off-screen so it can't re-trigger
                # next frame while the player is still overlapping its rect
                sprite = hit_enemy or hit_obs
                sprite.rect.y = -200
                sprite.image.set_alpha(0)
            else:
                # Game over
                play_sound(MEDIA_DIR / "crash.wav", settings)
                pygame.time.set_timer(obstacle_timer, 0) # stop timer

                final_score = calculate_score(COINS, int(DISTANCE), pup_mgr.bonus_pts)
                add_entry(username, final_score, int(DISTANCE), COINS)

                action = game_over_screen(DISPLAYSURF, clock, final_score, int(DISTANCE), COINS)
                return {"score": final_score, "distance": int(DISTANCE),
                        "coins": COINS, "action": action}

        # Collision: coin 
        coin_hit = pygame.sprite.spritecollideany(P1, coins)
        
        if coin_hit and coin_hit.collidable:
            coin_hit.collidable = False
            coin_hit.image.set_alpha(0)
            play_sound(MEDIA_DIR / "deposit.wav", settings)
            COINS += coin_hit.weight

        #─ Collision: power-ups 
        pup_hit = pygame.sprite.spritecollideany(P1, powerups)
        
        if pup_hit and pup_hit.collidable:
            pup_hit.collidable = False
            pup_hit.image.set_alpha(0)
            pup_mgr.activate(pup_hit.kind)

        pygame.display.update()


#  Top-level state machine
def main():
    settings = load_settings()
    username = ""

    screen = "menu" # menu | username | game | leaderboard | settings

    while True:
        if screen == "menu":
            choice = main_menu_screen(DISPLAYSURF, FramePerSec)
            if choice == "play":
                if not username:
                    screen = "username"
                else:
                    screen = "game"
            elif choice == "leaderboard":
                screen = "leaderboard"
            elif choice == "settings":
                screen = "settings"
            elif choice == "quit":
                pygame.quit()
                sys.exit()

        elif screen == "username":
            username = username_entry_screen(DISPLAYSURF, FramePerSec)
            screen   = "game"

        elif screen == "game":
            result = run_game(settings, username)
            screen = "game" if result["action"] == "retry" else "menu"

        elif screen == "leaderboard":
            leaderboard_screen(DISPLAYSURF, FramePerSec)
            screen = "menu"

        elif screen == "settings":
            settings = settings_screen(DISPLAYSURF, FramePerSec, settings)
            screen   = "menu"


main()