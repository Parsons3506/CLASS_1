import rhinoscriptsyntax as rs
import math
import random

<<<<<<< HEAD
def main ():
    pt = rs.AddPoint(0,0,0)
    vecDir [0,0,1]
    
    minTwigCount = 1
    maxTwigCount = 2
    maxGen = 3
    maxTwigLength = 10
=======


def main():
    
    ptStart = rs.AddPoint(0,0,0)
    vecDir = [0,0,1]
    
    minTwigCount = 1 
    maxTwigCount = 5
    maxGen = 5
    maxTwigLength = 1
>>>>>>> origin/master
    lengthMutation = .5
    maxTwigAngle = 90
    angleMutation = .5
    
<<<<<<< HEAD
    newProps = minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation
    
    RecursiveGrowth (ptStart, vecDir, props, 0)
    
def AddArcDir (ptStart, ptEnd, vecDir):
    
    

def RandomPointInCone(origin, direction, minDistance, maxDistance, maxAngle):
    vecTwig = rs.VectorUnitize (direction)
    vecTwig = rs.VectorScale (vecTwig, minDistance + random.random()* (maxDistance-minDistance))
    

def RecursiveGrowth (ptStart, vedDi, props, gen):
    minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation = props
=======
    
    props = minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation,maxTwigAngle, angleMutation
    
    RecursiveGrowth(ptStart, vecDir, props, 0)


def AddArcDir(ptStart, ptEnd, vecDir):
    vecBase = rs.PointSubtract(ptEnd, ptStart)
    if rs.VectorLength(vecBase)==0.0: return
    if rs.IsVectorParallelTo(vecBase, vecDir): return
    vecBase = rs.VectorUnitize(vecBase)
    vecDir = rs.VectorUnitize(vecDir)
    vecBisector = rs.VectorAdd(vecDir, vecBase)
    vecBisector = rs.VectorUnitize(vecBisector)
    dotProd = rs.VectorDotProduct(vecBisector, vecDir)
    midLength = (0.5*rs.Distance(ptStart, ptEnd))/dotProd
    vecBisector = rs.VectorScale(vecBisector, midLength)
    return rs.AddArc3Pt(ptStart, rs.PointAdd(ptStart, vecBisector), ptEnd)



def RandomPointInCone(origin, direction, minDistance, maxDistance, maxAngle):
    vecTwig = rs.VectorUnitize(direction)
    vecTwig = rs.VectorScale(vecTwig, minDistance + random.random()*(maxDistance-minDistance))
    MutationPlane = rs.PlaneFromNormal((0,0,0), vecTwig)
    vecTwig = rs.VectorRotate(vecTwig, random.random()*maxAngle, MutationPlane[1])
    vecTwig = rs.VectorRotate(vecTwig, random.random()*360, direction)
    return rs.PointAdd(origin, vecTwig)



def RecursiveGrowth(ptStart, vecDir, props, gen):
    minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation,maxTwigAngle, angleMutation = props
>>>>>>> origin/master
    
    if gen > maxGen : return
    
    newProps = props
    
    maxTwigLength *= lengthMutation
    maxTwigAngle *= angleMutation
    
    if maxTwigAngle>90:maxTwigAngle=90
    
<<<<<<< HEAD
    newProps = minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation
    
    maxN=int(minTwigCount+random.random()* (maxTwigCount-minTwigCount))
    
    for n in range (0,maxN):
        newPoint = RandomPointInCone (ptStart, vecDir, .25*maxTwigLength, maxTwigLength, maxTwigAngle)
=======
    newProps = minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation,maxTwigAngle, angleMutation
    
    maxN=int(minTwigCount+random.random()* (maxTwigCount-minTwigCount) )
    
    for n in range(0,maxN):
        newPoint = RandomPointInCone(ptStart, vecDir, .25*maxTwigLength, maxTwigLength, maxTwigAngle)
>>>>>>> origin/master
        newTwig = AddArcDir(ptStart, newPoint, vecDir)
        if newTwig:
            vecGrow = rs.CurveTangent(newTwig, rs.CurveDomain(newTwig)[1])
            RecursiveGrowth(newPoint, vecGrow, newProps, gen+1)
            
            
<<<<<<< HEAD
if __name__ == "__main__"
    main()
    
=======
            

if __name__ == "__main__":
    main()




>>>>>>> origin/master
