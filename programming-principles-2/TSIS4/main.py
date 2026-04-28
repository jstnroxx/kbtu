import pygame

from game import Game

WINDOW_WIDTH  = 640
WINDOW_HEIGHT = 480
FPS = 15


def main() -> None:
    pygame.init()
    fpsclock    = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    basicfont   = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')

    game = Game(displaysurf, basicfont, WINDOW_WIDTH, WINDOW_HEIGHT, FPS)

   
    # Top-level screen loop
    screen = 'menu'

    while True:
        if screen == 'menu':
            action = game.show_main_menu(fpsclock)
            if action == 'play':
                screen = 'play'
            elif action == 'leaderboard':
                screen = 'leaderboard'
            elif action == 'settings':
                screen = 'settings'

        elif screen == 'play':
            score, level = game.run(fpsclock)
            
            # Pass score/level to the game-over screen
            result = game.show_game_over_screen(fpsclock, score, level)
            screen = 'play' if result == 'retry' else 'menu'

        elif screen == 'leaderboard':
            game.show_leaderboard_screen(fpsclock)
            screen = 'menu'

        elif screen == 'settings':
            game.show_settings_screen(fpsclock)
            screen = 'menu'


if __name__ == '__main__':
    main()