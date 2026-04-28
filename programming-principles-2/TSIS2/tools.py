import pygame
import math

from utility import getColor

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
    elif tool == 'line':
        lineWidth = max(1, radius)
        
        pygame.draw.line(surface, color, start, end, lineWidth)
            

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
        
        
def floodFill(surface, startPos, fillColor):
    sizeW, sizeH = surface.get_size()
    x0, y0 = startPos
 
    # clamp to canvas
    if not (0 <= x0 < sizeW and 0 <= y0 < sizeH):
        return
 
    targetColor = surface.get_at((x0, y0))[:3] # get pixel color and ignore alpha
    fillColor3   = fillColor[:3] if len(fillColor) >= 3 else fillColor
 
    if targetColor == fillColor3:
        return # already the fill color, do nothing
 
    queue = [(x0, y0)]
    visited = set()
    visited.add((x0, y0))
 
    while queue:
        x, y = queue.pop()
        surface.set_at((x, y), fillColor)
 
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < sizeW and 0 <= ny < sizeH and (nx, ny) not in visited:
                if surface.get_at((nx, ny))[:3] == targetColor:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        
def renderText(surface, font, text, pos, color):
    textSurface = font.render(text, True, color)
    
    surface.blit(textSurface, pos)