from App.MeshReader.Mesh import Mesh
from App.MeshReader.Entities import Entity, Entities
from App.MeshReader.PhysicalGroups import PhysicalVolume, PhysicalSurface
from App.MeshReader.Nodes import Nodes
from App.MeshReader.Elements import Elements

def AddPhysicalGroups(input: list[str], mesh: Mesh) -> Mesh:
  physicalSurfaces: list[PhysicalSurface] = []
  physicalVolumes: list[PhysicalVolume] = []

  for line in input:
    values = line.split()
    if(int(values[0]) == 2):
      physicalSurfaces.append(PhysicalSurface(int(values[1]), str(values[2])))
    elif(int(values[0]) == 3):
      physicalVolumes.append(PhysicalVolume(int(values[1]), str(values[2])))

  mesh.physicalSurfaces = physicalSurfaces
  mesh.physicalVolumes = physicalVolumes

  return mesh

def AddEntities(input: list[str], mesh: Mesh) -> Mesh:
  line = input.pop(0)
  values = line.split()

  numPoints = int(values[0])
  numCurves = int(values[1])
  numSurfaces = int(values[2])
  numVolumes = int(values[3])

  for _ in range(numPoints):
    line = input.pop(0)

  for _ in range(numCurves):
    line = input.pop(0)

  for _ in range(numSurfaces):
    line = input.pop(0)
    values = line.split()

    surfaceTag = int(values.pop(0))
    minX = float(values.pop(0))
    minY = float(values.pop(0))
    minZ = float(values.pop(0))
    maxX = float(values.pop(0))
    maxY = float(values.pop(0))
    maxZ = float(values.pop(0))

    numPhysicalTags = int(values.pop(0))

    for _ in range(numPhysicalTags):
      physicalTag = int(values.pop(0))
      for physicalSurface in mesh.physicalSurfaces:
        if(physicalSurface.physicalTag == physicalTag):
          physicalSurface.AddEntityTag(surfaceTag)

  for _ in range(numVolumes):
    line = input.pop(0)
    values = line.split()

    volumeTag = int(values.pop(0))
    minX = float(values.pop(0))
    minY = float(values.pop(0))
    minZ = float(values.pop(0))
    maxX = float(values.pop(0))
    maxY = float(values.pop(0))
    maxZ = float(values.pop(0))

    numPhysicalTags = int(values.pop(0))

    for _ in range(numPhysicalTags):
      physicalTag = int(values.pop(0))
      for physicalVolume in mesh.physicalVolumes:
        if(physicalVolume.physicalTag == physicalTag):
          physicalVolume.AddEntityTag(volumeTag)

  return mesh

def ReadMesh(fileLocation) -> Mesh:

  mesh = Mesh()

  file = open(fileLocation, "r")
  lines = file.readlines()

  while(lines):

    line = lines.pop(0)

    if(line == "$PhysicalNames\n"):
      physicalGroupsInput = []
      
      line = lines.pop(0)

      while True:
        line = lines.pop(0)

        if(line == "$EndPhysicalNames\n"):
          break
        else:
          physicalGroupsInput.append(line)

      mesh = AddPhysicalGroups(physicalGroupsInput, mesh)

    if(line == "$Entities\n"):
      entitiesInput = []
      
      while True:
        line = lines.pop(0)

        if(line == "$EndEntities\n"):
          break
        else:
          entitiesInput.append(line)

      mesh = AddEntities(entitiesInput, mesh)

    if(line == "$Nodes\n"):
      nodesInput = []
      
      while True:
        line = lines.pop(0)

        if(line == "$EndNodes\n"):
          break
        else:
          nodesInput.append(line)

      line: str  = nodesInput.pop(0)
      nodes = Nodes(nodesInput)

      xValues = []
      yValues = []
      zValues = []

      for node in nodes.all:
        xValues.append(node.x)
        yValues.append(node.y)
        zValues.append(node.z)

      mesh.xMin = min(xValues)
      mesh.yMin = min(yValues)
      mesh.zMin = min(zValues)

      mesh.xMax = max(xValues)
      mesh.yMax = max(yValues)
      mesh.zMax = max(zValues)

    if(line == "$Elements\n"):
      elementsInput = []
      
      while True:
        line = lines.pop(0)

        if(line == "$EndElements\n"):
          break
        else:
          elementsInput.append(line)

      line = elementsInput.pop(0)

      elements = Elements(elementsInput, nodes)

  mesh.ConnectElementsToPhysicalGroups(elements)
  mesh.ConnectNeighbors()

  file.close()
  node = mesh.physicalElements[0].elementSurfaces[0].nodes[0]

  return mesh

