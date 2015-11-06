import math
class mapPoint:
    def __init__(self,pid,x,y,z):
        self.pid = pid
        self.x = x
        self.y = y
        self.z = z
        self.color = None
        self.neighbor = []
        self.state = None
        
    def __repr__(self):
        return 'P'+str(self.pid)+'('+str(self.x)+','+str(self.y)+')'

    def addNeighbor(self,p):
        self.neighbor.append(p)

    def idistance(self,p):
        return math.sqrt((p.x - self.x)*(p.x - self.x) + (p.y - self.y)*(p.y - self.y))
                                     
