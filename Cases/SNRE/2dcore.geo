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
Point(91) = {0, 0, 0, 1.0};
//+
Point(92) = {0.0110274/2, 0.0191/2, 0, 1.0};
//+
Point(93) = {-0.0110274/2, 0.0191/2, 0, 1.0};
//+
Point(94) = {0.0110274/2, -0.0191/2, 0, 1.0};
//+
Point(95) = {-0.0110274/2, -0.0191/2, 0, 1.0};
//+
Point(96) = {0.0220548/2, 0, 0, 1.0};
//+
Point(97) = {-0.0220548/2, 0, 0, 1.0};
//+
Line(91) = {97, 93};
//+
Line(92) = {93, 92};
//+
Line(93) = {92, 96};
//+
Line(94) = {96, 94};
//+
Line(95) = {94, 95};
//+
Line(96) = {95, 97};//+
Circle(97) = {0, 0, 0, 0.00813, 0, 2*Pi};
//+
Circle(98) = {0, 0, 0, 0.0068825, 0, 2*Pi};
//+
Circle(99) = {0, 0, 0, 0.00584, 0, 2*Pi};
//+
Circle(910) = {0, 0, 0, 0.002095, 0, 2*Pi};
//+
Curve Loop(91) = {92, 93, 94, 95, 96, 91};
//+
Curve Loop(92) = {97};
//+
Plane Surface(91) = {91, 92};
//+
Curve Loop(93) = {97};
//+
Curve Loop(94) = {98};
//+
Plane Surface(92) = {93, 94};
//+
Curve Loop(95) = {98};
//+
Curve Loop(96) = {99};
//+
Plane Surface(93) = {95, 96};
//+
Curve Loop(97) = {99};
//+
Curve Loop(98) = {910};
//+
Plane Surface(94) = {97, 98};
//+
Curve Loop(99) = {910};
//+
Plane Surface(95) = {99};










Translate {0.03308217042456556, 0.0191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.049623255636848336, 0.00955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.06616434084913111, 0.0191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.0827054260614139, 0.00955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.09924651127369667, 0.0191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.11578759648597944, 0.00955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.13232868169826223, 0.0191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.14886976691054501, 0.00955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1654108521228278, 0.0191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1819519373351106, 0.00955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.19849302254739334, 0.0191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.21503410775967613, 0.00955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.01654108521228278, 0.04775, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.03308217042456556, 0.0382, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.049623255636848336, 0.04775, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.06616434084913111, 0.0382, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.0827054260614139, 0.04775, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.09924651127369669, 0.0382, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.11578759648597944, 0.04775, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.13232868169826223, 0.0382, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.14886976691054501, 0.04775, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1654108521228278, 0.0382, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1819519373351106, 0.04775, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.19849302254739337, 0.0382, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.21503410775967613, 0.04775, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.23157519297195892, 0.0382, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0, 0.0764, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.01654108521228278, 0.06684999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.03308217042456556, 0.0764, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.049623255636848336, 0.06684999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.06616434084913111, 0.0764, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.0827054260614139, 0.06684999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.09924651127369667, 0.0764, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.11578759648597944, 0.06684999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.13232868169826223, 0.0764, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.14886976691054501, 0.06684999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1654108521228278, 0.0764, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1819519373351106, 0.06684999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.19849302254739334, 0.0764, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.21503410775967613, 0.06684999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.01654108521228278, 0.10505, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.03308217042456556, 0.0955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.049623255636848336, 0.10505, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.06616434084913111, 0.0955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.0827054260614139, 0.10505, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.09924651127369669, 0.0955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.11578759648597944, 0.10505, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.13232868169826223, 0.0955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.14886976691054501, 0.10505, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1654108521228278, 0.0955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1819519373351106, 0.10505, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.19849302254739337, 0.0955, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0, 0.13369999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.01654108521228278, 0.12415, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.03308217042456556, 0.13369999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.049623255636848336, 0.12415, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.06616434084913111, 0.13369999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.0827054260614139, 0.12415, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.09924651127369667, 0.13369999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.11578759648597944, 0.12415, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.13232868169826223, 0.13369999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.14886976691054501, 0.12415, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1654108521228278, 0.13369999999999999, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1819519373351106, 0.12415, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.01654108521228278, 0.16235, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.03308217042456556, 0.1528, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.049623255636848336, 0.16235, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.06616434084913111, 0.1528, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.0827054260614139, 0.16235, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.09924651127369669, 0.1528, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.11578759648597944, 0.16235, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.13232868169826223, 0.1528, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.14886976691054501, 0.16235, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.1654108521228278, 0.1528, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0, 0.191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.01654108521228278, 0.18145, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.03308217042456556, 0.191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.049623255636848336, 0.18145, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.06616434084913111, 0.191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.0827054260614139, 0.18145, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.09924651127369667, 0.191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.11578759648597944, 0.18145, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.13232868169826223, 0.191, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.14886976691054501, 0.18145, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.01654108521228278, 0.21964999999999998, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.03308217042456556, 0.21009999999999998, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.049623255636848336, 0.21964999999999998, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.06616434084913111, 0.21009999999999998, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.0827054260614139, 0.21964999999999998, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.09924651127369669, 0.21009999999999998, 0} {
  Duplicata { Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
}

Translate {0.03308217042456556, 0, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.06616434084913111, 0, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.09924651127369667, 0, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.13232868169826223, 0, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.1654108521228278, 0, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.19849302254739334, 0, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.01654108521228278, 0.02865, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.049623255636848336, 0.02865, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.0827054260614139, 0.02865, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.11578759648597944, 0.02865, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.14886976691054501, 0.02865, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.1819519373351106, 0.02865, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.21503410775967613, 0.02865, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0, 0.0573, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.0, 0.0573, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.03308217042456556, 0.0573, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.06616434084913111, 0.0573, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.09924651127369667, 0.0573, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.13232868169826223, 0.0573, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.1654108521228278, 0.0573, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.19849302254739334, 0.0573, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.01654108521228278, 0.08595, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.049623255636848336, 0.08595, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.0827054260614139, 0.08595, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.11578759648597944, 0.08595, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.14886976691054501, 0.08595, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.1819519373351106, 0.08595, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0, 0.1146, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.0, 0.1146, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.03308217042456556, 0.1146, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.06616434084913111, 0.1146, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.09924651127369667, 0.1146, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.13232868169826223, 0.1146, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.1654108521228278, 0.1146, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.01654108521228278, 0.14325, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.049623255636848336, 0.14325, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.0827054260614139, 0.14325, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.11578759648597944, 0.14325, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.14886976691054501, 0.14325, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0, 0.1719, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.0, 0.1719, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.03308217042456556, 0.1719, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.06616434084913111, 0.1719, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.09924651127369667, 0.1719, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.13232868169826223, 0.1719, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.01654108521228278, 0.20054999999999998, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.049623255636848336, 0.20054999999999998, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Translate {0.0827054260614139, 0.20054999999999998, 0} {
  Duplicata { Surface{91}; Surface{92}; Surface{93}; Surface{94}; Surface{95}; }
}

Coherence;

Delete{  Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{17}; Surface{16}; Surface{15}; Surface{14}; Surface{18}; Surface{19}; Surface{20}; }
