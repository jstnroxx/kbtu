import pygame
import os
import math

# Image to surface loader
_imageLibrary = {}
def getImage(path):
    global _imageLibrary
    image = _imageLibrary.get(path)
    
    if image == None:
        canonicalPath = path.replace("/", os.sep).replace("\\", os.sep)
        image = pygame.image.load(canonicalPath).convert_alpha()
        _imageLibrary[path] = image
        
    return image

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

# Automatically position hours on the watchface
def getClockPosition(hour, textSurface, radius, centerX, centerY):
    angle = math.radians((hour * 30) - 90)
    
    x = centerX + radius * math.cos(angle)
    y = centerY + radius * math.sin(angle)
    
    x -= textSurface.get_width() // 2
    y -= textSurface.get_height() // 2
    
    return (x, y)

# Hand rotation
def rotateHand(image, origin, pivot, angle):
    imageRect = image.get_rect(topleft = (origin[0] - pivot[0], origin[1]-pivot[1]))
    offsetCenterToPivot = pygame.math.Vector2(origin) - imageRect.center
    
    rotatedOffset = offsetCenterToPivot.rotate(-angle)
    rotatedImageCenter = (origin[0] - rotatedOffset.x, origin[1] - rotatedOffset.y)
    rotatedImage = pygame.transform.rotate(image, angle)
    rotatedImageRect = rotatedImage.get_rect(center = rotatedImageCenter)
    
    return rotatedImage, rotatedImageRect