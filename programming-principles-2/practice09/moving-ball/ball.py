import pygame

def drawBall(canvas, color, position, radius):
    pygame.draw.circle(canvas, color, position, radius)
    
def ballMovement(canvasSize, ballRadius, pressedKeys, currentCoordinates, step):
    if pressedKeys[pygame.K_w] or pressedKeys[pygame.K_UP]: 
        if currentCoordinates["Y"] - step - ballRadius >= 0: 
            currentCoordinates["Y"] -= step
        
    if pressedKeys[pygame.K_a] or pressedKeys[pygame.K_LEFT]:
        if currentCoordinates["X"] - step - ballRadius >= 0:
            currentCoordinates["X"] -= step
        
    if pressedKeys[pygame.K_s] or pressedKeys[pygame.K_DOWN]:
        if currentCoordinates["Y"] + step + ballRadius <= canvasSize[1]:
            currentCoordinates["Y"] += step
        
    if pressedKeys[pygame.K_d] or pressedKeys[pygame.K_RIGHT]:
        if currentCoordinates["X"] + step + ballRadius <= canvasSize[0]:
            currentCoordinates["X"] += step
    
    return currentCoordinates