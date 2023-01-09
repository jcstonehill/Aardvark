from App.MeshReader.PhysicalGroups import PhysicalSurface, PhysicalVolume
from App.MeshReader.Nodes import Nodes
from App.MeshReader.Elements import Elements, Element
from App.MCBC_Base import MCBC
from App.MCBC import CoupledElementSurfaceBC
from Materials.MaterialBase import MaterialBase

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

  def GetPhysicalSurface(self, name: str) -> PhysicalSurface:
    for physicalSurface in self.physicalSurfaces:
      if(physicalSurface.name == name):
        return physicalSurface

  def GetPhysicalVolume(self, name: str) -> PhysicalVolume:
    for physicalGroup in self.physicalVolumes:
      if(physicalGroup.name == name):
        return physicalGroup

  def GetPhysicalElement(self, elementTag: int) -> Element:
    for physicalElement in self.physicalElements:
      if(physicalElement.elementTag == elementTag):
        return physicalElement

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

  def SetBC(self, physicalTag: int, bc: MCBC):
    physicalSurface = self.GetPhysicalSurface(physicalTag)

    for elementSurface in physicalSurface.elementSurfaces:
      elementSurface.neutronHandler = bc

  def SetMaterial(self, physicalTag: int, material: MaterialBase):
    physicalVolume = self.GetPhysicalVolume(physicalTag)

    for element in physicalVolume.elements:
      element.material = material
    
  def ConnectNeighbors(self):
    for firstElement in self.physicalElements:
      for secondElement in self.physicalElements:
        if firstElement != secondElement:
          for firstSurface in firstElement.elementSurfaces:
            for secondSurface in secondElement.elementSurfaces:
              if firstSurface.IsSister(secondSurface.nodes):
                firstSurface.neutronHandler = CoupledElementSurfaceBC(secondElement)
  
  def ResetFluxTallies(self):
    for element in self.physicalElements:
      element.ResetFluxTally()