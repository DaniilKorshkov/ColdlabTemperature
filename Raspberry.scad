module RaspberryWithHats()

{
Raspberry = [85.10, 56.10, 1.6];
cube( Raspberry);


ThermalHat = [93.24,56.34,1.7];
ThermalHatDisplacement = [-8.24,0,20.44];  
translate(ThermalHatDisplacement)
cube( ThermalHat);


MegaindHat = [98.00,64.78,1.7];
MegaindHatDisplacement = [-11.08,-8.44,40.98];
MegaindHatDisplacement2 = [-11.08,-8.44,61.52];

translate(MegaindHatDisplacement)
cube( MegaindHat);

translate(MegaindHatDisplacement2)
cube( MegaindHat);





TypeC = [9.01,10,3.32];
TypeCDisplacement = [6.68,-1.5,1.6];

translate(TypeCDisplacement)
cube( TypeC);

MicroHDMI = [6.64,10,3.54];
MicroHDMIDisplacement = [22.34,-1.26,1.6];
MicroHDMIDisplacement2 = [35.30,-1.26,1.6];

translate(MicroHDMIDisplacement)
cube( MicroHDMI);

translate(MicroHDMIDisplacement2)
cube( MicroHDMI);

Jack = [7.06,10,6.04];
JackDisplacement = [50.58,-2.5,1.6];

translate(JackDisplacement)
cube( Jack);

TypeA = [17.66,52,15.26];
TypeADisplacement = [70.88,1.6,1.26];

translate(TypeADisplacement)
cube( TypeA);

sdcard = [20,11.1,1];
sdcardDisplacement = [-2.52,22.56,-1.36];

translate(sdcardDisplacement)
cube( sdcard);




GPIOheight = 7.1;
GPIOdepth = 9.24;
GPIO2333y = [GPIOdepth,56.08,GPIOheight];
GPIO3x = [11.9,GPIOdepth,GPIOheight];

ThermalGPIOdisplacement1 = [-10.46,0.5,22.14];
translate(ThermalGPIOdisplacement1)
cube( GPIO2333y);

ThermalGPIOdisplacement2 = [65.08,-2.36,22.14];
translate(ThermalGPIOdisplacement2)
cube( GPIO3x);

ThermalGPIOdisplacement3 = [78.02,0,22.14];
translate(ThermalGPIOdisplacement3)
cube( GPIO2333y);

Button = [4.5,3,4.5];
ThermalButtonDisplacement = [53.38,2.78,22.14];
translate(ThermalButtonDisplacement)
cube( Button);




GPIO88y = [GPIOdepth,59,GPIOheight];
MegaindGPIOdisplacement1_1 = [-12.9,-3.04,42.68];
MegaindGPIOdisplacement1_2 = [-12.9,-3.04,63.22];
translate(MegaindGPIOdisplacement1_1)
cube( GPIO88y);
translate(MegaindGPIOdisplacement1_2)
cube( GPIO88y);

MegaindButtonDisplacement_1 = [-5.68,-6.64,42.68];
MegaindButtonDisplacement_2 = [-5.68,-6.64,63.22];
translate(MegaindButtonDisplacement_1)
cube( Button);
translate(MegaindButtonDisplacement_2)
cube( Button);


GPIO885x = [78.74,GPIOdepth,GPIOheight];
MegaindGPIOdisplacement2_1 = [-0.68,-10.14,42.68];
MegaindGPIOdisplacement2_2 = [-0.68,-10.14,63.22];
translate(MegaindGPIOdisplacement2_1)
cube( GPIO885x);
translate(MegaindGPIOdisplacement2_2)
cube( GPIO885x);

GPIO8y = [GPIOdepth,29.52,GPIOheight];
MegaindGPIOdisplacement3_1 = [80.52,-7.6,42.68];
MegaindGPIOdisplacement3_2 = [80.52,-7.6,63.22];
translate(MegaindGPIOdisplacement3_1)
cube( GPIO8y);
translate(MegaindGPIOdisplacement3_2)
cube( GPIO8y);

MegaindGPIOdisplacement3_3 = [80.52,26.3,42.68];
MegaindGPIOdisplacement3_4 = [80.52,26.3,63.22];
translate(MegaindGPIOdisplacement3_3)
cube( GPIO8y);
translate(MegaindGPIOdisplacement3_4)
cube( GPIO8y);

GPIO2x = [8.34,GPIOdepth,GPIOheight];
MegaindGPIOdisplacement4_1 = [71.12,49,42.68];
MegaindGPIOdisplacement4_2 = [71.12,49,63.22];
translate(MegaindGPIOdisplacement4_1)
cube( GPIO2x);
translate(MegaindGPIOdisplacement4_2)
cube( GPIO2x);


screw_r = 1.24;
screw_h = 4.5;

gear_r = 2.83;
gear_h = 2.00;

translate([3.38,3.48,-screw_h])
cylinder(h = screw_h, r = screw_r);
translate([3.38,52.14,-screw_h])
cylinder(h = screw_h, r = screw_r);
translate([61.76,3.48,-screw_h])
cylinder(h = screw_h, r = screw_r);
translate([61.76,52.14,-screw_h])
cylinder(h = screw_h, r = screw_r);

beam_r = 2.31;
beam_h = 59.92;

translate([3.38,3.48,1.6])
cylinder(h = beam_h, r = beam_r);
translate([3.38,52.14,1.6])
cylinder(h = beam_h, r = beam_r);
translate([61.76,3.48,1.6])
cylinder(h = beam_h, r = beam_r);
translate([61.76,52.14,1.6])
cylinder(h = beam_h, r = beam_r);

};




