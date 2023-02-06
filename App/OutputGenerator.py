from App.ProblemBuilder.Problem import Problem

def OutputGenerator(problem: Problem, fileName: str):
  with open(fileName, 'w') as file:
    file.write("x, y, z, value\n")
    
    # for region in problem.regions:
    #   if(region.name=="solid"):
    #     for cell in region.cells:
    #       x = str(cell.centerPoint[0])
    #       y = str(cell.centerPoint[1])
    #       z = str(cell.centerPoint[2])

    #       flux = str(cell.T)

    #       file.write(x + ", " + y + ", " + z + ", " + flux + "\n")

    for cell in problem.cells:
      x = str(cell.centerPoint[0])
      y = str(cell.centerPoint[1])
      z = str(cell.centerPoint[2])

      flux = str(sum(cell.flux)/len(cell.flux))

      file.write(x + ", " + y + ", " + z + ", " + flux + "\n")