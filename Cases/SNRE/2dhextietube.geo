// Gmsh project created on Sun Jan 08 22:42:45 2023
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0.0110274/2, 0.0191/2, 0, 1.0};
//+
Point(3) = {-0.0110274/2, 0.0191/2, 0, 1.0};
//+
Point(4) = {0.0110274/2, -0.0191/2, 0, 1.0};
//+
Point(5) = {-0.0110274/2, -0.0191/2, 0, 1.0};
//+
Point(6) = {0.0220548/2, 0, 0, 1.0};
//+
Point(7) = {-0.0220548/2, 0, 0, 1.0};
//+
Line(1) = {7, 3};
//+
Line(2) = {3, 2};
//+
Line(3) = {2, 6};
//+
Line(4) = {6, 4};
//+
Line(5) = {4, 5};
//+
Line(6) = {5, 7};//+
Circle(7) = {0, 0, 0, 0.00813, 0, 2*Pi};
//+
Circle(8) = {0, 0, 0, 0.0068825, 0, 2*Pi};
//+
Circle(9) = {0, 0, 0, 0.00584, 0, 2*Pi};
//+
Circle(10) = {0, 0, 0, 0.002095, 0, 2*Pi};
//+
Curve Loop(1) = {2, 3, 4, 5, 6, 1};
//+
Curve Loop(2) = {7};
//+
Plane Surface(1) = {1, 2};
//+
Curve Loop(3) = {7};
//+
Curve Loop(4) = {8};
//+
Plane Surface(2) = {3, 4};
//+
Curve Loop(5) = {8};
//+
Curve Loop(6) = {9};
//+
Plane Surface(3) = {5, 6};
//+
Curve Loop(7) = {9};
//+
Curve Loop(8) = {10};
//+
Plane Surface(4) = {7, 8};
//+
Curve Loop(9) = {10};
//+
Plane Surface(5) = {9};
