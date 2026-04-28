import pygame
import json

from pathlib import Path
from persistence import load_leaderboard

# Paths 
BASE_DIR      = Path(__file__).parent
SETTINGS_FILE = BASE_DIR / "settings.json"

# Colors
BLACK      = (0,   0,   0)
WHITE      = (255, 255, 255)
GRAY       = (180, 180, 180)
DARK_GRAY  = (80,  80,  80)
RED        = (200, 50,  50)
GREEN      = (50,  200, 80)
YELLOW     = (230, 200, 50)
BLUE       = (50,  120, 220)
DARK_BG    = (20,  20,  30)
PANEL      = (35,  35,  50)
ACCENT     = (255, 200, 50)

# Default settings
DEFAULT_SETTINGS = {
    "sound":      True,
    "difficulty": "Normal", # "Easy" | "Normal" | "Hard"
}

DIFFICULTY_OPTIONS = ["Easy", "Normal", "Hard"]


#  Settings persistence
def load_settings() -> dict:
    if not SETTINGS_FILE.exists():
        return dict(DEFAULT_SETTINGS)
    try:
        with open(SETTINGS_FILE) as f:
            data = json.load(f)
            
        # fill missing keys with defaults
        for k, v in DEFAULT_SETTINGS.items():
            data.setdefault(k, v)
            
        return data
    except (json.JSONDecodeError, OSError):
        return dict(DEFAULT_SETTINGS)


def save_settings(settings: dict) -> None:
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)


#  Shared helpers
def _make_fonts():
    return {
        "title":  pygame.font.SysFont("Verdana", 48, bold=True),
        "large":  pygame.font.SysFont("Verdana", 32, bold=True),
        "medium": pygame.font.SysFont("Verdana", 22),
        "small":  pygame.font.SysFont("Verdana", 18),
    }


class Button:
    def __init__(self, rect: pygame.Rect, label: str, font: pygame.font.Font,
                 color=DARK_GRAY, hover_color=ACCENT, text_color=WHITE):
        self.rect        = rect
        self.label       = label
        self.font        = font
        self.color       = color
        self.hover_color = hover_color
        self.text_color  = text_color

    def draw(self, surface: pygame.Surface) -> None:
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        bg = self.hover_color if hovered else self.color
        
        pygame.draw.rect(surface, bg, self.rect, border_radius=8)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=8)
        
        text_surf = self.font.render(self.label, True, self.text_color if not hovered else BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event: pygame.event.Event) -> bool:
        return (event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and self.rect.collidepoint(event.pos))


def _draw_background(surface: pygame.Surface) -> None:
    surface.fill(DARK_BG)
    
    # subtle grid lines for depth
    for x in range(0, surface.get_width(), 40):
        pygame.draw.line(surface, PANEL, (x, 0), (x, surface.get_height()))
    for y in range(0, surface.get_height(), 40):
        pygame.draw.line(surface, PANEL, (0, y), (surface.get_width(), y))


