import pygame
import os
from pathlib import Path

AUDIO_EXTENSIONS = {'.mp3', '.wav', '.flac', '.m4a', '.ogg', '.aac'}
pygame.mixer.init()

# Load music files into the playlist
_playlist = []

for item in Path("music").iterdir():
    if item.is_file() and item.suffix.lower() in AUDIO_EXTENSIONS:
        _playlist.append(item)
        
if len(_playlist) > 0:
    currentSong = _playlist[0]
    pygame.mixer.music.load(currentSong)
else:
    currentSong = None
    
# Playlist as pygame sound (to extract durations)
_soundLibrary = {}
def getSound(path):
  global _soundLibrary
  sound = _soundLibrary.get(str(path))
  
  if sound == None:
    sound = pygame.mixer.Sound(path)
    _soundLibrary[str(path)] = sound
  
  return sound

# Get songs author, name and duration
def getSongInfo(path):
    if path is not None:
        songData = currentSong.stem.split(" - ")
        timeDuration = str(int(getSound(currentSong).get_length()))
        
        return (songData[0], songData[1], timeDuration)
  
# Player functionality
def playSong():
    if currentSong is not None:
        pygame.mixer.music.play()
    
def stopSong():
    pygame.mixer.music.stop()
    
def nextSong(next = True):
    global _playlist
    global currentSong
    
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.set_pos(-1)
    
    if currentSong is not None:
        if next:
            _playlist = _playlist[1:] + [_playlist[0]]
            currentSong = _playlist[0]
            
            pygame.mixer.music.load(currentSong)
        else:
            _playlist = _playlist[-1:] + _playlist[:-1]
            currentSong = _playlist[0]
            
            pygame.mixer.music.load(currentSong)
        
        return getSongInfo(currentSong)
    else:
        return None
        
def getSongProgress():
    position = pygame.mixer.music.get_pos() // 1000
    if position == -1: position = 0
    
    return position