from __future__ import annotations
import random
import sys
import pygame

from pygame.locals import *

import db
import settings as settings_mod


# Layout constants
CELLSIZE = 20
BASE_FPS = 15
MAX_FPS = 60
POWERUP_FIELD_SECS  = 8 # seconds a power-up sits on the field
POWERUP_EFFECT_SECS = 5 # seconds an active power-up effect lasts

# Colors  (R, G, B)
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
GRAY      = (120, 120, 120)
PURPLE    = (180,   0, 255)
ORANGE    = (255, 140,   0)
YELLOW    = (255, 230,   0)
DARKRED   = (139,   0,   0)   # poison food
CYAN      = (  0, 220, 220)   # speed-boost power-up
PINK      = (255, 105, 180)   # shield power-up
BROWN     = (101,  67,  33)   # obstacle wall block
BGCOLOR   = BLACK
BTN_COLOR = ( 50, 120,  50)
BTN_HOVER = ( 80, 180,  80)
BTN_TEXT  = WHITE
 
 
# Direction tokens
UP    = 'up'
DOWN  = 'down'
LEFT  = 'left'
RIGHT = 'right'
HEAD  = 0  # index of the head in worm_coords


# Food definitions  (color, points, timed-field-life in frames at BASE_FPS)
FOOD_TYPES = [
    {'color': RED, 'points': 1, 'timer': None},
    {'color': ORANGE, 'points': 2, 'timer': 90},
    {'color': PURPLE, 'points': 3, 'timer': 60},
]


# Power-up definitions
POWERUP_TYPES  = ['speed', 'slow', 'shield']
POWERUP_COLORS = {'speed': CYAN,   'slow': YELLOW, 'shield': PINK}
POWERUP_LABELS = {'speed': 'SPD',  'slow': 'SLW',  'shield': 'SHD'}


# Obstacle constants
OBSTACLE_START_LEVEL = 3 # obstacles appear from this level onward
OBSTACLES_PER_LEVEL  = 3 # extra blocks added per level after level 3


