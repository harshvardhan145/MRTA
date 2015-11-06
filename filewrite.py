def writepoints(filename,points):
    pids=[]
    f = open('out'+filename+'.dat','w+')
    for point in points:
        for p2 in points:
            f.write("%f " % point.idistance(p2))
        f.write("\n")
    f.close()
    for point in points:
    	pids.append(point.pid)
    return pids
