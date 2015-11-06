from mapPoint import *
def readpoints(filename):
    points = []
    with open(filename) as f:
        for line in f:
            pid,x,y,z = [int(x) for x in line.split()]
            points.append(mapPoint(pid,x,y,z))
    return points
                
