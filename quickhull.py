import math

hull = []

def quickHull(S):
    S = sorted(S, key=lambda x: x[0])
    hull.append(S[0])
    hull.append(S[-1])
    S1 = []
    S2 = []

    for x in S:
        if (sideOfLinePointIsOn([S[0], S[-1]], x) > 0.00):
                S2.append(x)
                
        if(sideOfLinePointIsOn([S[0], S[-1]], x) < 0.00):
                S1.append(x)
    
    findHull(S1, S[0], S[-1])
    findHull(S2, S[-1], S[0])

def findHull(Sk, P, Q):
    if(len(Sk) == 0): return
    furthestPoint = Sk[0]
    maxDist = 0
    for x in Sk:
        
        dist = findDistPointLine(x, [P, Q])
        if(dist > maxDist): 
            maxDist = dist;
            furthestPoint = x;
    
    Sk.remove(furthestPoint);

    hull.insert(1, furthestPoint);
    S1 = []
    S2 = []
    for p in Sk: 
        if(isInsideTriangle(P, furthestPoint, Q, p)): Sk.remove(p)
        if(sideOfLinePointIsOn([P, furthestPoint], p) > 0.00):
                S2.append(x)
        if(sideOfLinePointIsOn([furthestPoint, Q], x) < 0.00):
                S1.append(x)
    findHull(S1, P, furthestPoint);
    findHull(S2, furthestPoint, Q);

        

def slopeCalc(P, Q):
    return (Q[1] - P[1])/(Q[0]-P[0])


# y =ax+b, y=cx+d
# x = (d-b)/(a-c)
def findNearestPoint(point, line):
    line = sorted(line, key=lambda x: x[0])
    # reg line
    slope = slopeCalc(line[0], line[1]);

    yInt = line[0][1] - (slope * line[0][0]);

    #neg reciprocal
    slopeRecip = (-1)/slope;
    yIntRecip = point[1] - (slopeRecip * line[0][0]);

    nearestPoint = [0,0]
    nearestPoint[0] = (yIntRecip -yInt)/(slope-slopeRecip)
    nearestPoint[1] = slope * nearestPoint[0] + yInt
    
    # if nearestPoint x val is less than min x val on segment PQ
    if(nearestPoint[0] < line[0][0]):
        return line[0]

    # if nearestPoint x val is greater than max x val on segment PQ
    if(nearestPoint[0] > line[-1][0]):
        return line[-1]
    
   
    return nearestPoint;
    
def findPointDistance(P1, P2):
    
    return math.hypot(P2[0] - P1[0], P2[1] - P1[1])


def findDistPointLine(point, line):
    return findPointDistance(point, findNearestPoint(point, line));


def sideOfLinePointIsOn(line, x):
    vectAB = ((line[1][0] - line[0][0]), line[1][1] - line[0][1])
    vectAX = ((x[0] - line[0][0]), x[1] - line[0][1])
    zCoord = (vectAB[0] * vectAX[1]) - (vectAB[1] * vectAX[0])
    return zCoord;

def isInsideTriangle(A, B, C, p):
    if(
    (sideOfLinePointIsOn((A,B), p) > 0) and
    (sideOfLinePointIsOn((B,C), p) > 0) and
    (sideOfLinePointIsOn((C,A), p) > 0)):
     return True;

quickHull([
    [732.0, 590.0],
    [415.0, 360.0],
    [276.0, 276.0],
    [229.0, 544.0],
    [299.0, 95.0]
]);

print(hull)