PlasticThickness = 2.5;
StandardGap = 3;


module ScrewHolder()

{
    
difference()
{
cylinder(r=(2.83+PlasticThickness+1),h=(4.5+PlasticThickness),$fn=100);
translate([0,0,-1])      
cylinder(r=(2.83+1),h=(6),$fn=100);    

translate([0,0,4.5])  
cylinder(r=(1.24),h=(PlasticThickness+1),$fn=100); 
}
translate([0,0,4.5+PlasticThickness])
difference()
{
cylinder(r=(1.24+1.1),h=(0.5),$fn=100);
translate([0,0,-0.5])      
cylinder(r=(1.24),h=(1.5),$fn=100);    

translate([0,0,4.5])  
cylinder(r=(1.24),h=(PlasticThickness+1)); 
}

};

module NutHolder(){
    
    
    translate([-4.95,0,0])
difference(){
union(){
    
    cube([9.9,7.65,5]);
    translate([4.95,7.65,0])
    cylinder(r=4.95,h=5,$fn=100);
    
};    

translate([4.95,7.65,-0.5])
cylinder(r=3.118,h=3.5,$fn=6);

translate([4.95,7.65,-0.5])
cylinder(r=1.5,h=6.5,$fn=100);

};
};

module BottomSideSupport(){
    
cube([0.5,(PlasticThickness+StandardGap-1),11]);  
    
    
};    

