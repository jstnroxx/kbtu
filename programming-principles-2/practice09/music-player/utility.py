import pygame

# Font and text loader
def makeFont(fonts, size):
    available = pygame.font.get_fonts()
    
    choices = map(lambda name : name.lower().replace(" ", ""), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
        
    return pygame.font.Font(None, size)

_cachedFonts = {}
def getFont(fonts, size):
    global _cachedFonts
    key = str(fonts) + "|" + str(size)
    font = _cachedFonts.get(key)
    
    if font == None:
        font = makeFont(fonts, size)
        _cachedFonts[key] = font
        
    return font

_cachedText = {}
def createText(text, fonts, size, color):
    global _cachedText
    key = "|".join(map(str, (fonts, size, color, text)))
    image = _cachedText.get(key)
    
    if image == None:
        font = getFont(fonts, size)
        image = font.render(text, True, color)
        _cachedText[key] = image
    
    return image

# Check if the text exceeds the window width and scale it down
def respectWidth(textSurface, maxWidth):
    if textSurface.get_width() > maxWidth:
        textSurface = pygame.transform.smoothscale(textSurface, (maxWidth, textSurface.get_height()))
        
    return textSurface

