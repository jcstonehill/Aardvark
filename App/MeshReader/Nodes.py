from dataclasses import dataclass

@dataclass
class Node:
  entityDim: int
  entityTag: int
  parametric: int
  numNodesInBlock: int
  nodeTag: int

  x: float
  y: float
  z: float

class Nodes():

  all: list[Node]

  def __init__(self, input: list[str]):
    self.all = []
    while len(input) > 0:
      line = input.pop(0)
      values = line.split()
      entityDim: int = int(values[0])
      entityTag: int = int(values[1])
      parametric: int = int(values[2])
      numNodesInBlock: int = int(values[3])

      nodeTags: list[int] = []
      nodeXs: list[float] = []
      nodeYs: list[float] = []
      nodeZs: list[float] = []

      for _ in range(numNodesInBlock):
        line = input.pop(0)
        value = line.split()
        nodeTags.append(int(value[0]))

      for _ in range(numNodesInBlock):
        line = input.pop(0)
        values = line.split()

        nodeXs.append(float(values[0]))
        nodeYs.append(float(values[1]))
        nodeZs.append(float(values[2]))
      
      for i in range(numNodesInBlock):
        self.all.append(Node(entityDim, entityTag, parametric, numNodesInBlock, nodeTags[i], nodeXs[i], nodeYs[i], nodeZs[i]))

  def Get(self, nodeTag) -> Node:
    for node in self.all:
      if(node.nodeTag == nodeTag):
        return node

  def GetAll(self) -> list[Node]:
    return self.all