from App.MeshReader.MeshReader import ReadMesh
from App.ProblemBuilder.Builder import CreateProblemFrom
from App.THSolver.ThermalSolver import ThermalSolver
from App.THSolver.FlowChannel import FlowChannel
from Materials.TH_TEST1 import TH_TEST1
from Materials.Fluids.FluidHydrogen import FluidHydrogen
from App.OutputGenerator import OutputGenerator

if __name__ == "__main__":
    # mesh = ReadMesh("Cases/Case1/mesh.msh")
    # problem = CreateProblemFrom(mesh)

    # problem.SetMaterial("vol1", TH_TEST1())
    # problem.SetMaterial("vol2", TH_TEST1())

    # problem.SetConstantTempThermalBC("front", 500)
    # problem.SetConstantTempThermalBC("back", 300)

    # thermalSolver = ThermalSolver()

    # thermalSolver.Solve(problem, 1)

    # OutputGenerator(problem, "ProblemBuilderTest.csv")

    mesh = ReadMesh("Cases/Case3/mesh.msh")
    print("mesh read")
    problem = CreateProblemFrom(mesh)
    print("problem created")

    problem.SetMaterial("solid", TH_TEST1())
    problem.SetMaterial("fluid", TH_TEST1())
    print("materials assigned")

    problem.SetConstantTempThermalBC("hot", 1000)
    problem.SetConstantTempThermalBC("cold", 1000)
    print("thermal bc's created")

    flowChannel = FlowChannel(-0.5, 0.5, 20, FluidHydrogen(), 0.628318, 0.0314159)
    flowChannel.SetInletConditions(300, 300000, 0.001)

    problem.InsertFlowChannel("fluid", "interface", flowChannel)
    print("flow channel created")

    thermalSolver = ThermalSolver()

    thermalSolver.Solve(problem, 1)

    for cell in problem.flowChannels[0].flowCells:
        print(cell.T)
    OutputGenerator(problem, "FlowChannelTest.csv")
