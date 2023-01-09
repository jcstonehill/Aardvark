from Neutron import Neutron
from Materials.MaterialBase import Nuclide
from RNG import RandomFromRange
from math import sqrt, acos, sin, cos, pi
from MeshReader.Elements import ElementSurface
from FissionSite import FissionSite

def DetermineNuclideHit(neutron: Neutron) -> Nuclide:
  divisions: list[float] = []
  nuclides = neutron.currentElement.material.nuclides

  for i in range(len(nuclides)):
    nuclideTotalXS = nuclides[i].xs.totalInterp(neutron.energy)
    materialTotalXS = neutron.currentElement.material.TotalMicroXS(neutron.energy, 0)
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
  # x = [neutron.position[0]]
  # y = [neutron.position[1]]
  # z = [neutron.position[2]]

  newFissionSite = None
  fluxTallies = []
  # print("New Neutron")
  while(neutron.isAlive):

    neutron.DetermineTravelDistance()

    destination = neutron.GetDestination()

    intersection: list[float] = None
    intersectedSurface: ElementSurface = None

    for elementSurface in neutron.currentElement.elementSurfaces:
      intersection = elementSurface.Intersection(neutron.position, destination)

      if(intersection is not None):
        intersectedSurface = elementSurface
        break

    if(intersection is None):
      neutron.position = destination

      scatteringXS = neutron.currentElement.material.ScatteringXS(neutron.energy, 0)

      totalXS = neutron.currentElement.material.TotalXS(neutron.energy, 0)

      chanceOfScattering = scatteringXS / totalXS

      randomNumber = RandomFromRange(0,1)

      if(randomNumber < chanceOfScattering):
        HandleScattering(neutron)

      else:
        fissionXS = neutron.currentElement.material.FissionXS(neutron.energy, 0)
        absorptionXS = neutron.currentElement.material.AbsorptionXS(neutron.energy, 0)
        chanceOfFission = fissionXS / absorptionXS

        randomNumber = RandomFromRange(0,1)

        if(randomNumber < chanceOfFission):
          newFissionSite = FissionSite(neutron.position, neutron.currentElement.elementTag)

        neutron.isAlive = False
    else:

      intersectedSurface.neutronHandler.Handle(neutron, intersection)

    fluxTallies.append(neutron.currentElement.elementTag)
  return fluxTallies, newFissionSite