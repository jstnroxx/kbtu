import pygame
import math

from utility import getColor
from tools import *

def main():
    # initialization
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    verdanaFont = pygame.font.SysFont("Verdana", 20)
    
    # basic parameters
    radius = 5
    mode = 'blue'
    tool = 'brush'
    
    BG_COLOR = (0, 0, 0)
    screen.fill(BG_COLOR)
    
    # a separate canvas to preview shapes
    permCanvas = pygame.Surface((640, 480))
    permCanvas.fill(BG_COLOR)
    
    # shape drag start position
    shapeStartPos = None
    
    lastPos = None
    
    while True:
        
        pressed = pygame.key.get_pressed()
        mousePressed = pygame.mouse.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed (selecting colors and tools)
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'eraser'
                elif event.key == pygame.K_3:
                    tool = 'rectangle'
                elif event.key == pygame.K_4:
                    tool = 'circle'
                elif event.key == pygame.K_5:
                    tool = 'square'
                elif event.key == pygame.K_6:
                    tool = 'right triangle'
                elif event.key == pygame.K_7:
                    tool = 'equilateral triangle'
                elif event.key == pygame.K_8:
                    tool = 'rhombus'
            
            # scroll to change tool radius
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0: # scrolling up grows radius
                    radius = min(200, radius + 1)
                elif event.y < 0: # scrolling down shrinks radius
                    radius = max(1, radius - 1)
                    
            SHAPE_TOOLS = ('rectangle', 'circle', 'square', 'right triangle', 'equilateral triangle', 'rhombus')
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if tool in SHAPE_TOOLS:
                    shapeStartPos = event.pos
                else:
                    color = getColor(mode) if tool == 'brush' else BG_COLOR
                    
                    drawPoint(permCanvas, {
                        "color": color,
                        "pos": event.pos,
                        "radius": radius
                    })
                    
                    lastPos = event.pos
                
            if mousePressed[0] and event.type == pygame.MOUSEMOTION:
                if tool in ('brush', 'eraser'):
                    color = getColor(mode) if tool == 'brush' else BG_COLOR
                    
                    if lastPos is not None:
                        drawLineBetween(permCanvas, lastPos, event.pos, color, radius)
                    else:
                        drawPoint(permCanvas, {
                            "color": color,
                            "pos": event.pos,
                            "radius": radius
                        })
                        
                    lastPos = event.pos
                    
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if tool in SHAPE_TOOLS and shapeStartPos is not None:
                    drawShape(permCanvas, tool, shapeStartPos, event.pos, mode, radius)
                    shapeStartPos = None
                    
                lastPos = None
                    
            screen.blit(permCanvas, (0, 0))
            
            if shapeStartPos is not None and mousePressed[0] and tool in SHAPE_TOOLS:
                currentPos = pygame.mouse.get_pos()
                drawShape(screen, tool, shapeStartPos, currentPos, mode, radius, preview = True)
        
        # info hud
        modeText = verdanaFont.render("Color: " + mode, True, (255, 255, 255), BG_COLOR)
        radiusText = verdanaFont.render("Radius: " + str(radius), True, (255, 255, 255), BG_COLOR)
        toolText =  verdanaFont.render("Tool: " + tool, True, (255, 255, 255), BG_COLOR)
        
        screen.blit(toolText, (10, 10))
        screen.blit(modeText, (10, toolText.get_height() + 10))
        screen.blit(radiusText, (10, toolText.get_height() + modeText.get_height() + 10))
        
        pygame.display.flip()
        
        clock.tick(60)

# run the main loop
main()