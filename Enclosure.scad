StandardThickness = 2.5;
Bottom = [(85.10+2.52+2*StandardThickness+2), (56.10+2*StandardThickness+2), StandardThickness];
cube(Bottom);

BottomWall1 = [(85.10+2.52+2*StandardThickness+2),StandardThickness,(6.5+StandardThickness)];
cube(BottomWall1);

RearWall = [(85.10+2.52+2*StandardThickness+2),StandardThickness,(6.5+StandardThickness+1.6+1.7*2+18.84*2)];

RearWalldisplacement = [0,(56.10+StandardThickness+2),0];
RearWallHole = 
translate(RearWalldisplacement)
cube(RearWall);

BottomWall3 = [StandardThickness,(56.10+2*StandardThickness+2),(6.5+StandardThickness)];
cube(BottomWall3);

BottomWall4displacement = [(85.10+2.52+StandardThickness+2),0,0];
translate(BottomWall4displacement)
cube(BottomWall3);
