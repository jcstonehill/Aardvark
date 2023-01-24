from App.ProblemBuilder.Region import Region
from App.ProblemBuilder.Boundary import Boundary
from App.ProblemBuilder.Cell import Cell
from App.ProblemBuilder.CellBoundary import CellBoundary
from App.THSolver.FlowChannel import FlowChannel
from Materials.MaterialBase import MaterialBase

class Problem:
    regions: list[Region]
    boundaries: list[Boundary]
    cells: list[Cell]
    cellBoundaries: list[CellBoundary]
    flowChannels: list[FlowChannel]

    def __init__(self):
        self.regions = []
        self.boundaries = []
        self.cells = []
        self.cellBoundaries = []
        self.flowChannels = []

    def GetRegion(self, name: str) -> Region:
        for region in self.regions:
            if(region.name == name):
                return region

        return None

    def GetBoundary(self, name: str) -> Boundary:
        for boundary in self.boundaries:
            if(boundary.name == name):
                return boundary

        return None

    def SetConstantTempThermalBC(self, name: str, T: float):
        boundary = self.GetBoundary(name)

        for cellBoundary in boundary.cellBoundaries:
            cellBoundary.SetConstantTempThermalBC(T)

    def SetMaterial(self, name: str, material: MaterialBase):
        region = self.GetRegion(name)

        for cell in region.cells:
            cell.material = material

    def InsertFlowChannel(self, regionName: str, boundaryName: str, flowChannel: FlowChannel):
        flowChannel.regionName = regionName

        region = self.GetRegion(regionName)
        boundary = self.GetBoundary(boundaryName)

        for cell in region.cells:
            for cellSurface in cell.surfaces:
                cellSurface.boundary = CellBoundary([cell], cellSurface.centerPosition, cellSurface.area)
                cellSurface.boundary.SetAdiabaticThermalBC()

        for cellBoundary in boundary.cellBoundaries:
            for cell in cellBoundary.cells:
                if(cell not in region.cells):
                    cellBoundary.SetConvectionToFlowChannelThermalBC(cell, flowChannel)

        self.flowChannels.append(flowChannel)