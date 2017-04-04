from ezmath import *

def getPoints(pts, ):
    global score
    global scoredrop
    global scoredropper
    score += pts
    if (score >= scoredrop):
        scoredropper = 60
        if (scoredrop <= 500):
            scoredrop += 500
        else:
            scoredrop += 1000

def collidingColchecks(pos, radius, p1, colcheck0, colcheck1, colcheck2):
    r = []
    dist = distance(pos, p1.pos)
    if (dist <= 200):
        r.append(colcheck0)
        if (dist + radius > 200):
            r.append(colcheck1)
    elif (dist <= 300):
        r.append(colcheck1)
        if (dist - radius <= 200):
            r.append(colcheck0)
        if (dist + radius > 300):
            r.append(colcheck2)
    else:
        r.append(colcheck2)
        if (dist - radius <= 300):
            r.append(colcheck1)
    return r

