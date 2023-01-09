// Gmsh project created on Wed Dec 21 17:43:21 2022
SetFactory("OpenCASCADE");
//+
Sphere(1) = {0, 0, 0, 0.08, -Pi/2, Pi/2, 2*Pi};
//+
Physical Volume("vol", 4) = {1};
//+
Physical Surface("interface", 5) = {1};
