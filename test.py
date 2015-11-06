from mapPoint import *
from inspireGraph import *
from fileinput import *
from filewrite import *
points = readpoints("pointset1.dat")
robots = readpoints("robots.dat")
bots = ['color'+str(i) for i in range (1,100)];


#Static Threshholding
'''
g = inspireGraph(points,bots,0,robots)
x=g.colorify()
print x

'''
low=0.1
res=0
high=100000
runs=[]
while(res!=len(robots)):
	curr=float((low+high)/2)
	runs.append(curr)
	g = inspireGraph(points,bots,curr,robots)
	res=g.colorify()
	if(res<len(robots)):
		high=curr
	elif(res>len(robots)):
		low=curr
	else:
		break
print runs
print curr