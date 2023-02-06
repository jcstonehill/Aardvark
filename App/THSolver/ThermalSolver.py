from App.ProblemBuilder.Problem import Problem
class ThermalSolver:

    def Solve(self, problem: Problem, convergenceCriteria: float):

        i = 0
        dt = 10
        
        error = convergenceCriteria + 1

        prevError = 1e24

        while(error > convergenceCriteria):
            
            for cell in problem.cells:
                cell.Q = cell.QGen

            for flowChannel in problem.flowChannels:
                flowChannel.ResetQ()

            for cellBoundary in problem.cellBoundaries.values():
                cellBoundary.thermalBC.Solve()
                

                # if((type(cellBoundary.thermalBC)) == ConvectionToFlowChannelThermalBC):
                #     print(cellBoundary.thermalBC.Q)
                #     print("hit")
                #     breakpoint()

            maxQ = 0
            error = 0
            for cell in problem.cells:
                error = error + abs(cell.Q)
                if(abs(cell.Q) > maxQ):
                    maxQ = abs(cell.Q)

            for cell in problem.cells:
                #cell.SolveForT(dt)

                cell.T = cell.T + dt*((cell.Q/maxQ))

                # if(cell.Q > 0):
                #     cell.T = cell.T + dt*((cell.Q/maxQ))
                # else:
                #     cell.T = cell.T - dt*((cell.Q/maxQ))

            for flowChannel in problem.flowChannels:
                flowChannel.Solve()

                fluidRegion = problem.GetRegion(flowChannel.regionName)

                for cell in fluidRegion.cells:
                    cell.T = flowChannel.GetTAtPosition(cell.centerPoint[2])

            if(abs(error-prevError) < 0.000001 or prevError < error):
                dt = dt*0.95
                prevError = 1e24
            else:

                prevError = error

            # if(prevError < error):

            #     for cell in problem.cells:
            #         cell.T = cell.previousT

            #     dt = dt*0.9
            # else:
            #     prevError = error
            
            i = i + 1
            print(str(i) + " | " + str(dt) + " | " + str(error))

            


            

