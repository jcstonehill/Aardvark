// Gmsh project created on Fri Dec 09 22:03:44 2022
SetFactory("OpenCASCADE");
//+
Box(1) = {0, 0, 0, 1, 1, 1};
//+
Physical Surface("TopTestSurface", 13) = {4};
//+
Physical Volume("SolidVolTest", 14) = {1};