module BottomCover()
{
    
MainBottom = [(85.10+2*PlasticThickness+2*StandardGap), (56.10+2*PlasticThickness+2*StandardGap), PlasticThickness];
    
difference(){
cube(MainBottom);
    translate([PlasticThickness+StandardGap,PlasticThickness+StandardGap,0])
translate([3.38,3.48,-0.5])
cylinder(r=(2.83+PlasticThickness+1),h=PlasticThickness+1);
    translate([PlasticThickness+StandardGap,PlasticThickness+StandardGap,0])
translate([3.38,52.14,-0.5])
cylinder(r=(2.83+PlasticThickness+1),h=PlasticThickness+1);
    translate([PlasticThickness+StandardGap,PlasticThickness+StandardGap,0])
translate([61.76,3.48,-0.5])
cylinder(r=(2.83+PlasticThickness+1),h=PlasticThickness+1);
    translate([PlasticThickness+StandardGap,PlasticThickness+StandardGap,0])
translate([61.76,52.14,-0.5])
cylinder(r=(2.83+PlasticThickness+1),h=PlasticThickness+1);
    
VentLength = 30;
for(i=[15:10:55])
translate([i,(28.05+PlasticThickness+StandardGap-VentLength/2),-0.5])
cube([5,VentLength,PlasticThickness+1]);   

SDCardGapWidth = 15;
translate([-0.5,(28.05+PlasticThickness+StandardGap-SDCardGapWidth/2),-0.5])
cube([3,SDCardGapWidth,PlasticThickness+1]);

;
};
translate([PlasticThickness+StandardGap,PlasticThickness+StandardGap,0])
translate([3.38,3.48,0])
ScrewHolder();
    translate([PlasticThickness+StandardGap,PlasticThickness+StandardGap,0])
translate([3.38,52.14,0])
ScrewHolder();
    translate([PlasticThickness+StandardGap,PlasticThickness+StandardGap,0])
translate([61.76,3.48,0])
ScrewHolder();
    translate([PlasticThickness+StandardGap,PlasticThickness+StandardGap,0])
translate([61.76,52.14,0])
ScrewHolder();


translate([(3.38+StandardGap+PlasticThickness-2),12.9,PlasticThickness])
cube([4,40,4]);

translate([(61.76+StandardGap+PlasticThickness-2),12.9,PlasticThickness])
cube([4,40,4]);

translate([72,(3.48+StandardGap+PlasticThickness-2),PlasticThickness])
cube([22,4,4]);


translate([72,(52.14+StandardGap+PlasticThickness-2),PlasticThickness])
cube([22,4,4]);


translate([13,(3.48+StandardGap+PlasticThickness-2),PlasticThickness])
cube([50,4,4]);


translate([13,(52.14+StandardGap+PlasticThickness-2),PlasticThickness])
cube([50,4,4]);

translate([24,0,0])
BottomSideSupport();

translate([52,0,0])
BottomSideSupport();

translate([22.5,((56.10+PlasticThickness+StandardGap)),0])
BottomSideSupport();


translate([52.5,((56.10+PlasticThickness+StandardGap)),0])
BottomSideSupport();


translate([8.5,((56.10+PlasticThickness+StandardGap+0.25)),65])
BottomSideSupport();


translate([67,((56.10+PlasticThickness+StandardGap+0.25)),65])
BottomSideSupport();


rotate(270)
translate([-20,0,0])
BottomSideSupport();

rotate(270)
translate([(-(56.10+2*PlasticThickness+2*StandardGap)+20),0,0])
BottomSideSupport();


rotate(270)
translate([-20,((85.10+PlasticThickness+StandardGap)),0])
cube([0.5,(PlasticThickness+StandardGap),9]);

rotate(270)
translate([(-(56.10+2*PlasticThickness+2*StandardGap)+20),((85.10+PlasticThickness+StandardGap)),0])
cube([0.5,(PlasticThickness+StandardGap),9]);

};

