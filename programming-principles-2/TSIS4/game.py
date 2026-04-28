import random
import pygame
import sys
from pygame.locals import *

CELLSIZE = 20

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
PURPLE    = (180,   0, 255)
ORANGE    = (255, 140,   0)
BGCOLOR   = BLACK

UP    = 'up'
DOWN  = 'down'
LEFT  = 'left'
RIGHT = 'right'

HEAD = 0  # index of the worm's head

FOOD_TYPES = [
    {'color': RED,    'points': 1, 'timer': None},
    {'color': ORANGE, 'points': 2, 'timer': 90},
    {'color': PURPLE, 'points': 3, 'timer': 60},
]


class Game:
    def __init__(self, displaysurf, basicfont, window_width, window_height, fps):
        self.displaysurf  = displaysurf
        self.basicfont    = basicfont
        self.window_width  = window_width
        self.window_height = window_height
        self.fps          = fps

        assert window_width  % CELLSIZE == 0, "Window width must be a multiple of cell size."
        assert window_height % CELLSIZE == 0, "Window height must be a multiple of cell size."

        self.cell_width  = window_width  // CELLSIZE
        self.cell_height = window_height // CELLSIZE

        self._reset_worm()

    
    # Public interface
    def run(self, fpsclock):
        self._reset_worm()
        self.fps = 15
        direction = RIGHT
        food = self._spawn_food()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._terminate()
                elif event.type == KEYDOWN:
                    if (event.key in (K_LEFT, K_a)) and direction != RIGHT:
                        direction = LEFT
                    elif (event.key in (K_RIGHT, K_d)) and direction != LEFT:
                        direction = RIGHT
                    elif (event.key in (K_UP, K_w)) and direction != DOWN:
                        direction = UP
                    elif (event.key in (K_DOWN, K_s)) and direction != UP:
                        direction = DOWN
                    elif event.key == K_ESCAPE:
                        self._terminate()

            # Check wall collision
            head = self.worm_coords[HEAD]
            if head['x'] in (-1, self.cell_width) or head['y'] in (-1, self.cell_height):
                return # game over

            # Check self collision
            for segment in self.worm_coords[1:]:
                if segment['x'] == head['x'] and segment['y'] == head['y']:
                    return # game over

            # Tick timed food
            food = self._tick_food(food)

            # Check food eaten
            if head['x'] == food['x'] and head['y'] == food['y']:
                for _ in range(food['points'] - 1):
                    self.worm_coords.append(self.worm_coords[-1])
                food = self._spawn_food()
            else:
                del self.worm_coords[-1]

            # Advance worm
            if direction == UP:
                new_head = {'x': head['x'],     'y': head['y'] - 1}
            elif direction == DOWN:
                new_head = {'x': head['x'],     'y': head['y'] + 1}
            elif direction == LEFT:
                new_head = {'x': head['x'] - 1, 'y': head['y']}
            else:  # RIGHT
                new_head = {'x': head['x'] + 1, 'y': head['y']}
            self.worm_coords.insert(0, new_head)

            # Draw frame
            self.displaysurf.fill(BGCOLOR)
            self._draw_grid()
            self._draw_worm()
            self._draw_food(food)
            self._draw_score_level(len(self.worm_coords) - 3)
            pygame.display.update()
            fpsclock.tick(self.fps)

    def show_start_screen(self, fpsclock):
        title_font   = pygame.font.Font('freesansbold.ttf', 100)
        title_surf1  = title_font.render('Snake!', True, WHITE, DARKGREEN)
        title_surf2  = title_font.render('Snake!', True, GREEN)
        degrees1 = degrees2 = 0

        while True:
            self.displaysurf.fill(BGCOLOR)

            rot1 = pygame.transform.rotate(title_surf1, degrees1)
            r1   = rot1.get_rect()
            r1.center = (self.window_width / 2, self.window_height / 2)
            self.displaysurf.blit(rot1, r1)

            rot2 = pygame.transform.rotate(title_surf2, degrees2)
            r2   = rot2.get_rect()
            r2.center = (self.window_width / 2, self.window_height / 2)
            self.displaysurf.blit(rot2, r2)

            self._draw_press_key_msg()

            if self._check_for_key_press():
                pygame.event.get() # clear event queue
                return

            pygame.display.update()
            fpsclock.tick(self.fps)
            degrees1 += 3
            degrees2 += 7

    def show_game_over_screen(self, fpsclock):
        game_over_font = pygame.font.Font('freesansbold.ttf', 150)
        game_surf = game_over_font.render('Game', True, WHITE)
        over_surf = game_over_font.render('Over', True, WHITE)
        game_rect = game_surf.get_rect()
        over_rect = over_surf.get_rect()
        game_rect.midtop = (self.window_width / 2, 10)
        over_rect.midtop = (self.window_width / 2, game_rect.height + 35)

        self.displaysurf.blit(game_surf, game_rect)
        self.displaysurf.blit(over_surf, over_rect)
        self._draw_press_key_msg()
        pygame.display.update()
        pygame.time.wait(500)
        self._check_for_key_press() # drain event queue

        while True:
            if self._check_for_key_press():
                pygame.event.get()
                return

    
    # Private helpers
    def _reset_worm(self):
        startx = random.randint(5, self.cell_width  - 6) if hasattr(self, 'cell_width')  else 10
        starty = random.randint(5, self.cell_height - 6) if hasattr(self, 'cell_height') else 10
        self.worm_coords = [
            {'x': startx,     'y': starty},
            {'x': startx - 1, 'y': starty},
            {'x': startx - 2, 'y': starty},
        ]

    def _spawn_food(self):
        food_type = random.choice(FOOD_TYPES)
        pos = self._get_random_location()
        return {
            'x':      pos['x'],
            'y':      pos['y'],
            'color':  food_type['color'],
            'points': food_type['points'],
            'timer':  food_type['timer'],
        }

    def _tick_food(self, food):
        if food['timer'] is not None and food['timer'] > 0:
            food['timer'] -= 1
        elif food['timer'] == 0:
            return self._spawn_food()
        return food

    def _get_random_location(self):
        loc = {'x': random.randint(0, self.cell_width - 1),
               'y': random.randint(0, self.cell_height - 1)}
        while loc in self.worm_coords:
            loc = {'x': random.randint(0, self.cell_width - 1),
                   'y': random.randint(0, self.cell_height - 1)}
        return loc

    def _speedup_snake(self, level):
        if self.fps < 60 and level > 1:
            new_fps = 15 + level - 1
            if new_fps != self.fps:
                self.fps = new_fps

    
    # Drawing helpers
    def _draw_worm(self):
        for coord in self.worm_coords:
            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE
            pygame.draw.rect(self.displaysurf, DARKGREEN, (x, y, CELLSIZE, CELLSIZE))
            pygame.draw.rect(self.displaysurf, GREEN,     (x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8))

    def _draw_food(self, food):
        x = food['x'] * CELLSIZE
        y = food['y'] * CELLSIZE
        pygame.draw.rect(self.displaysurf, food['color'], (x, y, CELLSIZE, CELLSIZE))

        if food['timer'] is not None:
            max_timer = next(f['timer'] for f in FOOD_TYPES if f['points'] == food['points'])
            bar_w = int(CELLSIZE * food['timer'] / max_timer)
            pygame.draw.rect(self.displaysurf, WHITE, (x, y + CELLSIZE - 3, bar_w, 3))

    def _draw_grid(self):
        for x in range(0, self.window_width, CELLSIZE):
            pygame.draw.line(self.displaysurf, DARKGRAY, (x, 0), (x, self.window_height))
        for y in range(0, self.window_height, CELLSIZE):
            pygame.draw.line(self.displaysurf, DARKGRAY, (0, y), (self.window_width, y))

    def _draw_score_level(self, score):
        level = score // 3 + 1

        level_surf = self.basicfont.render(f'Level: {level}', True, WHITE)
        score_surf = self.basicfont.render(f'Score: {score}', True, WHITE)

        level_rect = level_surf.get_rect()
        score_rect = score_surf.get_rect()
        level_rect.topleft = (self.window_width - 120, 10)
        score_rect.topleft = (self.window_width - 120, level_surf.get_height() + 10)

        self.displaysurf.blit(level_surf, level_rect)
        self.displaysurf.blit(score_surf, score_rect)

        self._speedup_snake(level)

    def _draw_press_key_msg(self):
        surf = self.basicfont.render('Press a key to play.', True, DARKGRAY)
        rect = surf.get_rect()
        rect.topleft = (self.window_width - 200, self.window_height - 30)
        self.displaysurf.blit(surf, rect)
        
        
    # Event helpers
    def _check_for_key_press(self):
        if pygame.event.get(QUIT):
            self._terminate()
        key_up_events = pygame.event.get(KEYUP)
        if not key_up_events:
            return None
        if key_up_events[0].key == K_ESCAPE:
            self._terminate()
        return key_up_events[0].key

    @staticmethod
    def _terminate():
        pygame.quit()
        sys.exit()