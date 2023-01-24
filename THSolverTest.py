from App.MeshReader.MeshReader import ReadMesh
from Materials.TH_TEST1 import TH_TEST1
from Materials.TH_TEST2 import TH_TEST2
from App.THSolver.Old_THBC import ConstantTempTHBC, ConductToNeighborTHBC
from App.OutputGenerator import OutputGenerator
from time import sleep

if __name__ == "__main__":
    mesh = ReadMesh("Cases/Case1/mesh.msh")

    mesh.SetMaterial("vol1", TH_TEST1())
    mesh.SetMaterial("vol2", TH_TEST2())

    thbcs = []

    for firstElement in mesh.physicalElements:
      for secondElement in mesh.physicalElements:
        if firstElement != secondElement:
          for firstSurface in firstElement.elementSurfaces:
            for secondSurface in secondElement.elementSurfaces:
              if firstSurface.IsSister(secondSurface.nodes):
                thbcs.append(ConductToNeighborTHBC(firstElement, secondElement, firstSurface.area))

    for elementSurface in mesh.GetPhysicalSurface("front").elementSurfaces:
        thbcs.append(ConstantTempTHBC(500, elementSurface.myElement, elementSurface.centerPosition, elementSurface.area))

    for elementSurface in mesh.GetPhysicalSurface("back").elementSurfaces:
        thbcs.append(ConstantTempTHBC(300, elementSurface.myElement, elementSurface.centerPosition, elementSurface.area))

    for physicalElement in mesh.physicalElements:
        physicalElement.t = 400


    i = 0
    totalError = 9999
    while(totalError > 1):

        i = i+1

        temperatures = []
        powers = []

        for element in mesh.physicalElements:
            temperatures.append(element.t)
            powers.append(element.q)
            
        for element in mesh.physicalElements:
            element.q = 0

        for thbc in thbcs:
            thbc.Solve()

        for element in mesh.physicalElements:
            cp = 300
            rho = element.material.Rho(1)
            v = element.volume

            element.previousT = element.t
            element.t = element.t + (1e-1*element.q/(v*rho*cp))

        totalError = 0
        for element in mesh.physicalElements:
            totalError = totalError + (abs(element.previousT-element.t))
        print("Iteration " + str(i) + " : " + str(totalError))


    OutputGenerator(mesh, "TH_Output.csv")