from App.MeshReader.Elements import Element, ElementSurface
from Materials.MaterialBase import MaterialBase

class PhysicalVolume:
  physicalTag: int
  name: str

  elements: list[Element]
  entityTags: list[int]
  
  def __init__(self, physicalTag: int, name: str):
    self.physicalTag = physicalTag
    self.name = name[1:-1]

    self.elements = []
    self.entityTags = []
  
  def AddEntityTag(self, newEntityTag: int):
    self.entityTags.append(newEntityTag)

  def AddElement(self, newElement: Element):
    self.elements.append(newElement)

class PhysicalSurface:
  physicalTag: int
  name: str

  elementSurfaces: list[ElementSurface]
  entityTags: list[int]
  
  def __init__(self, physicalTag: int, name: str):
    self.physicalTag = physicalTag
    self.name = name[1:-1]

    self.elementSurfaces = []
    self.entityTags = []
  
  def AddEntityTag(self, newEntityTag: int):
    self.entityTags.append(newEntityTag)

  def AddElementSurface(self, newElementSurface: ElementSurface):
    self.elementSurfaces.append(newElementSurface)