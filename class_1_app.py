import rhinoscriptsyntax as rs
import math


a = 1
c = 10

for u in range(50,100):
    for v in range(0,50):
        x = (c+a*math.cos(v))*math.cos(u)
        y = (c+a*math.cos(v))*math.sin(u)
        z = a*math.sin(v)
        pt = rs.AddPoint(x,y,z)

rs.AddPoint(x,y,z)