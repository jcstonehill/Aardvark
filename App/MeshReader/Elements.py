from App.MeshReader.Nodes import Node, Nodes
from App.MCBC_Base import MCBC
from Materials.MaterialBase import MaterialBase
import itertools
from App.HelperMath import IntersectionOfLineAndPlane

class ElementSurface:
  nodes: list[Node]
  normal: list[float]
  neutronHandler: MCBC = None

  def __init__(self, nodes: list[Node]):
    self.nodes = nodes

    v1 = [self.nodes[1].x - self.nodes[0].x, self.nodes[1].y - self.nodes[0].y, self.nodes[1].z - self.nodes[0].z]
    v2 = [self.nodes[2].x - self.nodes[0].x, self.nodes[2].y - self.nodes[0].y, self.nodes[2].z - self.nodes[0].z]

    self.normal = []
    self.normal.append(v1[1]*v2[2] - v1[2]*v2[1])
    self.normal.append(v1[0]*v2[2] - v1[2]*v2[0])
    self.normal.append(v1[0]*v2[1] - v1[1]*v2[0])

  def IsSister(self, sisterNodes: list[Node]) -> bool:
    for sisterNode in sisterNodes:
      if sisterNode not in self.nodes:
        return False

    return True

  def Intersection(self, startPosition: list[float], endPosition: list[float]):
    nodePosition = [self.nodes[0].x, self.nodes[0].y, self.nodes[0].z]
    intersection = IntersectionOfLineAndPlane(startPosition, endPosition, nodePosition, self.normal)
    if(intersection is not None):
      if(intersection[0] == startPosition[0] and intersection[1] == startPosition[1] and intersection[2] == startPosition[2]):
        intersection = None

    

    return intersection

class Element:
  entityDim: int
  entityTag: int
  elementType: int
  numElementsInBlock: int
  elementTag: int
  nodes: list[Node]
  elementSurfaces: list[ElementSurface]
  material: MaterialBase
  centerPoint: list[float]
  fluxTally: int

  def __init__(self, entityDim: int, entityTag: int, elementType: int, numElementsInBlock: int, elementTag: int, nodes: list[int]):
    self.entityDim = entityDim
    self.entityTag = entityTag
    self.elementType = elementType
    self.numElementsInBlock = numElementsInBlock
    self.elementTag = elementTag
    self.nodes = nodes

    self.CalculateCenterPoint()

    self.CreateElementSurfaces()

  def CalculateCenterPoint(self):
    x = 0
    y = 0
    z = 0
    n = len(self.nodes)

    for node in self.nodes:
      x = x + node.x
      y = y + node.y
      z = z + node.z

    x = x / n
    y = y / n
    z = z / n

    self.centerPoint = [x, y, z]
    
  def CreateElementSurfaces(self):
    self.elementSurfaces = []

    if(self.entityDim == 3):
      nodeCombinations = itertools.combinations(self.nodes, 3)
      for nodeCombination in nodeCombinations:
        self.elementSurfaces.append(ElementSurface(nodeCombination))

  def TallyFlux(self):
    self.fluxTally = self.fluxTally + 1

  def ResetFluxTally(self):
    self.fluxTally = 0
    

class Elements():
  all: list[Element]

  def __init__(self, input: list[str], nodes: Nodes):
    self.all = []
    
    while len(input) > 0:
      line = input.pop(0)
      values = line.split()
      entityDim: int = int(values[0])
      entityTag: int = int(values[1])
      elementType: int = int(values[2])
      numElementsInBlock: int = int(values[3])

      for _ in range(numElementsInBlock):
        line = input.pop(0)
        values = line.split()

        elementTag = int(values.pop(0))
        
        nodesForElement: list[Node] = []
        for value in values:
          nodesForElement.append(nodes.Get(int(value)))

        self.all.append(Element(entityDim, entityTag, elementType, numElementsInBlock, elementTag, nodesForElement))

  def Get(self, elementTag) -> Element:
    for element in self.all:
      if(element.elementTag == elementTag):
        return element

  def GetAll(self) -> list[Element]:
    return self.all