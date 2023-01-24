from typing import TYPE_CHECKING
from App.THSolver.ThermalBC import ThermalBC, ConstantTempThermalBC, ConductToNeighborThermalBC, AdiabaticThermalBC, ConvectionToFlowChannelThermalBC
from App.THSolver.FlowChannel import FlowChannel

if TYPE_CHECKING:
    from App.ProblemBuilder.Cell import Cell

class CellBoundary:
    cells: list["Cell"]
    thermalBC: ThermalBC
    centerPosition: list[float]
    area: float

    def __init__(self, cells: list["Cell"], centerPosition: list[float], area: float):
        self.cells = cells
        self.centerPosition = centerPosition
        self.area = area

    def SetConstantTempThermalBC(self, T: float):
        self.thermalBC = ConstantTempThermalBC(self.centerPosition, self.area, self.cells[0], T)

    def SetConductToNeighborThermalBC(self):
        self.thermalBC = ConductToNeighborThermalBC(self.cells, self.area)

    def SetAdiabaticThermalBC(self):
        self.thermalBC = AdiabaticThermalBC()

    def SetConvectionToFlowChannelThermalBC(self, cell: "Cell", flowChannel: FlowChannel):
        self.thermalBC = ConvectionToFlowChannelThermalBC(cell, self.area, flowChannel, self.centerPosition[2])