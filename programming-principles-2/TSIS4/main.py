import pygame

from game import Game

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480


def main():
    pygame.init()
    fpsclock = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    basicfont = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')

    game = Game(displaysurf, basicfont, WINDOWWIDTH, WINDOWHEIGHT, FPS)

    game.show_start_screen(fpsclock)
    while True:
        game.run(fpsclock)
        game.show_game_over_screen(fpsclock)


if __name__ == '__main__':
    main()