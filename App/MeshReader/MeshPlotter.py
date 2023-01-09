from App.MeshReader.Mesh import Mesh
import pyqtgraph.opengl as gl
import numpy as np

def PlotPhysicalElements(mesh: Mesh, plotWidget: gl.GLViewWidget):

  i = 0

  vertexes = []
  faces = []

  for element in mesh.physicalElements:
    for elementSurface in element.elementSurfaces:
      faces.append([i, i+1, i+2])

      for node in elementSurface.nodes:
        vertexes.append([node.x, node.y, node.z])
        
        i = i+1

  faces = np.array(faces)
  vertexes = np.array(vertexes)
        
  meshData = gl.MeshData(vertexes=vertexes, faces=faces)

  plotItem = gl.GLMeshItem(meshdata=meshData, computeNormals=False, drawEdges=True)
  plotItem.meshDataChanged()
  plotWidget.addItem(plotItem)


  # meshData = gl.MeshData(vertexes = np.array([x, y, z]), faces = np.array([faceIndex1, faceIndex2, faceIndex3]))
  # plotItem = gl.GLMeshItem(meshData = meshData)

  # plotWidget.addItem(plotItem)

  # for element in mesh.physicalElements:
  #   x = []
  #   y = []
  #   z = []

  #   for node in element.nodes:
  #     x.append(node.x)
  #     y.append(node.y)
  #     z.append(node.z)

  #   while(len(x) > 1):
  #     currentX = x.pop(0)
  #     currentY = y.pop(0)
  #     currentZ = z.pop(0)

  #     for i in range(len(x)):
  #       pointArray = np.array([(currentX, currentY, currentZ), (x[i], y[i], z[i])])
  #       plotItem = gl.GLLinePlotItem(pos=pointArray)
  #       plotWidget.addItem(plotItem)