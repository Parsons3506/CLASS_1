import rhinoscriptsyntax as rs
import math


def main():
    pt = rs.AddPoint(0,0,0)
    vecDir = [0,0,1]
    
    
    min
    
    
    Props = minTwigCount, minTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleLengthMutation = props

def Add

def randomPointInCone (orgin, direction, minDistance, maxDistance, maxAngle):
    vecTwig = rs.VectorUnitise(direction)
    vecTwig = rs.VectorScale(vecTwig,minDistance + random.random()*

def RecursiveGrowth(ptStart, vecDir, props, gen):
    minTwigCount, minTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleLengthMutation = props
    if gen > maxGen : return
    newProps = props
    maxTwiglength *= lengthMutation 
    maxTwigAngle *= angleMutation 
    
    if maxTwigAngle>90:maxTwigAngle=90
    
    minTwigCount, minTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleLengthMutation = props
    
    maxN=int(minTwigCount + random() *(maxTwigCount-minTwigCount) )
    for n in range(0, maxN):
    
    newPoint = RandomPointInCone (pointStart, vecDir, p25*maxTwigLength, maxTwigAngle
    newTwig = AddArcDir(ptStart, newPoint, vecDir)
    if newTwig:
        vecGrow = rs.CurveTangent(newTwig, rs.CurveDomain (newTwig) (1))
        RecursiveGrowth(newPoint, vecGrow,

if__name__=="main