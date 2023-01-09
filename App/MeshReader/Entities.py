from dataclasses import dataclass

class Entity:
  pass

@dataclass
class Point(Entity):
  pointTag: int
  x: float
  y: float
  z: float
  numPhysicalTags: int
  physicalTags: list[int]

@dataclass
class Curve(Entity):
  curveTag: int
  minX: float
  minY: float
  minZ: float
  maxX: float
  maxY: float
  maxZ: float
  numPhysicalTags: int
  physicalTags: list[int]
  numBoundingPoints: int
  pointTags: list[int]

@dataclass
class Surface(Entity):
  surfaceTag: int
  minX: float
  minY: float
  minZ: float
  maxX: float
  maxY: float
  maxZ: float
  numPhysicalTags: int
  physicalTags: list[int]
  numBoundingCurves: int
  curveTags: list[int]

@dataclass
class Volume(Entity):
  volumeTag: int
  minX: float
  minY: float
  minZ: float
  maxX: float
  maxY: float
  maxZ: float
  numPhysicalTags: int
  physicalTags: list[int]
  numBoundingSurfaces: int
  surfaceTags: list[int]

class Entities:
  numPoints: int = 0
  numCurves: int = 0
  numSurfaces: int = 0
  numVolumes: int = 0

  points: list[Point] = []
  curves: list[Curve] = []
  surfaces: list[Surface] = []
  volumes: list[Volume] = []

  def __init__(self, input: list[str]):
    # First line is the number of each entity
    line = input.pop(0)
    values = line.split()

    self.numPoints = int(values[0])
    self.numCurves = int(values[1])
    self.numSurfaces = int(values[2])
    self.numVolumes = int(values[3])

    # Create Points
    for _ in range(self.numPoints):
      line = input.pop(0)
      values = line.split()

      tag = int(values[0])
      x = float(values[1])
      y = float(values[2])
      z = float(values[3])
      numPhysicalTags = int(values[4])
      physicalTags = []

      for i in range(numPhysicalTags):
        physicalTags.append(values[5+i])

      self.points.append(Point(tag, x, y, z, numPhysicalTags, physicalTags))
    
    # Create Curves
    for _ in range(self.numCurves):
      line = input.pop(0)
      values = line.split()

      tag = int(values.pop(0))
      minX = float(values.pop(0))
      minY = float(values.pop(0))
      minZ = float(values.pop(0))
      maxX = float(values.pop(0))
      maxY = float(values.pop(0))
      maxZ = float(values.pop(0))

      numPhysicalTags = int(values.pop(0))
      physicalTags = []
      for i in range(numPhysicalTags):
        physicalTags.append(int(values.pop(0)))

      numBoundingPoints = int(values.pop(0))
      pointTags = []
      for i in range(numBoundingPoints):
        pointTags.append(int(values.pop(0)))

      self.curves.append(Curve(tag, minX, minY, minZ, maxX, maxY, maxZ, numPhysicalTags, physicalTags, numBoundingPoints, pointTags))

    # Create Surfaces
    for _ in range(self.numSurfaces):
      line = input.pop(0)
      values = line.split()

      tag = int(values.pop(0))
      minX = float(values.pop(0))
      minY = float(values.pop(0))
      minZ = float(values.pop(0))
      maxX = float(values.pop(0))
      maxY = float(values.pop(0))
      maxZ = float(values.pop(0))

      numPhysicalTags = int(values.pop(0))
      physicalTags = []
      for i in range(numPhysicalTags):
        physicalTags.append(int(values.pop(0)))

      numBoundingCurves = int(values.pop(0))
      curveTags = []
      for i in range(numBoundingCurves):
        curveTags.append(int(values.pop(0)))

      self.surfaces.append(Surface(tag, minX, minY, minZ, maxX, maxY, maxZ, numPhysicalTags, physicalTags, numBoundingCurves, curveTags))

    # Create Volumes
    for _ in range(self.numVolumes):
      line = input.pop(0)
      values = line.split()

      tag = int(values.pop(0))
      minX = float(values.pop(0))
      minY = float(values.pop(0))
      minZ = float(values.pop(0))
      maxX = float(values.pop(0))
      maxY = float(values.pop(0))
      maxZ = float(values.pop(0))

      numPhysicalTags = int(values.pop(0))
      physicalTags = []
      for i in range(numPhysicalTags):
        physicalTags.append(int(values.pop(0)))

      numBoundingSurfaces = int(values.pop(0))
      surfaceTags = []
      for i in range(numBoundingSurfaces):
        surfaceTags.append(int(values.pop(0)))

      self.volumes.append(Volume(tag, minX, minY, minZ, maxX, maxY, maxZ, numPhysicalTags, physicalTags, numBoundingCurves, curveTags))