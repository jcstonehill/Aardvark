from typing import TYPE_CHECKING

from Materials.Fluids.FluidBase import FluidBase

class FlowPoint:
    zPos: float
    T: float
    P: float

    def __init__(self, zPos: float):
        self.zPos = zPos

class FlowCell:
    startPoint: FlowPoint
    endPoint: FlowPoint
    Q: float
    Qgen: float
    mDot: float
    T: float
    fp: FluidBase

    def __init__(self, fp: FluidBase):
        self.fp = fp
        self.Q = 0
        self.Qgen = 0


    def SolveNextPoint(self):
        Ti = self.startPoint.T

        Cp = self.fp.Cp()

        To = Ti + self.Q/(self.mDot*Cp)

        self.T = (Ti+To)/2

        self.endPoint.T = To

class FlowChannel:

    regionName: str

    mDot: float
    flowCells: list[FlowCell]
    fp: FluidBase
    Dh: float

    def __init__(self, inletZ: float, outletZ: float, numOfFlowCells: int, fp: FluidBase, P: float, A: float):

        self.inletZ = inletZ
        self.outletZ = outletZ
        self.numOfFlowCells = numOfFlowCells
        self.fp = fp
        self.P = P
        self.A = A

        self.Dh = 4*A/P

        self.BuildFlowChannel()

    def BuildFlowChannel(self):
        self.flowCells = []

        distance = self.outletZ - self.inletZ
        dZ = distance/self.numOfFlowCells

        for i in range(self.numOfFlowCells):

            newFlowCell = FlowCell(self.fp)

            if(i==0):
                newFlowCell.startPoint = FlowPoint(self.inletZ)
                newFlowCell.endPoint = FlowPoint(self.inletZ + dZ)
            else:
                newFlowCell.startPoint = self.flowCells[-1].endPoint
                newFlowCell.endPoint = FlowPoint(self.inletZ + dZ*(i+1))

            self.flowCells.append(newFlowCell)

    def SetInletConditions(self, inletT: float, inletP: float, massFlow: float):

        self.mDot = massFlow

        inletPoint = self.flowCells[0].startPoint

        inletPoint.T = inletT
        inletPoint.P = inletP

        for flowCell in self.flowCells:
            flowCell.T = inletT
            flowCell.mDot = massFlow

    def GetFlowCellAtPosition(self, z: float) -> FlowCell:
        for flowCell in self.flowCells:

            bounds = [flowCell.startPoint.zPos, flowCell.endPoint.zPos]

            zMin = min(bounds)
            zMax = max(bounds)
            if(z>=zMin and z <= zMax):
                return flowCell

        return None

    def AddQToCellAtPosition(self, Q: float, z: float):

        flowCell = self.GetFlowCellAtPosition(z)
        flowCell.Q = flowCell.Q + Q

    def AddQGenToCellAtPosition(self, Qgen: float, z: float):
        flowCell = self.GetFlowCellAtPosition(z)
        flowCell.Qgen

    def GetTAtPosition(self, z: float):
        return self.GetFlowCellAtPosition(z).T

    def Solve(self):
        for flowCell in self.flowCells:
            flowCell.SolveNextPoint()

    def ResetQ(self):
        for flowCell in self.flowCells:
            flowCell.Q = 0