module RearWall(){
difference(){
MainWall = ([(85.10+2*PlasticThickness+2*StandardGap),PlasticThickness,85]);

cube(MainWall);

VentHeight = 27.5;

for(i=[15:10:55]){
translate([i,-0.5,10])
cube([5,PlasticThickness+1,VentHeight]);
};
for(i=[15:10:55]){
    
    translate([i,-0.5,42.5])
cube([5,PlasticThickness+1,VentHeight]);};

translate([75,-0.5,10])
cube([5,PlasticThickness+1,VentHeight]);
translate([85,-0.5,10])
cube([5,PlasticThickness+1,VentHeight]);

GPIO2gapxwidth = 1;
GPIO2gapheight = 14;
GPIO2gaplowerdisplacement = 5;

GPIO2gap = [(8.34+2*GPIO2gapxwidth),PlasticThickness+1,GPIO2gapheight];
translate([(71.12+PlasticThickness+StandardGap-GPIO2gapxwidth),-0.5,(42.68+5.5+PlasticThickness-GPIO2gaplowerdisplacement)])

cube(GPIO2gap);


translate([(71.12+PlasticThickness+StandardGap-GPIO2gapxwidth),-0.5,(63.22+5.5+PlasticThickness-GPIO2gaplowerdisplacement)])

cube(GPIO2gap);


    
};

VerticalBeam = [4,4,85];
translate([((3.38+StandardGap+PlasticThickness-2)),-2,0])
cube(VerticalBeam);

translate([((61.76+StandardGap+PlasticThickness-2)),-2,0])
cube(VerticalBeam);

HorizontalBeam = [(85.10+2*PlasticThickness+2*StandardGap-4),4,4];

translate([0,-2.5,38])
cube(HorizontalBeam);

height = 3;
width = 1.5;

translate([(85.10+2*PlasticThickness+2*StandardGap-4),-2.5,38])
polyhedron(points=[ [0,0,0],[0,0,4],[0,4,4],[0,4,0],[width,0,height],[width,0,(7+height)],[width,4,(7+height)],[width,4,height] ], faces = [[3,2,1,0],[0,1,5,4],[2,3,7,6],[1,2,6,5],[5,6,7,4],[3,0,4,7]]);


translate([-1,0,41])
cube([1,PlasticThickness,44]);

};

module BottomLeftWall(){

difference() {

cube([PlasticThickness,(56.10+2*PlasticThickness+2*StandardGap),28]);
    SDCardGapWidth = 15;
translate([-0.5,(28.05+PlasticThickness+StandardGap-SDCardGapWidth/2),-0.5])
cube([4,SDCardGapWidth,15]);


    
};

translate([0,(56.10+2*PlasticThickness+2*StandardGap-5),0])
cube([PlasticThickness,5,85]);

};



module BottomRightWall(){

cube([PlasticThickness,(56.10+2*PlasticThickness+2*StandardGap),9]);

};

module BottomFrontWall(){

difference(){
cube([(85.10+2*PlasticThickness+2*StandardGap),PlasticThickness,28]);

PortGap=2.25;

TypeCGap = [(9.01+2*PortGap),PlasticThickness+1,(3.32+2*PortGap)];   

translate([(PlasticThickness+StandardGap+6.68-PortGap),-0.5,(7.5+1.6-PortGap)])
cube(TypeCGap);

MicroHDMIGap = [(6.64+2*PortGap),(PlasticThickness+1),(3.54+2*PortGap)];

translate([(StandardGap+PlasticThickness+22.34-PortGap),-0.5,(7.5+1.6-PortGap)])
cube(MicroHDMIGap);
    
translate([(StandardGap+PlasticThickness+35.30-PortGap),-0.5,(7.5+1.6-PortGap)])
cube(MicroHDMIGap);
    
JackGap = ([(7.06+2*PortGap),(PlasticThickness+1),(6.04+2*PortGap)]);
translate([(50.58+PlasticThickness+StandardGap-PortGap),-0.5,(7.5-PortGap+1.6)])
cube(JackGap);  

    
};

difference(){

translate([0,0,28])
cube([(85.10+2*PlasticThickness+2*StandardGap),PlasticThickness,20]);

VentHeight=13;

for(i=[15:10:45]){

        
    translate([i,-0.5,28])
cube([5,PlasticThickness+1,VentHeight]);};

translate([55,-0.5,28])
cube([34,10,13]);

};
};


