from MeshReader.MeshReader import Mesh
from FissionSite import FissionSite
from Neutron import Neutron
import random
from multiprocessing import Pool
from NeutronSimulator import SimulateLifeOf



def Simulate(mesh: Mesh, numOfParticlesToSimulate: int, numOfInactiveBatches: int, numOfProcesses: int = 1, fissionSites: list[FissionSite] = []):
  

  if not fissionSites:
    for physicalElement in mesh.physicalVolumes[0].elements:
      fissionSites.append(FissionSite(physicalElement.centerPoint, physicalElement.elementTag))

  kEff: list[float] = []
  
  for i in range(numOfInactiveBatches):

    newFissionSites: list[FissionSite] = []
    mesh.ResetFluxTallies()

    neutrons: list[Neutron] = []
    for _ in range(numOfParticlesToSimulate):
      fissionSiteIndex = random.randint(0, len(fissionSites) - 1)
      fissionSite = fissionSites[fissionSiteIndex]
      newNeutron = Neutron()
      newNeutron.position = fissionSite.position
      newNeutron.DetermineNewFlightAngle()
      newNeutron.currentElement = mesh.GetPhysicalElement(fissionSite.physicalElementTag)
      newNeutron.energy = 2*(10**6)
      newNeutron.isAlive = True
      neutrons.append(newNeutron)

    print("batch " + str(i) + " / " + str(numOfInactiveBatches))

    with Pool(processes=numOfProcesses) as pool:
      results = pool.map(SimulateLifeOf, neutrons)

    for result in results:
      tallies = result[0]

      for tally in tallies:
        mesh.GetPhysicalElement(tally).TallyFlux()

      fissionSite = result[1]

      if(fissionSite is not None):
        newFissionSites.append(fissionSite)
      
    # 
    # while(particlesSimulated < particlesToSimulate):
    #   fissionSiteIndex = random.randint(0, len(fissionSites) - 1)
    #   fissionSite = fissionSites[fissionSiteIndex]

    #   neutron.position = fissionSite.position
    #   neutron.DetermineNewFlightAngle()
    #   neutron.currentElement = mesh.elements.Get(fissionSite.physicalElementTag)
    #   neutron.energy = 2*(10**6)
    #   neutron.isAlive = True

    #   Log.Debug("New neutron is born at position (" + str(neutron.position[0]) + ", " + str(neutron.position[1]) + ", " + str(neutron.position[2]) + ") with E = " + str(neutron.energy) + " and direction = (" + str(neutron.direction[0]) + ", " + str(neutron.direction[1]) + ", " + str(neutron.direction[2]) + ")")
    #   newFissionSite = SimulateLifeOf(neutron, mesh)

    #   if(newFissionSite is not None):
    #     newFissionSites.append(newFissionSite)

    #   particlesSimulated = particlesSimulated + 1
    #   print(str(i) + " / " + str(numOfInactiveBatches) +  "   :   " + str(particlesSimulated) + " / " + str(particlesToSimulate))
    #   Log.Debug("Batch: " + str(i) + " / " + str(numOfInactiveBatches) +  "   -   Particle: " + str(particlesSimulated) + " / " + str(particlesToSimulate))

    kEff.append(2.42*len(newFissionSites) / numOfParticlesToSimulate)
    
    fissionSites = newFissionSites

  print(kEff)

  return mesh




  
