import rhinoscriptsyntax as rs
import math
import random

def main ():
    pt = rs.AddPoint(0,0,0)
    vecDir [0,0,1]
    
    minTwigCount = 1
    maxTwigCount = 2
    maxGen = 3
    maxTwigLength = 10
    lengthMutation = .5
    maxTwigAngle = 90
    angleMutation = .5
    
    newProps = minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation
    
    RecursiveGrowth (ptStart, vecDir, props, 0)
    
def AddArcDir (ptStart, ptEnd, vecDir):
    
    

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
            
            
if __name__ == "__main__"
    main()
    