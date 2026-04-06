import pygame
import player
import utility

# Game configurations
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BG_COLOR = (250, 249, 245)
FONT_PREFERENCES = ["Century Gothic", "Arial"]

FPS = 60

# Game logics
centerX = WINDOW_WIDTH // 2
centerY = WINDOW_HEIGHT // 2

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

nowPlayingText = utility.createText("Now playing:", FONT_PREFERENCES, 16, (0, 0, 0))
byText = utility.createText("by", FONT_PREFERENCES, 16, (0, 0, 0))
keyInfoText = utility.createText("Controls: P (Play), S (Stop), N (Next), B (Back), Q (Quit)", FONT_PREFERENCES, 16, (0, 0, 0))

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
    
    nameText = utility.createText(currentSong[1], ["Centaur"] + FONT_PREFERENCES, 64, (0, 0, 0))
    nameText = utility.respectWidth(nameText, WINDOW_WIDTH)
    
    authorText = utility.createText(currentSong[0], ["Centaur"] + FONT_PREFERENCES, 32, (0, 0, 0))
    authorText = utility.respectWidth(authorText, WINDOW_WIDTH)
    
    progressText = utility.createText(f"{(player.getSongProgress() // 60):02d} : {(player.getSongProgress() % 60):02d}", FONT_PREFERENCES, 16, (0, 0, 0))
    progressText = utility.respectWidth(progressText, WINDOW_WIDTH)
    
    slashText = utility.createText("/", FONT_PREFERENCES, 16, (0, 0, 0))
    slashText = utility.respectWidth(slashText, WINDOW_WIDTH)
    
    durationText = utility.createText(f"{(int(currentSong[2]) // 60):02d} : {(int(currentSong[2]) % 60):02d}", FONT_PREFERENCES, 16, (0, 0, 0))
    durationText = utility.respectWidth(durationText, WINDOW_WIDTH)
    
    screen.blit(nowPlayingText, (centerX - nowPlayingText.get_width() // 2, 5))
    
    screen.blit(nameText, (centerX - nameText.get_width() // 2, nowPlayingText.get_height() + 5))
    
    screen.blit(byText, (centerX - byText.get_width() // 2, nameText.get_height() + nowPlayingText.get_height() + 5))
    
    screen.blit(authorText, (centerX - authorText.get_width() // 2, nameText.get_height() + nowPlayingText.get_height() + byText.get_height() + 5))
    
    timeCounterY = nowPlayingText.get_height() + nameText.get_height() + byText.get_height() + authorText.get_height() + 5
    
    screen.blit(progressText, (centerX - (progressText.get_width() * 1.5), timeCounterY))
    screen.blit(slashText, (centerX - slashText.get_width() // 2, timeCounterY))
    screen.blit(durationText, (centerX + durationText.get_width() // 2, timeCounterY))
    
    screen.blit(keyInfoText, (centerX - keyInfoText.get_width() // 2, WINDOW_HEIGHT - keyInfoText.get_height() - 5))
    
    pygame.display.flip()
    clock.tick(FPS)