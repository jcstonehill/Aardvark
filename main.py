
from App.ProblemBuilder.Builder import CreateProblem
from App.THSolver.ThermalSolver import ThermalSolver
from App.THSolver.FlowChannel import FlowChannel
from Materials.TH_TEST1 import TH_TEST1
from Materials.Fluids.FluidHydrogen import FluidHydrogen
from Materials.Hydrogen import Hydrogen
from Materials.HEU import HEU
from App.NSolver.NSolver import NSolver
from App.OutputGenerator import OutputGenerator
import sys
import time

if __name__ == "__main__":

  sys.setrecursionlimit(25000)

  problem = CreateProblem("\Cases\Case3\mesh.msh")
  problem.numOfProcesses = 12

  problem.SetMaterial("fluid", HEU())
  problem.SetMaterial("solid", Hydrogen())

  problem.inactiveBatches = 25
  problem.activeBatches = 10
  problem.numOfParticles = 1000

  nSolver = NSolver()
  start_time = time.time()
  nSolver.Solve(problem)
  print("--- %s seconds ---" % (time.time() - start_time))
  OutputGenerator(problem, "fluxOutput.csv")

  # for cell in problem.GetRegion("solid").cells:
  #     cell.QGen = 1e4 * cell.volume

  # for cell in problem.cells:
  #     cell.T = 850

  # problem.SetMaterial("solid", TH_TEST1())
  # problem.SetMaterial("fluid", TH_TEST1())
  # print("materials assigned")

  # problem.SetConstantTempThermalBC("hot", 1000)
  # problem.SetConstantTempThermalBC("cold", 1000)
  # print("thermal bc's created")

  # flowChannel = FlowChannel(-0.5, 0.5, 20, FluidHydrogen(), 0.628318, 0.0314159)
  # flowChannel.SetInletConditions(300, 300000, 0.01)

  # problem.InsertFlowChannel("fluid", "interface", flowChannel)
  # print("flow channel created")

  # thermalSolver = ThermalSolver()

  # thermalSolver.Solve(problem, 10)

  # # for cell in problem.flowChannels[0].flowCells:
  # #     print(cell.T)
  # OutputGenerator(problem, "NewBuilderTest.csv")

      
      