import rhinoscriptsyntax as rs
import math
import random



def main():
    
    aMesh = rs.GetObject("Pick mesh",32)
    if aMesh is None: return
    
    ptStart = rs.AddPoint(0,0,0)
    vecDir = [0,0,1]
    
    minTwigCount = 1 
    maxTwigCount = 5
    maxGen = 25
    maxTwigLength = 1
    lengthMutation = .5
    maxTwigAngle = 270
    angleMutation = .5
    
    
    props = minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation,maxTwigAngle, angleMutation
    
    RecursiveGrowth(ptStart, vecDir, props, 0, aMesh)

def getClosestPointOnMesh (point, mesh):
    data = rs.MeshClosestPoint(mesh, point)
    return data [0]

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
    #return rs.AddArc3Pt(ptStart, rs.PointAdd(ptStart, vecBisector), ptEnd)
    return rs.AddLine(ptStart, ptEnd)



def RandomPointInCone(origin, direction, minDistance, maxDistance, maxAngle):
    vecTwig = rs.VectorUnitize(direction)
    vecTwig = rs.VectorScale(vecTwig, minDistance + random.random()*(maxDistance-minDistance))
    MutationPlane = rs.PlaneFromNormal((0,0,0), vecTwig)
    vecTwig = rs.VectorRotate(vecTwig, random.random()*maxAngle, MutationPlane[1])
    vecTwig = rs.VectorRotate(vecTwig, random.random()*360, direction)
    return rs.PointAdd(origin, vecTwig)



def RecursiveGrowth(ptStart, vecDir, props, gen, aMesh):
    minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation,maxTwigAngle, angleMutation = props
    
    if gen > maxGen : return
    
    newProps = props
    
    maxTwigLength *= lengthMutation
    maxTwigAngle *= angleMutation
    
    if maxTwigAngle>90:maxTwigAngle=90
    
    newProps = minTwigCount, maxTwigCount, maxGen, maxTwigLength, lengthMutation,maxTwigAngle, angleMutation
    
    maxN=int(minTwigCount+random.random()* (maxTwigCount-minTwigCount) )
    
    for n in range(0,maxN):
        meshPoint = getClosestPointOnMesh(ptStart,aMesh)
        newVector = rs.VectorCreate(meshPoint, ptStart)
        vecDir = newVector
        newPoint = RandomPointInCone(ptStart, vecDir, .25*maxTwigLength, maxTwigLength, maxTwigAngle)
        newTwig = AddArcDir(ptStart, newPoint, vecDir)
        if newTwig:
            vecGrow = rs.CurveTangent(newTwig, rs.CurveDomain(newTwig)[1])
            RecursiveGrowth(newPoint, vecGrow, newProps, gen+1, aMesh)
            
            
            

if __name__ == "__main__":
    main()