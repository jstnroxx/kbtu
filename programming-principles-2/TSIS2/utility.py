def getColor(mode):
    if type(mode) is tuple:
        return mode
    
    return {
        "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)
    }.get(mode, (255, 255, 255))    