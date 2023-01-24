from App.ProblemBuilder.Cell import Cell

class Region:
    name: str
    cells: list[Cell]

    def __init__(self):
        self.name = ""
        self.cells = []

