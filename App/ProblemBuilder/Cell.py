from Materials.MaterialBase import MaterialBase
from App.ProblemBuilder.CellBoundary import CellBoundary
from App.HelperMath import TetrahedronVolume
import numpy as np

class Cell:

    id: int

    fissionsPerBatch: list[float]

    T: float
    previousT: float
    QGen: float
    Q: float

    material: MaterialBase
    centerPoint: list[float]

    points: list[list[float]]
    cellBoundaries: list[CellBoundary]
    flux: list[int]

    def __init__(self, cellID: int, points: list[list[float]], cellBoundaries: list[CellBoundary]):

        self.id = cellID

        self.Q = 0
        self.T = 300
        self.previousQ = 0
        self.QGen = 0
        
        self.flux = []

        self.points = points
        self.cellBoundaries = cellBoundaries

        self.CalculateCenter()
        self.CalculateVolume()

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

        self.centerPoint = [x, y, z]

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