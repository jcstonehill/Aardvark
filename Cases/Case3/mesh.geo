// Gmsh project created on Sat Jan 21 12:14:32 2023
SetFactory("OpenCASCADE");
//+
Box(1) = {-0.5, -0.5, -0.5, 1, 1, 1};
//+
Cylinder(2) = {0, 0, -0.5, 0, 0, 1, 0.1, 2*Pi};
//+
BooleanDifference{ Volume{1}; Delete; }{ Volume{2}; }
//+
Physical Volume("solid", 28) = {1};
//+
Physical Volume("fluid", 29) = {2};
//+
Physical Surface("interface", 30) = {7};

//+
Physical Surface("hot", 31) = {10};
//+
Physical Surface("cold", 32) = {15};
