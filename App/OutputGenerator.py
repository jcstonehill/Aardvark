from MeshReader.Mesh import Mesh
import csv
def OutputGenerator(mesh: Mesh, fileName: str):
  with open(fileName, 'w') as file:
    file.write("x, y, z, value\n")
    
    for physicalElement in mesh.physicalElements:
      x = str(physicalElement.centerPoint[0])
      y = str(physicalElement.centerPoint[1])
      z = str(physicalElement.centerPoint[2])

      flux = str(physicalElement.fluxTally)

      file.write(x + ", " + y + ", " + z + ", " + flux + "\n")