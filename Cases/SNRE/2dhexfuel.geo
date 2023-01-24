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
Line(6) = {5, 7};
//+
Circle(7) = {0, 0, 0, 0.0013, 0, 2*Pi};
//+
Circle(8) = {0.0041, 0, 0, 0.0013, 0, 2*Pi};
//+
Circle(9) = {0.0082, 0, 0, 0.0013, 0, 2*Pi};
//+
Circle(10) = {-0.0041, 0, 0, 0.0013, 0, 2*Pi};
//+
Circle(11) = {-0.0082, 0, 0, 0.0013, 0, 2*Pi};
//+
Circle(12) = {0.00205, 0.0035507, 0, 0.0013, 0, 2*Pi};
//+
Circle(13) = {-0.00205, 0.0035507, 0, 0.0013, 0, 2*Pi};
//+
Circle(14) = {0.00205, -0.0035507, 0, 0.0013, 0, 2*Pi};
//+
Circle(15) = {-0.00205, -0.0035507, 0, 0.0013, 0, 2*Pi};
//+
Circle(16) = {0.00615, 0.0035507, 0, 0.0013, 0, 2*Pi};
//+
Circle(17) = {-0.00615, 0.0035507, 0, 0.0013, 0, 2*Pi};
//+
Circle(18) = {0.00615, -0.0035507, 0, 0.0013, 0, 2*Pi};
//+
Circle(19) = {-0.00615, -0.0035507, 0, 0.0013, 0, 2*Pi};
//+
Circle(20) = {0, 0.0071014, 0, 0.0013, 0, 2*Pi};
//+
Circle(21) = {0.0041, 0.0071014, 0, 0.0013, 0, 2*Pi};
//+
Circle(22) = {-0.0041, 0.0071014, 0, 0.0013, 0, 2*Pi};
//+
Circle(23) = {0, -0.0071014, 0, 0.0013, 0, 2*Pi};
//+
Circle(24) = {0.0041, -0.0071014, 0, 0.0013, 0, 2*Pi};
//+
Circle(25) = {-0.0041, -0.0071014, 0, 0.0013, 0, 2*Pi};
//+
Curve Loop(1) = {1, 2, 3, 4, 5, 6};
//+
Curve Loop(2) = {22};
//+
Curve Loop(3) = {20};
//+
Curve Loop(4) = {21};
//+
Curve Loop(5) = {16};
//+
Curve Loop(6) = {12};
//+
Curve Loop(7) = {13};
//+
Curve Loop(8) = {17};
//+
Curve Loop(9) = {11};
//+
Curve Loop(10) = {10};
//+
Curve Loop(11) = {7};
//+
Curve Loop(12) = {8};
//+
Curve Loop(13) = {9};
//+
Curve Loop(14) = {18};
//+
Curve Loop(15) = {14};
//+
Curve Loop(16) = {15};
//+
Curve Loop(17) = {19};
//+
Curve Loop(18) = {25};
//+
Curve Loop(19) = {23};
//+
Curve Loop(20) = {24};
//+
Plane Surface(1) = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};

//+
Curve Loop(21) = {22};
//+
Plane Surface(2) = {21};
//+
Curve Loop(22) = {20};
//+
Plane Surface(3) = {22};
//+
Curve Loop(23) = {21};
//+
Plane Surface(4) = {23};
//+
Curve Loop(24) = {12};
//+
Curve Loop(25) = {17};
//+
Plane Surface(5) = {25};
//+
Curve Loop(26) = {13};
//+
Plane Surface(6) = {26};
//+
Curve Loop(27) = {12};
//+
Plane Surface(7) = {27};
//+
Curve Loop(28) = {16};
//+
Plane Surface(8) = {28};
//+
Curve Loop(29) = {11};
//+
Plane Surface(9) = {29};
//+
Curve Loop(30) = {10};
//+
Plane Surface(10) = {30};
//+
Curve Loop(31) = {7};
//+
Plane Surface(11) = {31};
//+
Curve Loop(32) = {8};
//+
Plane Surface(12) = {32};
//+
Curve Loop(33) = {9};
//+
Plane Surface(13) = {33};
//+
Curve Loop(34) = {18};
//+
Plane Surface(14) = {34};
//+
Curve Loop(35) = {14};
//+
Plane Surface(15) = {35};
//+
Curve Loop(36) = {15};
//+
Plane Surface(16) = {36};
//+
Curve Loop(37) = {19};
//+
Plane Surface(17) = {37};
//+
Curve Loop(38) = {25};
//+
Plane Surface(18) = {38};
//+
Curve Loop(39) = {23};
//+
Plane Surface(19) = {39};
//+
Curve Loop(40) = {24};
//+
Plane Surface(20) = {40};
//+
//Translate {1.65411, 0.955, 0} {
//  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
//}
//+
//Coherence;
