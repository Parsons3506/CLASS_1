import rhinoscriptsyntax as rs
import math


def RecursiveGrowth(ptStart, vecDir, props, gen):
    minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation = props
    
    if gen > maxGen : return
    
    newProps = props
    
    maxTwiglength *= lengthMutation
    maxTwigAngle *= angleMutation
    
    if max twigAngle > 90 : maxTwigAngle = 90
    
    newProps = minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation
    maxN = int(minTwigCount + random.random()* (maxTwigCount-minTwigCount)
    
    for n in range(0,maxN):
        newPoint = RandomPointinCone(ptStart, vecDir, .25*maxTwigLength, maxTwigLength, maxTwigAngle)
        newTwig = AddArcDir(ptStart, newPoint, vecDir)
        if newTwig: 
            vecGrow = rs.CurveTangent(newTwig, rs.CurveDomain(newTwig)[1])