// Gmsh project created on Wed Dec 14 00:55:47 2022
SetFactory("OpenCASCADE");
//+
Sphere(1) = {0, 0, 0, 0.5, -Pi/2, Pi/2, 2*Pi};
//+
Physical Volume("physicalSphere", 4) = {1};
