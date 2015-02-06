import rhinoscriptsyntaxas rs
import math


def RecursiveGrowth (ptStart, vecDir, props, gen):
    minTwigCont, maxTwigCount, maxGen, maxTwiglength, lengthMutation, angleMtation = props
    
    if gen > maxGen : return
    
    newProps = props
    
    maxTwigLength *= lengthMutation
    maxTwigAngle *= angleMutation
    
    if maxTwigAngle>90:maxTwigAngle=90
    
    newProps = minTwigCont, maxTwigCount, maxGen, maxTwiglength, lengthMutation, angleMtation = props
    
    maxN=int (minTwigCount+random.random()* (maxTwigCount-minTwigCount) )
    
    
    for n in range (0, maxN)
        newPoint = RandomPointInCone (ptStart, vecDir, .25*maxTwigLength, maxTwigLength, maxTwigAngle
        
        newTwig = AddArchDir (ptStart, newPoint, vecDir)
        if newTwig:
                vecGrow = rs.CurveTangent (newTwigm 


