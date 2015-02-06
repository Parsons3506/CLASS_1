import rhinoscriptsyntax as rs
import math
import random

def RandomPointInCone(origin, direction, minDistance, maxDistance, maxAngle):
    vecTwig = rs.VectorUnitize (direction)
    vecTwig = rs.VectorScale (vecTwig, minDistance + random.random()* (maxDistance-minDistance))
    

def RecursiveGrowth (ptStart, vedDi, props, gen):
    minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation = props
    
    if gen > maxGen : return
    
    newProps = props
    
    maxTwigLength *= lengthMutation
    maxTwigAngle *= angleMutation
    
    if maxTwigAngle>90:maxTwigAngle=90
    
    newProps = minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation
    
    maxN=int(minTwigCount+random.random()* (maxTwigCount-minTwigCount))
    
    for n in range (0,maxN):
        newPoint = RandomPointInCone (ptStart, vecDir, .25*maxTwigLength, maxTwigLength, maxTwigAngle)
        newTwig = AddArcDir(ptStart, newPoint, vecDir)
        if newTwig:
            vecGrow = rs.CurveTangent(newTwig, rs.CurveDomain(newTwig)[1])
            RecursiveGrowth(newPoint, vecGrow, newProps, gen+1)
            