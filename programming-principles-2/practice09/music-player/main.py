import pygame
import player
import utility

# Game configurations
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BG_COLOR = (255, 255, 255)
FONT_PREFERENCES = ["Comic Sans MS"]

FPS = 60

# Game logics
centerX = WINDOW_WIDTH // 2
centerY = WINDOW_HEIGHT // 2

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

keyInfoText = utility.createText("Controls: P, S, N, B, Q", FONT_PREFERENCES, 16, (0, 0, 0))
currentSong = player.getSongInfo(player.currentSong) or ("untitled", "untitled", "0")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            player.playSong()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            player.stopSong()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            currentSong = player.nextSong() or ("untitled", "untitled", "0")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            currentSong = player.nextSong(False) or ("untitled", "untitled", "0")
           
    screen.fill(BG_COLOR)
    
    nameText = utility.createText(currentSong[1], FONT_PREFERENCES, 64, (0, 0, 0))
    nameText = utility.respectWidth(nameText, WINDOW_WIDTH)
    
    authorText = utility.createText(currentSong[0], FONT_PREFERENCES, 32, (0, 0, 0))
    authorText = utility.respectWidth(authorText, WINDOW_WIDTH)
    
    progressText = utility.createText(str(player.getSongProgress()), FONT_PREFERENCES, 16, (0, 0, 0))
    progressText = utility.respectWidth(progressText, WINDOW_WIDTH)
    
    colonText = utility.createText(":", FONT_PREFERENCES, 16, (0, 0, 0))
    colonText = utility.respectWidth(colonText, WINDOW_WIDTH)
    
    durationText = utility.createText(currentSong[2], FONT_PREFERENCES, 16, (0, 0, 0))
    durationText = utility.respectWidth(durationText, WINDOW_WIDTH)
    
    screen.blit(nameText, (centerX - nameText.get_width() // 2, 0))
    screen.blit(authorText, (centerX - authorText.get_width() // 2, nameText.get_height()))
    screen.blit(progressText, (centerX - (progressText.get_width() * 2), nameText.get_height() + authorText.get_height()))
    screen.blit(colonText, (centerX - colonText.get_width() // 2, nameText.get_height() + authorText.get_height()))
    screen.blit(durationText, (centerX + durationText.get_width() // 2, nameText.get_height() + authorText.get_height()))
    
    screen.blit(keyInfoText, (centerX - keyInfoText.get_width() // 2, WINDOW_HEIGHT - keyInfoText.get_height()))
    
    pygame.display.flip()
    clock.tick(FPS)