#  Username Entry
def username_entry_screen(surface: pygame.Surface, clock: pygame.time.Clock) -> str:
    fonts   = _make_fonts()
    name    = ""
    cursor_visible = True
    cursor_timer   = 0

    while True:
        dt = clock.tick(60)
        cursor_timer += dt
        
        if cursor_timer >= 500:
            cursor_visible = not cursor_visible
            cursor_timer   = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip():
                    return name.strip()
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.unicode.isprintable() and len(name) < 16:
                    name += event.unicode

        _draw_background(surface)

        title = fonts["large"].render("ENTER YOUR NAME", True, ACCENT)
        surface.blit(title, title.get_rect(center=(surface.get_width() // 2, 180)))

        # Input box
        box = pygame.Rect(60, 270, 280, 60)
        pygame.draw.rect(surface, PANEL, box, border_radius=6)
        pygame.draw.rect(surface, ACCENT, box, 2, border_radius=6)

        display_str = name + ("|" if cursor_visible else " ")
        name_surf = fonts["large"].render(display_str, True, WHITE)
        surface.blit(name_surf, name_surf.get_rect(center=box.center).move(0, -3))

        hint = fonts["small"].render("Press ENTER to confirm", True, GRAY)
        surface.blit(hint, hint.get_rect(center=(surface.get_width() // 2, 350)))

        pygame.display.flip()


#  Main menu
def main_menu_screen(surface: pygame.Surface, clock: pygame.time.Clock) -> str:
    fonts = _make_fonts()
    W, H  = surface.get_width(), surface.get_height()
    cx    = W // 2

    buttons = [
        Button(pygame.Rect(cx - 100, 220, 200, 50), "PLAY",        fonts["large"], color=GREEN,     text_color=BLACK),
        Button(pygame.Rect(cx - 100, 290, 200, 50), "LEADERBOARD", fonts["medium"]),
        Button(pygame.Rect(cx - 100, 360, 200, 50), "SETTINGS",    fonts["medium"]),
        Button(pygame.Rect(cx - 100, 430, 200, 50), "QUIT",        fonts["medium"], color=RED),
    ]
    
    actions = ["play", "leaderboard", "settings", "quit"]

    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            for btn, action in zip(buttons, actions):
                if btn.is_clicked(event):
                    return action

        _draw_background(surface)

        title = fonts["title"].render("RACER", True, ACCENT)
        sub   = fonts["small"].render("Dodge. Collect. Survive.", True, GRAY)
        surface.blit(title, title.get_rect(center=(cx, 120)))
        surface.blit(sub,   sub.get_rect(center=(cx, 175)))

        for btn in buttons:
            btn.draw(surface)

        pygame.display.flip()


#  Settings
def settings_screen(surface: pygame.Surface, clock: pygame.time.Clock,
                    settings: dict) -> dict:
    fonts = _make_fonts()
    W, H  = surface.get_width(), surface.get_height()
    cx    = W // 2

    back_btn = Button(pygame.Rect(cx - 80, 500, 160, 45), "BACK", fonts["medium"])

    # Difficulty cycle button
    diff_btn  = Button(pygame.Rect(cx - 80, 360, 160, 45), "", fonts["medium"], color=BLUE)
    sound_btn = Button(pygame.Rect(cx - 80, 260, 160, 45), "", fonts["medium"])

    while True:
        clock.tick(60)

        # Update dynamic labels
        sound_btn.label = "Sound: ON" if settings["sound"] else "Sound: OFF"
        diff_btn.label  = f"Diff: {settings['difficulty']}"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_settings(settings)
                
                return settings
            if sound_btn.is_clicked(event):
                settings["sound"] = not settings["sound"]
            if diff_btn.is_clicked(event):
                idx = DIFFICULTY_OPTIONS.index(settings["difficulty"])
                settings["difficulty"] = DIFFICULTY_OPTIONS[(idx + 1) % len(DIFFICULTY_OPTIONS)]
            if back_btn.is_clicked(event):
                save_settings(settings)
                
                return settings

        _draw_background(surface)

        title = fonts["large"].render("SETTINGS", True, ACCENT)
        surface.blit(title, title.get_rect(center=(cx, 140)))

        sound_lbl = fonts["medium"].render("Audio", True, GRAY)
        surface.blit(sound_lbl, sound_lbl.get_rect(center=(cx, 230)))
        sound_btn.draw(surface)

        diff_lbl = fonts["medium"].render("Difficulty", True, GRAY)
        surface.blit(diff_lbl, diff_lbl.get_rect(center=(cx, 330)))
        diff_btn.draw(surface)

        hint = fonts["small"].render("(affects starting speed & spawn rate)", True, DARK_GRAY)
        surface.blit(hint, hint.get_rect(center=(cx, 430)))

        back_btn.draw(surface)
        pygame.display.flip()


#  Game Over
def game_over_screen(surface: pygame.Surface, clock: pygame.time.Clock,
                     score: int, distance: int, coins: int) -> str:
    fonts = _make_fonts()
    W     = surface.get_width()
    cx    = W // 2

    retry_btn = Button(pygame.Rect(cx - 110, 430, 200, 50), "RETRY",     fonts["large"], color=GREEN, text_color=BLACK)
    menu_btn  = Button(pygame.Rect(cx - 110, 500, 200, 50), "MAIN MENU", fonts["medium"])

    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "menu"
            if retry_btn.is_clicked(event):
                return "retry"
            if menu_btn.is_clicked(event):
                return "menu"

        _draw_background(surface)

        # Title
        title = fonts["title"].render("GAME OVER", True, RED)
        surface.blit(title, title.get_rect(center=(cx, 120)))

        # Stats panel
        panel = pygame.Rect(50, 190, W - 100, 200)
        
        pygame.draw.rect(surface, PANEL, panel, border_radius=10)
        pygame.draw.rect(surface, ACCENT, panel, 2, border_radius=10)

        stats = [
            ("Score",    str(score)),
            ("Distance", f"{distance} m"),
            ("Coins",    str(coins)),
        ]
        
        for i, (label, value) in enumerate(stats):
            y = panel.top + 30 + i * 55
            lbl_s = fonts["medium"].render(label, True, GRAY)
            val_s = fonts["large"].render(value,  True, WHITE)
            surface.blit(lbl_s, (panel.left + 20,       y))
            surface.blit(val_s, (panel.right - val_s.get_width() - 20, y))

        retry_btn.draw(surface)
        menu_btn.draw(surface)
        
        pygame.display.flip()


#  Leaderboard
def leaderboard_screen(surface: pygame.Surface, clock: pygame.time.Clock) -> None:
    fonts   = _make_fonts()
    W, H    = surface.get_width(), surface.get_height()
    cx      = W // 2
    entries = load_leaderboard()
    back_btn = Button(pygame.Rect(cx - 70, H - 60, 140, 44), "BACK", fonts["medium"])

    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if back_btn.is_clicked(event):
                return

        _draw_background(surface)

        title = fonts["large"].render("LEADERBOARD", True, ACCENT)
        surface.blit(title, title.get_rect(center=(cx, 50)))

        # Header row
        header_y = 100
        cols = [20, 65, 165, 260, 330]
        headers = ["#", "Name", "Score", "Dist", "Coins"]
        
        for col_x, hdr in zip(cols, headers):
            h_surf = fonts["small"].render(hdr, True, GRAY)
            surface.blit(h_surf, (col_x, header_y))
            
        pygame.draw.line(surface, DARK_GRAY, (20, header_y + 22), (W - 20, header_y + 22))

        # Rows
        for rank, entry in enumerate(entries[:10], start=1):
            row_y = header_y + 28 + (rank - 1) * 34
            color = ACCENT if rank == 1 else (GRAY if rank <= 3 else WHITE)
            row_panel = pygame.Rect(20, row_y - 3, W - 40, 30)
            
            if rank % 2 == 0:
                pygame.draw.rect(surface, PANEL, row_panel, border_radius=4)

            row_data = [
                str(rank),
                entry.get("name", "?")[:12],
                str(entry.get("score", 0)),
                f"{entry.get('distance', 0)} m",
                str(entry.get("coins", 0)),
            ]
            for col_x, val in zip(cols, row_data):
                v_surf = fonts["small"].render(val, True, color)
                surface.blit(v_surf, (col_x, row_y))

        if not entries:
            empty = fonts["medium"].render("No scores yet!", True, GRAY)
            surface.blit(empty, empty.get_rect(center=(cx, 300)))

        back_btn.draw(surface)
        pygame.display.flip()