module RightBeam(){

cube([7,7,48]);
translate([0,-5,41])
cube([7,7,44]);

translate([4.5,0,41])
cube([2.5,(56.10+PlasticThickness+2*StandardGap+7),7]);    

polyhedron(points=[ [0,0,0],[7,0,0],[0,0,41],[7,0,41],[0,-5,41],[7,-5,41] ],faces=[ [0,2,4],[1,5,3],[1,3,2,0],[0,4,5,1],[2,3,5,4] ]);
    
    
    
translate([3.25,-0.9,65])
BottomSideSupport();    

translate([3.5,(-1.5),85])
cylinder(r=3,h=5,$fn=100);   

translate([3.5,-1.5,80])
rotate(225)    
NutHolder();    

    
};







module LeftBeam(){
    
cube([7,7,48]);    
translate([-8,-5,41])
cube([7,7,44]);

translate([-8,-5,41])
    
polyhedron(points=[ [0,0,0],[0,7,0],[8,14,0],[15,14,0],[15,5,0],[7,0,0],[0,0,7],[0,7,7],[8,14,7],[15,14,7],[15,5,7],[7,0,7] ],faces=[ [5,4,3,2,1,0],[6,7,8,9,10,11],[5,0,6,11],[0,1,7,6],[1,2,8,7],[2,3,9,8],[3,4,10,9],[4,5,11,10]]);
translate([-8,-5,0])
polyhedron(points=[ [8,5,0],[8,14,0],[15,14,0],[15,5,0],[7,0,0],[0,0,41],[0,7,41],[8,14,41],[15,14,41],[15,5,41],[7,0,41]],faces=[[3,2,1,0],[9,8,2,3],[3,10,9],[0,10,3],[8,7,1,2],[0,1,6,5],[0,5,10],[1,7,6],[5,6,7,8,9,10]]);
    
translate([-4.7,-0.9,65])
BottomSideSupport();

translate([-4.5,(-1.5),85])
cylinder(r=3,h=5,$fn=100);   


translate([-4.5,-1.5,80])
rotate(135)    
NutHolder();    


    
};    


module CentralFrontBeam(){

cube([(85.10+2*PlasticThickness+2*StandardGap),4,7]);

};


module RightRearBeam(){

cube([7,7,85]);
    
translate([3.5,3.5,85])
cylinder(r=3,h=5,$fn=100);     


translate([3.5,3.5,80])
rotate(315)    
NutHolder();    

};


module LeftRearBeam(){

cube([7,7,48]);
translate([-8,0,41])
cube([7,7,44]);
translate([-8,0,41])
cube([15,7,7]);    

polyhedron(points=[ [0,0,0],[0,7,0],[0,0,41],[0,7,41],[-8,0,41],[-8,7,41] ],faces=[[0,1,5,4],[1,3,5],[0,4,2],[1,0,2,3],[4,5,3,2]]);

translate([-1,0,48])
polyhedron(points=[ [0,0,0],[0,7,0],[8,7,0],[8,0,0],[0,0,37],[0,7,37] ],faces=[[3,2,1,0],[0,4,3],[1,2,5],[2,3,4,5],[0,1,5,4]]);

translate([-4.5,3.5,85])
cylinder(r=3,h=5,$fn=100); 

translate([-4.5,3.5,80])
rotate(45)    
NutHolder();    


};

module Enclosure(){
BottomCover();
BottomLeftWall();    
translate([0,(56.10+PlasticThickness+2*StandardGap),0])
RearWall();
translate([(85.10+PlasticThickness+2*StandardGap),0,0])
BottomRightWall();
BottomFrontWall();
    
translate([((85.10+2*PlasticThickness+2*StandardGap-7)),-6.5,0])
RightBeam();
translate([0,-6.5,0])    
LeftBeam();

translate([0,-4,41])
CentralFrontBeam();    

translate([((85.10+2*PlasticThickness+2*StandardGap-7)),(56.10+PlasticThickness+2*StandardGap),0])
RightRearBeam();    

translate([0,(56.10+PlasticThickness+2*StandardGap),0])
LeftRearBeam();    

    
};

