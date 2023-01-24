from App.ProblemBuilder.Problem import Problem
from time import sleep

class ThermalSolver:

    def Solve(self, problem: Problem, convergenceCriteria: float):

        i = 0
        dt = 1
        
        error = convergenceCriteria + 1
        prevError = 1e24

        while(error > convergenceCriteria):

            for cell in problem.cells:
                cell.Q = cell.QGen

            for flowChannel in problem.flowChannels:
                flowChannel.ResetQ()

            for cellBoundary in problem.cellBoundaries:
                cellBoundary.thermalBC.Solve()

            for flowChannel in problem.flowChannels:
                flowChannel.Solve()

                fluidRegion = problem.GetRegion(flowChannel.regionName)

                for cell in fluidRegion.cells:
                    cell.T = flowChannel.GetTAtPosition(cell.centerPosition[2])

            error = 0
            for cell in problem.cells:
                cell.SolveForT(dt)
                error = error + cell.Error()

            i = i + 1
            print(str(i) + " | " + str(dt) + " | " + str(error))

            if(prevError < error):
                for cell in problem.cells:
                    cell.T = cell.previousT
                dt = 0.9*dt
            else:
                prevError = error
                
            


            

