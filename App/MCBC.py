from App.Neutron import Neutron
from App.MCBC_Base import MCBC
import time

class CoupledElementSurfaceBC(MCBC):

  def __init__(self, otherElement):
    self.otherElement = otherElement

  def Handle(self, neutron: Neutron, intersection: list[float]):
    neutron.position = intersection
    neutron.currentElement = self.otherElement

class VoidElementSurfaceBC(MCBC):

  def Handle(self, neutron: Neutron, intersection: list[float]):
    neutron.position = intersection
    neutron.isAlive = False