module TopScrewHolder(){

translate([-4.95,0,0])

difference(){
union(){
    
    cube([9.9,7.65,5]);
    translate([4.95,7.65,0])
    cylinder(r=4.95,h=5,$fn=100);
    
};    

translate([4.95,7.65,2.5])
cylinder(r=2.89,h=3.5,$fn=100);

translate([4.95,7.65,-0.5])
cylinder(r=1.5,h=6.5,$fn=100);

};
};



module TopCover(){

difference(){
union(){
MainTop = [(85.10+2*PlasticThickness+2*StandardGap+8), (56.10+2*PlasticThickness+2*StandardGap+16), PlasticThickness];
cube(MainTop);

translate([3.5,3.5,0])
rotate(135)
TopScrewHolder();
translate([3.5,(56.10+2*PlasticThickness+2*StandardGap+12.5),0])
rotate(45)
TopScrewHolder();
    
translate([(85.10+2*PlasticThickness+2*StandardGap+8-3.5),(56.10+2*PlasticThickness+2*StandardGap+12.5),0])
rotate(315)
TopScrewHolder();

translate([(85.10+2*PlasticThickness+2*StandardGap+8-3.5),3.5,0])
rotate(225)
TopScrewHolder();      
    
translate([0.5,0,0])
cube([(85.10+2*PlasticThickness+2*StandardGap+8-1),3.5,5]);    
translate([0.5,(56.10+2*PlasticThickness+2*StandardGap+12.5),0])
cube([(85.10+2*PlasticThickness+2*StandardGap+8-1),3.5,5]);
    
translate([0,0.5,0])
cube([3.5,(56.10+2*PlasticThickness+2*StandardGap+16-1),5]);
translate([(85.10+2*PlasticThickness+2*StandardGap+4.5),0.5,0])
cube([3.5,(56.10+2*PlasticThickness+2*StandardGap+16-1),5]);    

translate([3.5,3.5,0])    
cylinder(r=4.7,h=5,$fn=100);

translate([3.5,(56.10+2*PlasticThickness+2*StandardGap+16-3.5),0])    
cylinder(r=4.7,h=5,$fn=100);

translate([(85.10+2*PlasticThickness+2*StandardGap+8-3.5),(56.10+2*PlasticThickness+2*StandardGap+16-3.5),0])    
cylinder(r=4.7,h=5,$fn=100);

translate([(85.10+2*PlasticThickness+2*StandardGap+8-3.5),3.5,0])    
cylinder(r=4.7,h=5,$fn=100);  
};

translate([3.5,3.5,-0.5])    
cylinder(r=3,h=6,$fn=100);

translate([3.5,(56.10+2*PlasticThickness+2*StandardGap+16-3.5),-0.5])    
cylinder(r=3,h=6,$fn=100);

translate([(85.10+2*PlasticThickness+2*StandardGap+8-3.5),(56.10+2*PlasticThickness+2*StandardGap+16-3.5),-0.5])    
cylinder(r=3,h=6,$fn=100);

translate([(85.10+2*PlasticThickness+2*StandardGap+8-3.5),3.5,-0.5])    
cylinder(r=3,h=6,$fn=100); 


midpoint = (56.10+2*PlasticThickness+2*StandardGap+16)/2;
outer_offset = 32.5;
inner_offset = 2.5;

for(i=[15:10:85]){
translate([(i-2),(midpoint+inner_offset),-0.5])
cube([5,(outer_offset-inner_offset),PlasticThickness+1]);

translate([(i-2),(midpoint-outer_offset),-0.5])
cube([5,(outer_offset-inner_offset),PlasticThickness+1]);
    
};

};

};

RaspberryWithHats();


translate([-(PlasticThickness+StandardGap),-(PlasticThickness+StandardGap),-8])
Enclosure();

translate([-(PlasticThickness+StandardGap+8),-(PlasticThickness+StandardGap+11.5),77.5])
TopCover();

