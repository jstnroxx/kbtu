import pygame
import math

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
        
        wid = abs(end[0] - start[0])
        hei = abs(end[1] - start[1])
        
        if wid > 0 and hei > 0:
            pygame.draw.rect(surface, color, (x, y, wid, hei), width)
    elif tool == 'circle':
        centerX = (start[0] + end[0]) // 2
        centerY = (start[1] + end[1]) // 2
        
        radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5 // 2)
        
        if radius > 0:
            pygame.draw.circle(surface, color, (centerX, centerY), radius, width)
    elif tool == 'square':
        
        # use the smaller of dx/dy so the shape stays a square,
        # and preserve the drag direction on each axis
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        
        side = min(abs(dx), abs(dy))
        
        if side > 0:
            x = start[0] if dx >= 0 else start[0] - side
            y = start[1] if dy >= 0 else start[1] - side
            
            pygame.draw.rect(surface, color, (x, y, side, side), width)
    elif tool == 'right triangle':
        
        # right angle sits at bottom-left of the drag bounding box
        # the three vertices are: top-left, bottom-left (right angle), bottom-right
        x0, y0 = min(start[0], end[0]), min(start[1], end[1])
        x1, y1 = max(start[0], end[0]), max(start[1], end[1])
        
        if abs(x1 - x0) > 0 and abs(y1 - y0) > 0:
            pts = [(x0, y0), (x0, y1), (x1, y1)]
            
            pygame.draw.polygon(surface, color, pts, width)
    elif tool == 'equilateral triangle':
        
        # base runs along the bottom of the bounding box,
        # apex is centered above it at height (base * sqrt(3)/2)
        x0, y0 = min(start[0], end[0]), min(start[1], end[1])
        x1, y1 = max(start[0], end[0]), max(start[1], end[1])
        
        base = abs(x1 - x0)
        
        if base > 0:
            apexX = (x0 + x1) / 2
            apexY = y1 - base * math.sqrt(3) / 2   # upward from bottom edge
            
            pts = [(x0, y1), (x1, y1), (apexX, apexY)]
            
            pygame.draw.polygon(surface, color, pts, width)
    elif tool == 'rhombus':
        
        # four points: top-center, right-middle, bottom-center, left-middle
        x0, y0 = min(start[0], end[0]), min(start[1], end[1])
        x1, y1 = max(start[0], end[0]), max(start[1], end[1])
        
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        
        if abs(x1 - x0) > 0 and abs(y1 - y0) > 0:
            pts = [(cx, y0), (x1, cy), (cx, y1), (x0, cy)]
            
            pygame.draw.polygon(surface, color, pts, width)
            

def drawLineBetween(surface, start, end, color, radius):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    
    iterations = max(abs(dx), abs(dy))
    
    if iterations == 0:
        return
    for i in range(iterations):
        progress = i / iterations
        
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        
        pygame.draw.circle(surface, color, (x, y), radius)
        
    
main()