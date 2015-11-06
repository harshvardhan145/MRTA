class mapPoint:
    def __init__(self,pid,x,y,z):
        self.pid = pid
        self.x = x
        self.y = y
        self.z = z
        self.color = None
        self.neighbor = []
        self.state = None
        
