import rhinoscriptsyntax as rs
import math

a=2
c=5


for v in range (0,100):
    for u in range (0,100):
       x = (c+a*math.cos(v))*math.cos(u)
       y = (c+a*math.cos(v))*math.sin(u)
       z = a*math.sin(v)
       pt = rs.AddPoint( x,y,z)




