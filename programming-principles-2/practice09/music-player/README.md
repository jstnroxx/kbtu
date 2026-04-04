### 3.2 Music Player with Keyboard Controller

**Objective**: Build an interactive music player with keyboard controls

**Requirements**:
1. Play/Stop/Next/Previous tracks with keyboard commands
2. Display current track information
3. Show playback progress or track position
4. Handle playlist management

**Keyboard Controls Example**:
- **P** = Play
- **S** = Stop
- **N** = Next track
- **B** = Previous (Back)
- **Q** = Quit

**Implementation Tips**:
- Use pygame.mixer for audio playback
- Load multiple MP3/WAV files
- Track current playlist position
- Display UI with pygame.font

**Repository Structure**:
```
Practice7/
├── music_player/
│   ├── main.py
│   ├── player.py
│   ├── music/
│   │   ├── track1.wav
│   │   └── track2.wav
│   └── README.md
```