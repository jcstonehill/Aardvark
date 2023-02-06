from App.RNG import RandomFromRange
from math import sqrt, acos, sin, cos, pi
from App.ProblemBuilder.Cell import Cell
import numpy as np

class Neutron:
  position: list[float]
  direction: list[float]
  travelDistance: float
  energy: float
  isAlive: bool
  currentCell: Cell
  debug = True
  id: int

  def DetermineTravelDistance(self):
    totalCrossSection = self.currentCell.material.TotalXS(self.energy, 0)
    if(totalCrossSection == 0):
      self.travelDistance = 10**12
    else:
      self.travelDistance = -(1/totalCrossSection)*np.log(RandomFromRange(0, 1))

  def DetermineNewFlightAngle(self):
    mu = RandomFromRange(-1, 1)
    omega = RandomFromRange(0, 2*pi)

    x = mu
    y = sqrt(1-(mu**2)) * cos(omega)
    z = sqrt(1-(mu**2)) * sin(omega)
    
    newDirection = [x, y, z]
    magnitude = sqrt((x**2)+(y**2)+(z**2))
    for i in range(len(newDirection)):
      newDirection[i] = newDirection[i] / magnitude

    self.direction = newDirection

  def GetDestination(self) -> list[float]:
    destination = []
    for i in range(len(self.direction)):
      destination.append(self.position[i] + (self.direction[i]*self.travelDistance))

    return destination

  
