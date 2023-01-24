from typing import TYPE_CHECKING
from App.THSolver.FlowChannel import FlowChannel
import math

if TYPE_CHECKING:
    from App.ProblemBuilder.Cell import Cell
from abc import ABC, abstractmethod

class ThermalBC(ABC):
    
    @abstractmethod
    def Solve(self):
        pass

class ConductToNeighborThermalBC(ThermalBC):

    cells: list["Cell"]
    A: float
    distance: float

    def __init__(self, cells: list["Cell"], A: float):
        self.cells = cells
        self.A = A

        dx = self.cells[0].centerPosition[0] - self.cells[1].centerPosition[0]
        dy = self.cells[0].centerPosition[1] - self.cells[1].centerPosition[1]
        dz = self.cells[0].centerPosition[2] - self.cells[1].centerPosition[2]

        self.distance = (dx**2 + dy**2 + dz**2)**0.5

    def Solve(self):
        material1 = self.cells[0].material
        material2 = self.cells[1].material

        T1 = self.cells[0].T
        T2 = self.cells[1].T

        k1 = material1.k(T1)
        k2 = material2.k(T2)

        k = (k1+k2)/2

        Q = k*self.A*abs(T2-T1)/self.distance

        if(T1 > T2):
            self.cells[0].Q = self.cells[0].Q - Q
            self.cells[1].Q = self.cells[1].Q + Q
        else:
            self.cells[0].Q = self.cells[0].Q + Q
            self.cells[1].Q = self.cells[1].Q - Q

class AdiabaticThermalBC(ThermalBC):

    def Solve(self):
        pass

class ConstantTempThermalBC(ThermalBC):

    centerPosition: list[float]
    A: float
    T: float
    cell: "Cell"
    distance: float

    def __init__(self, centerPosition: list[float], A: float, cell: "Cell", T: float):
        self.centerPosition = centerPosition
        self.A = A
        self.T = T
        self.cell = cell

        dx = self.centerPosition[0] - self.cell.centerPosition[0]
        dy = self.centerPosition[1] - self.cell.centerPosition[1]
        dz = self.centerPosition[2] - self.cell.centerPosition[2]

        self.distance = (dx**2 + dy**2 + dz**2)**0.5

    def Solve(self):
        material = self.cell.material

        T1 = self.T
        T2 = self.cell.T

        k1 = material.k(T1)
        k2 = material.k(T2)

        k = (k1+k2)/2

        Q = k*self.A*abs(T2-T1)/self.distance

        if(T1>T2):
            self.cell.Q = self.cell.Q + Q
        else:
            self.cell.Q = self.cell.Q - Q

class ConvectionToFlowChannelThermalBC(ThermalBC):
    def __init__(self, cell: "Cell", A: float, flowChannel: FlowChannel, zPosition: float):
        self.cell = cell
        self.A = A
        self.flowChannel = flowChannel
        self.zPosition = zPosition

    def Solve(self):

        mDot = self.flowChannel.mDot
        Dh = self.flowChannel.Dh
        mu = self.flowChannel.fp.mu()

        Re = 4*mDot/(math.pi*Dh*mu)

        Cp = self.flowChannel.fp.Cp()
        k = self.flowChannel.fp.k()
        
        Pr = Cp*mu/k


        Nu = 0.023*(Re**0.8)*(Pr**0.4)

        h = Nu*k/Dh

        solidT = self.cell.T
        fluidT = self.flowChannel.GetTAtPosition(self.zPosition)

        Q = h*self.A*abs(solidT - fluidT)

        if(solidT > fluidT):
            self.cell.Q = self.cell.Q - Q
            self.flowChannel.AddQToCellAtPosition(Q, self.zPosition)
        else:
            self.cell.Q = self.cell.Q + Q
            self.flowChannel.AddQToCellAtPosition(-1*Q, self.zPosition)