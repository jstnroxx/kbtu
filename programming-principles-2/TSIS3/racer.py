import pygame
import random
import time

from pygame.locals import *
from pathlib import Path

pygame.init()

# Paths 
BASE_DIR  = Path(__file__).parent
MEDIA_DIR = BASE_DIR / "assets"

# Screen constants 
SCREEN_WIDTH  = 400
SCREEN_HEIGHT = 600

# Colors 
BLUE       = (0,   0,   255)
RED        = (255, 0,   0)
GREEN      = (0,   255, 0)
BLACK      = (0,   0,   0)
WHITE      = (255, 255, 255)
YELLOW     = (255, 220, 0)
CYAN       = (0,   220, 255)
ORANGE     = (255, 140, 0)

# Fonts (initialised once here, imported everywhere)
font       = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
font_tiny  = pygame.font.SysFont("Verdana", 14)

# Difficulty presets
DIFFICULTY = {
    "Easy":   {"base_speed": 4,  "enemy_count": 1, "obstacle_interval": 4000},
    "Normal": {"base_speed": 5,  "enemy_count": 2, "obstacle_interval": 2800},
    "Hard":   {"base_speed": 7,  "enemy_count": 3, "obstacle_interval": 1800},
}


def get_difficulty_cfg(name: str) -> dict:
    return DIFFICULTY.get(name, DIFFICULTY["Normal"])


# Safe-spawn helper
def safe_x(player_rect: pygame.Rect, margin: int = 60) -> int:
    for _ in range(20):
        x = random.randint(40, SCREEN_WIDTH - 40)
        if abs(x - player_rect.centerx) >= margin:
            return x
        
    return random.randint(40, SCREEN_WIDTH - 40)


#  Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image  = pygame.image.load(MEDIA_DIR / "Player.png").convert_alpha()
        self.rect   = self.image.get_rect(center=(160, 520))
        self.shield = False

    def move(self, speed=None):
        keys = pygame.key.get_pressed()
        
        if self.rect.left > 0 and (keys[K_LEFT] or keys[K_a]):
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and (keys[K_RIGHT] or keys[K_d]):
            self.rect.move_ip(5, 0)

    def draw_shield_ring(self, surface: pygame.Surface) -> None:
        if self.shield:
            pygame.draw.circle(surface, CYAN,
                               self.rect.center,
                               max(self.rect.width, self.rect.height) // 2 + 6,
                               3)


#  Enemy (traffic car)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, player_rect: pygame.Rect):
        super().__init__()
        self.image = pygame.image.load(MEDIA_DIR / "Enemy.png").convert_alpha()
        self.rect  = self.image.get_rect()
        self._respawn(player_rect)

    def _respawn(self, player_rect: pygame.Rect) -> None:
        self.rect.center = (safe_x(player_rect), -random.randint(0, 200))

    def move(self, speed: float, score: int, player_rect: pygame.Rect) -> int:
        self.rect.move_ip(0, speed)
        
        if self.rect.top > SCREEN_HEIGHT:
            score += 1
            self._respawn(player_rect)
            
        return score


#  Obstacle (static barrier)
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, player_rect: pygame.Rect):
        super().__init__()
        self.image = pygame.image.load(MEDIA_DIR / "Barrier.png").convert_alpha()
        self.rect  = self.image.get_rect()
        self._respawn(player_rect)

    def _respawn(self, player_rect: pygame.Rect) -> None:
        self.rect.center = (safe_x(player_rect, margin=70), -random.randint(20, 150))

    def move(self, speed: float, player_rect: pygame.Rect) -> None:
        self.rect.move_ip(0, speed * 0.75)
        
        if self.rect.top > SCREEN_HEIGHT:
            self._respawn(player_rect)


# Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self, player_rect: pygame.Rect):
        super().__init__()
        self.collidable = True
        self._load_image()
        self.rect.center = (safe_x(player_rect), -random.randint(0, 300))

    def _load_image(self) -> None:
        self.image  = pygame.image.load(MEDIA_DIR / "Coin.png").convert_alpha()
        self.rect   = self.image.get_rect()
        self.weight = random.randint(1, 3)
        
        w_surf = font_small.render(str(self.weight), True, GREEN)
        w_rect = w_surf.get_rect(center=self.image.get_rect().center)
        
        self.image.blit(w_surf, w_rect)

    def move(self, speed: float, player_rect: pygame.Rect) -> None:
        self.rect.move_ip(0, speed)
        
        if self.rect.top > SCREEN_HEIGHT:
            self.collidable = True
            self._load_image()
            self.rect.center = (safe_x(player_rect), 0)
            self.image.set_alpha(255)


#  Power-ups
class _PowerUp(pygame.sprite.Sprite):
    image_file: str = "PowerUp.png"
    kind: str = "powerup"

    def __init__(self, player_rect: pygame.Rect):
        super().__init__()
        self.image      = pygame.image.load(MEDIA_DIR / self.image_file).convert_alpha()
        self.rect        = self.image.get_rect()
        self.collidable  = True
        self.rect.center = (safe_x(player_rect, margin=50), -random.randint(0, 200))

    def move(self, speed: float, player_rect: pygame.Rect) -> None:
        self.rect.move_ip(0, speed * 0.9)
        
        if self.rect.top > SCREEN_HEIGHT:
            self.collidable = True
            self.image.set_alpha(255)
            self.rect.center = (safe_x(player_rect, margin=50), 0)


class NitroPowerUp(_PowerUp):
    image_file = "Nitro.png"
    kind       = "nitro"
    DURATION   = 4.0


class ShieldPowerUp(_PowerUp):
    """Absorbs one collision."""
    image_file = "Shield.png" 
    kind       = "shield"


#  PowerUpManager
class PowerUpManager:
    def __init__(self):
        self.active:    str | None = None
        self.end_time:  float      = 0.0
        self.bonus_pts: int        = 0

    def activate(self, kind: str) -> None:
        self.active = kind
        
        if kind == "nitro":
            self.end_time = time.time() + NitroPowerUp.DURATION
        else:
            self.end_time = float("inf") # shield has no timer
        self.bonus_pts += 50

    def consume_shield(self) -> None:
        if self.active == "shield":
            self.active   = None
            self.end_time = 0.0

    def update(self) -> None:
        if self.active and self.active != "shield":
            if time.time() >= self.end_time:
                self.active   = None
                self.end_time = 0.0

    @property
    def nitro_active(self) -> bool:
        return self.active == "nitro"

    @property
    def shield_active(self) -> bool:
        return self.active == "shield"

    @property
    def remaining(self) -> float:
        if self.active and self.end_time != float("inf"):
            return max(0.0, self.end_time - time.time())
        
        return 0.0

    def draw_hud(self, surface: pygame.Surface, y_start: int) -> None:
        if not self.active:
            return
        
        label_color = YELLOW if self.active == "nitro" else CYAN
        text = ("NITRO  " + f"{self.remaining:.1f}s") if self.active == "nitro" else "SHIELD  ACTIVE"
        label = font_small.render(text, True, label_color)
        surface.blit(label, (10, y_start))
        
        if self.active == "nitro":
            pct   = self.remaining / NitroPowerUp.DURATION
            bar_w = 120
            pygame.draw.rect(surface, (80, 80, 80), (10, y_start + 22, bar_w, 8), border_radius=4)
            pygame.draw.rect(surface, YELLOW, (10, y_start + 22, int(bar_w * pct), 8), border_radius=4)