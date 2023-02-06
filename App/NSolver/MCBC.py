from App.NSolver.Neutron import Neutron
from App.NSolver.MCBC_Base import MCBC
from App.ProblemBuilder.Cell import Cell

class TransportToNeighborMCBC(MCBC):

  cells: list[Cell]

  def __init__(self, cells: list[Cell]):
    self.cells = cells

  def Handle(self, neutron: Neutron, intersection: list[float]):

    neutron.position = intersection

    for cell in self.cells:
      if(cell is not neutron.currentCell):
        neutron.currentCell = cell

class VoidMCBC(MCBC):

  def Handle(self, neutron: Neutron, intersection: list[float]):
    neutron.position = intersection
    neutron.isAlive = False
