from App.ProblemBuilder.Problem import Problem
import csv
def OutputGenerator(problem: Problem, fileName: str):
  with open(fileName, 'w') as file:
    file.write("x, y, z, value\n")
    
    for cell in problem.cells:
      x = str(cell.centerPosition[0])
      y = str(cell.centerPosition[1])
      z = str(cell.centerPosition[2])

      flux = str(cell.T)

      file.write(x + ", " + y + ", " + z + ", " + flux + "\n")