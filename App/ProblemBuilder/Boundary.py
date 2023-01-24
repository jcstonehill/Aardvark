from App.ProblemBuilder.CellBoundary import CellBoundary

class Boundary:
    name: str
    cellBoundaries: list[CellBoundary]

    def __init__(self):
        self.name = ""
        self.cellBoundaries = []