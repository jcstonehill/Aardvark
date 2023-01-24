from App.MeshReader.PhysicalGroups import PhysicalSurface, PhysicalVolume
from App.MeshReader.Elements import Elements, Element

class Mesh:
  physicalSurfaces: list[PhysicalSurface]
  physicalVolumes: list[PhysicalVolume]
  physicalElements: list[Element]

  xMin: float
  yMin: float
  zMin: float

  xMax: float
  yMax: float
  zMax: float

  def ConnectElementsToPhysicalGroups(self, elements: Elements):
    self.physicalElements = []
    
    elements2D: list[Element] = []
    elements3D: list[Element] = []

    for element in elements.all:
      if(element.entityDim == 2):
        elements2D.append(element)
      elif(element.entityDim == 3):
        elements3D.append(element)

    for element3D in elements3D:
      for elementSurface in element3D.elementSurfaces:
        for element2D in elements2D:
          if(elementSurface.IsSister(element2D.nodes)):
            for physicalSurface in self.physicalSurfaces:
              if(element2D.entityTag in physicalSurface.entityTags):
                physicalSurface.AddElementSurface(elementSurface)

      for physicalVolume in self.physicalVolumes:
        if(element3D.entityTag in physicalVolume.entityTags):
          physicalVolume.AddElement(element3D)
          self.physicalElements.append(element3D)