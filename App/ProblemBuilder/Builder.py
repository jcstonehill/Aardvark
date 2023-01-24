from App.MeshReader.Mesh import Mesh
from App.ProblemBuilder.Problem import Problem
from App.ProblemBuilder.Region import Region
from App.ProblemBuilder.Cell import Cell
from App.ProblemBuilder.CellBoundary import CellBoundary
from App.ProblemBuilder.Boundary import Boundary

def CreateProblemFrom(mesh: Mesh) -> Problem:
    problem = Problem()

    for physicalVolume in mesh.physicalVolumes:
        region = Region()
        region.name = physicalVolume.name

        for element in physicalVolume.elements:
            
            points = []
            for node in element.nodes:
                x = node.x
                y = node.y
                z = node.z

                points.append([x, y, z])
            
            cell = Cell(points)

            region.cells.append(cell)
            problem.cells.append(cell)
        
        problem.regions.append(region)

    for cell1 in problem.cells:
        for cell2 in problem.cells:
            if(cell1 != cell2):
                for surface1 in cell1.surfaces:
                    for surface2 in cell2.surfaces:
                        if(surface1.HasSamePoints(surface2.points)):
                            newCellBoundary = CellBoundary([cell1, cell2], surface1.centerPosition, surface1.area)

                            surface1.boundary = newCellBoundary
                            surface2.boundary = newCellBoundary

                            problem.cellBoundaries.append(newCellBoundary)

    for physicalSurface in mesh.physicalSurfaces:
        newBoundary = Boundary()
        newBoundary.name = physicalSurface.name

        for elementSurface in physicalSurface.elementSurfaces:
            points = []
            for node in elementSurface.nodes:
                points.append([node.x, node.y, node.z])

            for cell in problem.cells:
                for cellSurface in cell.surfaces:
                    if(cellSurface.HasSamePoints(points)):
                        newCellBoundary = CellBoundary([cell], cellSurface.centerPosition, cellSurface.area)

                        newBoundary.cellBoundaries.append(newCellBoundary)
                        problem.cellBoundaries.append(newCellBoundary)

                        cellSurface.boundary = newCellBoundary

        problem.boundaries.append(newBoundary)

    for cell in problem.cells:
        for cellSurface in cell.surfaces:
            
            if(cellSurface.boundary == None):
                newCellBoundary = CellBoundary([cell], cellSurface.centerPosition, cellSurface.area)

                problem.cellBoundaries.append(newCellBoundary)

    for cellBoundary in problem.cellBoundaries:
        if(len(cellBoundary.cells) == 1):
            cellBoundary.SetAdiabaticThermalBC()
        else:
            cellBoundary.SetConductToNeighborThermalBC()

    return problem

                
