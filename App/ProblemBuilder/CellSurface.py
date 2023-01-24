from App.ProblemBuilder.CellBoundary import CellBoundary
import numpy as np

class CellSurface:
    points: list[list[float]]
    normal: list[float]
    centerPosition: list[float]
    area: list[float]
    boundary: CellBoundary

    def __init__(self, points: list[list[float]]):
        self.boundary = None
        self.points = points

        self.CalculateCenterPosition()
        self.CalculateNormal()
        self.CalculateArea()

    def CalculateCenterPosition(self):
        x = 0
        y = 0
        z = 0

        for point in self.points:
            x = x + point[0]
            y = y + point[1]
            z = z + point[2]

        numOfPoints = len(self.points)

        x = x / numOfPoints
        y = y / numOfPoints
        z = z / numOfPoints

        self.centerPosition = [x, y, z]

    def CalculateNormal(self):
        v1 = [self.points[1][0] - self.points[0][0], self.points[1][1] - self.points[0][1], self.points[1][2] - self.points[0][2]]
        v2 = [self.points[2][0] - self.points[0][0], self.points[2][1] - self.points[0][1], self.points[2][2] - self.points[0][2]]

        self.normal = []
        self.normal.append(v1[1]*v2[2] - v1[2]*v2[1])
        self.normal.append(v1[0]*v2[2] - v1[2]*v2[0])
        self.normal.append(v1[0]*v2[1] - v1[1]*v2[0])

    def CalculateArea(self):
        #https://www.quora.com/How-can-I-find-the-area-of-a-triangle-in-3D-coordinate-geometry
        val1 = self.points[1][0] - self.points[0][0]
        val2 = self.points[1][1] - self.points[0][1]
        val3 = self.points[1][2] - self.points[0][2]
        array1 = np.array([val1, val2, val3])

        val1 = self.points[2][0] - self.points[0][0]
        val2 = self.points[2][1] - self.points[0][1]
        val3 = self.points[2][2] - self.points[0][2]
        array2 = np.array([val1, val2, val3])

        cross = np.cross(array1, array2)
        self.area = 0.5*np.linalg.norm(cross)

    def HasSamePoints(self, otherPoints: list[list[float]]) -> bool:
        for point in otherPoints:
            x = point[0]
            y = point[1]
            z = point[2]

            pointMatches = False
            for myPoint in self.points:
                if(myPoint[0] == x and myPoint[1] == y and myPoint[2] == z):
                    pointMatches = True

            if(not pointMatches):
                return False

        return True

