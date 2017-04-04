import GlobalVariables
from ezmath import *


def getPoints(pts, ):
    #global score
    #global scoredrop
    #global scoredropper
    GlobalVariables.score += pts
    if (GlobalVariables.score >= GlobalVariables.scoredrop):
        GlobalVariables.scoredropper = 60
        if (GlobalVariables.scoredrop <= 500):
            GlobalVariables.scoredrop += 500
        else:
            GlobalVariables.scoredrop += 1000

def collidingColchecks(pos, radius):
    r = []
    dist = distance(pos, GlobalVariables.p1.pos)
    if (dist <= 200):
        r.append(GlobalVariables.colcheck0)
        if (dist + radius > 200):
            r.append(GlobalVariables.colcheck1)
    elif (dist <= 300):
        r.append(GlobalVariables.colcheck1)
        if (dist - radius <= 200):
            r.append(GlobalVariables.colcheck0)
        if (dist + radius > 300):
            r.append(GlobalVariables.colcheck2)
    else:
        r.append(GlobalVariables.colcheck2)
        if (dist - radius <= 300):
            r.append(GlobalVariables.colcheck1)
    return r

