# from MeshReader.Mesh import Mesh
# from MeshReader.MeshReader import ReadMesh
# from statistics import mean
# from MCBC import VoidElementSurfaceBC
# from Materials.HEU import HEU
# from Materials.Hydrogen import Hydrogen
# from Simulator import Simulate
# from OutputGenerator import OutputGenerator
# from App.Logger import Log
# import time
#import sys
#import os
from App.App import App

if __name__ == "__main__":
  # sys.setrecursionlimit(25000)
  # starttime = time.time()
  # Log.Create(debugMode=False)
  # Log.Info("App has started.")
  # Log.Info("Reading mesh file.")
  # print("Reading mesh file.")
  # mesh = ReadMesh(os.getcwd() +"\\SampleMeshes\\box_new.msh")
  # Log.Info("Mesh created.")
  # print("Mesh created.")
  # Log.Info("Creating material objects.")
  # mesh.SetMaterial(23, HEU())
  # mesh.SetMaterial(24, Hydrogen())
  # Log.Info("Material objects created.")

  # mesh.SetBC(25, VoidElementSurfaceBC())
  # mesh.SetBC(26, VoidElementSurfaceBC())
  # mesh.SetBC(27, VoidElementSurfaceBC())
  # mesh.SetBC(28, VoidElementSurfaceBC())
  # mesh.SetBC(29, VoidElementSurfaceBC())
  # mesh.SetBC(30, VoidElementSurfaceBC())

  # print("Materials Created.")
  # print("Starting Simulation.")
  # Log.Info("Starting simulation.")
  # mesh = Simulate(mesh, 100000, 20, numOfProcesses=1)
  # print("Simulation Complete. Saving Output.")
  # OutputGenerator(mesh, "output.csv")
  # print("Output saved.")
  # print('That took {} seconds'.format(time.time() - starttime))

  app = App()

    
    