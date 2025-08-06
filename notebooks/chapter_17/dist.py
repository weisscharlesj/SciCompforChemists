pt1 = (1,5,9)
pt2 = (9, 0, 3)

def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    
    return ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5