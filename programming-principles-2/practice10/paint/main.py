import pygame

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
    viewCanvas = pygame.Surface((640, 480))
    viewCanvas.fill(BG_COLOR)
    
    # shape drag start position
    shapeStartPos = None
    
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
            
            # scroll to change tool radius
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0: # scrolling up grows radius
                    radius = min(200, radius + 1)
                elif event.y < 0: # scrolling down shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if tool in ('rectangle', 'circle'):
                    shapeStartPos = event.pos
                else:
                    point = {
                        "color" : mode if tool != 'eraser' else BG_COLOR,
                        "pos" : event.pos,
                        "radius" : radius
                    }
                    
                    drawPoint(viewCanvas, point)
                
            if mousePressed[0] and event.type == pygame.MOUSEMOTION:
                if tool == 'brush':
                    point = {
                        "color": mode,
                        "pos": event.pos,
                        "radius": radius
                    }
                    
                    drawPoint(viewCanvas, point)
                elif tool == 'eraser':
                    point = {
                        "color": BG_COLOR,
                        "pos": event.pos,
                        "radius": radius
                    }
                    
                    drawPoint(viewCanvas, point)
                    
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if tool in ('rectangle', 'circle') and shapeStartPos is not None:
                    drawShape(viewCanvas, tool, shapeStartPos, event.pos, mode, radius)
                    shapeStartPos = None
                    
            screen.blit(viewCanvas, (0, 0))
            
            if shapeStartPos is not None and mousePressed[0] and tool in ('rectangle', 'circle'):
                currentPos = pygame.mouse.get_pos()
                drawShape(screen, tool, shapeStartPos, currentPos, mode, radius, preview = True)
        
        # info hud
        modeText = verdanaFont.render("Color: " + mode, True, (255, 255, 255), BG_COLOR)
        radiusText = verdanaFont.render("Radius: " + str(radius), True, (255, 255, 255), BG_COLOR)
        toolText =  verdanaFont.render("Tool: " + tool, True, (255, 255, 255), BG_COLOR)
        
        pygame.draw.rect(screen, BG_COLOR, (10, 10, 150, toolText.get_height() + modeText.get_height() + radiusText.get_height()))
        
        screen.blit(toolText, (10, 10))
        screen.blit(modeText, (10, toolText.get_height() + 10))
        screen.blit(radiusText, (10, toolText.get_height() + modeText.get_height() + 10))
        
        pygame.display.flip()
        
        clock.tick(60)

# functions
def getColor(mode):
    if type(mode) is tuple:
        return mode
    
    return {
        "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)
    }.get(mode, (255, 255, 255))


def drawPoint(screen, point):
    color = getColor(point.get("color"))
    
    x = point.get("pos", [])[0]
    y = point.get("pos", [])[1]
    pygame.draw.circle(screen, color, (x, y), point.get("radius"))
    
    
def drawShape(surface, tool, start, end, mode, radius, preview = False):
    color = getColor(mode)
    width = radius if preview else 0
    
    if tool == 'rectangle':
        x = min(start[0], end[0])
        y = min(start[1], end[1])
        w = abs(end[0] - start[0])
        h = abs(end[1] - start[1])
        
        if w > 0 and h > 0:
            pygame.draw.rect(surface, color, (x, y, w, h), width)

    elif tool == 'circle':
        cx = (start[0] + end[0]) // 2
        cy = (start[1] + end[1]) // 2
        r = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5 // 2)
        
        if r > 0:
            pygame.draw.circle(surface, color, (cx, cy), r, width)
        
    
main()