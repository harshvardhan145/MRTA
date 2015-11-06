from filewrite import *
from javacall import *
from mapPoint import *
from hungarian import *
low=0
high=9999
class inspireGraph:
    def __init__(self,mapPoints,bots,threshold,robots):
        self.points = mapPoints
        self.bots = bots  # Represent simple colors of the graph to be assigned to real robots identified by positions in robots. Represent actual number of clusters
        self.colors_of_states = {}
        self.graphify(threshold)
        self.clusters = []
        self.robots = robots  # Positions of actual robots. Represent actual bots, waiting to get assigned to zero or more clusters.
    
    def graphify(self,threshold):
        for p1 in self.points:
            for p2 in self.points:
                if p1.idistance(p2) > threshold:
                    p1.addNeighbor(p2)
                    p2.addNeighbor(p1)
                
    def colorify(self):
        for point in self.points:
            point.color = self.get_color_for_state(point)
            try:  
                self.colors_of_states[point.color].append(point)
            except:
                self.colors_of_states[point.color] = []
                self.colors_of_states[point.color].append(point)
        num_clusters=0
        for bot in self.bots:
            try:
                cluster = self.colors_of_states[bot]
                pids=writepoints(bot,cluster)
                print bot +' -> '+str(pids)
                centroid = self.calcCentroid(cluster,bot)
                #print centroid.pid
                if len(cluster)>1:
                    path = Christofide('out'+bot+'.dat')
                else:
                    path=[0]
                #path=[pids[i] for i in Christofide('out'+bot+'.dat')]
                #print bot
                print path
                self.clusters.append((centroid,cluster,path))
                num_clusters+=1
            except Exception, e:
                print str(e) + ' has no clusters assigned'
        print self.clusters
        print num_clusters
        #self.hungarian() 
        #self.christofideTSP()

    def promising(self,point,color):
        for neighbor in point.neighbor:
            color_of_neighbor = neighbor.color
            if color_of_neighbor == color:
                return False
        return True

    def get_color_for_state(self,point):
        for bot in self.bots:
            if self.promising(point,bot):
                return bot
        
    def christofideTSP(self):
        for bot in self.bots:
            print "Solving for "+bot
            Christofide(bot+'.dat')
    def calcCentroid(self,cluster,name):
        x = 0.0
        y = 0.0
        z = 0.0
        i = 0
        for point in cluster:
            x+=point.x
            y+=point.y
            z+=point.z
            i+=1
        return mapPoint(name,x/i,y/i,z/i)
    def hungarian(self):
        a = []
        for robot in self.robots:
            b = []
            for cluster in self.clusters:
                b.append(robot.idistance(cluster[0]))
            a.append(b)
        print a
        hungarian = Hungarian(a)
        hungarian.calculate()
        allotment = hungarian.get_results()
        print allotment
        #self.plot()
                
    def plot(self):
        for ele in self.clusters:
            print ele[1]
    
