from App.NSolver.Neutron import Neutron
from Materials.MaterialBase import Nuclide
from App.RNG import RandomFromRange
from math import sqrt, acos, cos
from App.NSolver.FissionSite import FissionSite
from App.ProblemBuilder.CellBoundary import CellBoundary

def DetermineNuclideHit(neutron: Neutron) -> Nuclide:
  divisions: list[float] = []
  nuclides = neutron.currentCell.material.nuclides

  for i in range(len(nuclides)):
    nuclideTotalXS = nuclides[i].xs.totalInterp(neutron.energy)
    materialTotalXS = neutron.currentCell.material.TotalMicroXS(neutron.energy, 0)
    divisionWeight = nuclides[i].atomicFraction * nuclideTotalXS / materialTotalXS
    
    if not divisions:
      divisions.append(divisionWeight)
    else:
      divisions.append(divisions[i-1] + divisionWeight)

  randomNumber = RandomFromRange(0,1)

  for i in range(len(nuclides)):
    if(randomNumber <= divisions[i]):
      return nuclides[i]

def HandleScattering(neutron: Neutron):

  nuclide: Nuclide = DetermineNuclideHit(neutron)

  oldDirection = neutron.direction

  neutron.DetermineNewFlightAngle()
  
  newDirection = neutron.direction
  
  dotProduct = 0

  for i in range(len(oldDirection)):
    dotProduct = dotProduct + abs(oldDirection[i]*newDirection[i])

  angle = acos(dotProduct)

  a = nuclide.molarMass / 1.00784

  oldE = neutron.energy
  
  C1 = oldE / ((a+1)**2)
  C2 = cos(angle)

  C3 = sqrt((cos(angle)**2)+(a**2)-1)

  neutron.energy = C1*((C2+C3)**2)

  if(neutron.energy < 1e-5):
    neutron.energy = 1e-5

def SimulateLifeOf(neutron: Neutron):
  newFissionSite = None
  fluxTallies = []

  while(neutron.isAlive):

    neutron.DetermineTravelDistance()

    destination = neutron.GetDestination()

    intersection: list[float] = None
    intersectedBoundary: CellBoundary = None

    for cellBoundary in neutron.currentCell.cellBoundaries:
      intersection = cellBoundary.Intersection(neutron.position, destination)

      if(intersection is not None):
        intersectedBoundary = cellBoundary
        break

    if(intersection is None):
      neutron.position = destination

      scatteringXS = neutron.currentCell.material.ScatteringXS(neutron.energy, 0)

      totalXS = neutron.currentCell.material.TotalXS(neutron.energy, 0)

      chanceOfScattering = scatteringXS / totalXS

      randomNumber = RandomFromRange(0,1)

      if(randomNumber < chanceOfScattering):
        HandleScattering(neutron)

      else:
        fissionXS = neutron.currentCell.material.FissionXS(neutron.energy, 0)
        absorptionXS = neutron.currentCell.material.AbsorptionXS(neutron.energy, 0)
        chanceOfFission = fissionXS / absorptionXS

        randomNumber = RandomFromRange(0,1)

        if(randomNumber < chanceOfFission):
          newFissionSite = FissionSite(neutron.position, neutron.currentCell.id)

        neutron.isAlive = False
    else:

      intersectedBoundary.mcbc.Handle(neutron, intersection)

    fluxTallies.append(neutron.currentCell.id)
  return fluxTallies, newFissionSite