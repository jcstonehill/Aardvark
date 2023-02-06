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
    cellBoundaries: dict

    numOfProcesses: int
    numOfParticles: int
    inactiveBatches: int
    activeBatches: int

    flowChannels: list[FlowChannel]

    
    

    def __init__(self):
        self.numOfProcesses = 1
        self.numOfParticles = 1000
        self.inactiveBatches = 1
        self.activeBatches = 1

        self.regions = []
        self.boundaries = []
        self.cells = []
        self.flowChannels = []
        self.cellBoundaries = {}

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

    def GetCell(self, id: int) -> Cell:
        for cell in self.cells:
            if(cell.id == id):
                return cell

    def SetBatches(self, inactiveBatches: int, activeBatches: int):
        self.inactiveBatches = inactiveBatches
        self.activeBatches = activeBatches

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
            for cellBoundary in cell.cellBoundaries:
                cellBoundary.SetAdiabaticThermalBC()

        for cellBoundary in boundary.cellBoundaries:
            for cell in cellBoundary.cells:
                if(cell not in region.cells):
                    cellBoundary.SetConvectionToFlowChannelThermalBC(cell, flowChannel)

        self.flowChannels.append(flowChannel)