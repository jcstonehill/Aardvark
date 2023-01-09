// Gmsh project created on Fri Dec 16 18:52:11 2022
SetFactory("OpenCASCADE");
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0.1, 0, 0, 1.0};
//+
Point(3) = {0, 0.1, 0, 1.0};
//+
Point(4) = {0, 0, 0.1, 1.0};
//+
Point(5) = {0.1, 0.1, 0, 1.0};
//+
Point(6) = {0.1, 0, 0.1, 1.0};
//+
Point(7) = {0, 0.1, 0.1, 1.0};
//+
Point(8) = {0.1, 0.1, 0.1, 1.0};
//+
Point(9) = {0.05, 0, 0, 1.0};
//+
Point(10) = {0.05, 0.1, 0, 1.0};
//+
Point(11) = {0.05, 0.1, 0.1, 1.0};
//+
Point(12) = {0.05, 0, 0.1, 1.0};
//+
Line(1) = {3, 7};
//+
Line(2) = {7, 11};
//+
Line(3) = {11, 10};
//+
Line(4) = {10, 3};
//+
Line(5) = {3, 1};
//+
Line(6) = {1, 4};
//+
Line(7) = {4, 12};
//+
Line(8) = {12, 11};
//+
Line(9) = {9, 12};
//+
Line(10) = {9, 1};
//+
Line(11) = {9, 10};
//+
Line(12) = {4, 7};
//+
Line(13) = {11, 8};
//+
Line(14) = {5, 8};
//+
Line(15) = {8, 6};
//+
Line(16) = {12, 6};
//+
Line(17) = {6, 2};
//+
Line(18) = {2, 5};
//+
Line(19) = {5, 10};
//+
Line(20) = {9, 2};
//+
Curve Loop(1) = {1, 2, 3, 4};
//+
Surface(1) = {1};
//+
Curve Loop(3) = {5, -10, 11, 4};
//+
Surface(2) = {3};
//+
Curve Loop(5) = {6, 7, -9, 10};
//+
Surface(3) = {5};
//+
Curve Loop(7) = {12, 2, -8, -7};
//+
Surface(4) = {7};
//+
Curve Loop(9) = {9, 8, 3, -11};
//+
Surface(5) = {9};
//+
Curve Loop(11) = {16, -15, -13, -8};
//+
Surface(6) = {11};
//+
Curve Loop(13) = {17, 18, 14, 15};
//+
Surface(7) = {13};
//+
Curve Loop(15) = {20, 18, 19, -11};
//+
Surface(8) = {15};
//+
Curve Loop(17) = {3, -19, 14, -13};
//+
Surface(9) = {17};
//+
Curve Loop(19) = {5, 6, 12, -1};
//+
Surface(10) = {19};
//+
Surface Loop(1) = {10, 1, 4, 3, 5, 2};
//+
Volume(1) = {1};
//+
Curve Loop(21) = {9, 16, 17, -20};
//+
Surface(11) = {21};
//+
Surface Loop(2) = {6, 9, 7, 11, 8, 5};
//+
Volume(2) = {2};
//+
Physical Volume("vol1", 23) = {1};
//+
Physical Volume("vol2", 24) = {2};
//+
Physical Surface("front", 25) = {10};
//+
Physical Surface("top", 26) = {1, 9};
//+
Physical Surface("back", 27) = {7};
//+
Physical Surface("right", 28) = {4, 6};
//+
Physical Surface("left", 29) = {2, 8};
//+
Physical Surface("bottom", 30) = {11, 3};
