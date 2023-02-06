import gmsh
import os
import itertools
from App.ProblemBuilder.Problem import Problem
from App.ProblemBuilder.Region import Region
from App.ProblemBuilder.Cell import Cell
from App.ProblemBuilder.CellBoundary import CellBoundary
from App.ProblemBuilder.Boundary import Boundary
from App.THSolver.ThermalBC import ConductToNeighborThermalBC, AdiabaticThermalBC
from App.NSolver.MCBC import TransportToNeighborMCBC, VoidMCBC

def CreateProblem(filePath: str) -> Problem:

    problem = Problem()

    gmsh.initialize()
    gmsh.open(os.getcwd() + filePath)

    physicalVolumes = gmsh.model.getPhysicalGroups(dim=3)

    for physicalVolume in physicalVolumes:
        newRegion = Region()

        dim = 3
        physicalTag = physicalVolume[1]

        newRegion.name = gmsh.model.getPhysicalName(dim, physicalTag)
        
        entities = gmsh.model.getEntitiesForPhysicalGroup(dim, physicalTag)

        for entity in entities:
            elementTags = gmsh.model.mesh.getElements(dim, entity)[1][0]

            for elementTag in elementTags:

                nodeTags = gmsh.model.mesh.getElement(elementTag)[1]
                
                nodeTagCombinations = itertools.combinations(nodeTags, 3)
                nodeTagCombinations = [list(combination) for combination in nodeTagCombinations]

                sortedNodeTagCombinations = [sorted(nodeTagCombination) for nodeTagCombination in nodeTagCombinations]

                cellBoundaries = []

                for combination in sortedNodeTagCombinations:
                    key = str(combination[0]) + "_" + str(combination[1]) + "_" + str(combination[2])

                    if(key in problem.cellBoundaries):
                        cellBoundaries.append(problem.cellBoundaries[key])
                    else:
                        
                        points = []
                        for nodeTag in combination:
                            nodeCoord = gmsh.model.mesh.getNode(nodeTag)[0]

                            points.append(list(nodeCoord))

                        newCellBoundary = CellBoundary(points)
                        problem.cellBoundaries[key] = newCellBoundary
                        cellBoundaries.append(newCellBoundary)

                points = []
                for nodeTag in nodeTags:
                    points.append(list(gmsh.model.mesh.getNode(nodeTag)[0]))

                newCell = Cell(elementTag, points, cellBoundaries)
                newRegion.cells.append(newCell)
                problem.cells.append(newCell)

        problem.regions.append(newRegion)

    for cell in problem.cells:
        for cellBoundary in cell.cellBoundaries:
            cellBoundary.cells.append(cell)

    physicalSurfaces = gmsh.model.getPhysicalGroups(dim=2)

    for physicalSurface in physicalSurfaces:
        newBoundary = Boundary()

        dim = 2
        physicalTag = physicalSurface[1]

        newBoundary.name = gmsh.model.getPhysicalName(dim, physicalTag)

        entities = gmsh.model.getEntitiesForPhysicalGroup(dim, physicalTag)

        for entity in entities:
            elementTags = gmsh.model.mesh.getElements(dim, entity)[1][0]

            for elementTag in elementTags:

                nodeTags = list(gmsh.model.mesh.getElement(elementTag)[1])
                sortedNodeTags = sorted(nodeTags)

                key = str(sortedNodeTags[0]) + "_" + str(sortedNodeTags[1]) + "_" + str(sortedNodeTags[2])
                
                newBoundary.cellBoundaries.append(problem.cellBoundaries[key])

        problem.boundaries.append(newBoundary)

    for cellBoundary in problem.cellBoundaries.values():
        
        if(len(cellBoundary.cells) == 2):
            cellBoundary.thermalBC = ConductToNeighborThermalBC(cellBoundary.cells, cellBoundary.area)
            cellBoundary.mcbc = TransportToNeighborMCBC(cellBoundary.cells)
        elif(len(cellBoundary.cells) == 1):
            cellBoundary.thermalBC = AdiabaticThermalBC()
            cellBoundary.mcbc = VoidMCBC()

    return problem