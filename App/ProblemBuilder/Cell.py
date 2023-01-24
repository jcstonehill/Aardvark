from Materials.MaterialBase import MaterialBase
from App.ProblemBuilder.CellSurface import CellSurface
from App.HelperMath import IntersectionOfLineAndPlane, TetrahedronVolume
import itertools
import numpy as np

class Cell:
    T: float
    previousT: float
    QGen: float
    Q: float
    surfaces: list[CellSurface]
    points: list[list[float]]
    material: MaterialBase
    centerPosition: list[float]

    def __init__(self, points: list[list[float]]):
        self.T = 300
        self.previousQ = 0
        self.QGen = 0
        self.cellBoundaries = []
        self.points = points

        self.CreateCellSurfaces()
        self.CalculateCenter()
        self.CalculateVolume()

    def CreateCellSurfaces(self):
        self.surfaces = []

        nodeCombinations = itertools.combinations(self.points, 3)

        for nodeCombination in nodeCombinations:
            self.surfaces.append(CellSurface(nodeCombination))

    def CalculateCenter(self):
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

    def CalculateVolume(self):
        vertices = np.array(self.points)
        self.volume = TetrahedronVolume(vertices=vertices)

    def ContainsPoint(self, point: list[float]) -> bool:

        x = point[0]
        y = point[1]
        z = point[2]

        for myPoint in self.points:
            if(myPoint[0] == x and myPoint[1] == y and myPoint[2] == z):
                return True

        return False

    def SolveForT(self, dt: float):

        cp = self.material.Cp(self.T)
        rho = self.material.Rho(self.T)
        v = self.volume

        self.previousT = self.T
        self.T = self.T + (dt*self.Q/(v*rho*cp))

    def Error(self) -> float:
        return abs(self.previousT - self.T)