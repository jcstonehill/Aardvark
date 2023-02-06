import numpy as np
from typing import TYPE_CHECKING
from App.THSolver.ThermalBC import ThermalBC, ConstantTempThermalBC, ConductToNeighborThermalBC, AdiabaticThermalBC, ConvectionToFlowChannelThermalBC
from App.NSolver.MCBC_Base import MCBC
from App.THSolver.FlowChannel import FlowChannel
from App.HelperMath import IntersectionOfLineAndPlane

if TYPE_CHECKING:
    from App.ProblemBuilder.Cell import Cell

class CellBoundary:
    normal: list[float]
    cells: list["Cell"]
    thermalBC: ThermalBC
    mcbc: MCBC
    centerPosition: list[float]
    area: float
    points: list[list[float]]
    

    def __init__(self, points: list[list[float]]):
        self.points = points
        self.cells = []
        self.centerPosition = [0, 0, 0]

        self.CalculateNormal()

        for point in self.points:
            self.centerPosition[0] = self.centerPosition[0] + point[0]
            self.centerPosition[1] = self.centerPosition[1] + point[1]
            self.centerPosition[2] = self.centerPosition[2] + point[2]

        self.centerPosition[0] = self.centerPosition[0]/len(self.points)
        self.centerPosition[1] = self.centerPosition[1]/len(self.points)
        self.centerPosition[2] = self.centerPosition[2]/len(self.points)

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

    def Intersection(self, startPosition: list[float], endPosition: list[float]):
        nodePosition = [self.points[0][0], self.points[0][1], self.points[0][2]]
        intersection = IntersectionOfLineAndPlane(startPosition, endPosition, nodePosition, self.normal)
        if(intersection is not None):
            if(intersection[0] == startPosition[0] and intersection[1] == startPosition[1] and intersection[2] == startPosition[2]):
                intersection = None

        return intersection

    def CalculateNormal(self):
        v1 = [self.points[1][0] - self.points[0][0], self.points[1][1] - self.points[0][1], self.points[1][2] - self.points[0][2]]
        v2 = [self.points[2][0] - self.points[0][0], self.points[2][1] - self.points[0][1], self.points[2][2] - self.points[0][2]]

        self.normal = []
        self.normal.append(v1[1]*v2[2] - v1[2]*v2[1])
        self.normal.append(v1[0]*v2[2] - v1[2]*v2[0])
        self.normal.append(v1[0]*v2[1] - v1[1]*v2[0])

    def SetConstantTempThermalBC(self, T: float):
        self.thermalBC = ConstantTempThermalBC(self.centerPosition, self.area, self.cells[0], T)

    def SetConductToNeighborThermalBC(self):
        self.thermalBC = ConductToNeighborThermalBC(self.cells, self.area)

    def SetAdiabaticThermalBC(self):
        self.thermalBC = AdiabaticThermalBC()

    def SetConvectionToFlowChannelThermalBC(self, cell: "Cell", flowChannel: FlowChannel):
        self.thermalBC = ConvectionToFlowChannelThermalBC(cell, self.area, flowChannel, self.centerPosition[2])