# Utility: simple clickable button
class Button:
    def __init__(self, rect, label, font):
        self.rect  = rect
        self.label = label
        self.font  = font

    def draw(self, surf, mouse_pos):
        color = BTN_HOVER if self.rect.collidepoint(mouse_pos) else BTN_COLOR
        
        pygame.draw.rect(surf, color, self.rect, border_radius=6)
        pygame.draw.rect(surf, WHITE, self.rect, 2, border_radius=6)
        
        text = self.font.render(self.label, True, BTN_TEXT)
        surf.blit(text, text.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        return (event.type == MOUSEBUTTONDOWN
                and event.button == 1
                and self.rect.collidepoint(event.pos))


# Main Game class
class Game:
    def __init__(self, displaysurf, basicfont, window_width, window_height, fps):
        self.displaysurf   = displaysurf
        self.basicfont     = basicfont
        self.window_width  = window_width
        self.window_height = window_height
        self.base_fps      = fps

        assert window_width  % CELLSIZE == 0, "Width must be a multiple of CELLSIZE"
        assert window_height % CELLSIZE == 0, "Height must be a multiple of CELLSIZE"
        self.cell_width  = window_width  // CELLSIZE
        self.cell_height = window_height // CELLSIZE

        # Fonts
        self.title_font  = pygame.font.Font('freesansbold.ttf', 64)
        self.medium_font = pygame.font.Font('freesansbold.ttf', 28)
        self.small_font  = pygame.font.Font('freesansbold.ttf', 18)
        self.tiny_font   = pygame.font.Font('freesansbold.ttf', 14)

        # Persistent player state
        self.prefs = settings_mod.load_settings()
        self.username = ''
        self.player_id = None
        self.personal_best = 0

        # Runtime game state — properly initialised in _reset_game()
        self.fps = BASE_FPS
        self.score = 0
        self.level = 1
        self.worm_coords = []
        self.obstacles= []
        self.food = None
        self.poison = None
        self.powerup_field = None # item on the field
        self.powerup_active = None # collected effect
        self.shield_active = False

        db.ensure_schema()


    # Public entry points (called from main.py)
    def show_main_menu(self, fpsclock):
        if not self.username:
            self.username      = self._prompt_username(fpsclock)
            self.player_id     = db.get_or_create_player(self.username)
            self.personal_best = (db.get_personal_best(self.player_id)
                                  if self.player_id else 0)

        cx = self.window_width  // 2
        bw, bh = 260, 52
        gap = 18
        base_y = self.window_height // 2 - 90

        buttons = {
            'play':        Button(pygame.Rect(cx - bw//2, base_y,                  bw, bh), 'Play',        self.medium_font),
            'leaderboard': Button(pygame.Rect(cx - bw//2, base_y +   (bh + gap),   bw, bh), 'Leaderboard', self.medium_font),
            'settings':    Button(pygame.Rect(cx - bw//2, base_y + 2*(bh + gap),   bw, bh), 'Settings',    self.medium_font),
            'quit':        Button(pygame.Rect(cx - bw//2, base_y + 3*(bh + gap),   bw, bh), 'Quit',        self.medium_font),
        }

        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._terminate()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self._terminate()
                for action, btn in buttons.items():
                    if btn.is_clicked(event):
                        if action == 'quit':
                            self._terminate()
                        return action

            self.displaysurf.fill(BGCOLOR)
            title = self.title_font.render('Snake', True, GREEN)
            self.displaysurf.blit(title, title.get_rect(center=(cx, base_y - 80)))
            sub = self.small_font.render(
                f'Player: {self.username}   |   Best: {self.personal_best}', True, GRAY)
            self.displaysurf.blit(sub, sub.get_rect(center=(cx, base_y - 28)))
            
            for btn in buttons.values():
                btn.draw(self.displaysurf, mouse_pos)
                
            pygame.display.update()
            fpsclock.tick(30)

    def run(self, fpsclock):
        self._reset_game()
        direction = pending_dir = RIGHT
        self.food   = self._spawn_food()
        self.poison = self._spawn_poison()
        self._maybe_spawn_powerup_field()
        self._rebuild_obstacles()

        while True:
            # Events
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._terminate()
                elif event.type == KEYDOWN:
                    if   event.key in (K_LEFT,  K_a) and direction != RIGHT:
                        pending_dir = LEFT
                    elif event.key in (K_RIGHT, K_d) and direction != LEFT:
                        pending_dir = RIGHT
                    elif event.key in (K_UP,    K_w) and direction != DOWN:
                        pending_dir = UP
                    elif event.key in (K_DOWN,  K_s) and direction != UP:
                        pending_dir = DOWN
                    elif event.key == K_ESCAPE:
                        return self.score, self.level

            direction = pending_dir

            # Compute new head 
            head  = self.worm_coords[HEAD]
            dx, dy = {UP: (0,-1), DOWN: (0,1), LEFT: (-1,0), RIGHT: (1,0)}[direction]
            new_head = {'x': head['x'] + dx, 'y': head['y'] + dy}

            # Collision detection 
            wall_hit = (new_head['x'] < 0 or new_head['x'] >= self.cell_width
                        or new_head['y'] < 0 or new_head['y'] >= self.cell_height)
            
            self_hit = new_head in self.worm_coords[1:]
            obs_hit  = new_head in self.obstacles

            if wall_hit or self_hit or obs_hit:
                if self.shield_active:
                    self.shield_active  = False
                    self.powerup_active = None
                    new_head = head   # freeze for one frame
                else:
                    return self.score, self.level

            # Advance snake 
            self.worm_coords.insert(0, new_head)
            grew = False

            #  Food collection 
            if new_head == {'x': self.food['x'], 'y': self.food['y']}:
                grew = True
                self.score += self.food['points']
                
                for _ in range(self.food['points'] - 1):
                    self.worm_coords.append(self.worm_coords[-1])
                    
                new_level = self.score // 3 + 1
                
                if new_level > self.level:
                    self.level = new_level
                    self._rebuild_obstacles()
                    
                self.food = self._spawn_food()

            # Poison collection
            elif (self.poison
                  and new_head == {'x': self.poison['x'], 'y': self.poison['y']}):
                grew = True # skip tail removal, shorten manually below
                
                for _ in range(2):
                    if len(self.worm_coords) > 1:
                        self.worm_coords.pop()
                        
                if len(self.worm_coords) <= 1:
                    return self.score, self.level
                
                self.poison = self._spawn_poison()

            # Power-up collection 
            elif (self.powerup_field
                  and new_head == {'x': self.powerup_field['x'],
                                   'y': self.powerup_field['y']}):
                self._activate_powerup(self.powerup_field['kind'])
                self.powerup_field = None

            if not grew:
                self.worm_coords.pop()

            # Tick timed items 
            self.food = self._tick_food(self.food)
            self.powerup_field = self._tick_powerup_field(self.powerup_field)
            self._tick_powerup_effect()

            # Speed update 
            self._update_fps()

            # Draw frame 
            self.displaysurf.fill(BGCOLOR)
            if self.prefs.get('grid_overlay', True):
                self._draw_grid()
            self._draw_obstacles()
            self._draw_worm()
            self._draw_food_item(self.food)
            if self.poison:
                self._draw_poison(self.poison)
            if self.powerup_field:
                self._draw_powerup_field(self.powerup_field)
            self._draw_hud()
            pygame.display.update()
            fpsclock.tick(self.fps)

    def show_game_over_screen(self, fpsclock, score, level):
        if self.player_id:
            db.save_session(self.player_id, score, level)
            self.personal_best = db.get_personal_best(self.player_id)

        cx = self.window_width  // 2
        cy = self.window_height // 2
        bw, bh  = 220, 48

        btn_retry = Button(pygame.Rect(cx - bw - 20, cy + 90, bw, bh), 'Retry',     self.medium_font)
        btn_menu  = Button(pygame.Rect(cx + 20,      cy + 90, bw, bh), 'Main Menu', self.medium_font)

        pygame.time.wait(400)
        pygame.event.clear()

        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._terminate()
                if btn_retry.is_clicked(event):
                    return 'retry'
                if btn_menu.is_clicked(event):
                    return 'menu'
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        return 'retry'
                    if event.key == K_ESCAPE:
                        return 'menu'

            self.displaysurf.fill(BGCOLOR)
            go_surf = self.title_font.render('GAME  OVER', True, RED)
            self.displaysurf.blit(go_surf, go_surf.get_rect(center=(cx, cy - 120)))

            info = [
                f'Score:          {score}',
                f'Level reached:  {level}',
                f'Personal best:  {self.personal_best}',
            ]
            for i, line in enumerate(info):
                s = self.medium_font.render(line, True, WHITE)
                self.displaysurf.blit(s, s.get_rect(center=(cx, cy - 20 + i * 40)))

            btn_retry.draw(self.displaysurf, mouse_pos)
            btn_menu.draw(self.displaysurf,  mouse_pos)
            
            pygame.display.update()
            fpsclock.tick(30)

    def show_leaderboard_screen(self, fpsclock):
        rows    = db.get_leaderboard(10)
        cx      = self.window_width // 2
        bw, bh  = 180, 44
        btn_back = Button(
            pygame.Rect(cx - bw//2, self.window_height - 64, bw, bh),
            'Back', self.medium_font)

        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._terminate()
                if btn_back.is_clicked(event):
                    return
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return

            self.displaysurf.fill(BGCOLOR)
            title = self.title_font.render('Leaderboard', True, GREEN)
            self.displaysurf.blit(title, title.get_rect(center=(cx, 38)))

            hdr = self.small_font.render(
                f"{'#':>3}  {'Player':<18} {'Score':>6}  {'Lvl':>4}  {'Date'}",
                True, ORANGE)
            self.displaysurf.blit(hdr, (30, 92))
            pygame.draw.line(self.displaysurf, GRAY, (30, 114), (self.window_width - 30, 114), 1)

            if not rows:
                msg = self.medium_font.render('No scores recorded yet!', True, GRAY)
                self.displaysurf.blit(msg, msg.get_rect(center=(cx, 260)))
            else:
                for i, (rank, uname, sc, lvl, played_at) in enumerate(rows):
                    date_str = played_at.strftime('%Y-%m-%d') if played_at else '-'
                    color    = YELLOW if i == 0 else WHITE
                    row_surf = self.small_font.render(
                        f"{rank:>3}  {uname:<18} {sc:>6}  {lvl:>4}  {date_str}",
                        True, color)
                    self.displaysurf.blit(row_surf, (30, 122 + i * 28))

            btn_back.draw(self.displaysurf, mouse_pos)
            pygame.display.update()
            fpsclock.tick(30)

    def show_settings_screen(self, fpsclock):
        cx      = self.window_width // 2
        bw, bh  = 260, 46
        gap     = 16
        btn_grid  = Button(pygame.Rect(cx - bw//2, 160,               bw, bh), '', self.medium_font)
        btn_save  = Button(pygame.Rect(cx - bw//2, self.window_height - 78, bw, bh),
                           'Save & Back', self.medium_font)

        colour_options = [
            ('Green',  (  0, 200,   0)),
            ('Blue',   (  0, 120, 255)),
            ('White',  (220, 220, 220)),
            ('Yellow', (230, 210,   0)),
            ('Pink',   (255, 100, 200)),
        ]
        swatch_y   = 160 + 2 * (bh + gap) + 50
        swatch_sz  = 40
        swatch_gap = 20
        total_w    = len(colour_options) * (swatch_sz + swatch_gap) - swatch_gap
        swatch_x0  = cx - total_w // 2
        swatch_rects = [
            pygame.Rect(swatch_x0 + i * (swatch_sz + swatch_gap), swatch_y, swatch_sz, swatch_sz)
            for i in range(len(colour_options))
        ]

        while True:
            btn_grid.label  = f"Grid:  {'ON'  if self.prefs['grid_overlay'] else 'OFF'}"
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self._terminate()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    settings_mod.save_settings(self.prefs)
                    return
                if btn_grid.is_clicked(event):
                    self.prefs['grid_overlay'] = not self.prefs['grid_overlay']
                if btn_save.is_clicked(event):
                    settings_mod.save_settings(self.prefs)
                    return
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    for idx, (_, rgb) in enumerate(colour_options):
                        if swatch_rects[idx].collidepoint(event.pos):
                            self.prefs['snake_color'] = list(rgb)

            self.displaysurf.fill(BGCOLOR)
            title = self.title_font.render('Settings', True, GREEN)
            self.displaysurf.blit(title, title.get_rect(center=(cx, 60)))
            btn_grid.draw(self.displaysurf,  mouse_pos)

            clabel = self.small_font.render('Snake Colour:', True, WHITE)
            self.displaysurf.blit(clabel, clabel.get_rect(center=(cx, swatch_y - 24)))

            cur_color = tuple(self.prefs['snake_color'])
            for (cname, rgb), sr in zip(colour_options, swatch_rects):
                pygame.draw.rect(self.displaysurf, rgb, sr, border_radius=5)
                if tuple(rgb) == cur_color:
                    pygame.draw.rect(self.displaysurf, WHITE, sr, 3, border_radius=5)
                tip = self.tiny_font.render(cname, True, GRAY)
                self.displaysurf.blit(tip, tip.get_rect(center=(sr.centerx, sr.bottom + 12)))

            btn_save.draw(self.displaysurf, mouse_pos)
            pygame.display.update()
            fpsclock.tick(30)


    # Username prompt
    def _prompt_username(self, fpsclock):
        name      = ''
        max_chars = 16
        cx        = self.window_width  // 2
        cy        = self.window_height // 2

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and name.strip():
                        return name.strip()
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    elif event.key == K_ESCAPE:
                        self._terminate()
                    elif len(name) < max_chars and event.unicode.isprintable():
                        name += event.unicode

            self.displaysurf.fill(BGCOLOR)
            prompt = self.medium_font.render('Enter your username:', True, WHITE)
            self.displaysurf.blit(prompt, prompt.get_rect(center=(cx, cy - 70)))

            box = pygame.Rect(cx - 190, cy - 28, 380, 52)
            pygame.draw.rect(self.displaysurf, DARKGRAY, box, border_radius=6)
            pygame.draw.rect(self.displaysurf, GREEN,    box, 2, border_radius=6)

            # Blinking cursor
            cursor    = '|' if (pygame.time.get_ticks() // 500) % 2 == 0 else ' '
            name_surf = self.medium_font.render(name + cursor, True, GREEN)
            self.displaysurf.blit(name_surf,
                                  name_surf.get_rect(midleft=(box.left + 12, box.centery)))

            hint = self.small_font.render('Press ENTER to confirm  (max 16 chars)', True, GRAY)
            self.displaysurf.blit(hint, hint.get_rect(center=(cx, cy + 48)))

            pygame.display.update()
            fpsclock.tick(30)


    # Game-state reset
    def _reset_game(self):
        self.fps            = BASE_FPS
        self.score          = 0
        self.level          = 1
        self.shield_active  = False
        self.powerup_field  = None
        self.powerup_active = None
        self.obstacles      = []
        self._reset_worm()

    def _reset_worm(self):
        sx = random.randint(5, self.cell_width  - 6)
        sy = random.randint(5, self.cell_height - 6)
        
        self.worm_coords = [
            {'x': sx,     'y': sy},
            {'x': sx - 1, 'y': sy},
            {'x': sx - 2, 'y': sy},
        ]


    # Obstacles
    def _rebuild_obstacles(self):
        if self.level < OBSTACLE_START_LEVEL:
            self.obstacles = []
            
            return
        
        count    = (self.level - OBSTACLE_START_LEVEL + 1) * OBSTACLES_PER_LEVEL
        occupied = self._all_occupied_cells()
        
        # Safety buffer around worm head (7x7 clear zone)
        head = self.worm_coords[HEAD]
        
        for ddx in range(-3, 4):
            for ddy in range(-3, 4):
                occupied.add((head['x'] + ddx, head['y'] + ddy))
                
        candidates = [
            {'x': x, 'y': y}
            for x in range(self.cell_width)
            for y in range(self.cell_height)
            if (x, y) not in occupied
        ]
        
        random.shuffle(candidates)
        self.obstacles = candidates[:count]


    # Spawn helpers
    def _get_random_location(self):
        blocked = self._all_occupied_cells()
        
        while True:
            loc = {'x': random.randint(0, self.cell_width  - 1),
                   'y': random.randint(0, self.cell_height - 1)}
            if (loc['x'], loc['y']) not in blocked:
                return loc

    def _all_occupied_cells(self):
        occupied = set()
        
        for c in self.worm_coords:
            occupied.add((c['x'], c['y']))
        for o in self.obstacles:
            occupied.add((o['x'], o['y']))
        if self.food:
            occupied.add((self.food['x'], self.food['y']))
        if self.poison:
            occupied.add((self.poison['x'], self.poison['y']))
        if self.powerup_field:
            occupied.add((self.powerup_field['x'], self.powerup_field['y']))
        return occupied

    def _spawn_food(self):
        ft  = random.choice(FOOD_TYPES)
        pos = self._get_random_location()
        
        return {'x': pos['x'], 'y': pos['y'],
                'color': ft['color'], 'points': ft['points'], 'timer': ft['timer']}

    def _spawn_poison(self):
        pos = self._get_random_location()
        
        return {'x': pos['x'], 'y': pos['y']}

    def _maybe_spawn_powerup_field(self):
        if self.powerup_field is None and random.random() < 0.33:
            pos  = self._get_random_location()
            kind = random.choice(POWERUP_TYPES)
            
            self.powerup_field = {
                'x':       pos['x'],
                'y':       pos['y'],
                'kind':    kind,
                'expires': pygame.time.get_ticks() + POWERUP_FIELD_SECS * 1000,
            }


    # Tick helpers
    def _tick_food(self, food):
        if food['timer'] is not None:
            food['timer'] -= 1
            
            if food['timer'] <= 0:
                return self._spawn_food()
        return food

    def _tick_powerup_field(self, pu):
        if pu is None:
            self._maybe_spawn_powerup_field()
            
            return self.powerup_field
        if pygame.time.get_ticks() >= pu['expires']:
            return None # expired = remove
        return pu

    def _tick_powerup_effect(self):
        if self.powerup_active and pygame.time.get_ticks() >= self.powerup_active['expires']:
            self._deactivate_powerup(self.powerup_active['kind'])
            self.powerup_active = None


    # Power-up activation / deactivation
    def _activate_powerup(self, kind):
        expires = pygame.time.get_ticks() + POWERUP_EFFECT_SECS * 1000
        self.powerup_active = {'kind': kind, 'expires': expires}
        
        if kind == 'speed':
            self.fps = min(self.fps + 8, MAX_FPS)
        elif kind == 'slow':
            self.fps = max(self.fps - 6, 5)
        elif kind == 'shield':
            self.shield_active = True

    def _deactivate_powerup(self, kind):
        if kind in ('speed', 'slow'):
            self._update_fps() # revert to level-based fps
        elif kind == 'shield':
            self.shield_active = False


    # Speed management
    def _update_fps(self):
        if self.powerup_active and self.powerup_active['kind'] in ('speed', 'slow'):
            return
        self.fps = min(BASE_FPS + max(self.level - 1, 0), MAX_FPS)


    # Drawing helpers
    def _draw_worm(self):
        outer = tuple(self.prefs.get('snake_color', [0, 200, 0]))
        inner = tuple(max(0, c - 60) for c in outer)
        
        for coord in self.worm_coords:
            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE
            
            pygame.draw.rect(self.displaysurf, outer, (x,   y,   CELLSIZE,   CELLSIZE))
            pygame.draw.rect(self.displaysurf, inner, (x+4, y+4, CELLSIZE-8, CELLSIZE-8))
            
        # Shield glow around the head
        if self.shield_active:
            hx = self.worm_coords[HEAD]['x'] * CELLSIZE
            hy = self.worm_coords[HEAD]['y'] * CELLSIZE
            
            pygame.draw.rect(self.displaysurf, PINK,
                             (hx-2, hy-2, CELLSIZE+4, CELLSIZE+4), 2, border_radius=4)

    def _draw_food_item(self, food):
        x = food['x'] * CELLSIZE
        y = food['y'] * CELLSIZE
        
        pygame.draw.rect(self.displaysurf, food['color'], (x, y, CELLSIZE, CELLSIZE))
        
        if food['timer'] is not None and food['timer'] > 0:
            max_t = next(f['timer'] for f in FOOD_TYPES if f['points'] == food['points'])
            bar_w = int(CELLSIZE * food['timer'] / max_t)
            
            pygame.draw.rect(self.displaysurf, WHITE, (x, y + CELLSIZE - 3, bar_w, 3))

    def _draw_poison(self, poison):
        x = poison['x'] * CELLSIZE
        y = poison['y'] * CELLSIZE
        
        pygame.draw.rect(self.displaysurf, DARKRED, (x, y, CELLSIZE, CELLSIZE))
        pygame.draw.line(self.displaysurf, WHITE, (x+4, y+4),          (x+CELLSIZE-4, y+CELLSIZE-4), 2)
        pygame.draw.line(self.displaysurf, WHITE, (x+CELLSIZE-4, y+4), (x+4, y+CELLSIZE-4),          2)

    def _draw_powerup_field(self, pu):
        x     = pu['x'] * CELLSIZE
        y     = pu['y'] * CELLSIZE
        color = POWERUP_COLORS[pu['kind']]
        
        pygame.draw.rect(self.displaysurf, color, (x, y, CELLSIZE, CELLSIZE), border_radius=4)
        
        lbl = self.tiny_font.render(POWERUP_LABELS[pu['kind']], True, BLACK)
        self.displaysurf.blit(lbl, lbl.get_rect(center=(x + CELLSIZE//2, y + CELLSIZE//2)))
        total_ms  = POWERUP_FIELD_SECS * 1000
        remaining = max(0, pu['expires'] - pygame.time.get_ticks())
        bar_w     = int(CELLSIZE * remaining / total_ms)
        
        pygame.draw.rect(self.displaysurf, WHITE, (x, y + CELLSIZE - 3, bar_w, 3))

    def _draw_obstacles(self):
        for obs in self.obstacles:
            x = obs['x'] * CELLSIZE
            y = obs['y'] * CELLSIZE
            
            pygame.draw.rect(self.displaysurf, BROWN, (x, y, CELLSIZE, CELLSIZE))
            pygame.draw.rect(self.displaysurf, GRAY,  (x, y, CELLSIZE, CELLSIZE), 1)

    def _draw_grid(self):
        for x in range(0, self.window_width, CELLSIZE):
            pygame.draw.line(self.displaysurf, DARKGRAY, (x, 0), (x, self.window_height))
        for y in range(0, self.window_height, CELLSIZE):
            pygame.draw.line(self.displaysurf, DARKGRAY, (0, y), (self.window_width, y))

    def _draw_hud(self):
        score_s = self.small_font.render(f'Score: {self.score}',         True, WHITE)
        level_s = self.small_font.render(f'Level: {self.level}',         True, WHITE)
        best_s  = self.small_font.render(f'Best:  {self.personal_best}', True, GRAY)
        lh = score_s.get_height() + 3
        rx = self.window_width - 132
        
        self.displaysurf.blit(level_s, (rx, 8))
        self.displaysurf.blit(score_s, (rx, 8 + lh))
        self.displaysurf.blit(best_s,  (rx, 8 + lh * 2))
        
        if self.powerup_active:
            kind      = self.powerup_active['kind']
            secs_left = max(0, (self.powerup_active['expires'] - pygame.time.get_ticks()) // 1000)
            pu_surf   = self.small_font.render(
                f'{POWERUP_LABELS[kind]} {secs_left}s', True, POWERUP_COLORS[kind])
            self.displaysurf.blit(pu_surf, (rx, self.window_height - 28))


    # Misc helpers
    def _check_for_key_press(self):
        if pygame.event.get(QUIT):
            self._terminate()
            
        evts = pygame.event.get(KEYUP)
        
        if not evts:
            return None
        if evts[0].key == K_ESCAPE:
            self._terminate()
            
        return evts[0].key

    @staticmethod
    def _terminate():
        pygame.quit()
        sys.exit()