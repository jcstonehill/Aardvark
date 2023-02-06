from App.NSolver.FissionSite import FissionSite
from App.NSolver.Neutron import Neutron
from App.ProblemBuilder.CellBoundary import CellBoundary
from App.ProblemBuilder.Problem import Problem
from App.NSolver.NeutronSimulator import SimulateLifeOf
import random
from multiprocessing import Pool

class NSolver:

    def Solve(self, problem: Problem):

        fissionSites: list[FissionSite] = []

        for cell in problem.cells:
            fissionSites.append(FissionSite(cell.centerPoint, cell.id))

        kEff = []
        for i in range(problem.inactiveBatches):

            neutrons: list[Neutron] = []
            
            for _ in range(problem.numOfParticles):
                fissionSite = fissionSites[random.randint(0, len(fissionSites)-1)]
                newNeutron = Neutron()
                newNeutron.position = fissionSite.position
                newNeutron.DetermineNewFlightAngle()
                newNeutron.currentCell = problem.GetCell(fissionSite.cellID)
                newNeutron.energy = 2*(10**6)
                newNeutron.isAlive = True
                neutrons.append(newNeutron)

            with Pool(processes=problem.numOfProcesses) as pool:
                results = pool.map(SimulateLifeOf, neutrons)

            # results = []
            # for j in range(len(neutrons)):
            #     neutron = neutrons[j]
            #     results.append(SimulateLifeOf(neutron))
            #     print("inactive batch " + str(i) + " | " + str(problem.inactiveBatches) + "   -   " + str(j) + " | " + str(problem.numOfParticles))

            print("inactive batch " + str(i) + " | " + str(problem.inactiveBatches))

            newFissionSites: list[FissionSite] = []
            for result in results:
                fissionSite = result[1]

                if(fissionSite is not None):
                    newFissionSites.append(fissionSite)

            fissionSites = newFissionSites

            

            kEff.append(2.42*len(newFissionSites) / problem.numOfParticles)

        print(kEff)

        kEff = []
        for i in range(problem.activeBatches):

            neutrons: list[Neutron] = []
            
            for cell in problem.cells:
                cell.flux.append(0)

            for _ in range(problem.numOfParticles):
                fissionSite = fissionSites[random.randint(0, len(fissionSites)-1)]
                newNeutron = Neutron()
                newNeutron.position = fissionSite.position
                newNeutron.DetermineNewFlightAngle()
                newNeutron.currentCell = problem.GetCell(fissionSite.cellID)
                newNeutron.energy = 2*(10**6)
                newNeutron.isAlive = True
                neutrons.append(newNeutron)

            with Pool(processes=problem.numOfProcesses) as pool:
                results = pool.map(SimulateLifeOf, neutrons)
            
            

            # results = []
            # for j in range(len(neutrons)):
            #     neutron = neutrons[j]
            #     results.append(SimulateLifeOf(neutron))
            #     print("active batch " + str(i) + " | " + str(problem.inactiveBatches) + "   -   " + str(j) + " | " + str(problem.numOfParticles))
            print("active batch " + str(i) + " | " + str(problem.inactiveBatches))
            newFissionSites: list[FissionSite] = []
            for result in results:
                cellIDs = result[0]
                for cellID in cellIDs:
                    cell = problem.GetCell(cellID)
                    cell.flux[-1] = cell.flux[-1] + 1

                fissionSite = result[1]

                if(fissionSite is not None):
                    newFissionSites.append(fissionSite)

            fissionSites = newFissionSites

            

            kEff.append(2.42*len(newFissionSites) / problem.numOfParticles)

        print(kEff)