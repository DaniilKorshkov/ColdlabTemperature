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
cylinder(r=(1.5),h=(PlasticThickness+1),$fn=100); 
}
translate([0,0,4.5+PlasticThickness])
difference()
{
cylinder(r=(1.24+1.1),h=(0.5),$fn=100);
translate([0,0,-0.5])      
cylinder(r=(1.5),h=(1.5),$fn=100);    

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
    
cube([0.5,(PlasticThickness+StandardGap-2),11]);  
    
    
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
translate([i+1,(28.05+1+PlasticThickness+StandardGap-VentLength/2),-0.5])

minkowski(){
cube([3,VentLength-2,PlasticThickness+1]);
cylinder(h=10,r=1,$fn=100);    

};   

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
cube([4,40,2.5]);

translate([(61.76+StandardGap+PlasticThickness-2),12.9,PlasticThickness])
cube([4,40,2.5]);

translate([72,(3.48+StandardGap+PlasticThickness-2),PlasticThickness])
cube([22,4,4]);


translate([72,(52.14+StandardGap+PlasticThickness-2),PlasticThickness])
cube([22,4,4]);


translate([13,(3.48+StandardGap+PlasticThickness-2),PlasticThickness])
cube([50,4,2.5]);


translate([13,(52.14+StandardGap+PlasticThickness-2),PlasticThickness])
cube([50,4,2]);





};

module RearWall(){
difference(){
MainWall = ([(85.10+2*PlasticThickness+2*StandardGap),PlasticThickness,85]);

cube(MainWall);

VentHeight = 9.75;

for(i=[15:10:55]){
translate([i+1,-0.5,10+1])
minkowski(){
cube([3,PlasticThickness+1,VentHeight-2]);
rotate([90,0,0])
cylinder(h=3.5,r=1,$fn=100);
};

translate([i+1,-0.5,27.75])
minkowski(){
cube([3,PlasticThickness+1,VentHeight-2]);
rotate([90,0,0])
cylinder(h=3.5,r=1,$fn=100);
};


translate([i+1,-0.5,61.25])
minkowski(){
cube([3,PlasticThickness+1,VentHeight-2]);
rotate([90,0,0])
cylinder(h=3.5,r=1,$fn=100);
};

translate([i+1,-0.5,42.5+1])
minkowski(){
cube([3,PlasticThickness+1,VentHeight-2]);
rotate([90,0,0])
cylinder(h=3.5,r=1,$fn=100);
};

};
    
    
    
for(i=[76:10:76]){

translate([i,-0.5,10+1])
minkowski(){
cube([8,PlasticThickness+1,VentHeight-2]);
rotate([90,0,0])
cylinder(h=3.5,r=1,$fn=100);};

translate([i,-0.5,27.75])
minkowski(){
cube([8,PlasticThickness+1,VentHeight-2]);
rotate([90,0,0])
cylinder(h=3.5,r=1,$fn=100);};

};

GPIO2gapxwidth = 1;
GPIO2gapheight = 14;
GPIO2gaplowerdisplacement = 5;

GPIO2gap = [(8.64+2*GPIO2gapxwidth-2),PlasticThickness+1,(GPIO2gapheight-2)];
translate([(71.12+PlasticThickness+StandardGap-GPIO2gapxwidth+1+1.17),-0.5,(42.68+5.5+PlasticThickness-GPIO2gaplowerdisplacement+1)])

minkowski(){
cube(GPIO2gap);
    rotate([90,0,0])
cylinder(h=10,r=1,$fn=100);
};

translate([(71.12+PlasticThickness+StandardGap-GPIO2gapxwidth+1+1.17),-0.5,(63.22+5.5+PlasticThickness-GPIO2gaplowerdisplacement+1)])

minkowski(){
cube(GPIO2gap);
    rotate([90,0,0])
cylinder(h=10,r=1,$fn=100);
};


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




translate([-1,0,41])
cube([1,PlasticThickness,44]);


};

module BottomLeftWall(){

difference() {

cube([PlasticThickness,(56.10+2*PlasticThickness+2*StandardGap),26]);
    SDCardGapWidth = 15;
    

translate([-0.5,(28.05+3+PlasticThickness+StandardGap-SDCardGapWidth/2),-0.5])
minkowski(){
cube([4,SDCardGapWidth-6,15]);
rotate([0,90,0])
cylinder(r=3,h=4,$fn=100);
};

    
};

translate([0,(56.10+2*PlasticThickness+2*StandardGap-5),0])
cube([PlasticThickness,5,85]);

};



module BottomRightWall(){

cube([PlasticThickness,(56.10+2*PlasticThickness+2*StandardGap),9]);

};

module BottomFrontWall(){

difference(){
cube([(85.10+2*PlasticThickness+2*StandardGap),PlasticThickness,46]);

PortGap=2.25;

TypeCGap = [(9.01+2*PortGap-2),PlasticThickness+1,(3.32+2*PortGap-2)];   

translate([(PlasticThickness+StandardGap+6.68-PortGap+1),-0.5,(7.5+1.6-PortGap+1)])
minkowski(){
cube(TypeCGap);
rotate([90,0,0])
cylinder(h=10,r=1,$fn=100);
};

MicroHDMIGap = [(6.64+2*PortGap-2),(PlasticThickness+1),(3.54+2*PortGap-2)];


translate([(StandardGap+PlasticThickness+22.34-PortGap+1),-0.5,(7.5+1.6-PortGap+1)])
minkowski(){
cube(MicroHDMIGap);
rotate([90,0,0])
cylinder(h=10,r=1,$fn=100);
};
    
translate([(StandardGap+PlasticThickness+35.30-PortGap+1.5),-0.5,(7.5+1.6-PortGap+1)])
minkowski(){
cube(MicroHDMIGap);
rotate([90,0,0])
cylinder(h=10,r=1,$fn=100);
};
    
JackGap = ([(7.06+2*PortGap-6),(PlasticThickness+1),(6.04+2*PortGap-6)]);
translate([(50.58+PlasticThickness+StandardGap-PortGap+3),-0.5,(7.5-PortGap+1.6+3)])
minkowski(){
cube(JackGap);
rotate([90,0,0])
cylinder(h=10,r=3,$fn=100);
};
    




VentHeight=13;

for(i=[15:10:45]){

        
    translate([i+1,-0.5,29])
minkowski(){
cube([3,PlasticThickness+1,VentHeight-2]);
    rotate([90,0,0])
cylinder(h=10,r=1,$fn=100);
    
};
    };

translate([58,-0.5,29])
minkowski(){
cube([28,10,8]);
rotate([90,0,0])
cylinder(h=10,r=3,$fn=100);
};


};
};

module RightBeam(){

cube([7,7,46]);
translate([0,-5,41])
difference(){
polyhedron(points=[ [0,0,0],[0,7,0],[7,7,0],[7,0,0],[0,-5.5,44],[0,7,44],[12.5,7,44],[12.5,-5.5,44] ],faces=[ [3,2,1,0],[0,1,5,4],[3,0,4,7],[2,3,7,6],[1,2,6,5],[4,5,6,7] ]);

translate([6.25,0.75,40])
cylinder(r=3,h=4.5,$fn=100);

}; 


polyhedron(points=[ [0,0,0],[7,0,0],[0,0,41],[7,0,41],[0,-5,41],[7,-5,41] ],faces=[ [0,2,4],[1,5,3],[1,3,2,0],[0,4,5,1],[2,3,5,4] ]);
    

  
    
  

  

  

    
};







module LeftBeam(){
    
cube([7,7,46]);    
translate([-8,-5,41])

difference(){
polyhedron(points=[ [0,0,0],[0,7,0],[7,7,0],[7,0,0],[-5.5,-5.5,44],[-5.5,7,44],[7,7,44],[7,-5.5,44] ],faces=[ [3,2,1,0],[0,1,5,4],[3,0,4,7],[2,3,7,6],[1,2,6,5],[4,5,6,7] ]);
    
 translate([0.75,0.75,40])
cylinder(r=3,h=4.5,$fn=100);
    
    
};

translate([-8,-5,41])
    
polyhedron(points=[ [0,0,0],[0,7,0],[8,14,0],[15,14,0],[15,5,0],[7,0,0],[0,0,5],[0,7,5],[8,14,5],[15,14,5],[15,5,5],[7,0,5] ],faces=[ [5,4,3,2,1,0],[6,7,8,9,10,11],[5,0,6,11],[0,1,7,6],[1,2,8,7],[2,3,9,8],[3,4,10,9],[4,5,11,10]]);
translate([-8,-5,0])
polyhedron(points=[ [8,5,0],[8,14,0],[15,14,0],[15,5,0],[7,0,0],[0,0,41],[0,7,41],[8,14,41],[15,14,41],[15,5,41],[7,0,41]],faces=[[3,2,1,0],[9,8,2,3],[3,10,9],[0,10,3],[8,7,1,2],[0,1,6,5],[0,5,10],[1,7,6],[5,6,7,8,9,10]]);
    

  





    
};    


module CentralFrontBeam(){

cube([(85.10+2*PlasticThickness+2*StandardGap),PlasticThickness,7]);

};


module RightRearBeam(){

cube([7,7,46]);
translate([0,0,41])
difference(){
polyhedron(points=[ [0,0,0],[0,7,0],[7,7,0],[7,0,0],[0,0,44],[0,12.5,44],[12.5,12.5,44],[12.5,0,44] ],faces=[ [3,2,1,0],[0,1,5,4],[3,0,4,7],[2,3,7,6],[1,2,6,5],[4,5,6,7] ]); 

translate([6.25,6.25,40])
cylinder(r=3,h=4.5,$fn=100);

}; 

};


module LeftRearBeam(){

cube([7,7,48]);
translate([-8,0,41])

difference(){
polyhedron(points=[ [0,0,0],[0,7,0],[7,7,0],[7,0,0],[-5.5,0,44],[-5.5,12.5,44],[7,12.5,44],[7,0,44] ],faces=[ [3,2,1,0],[0,1,5,4],[3,0,4,7],[2,3,7,6],[1,2,6,5],[4,5,6,7] ]);

translate([0.75,6.25,40])
cylinder(r=3,h=4.5,$fn=100);

}    

translate([-8,0,41])
cube([15,7,7]);    

polyhedron(points=[ [0,0,0],[0,7,0],[0,0,41],[0,7,41],[-8,0,41],[-8,7,41] ],faces=[[0,1,5,4],[1,3,5],[0,4,2],[1,0,2,3],[4,5,3,2]]);

translate([-1,0,48])
polyhedron(points=[ [0,0,0],[0,7,0],[8,7,0],[8,0,0],[0,0,37],[0,12.5,37] ],faces=[[3,2,1,0],[0,4,3],[1,2,5],[2,3,4,5],[0,1,5,4]]);



 


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

   

translate([((85.10+2*PlasticThickness+2*StandardGap-7)),(56.10+PlasticThickness+2*StandardGap),0])
RightRearBeam();    

translate([0,(56.10+PlasticThickness+2*StandardGap),0])
LeftRearBeam();    

    
};

module TopScrewHolder(){

translate([-3.5,-3.5,0])



    difference(){
    cube([12.5,12.5,5]);
    
        translate([6.25,6.25,-0.5])
        cylinder(r=2,h=6);
    
    };
   
};    

module TopCover(){

difference(){
union(){
MainTop = [(85.10+2*PlasticThickness+2*StandardGap+8), (56.10+2*PlasticThickness+2*StandardGap+16), PlasticThickness];
cube(MainTop);

translate([3.5,3.5,0])
rotate(135+45)
TopScrewHolder();
translate([3.5,(56.10+2*PlasticThickness+2*StandardGap+12.5),0])
rotate(45+45)
TopScrewHolder();
    
translate([(85.10+2*PlasticThickness+2*StandardGap+8-3.5),(56.10+2*PlasticThickness+2*StandardGap+12.5),0])
rotate(315+45)
TopScrewHolder();

translate([(85.10+2*PlasticThickness+2*StandardGap+8-3.5),3.5,0])
rotate(225+45)
TopScrewHolder();      
    
translate([3,0,0])
cube([(85.10+2*PlasticThickness+2*StandardGap+8-1),3.5,5]);    
translate([0.5,(56.10+2*PlasticThickness+2*StandardGap+12.5),0])
cube([(85.10+2*PlasticThickness+2*StandardGap+8-1),3.5,5]);
    
translate([0,0.5,0])
cube([3.5,(56.10+2*PlasticThickness+2*StandardGap+16-1),5]);
translate([(85.10+2*PlasticThickness+2*StandardGap+4.5),0.5,0])
cube([3.5,(56.10+2*PlasticThickness+2*StandardGap+16-1),5]); 


  
};




 


midpoint = (56.10+2*PlasticThickness+2*StandardGap+16)/2;
outer_offset = 31.5;
inner_offset = 3.5;

for(i=[15.5:5:95.5]){
translate([(i-2),(midpoint+inner_offset),-0.5])
minkowski(){
cube([0.5,(outer_offset-inner_offset),PlasticThickness+1]);
cylinder(h=10,r=1,$fn=100);
  
};


translate([(i-2),(midpoint-outer_offset),-0.5])
minkowski(){
cube([0.5,(outer_offset-inner_offset),PlasticThickness+1]);
cylinder(h=10,r=1,$fn=100);

};
    
};

translate([0.75,0.75,-0.5])
cylinder(r=2,h=6,$fn=100);
translate([0.75,82.35,-0.5])
cylinder(r=2,h=6,$fn=100);
translate([103.35,0.75,-0.5])
cylinder(r=2,h=6,$fn=100);
translate([103.35,82.35,-0.5])
cylinder(r=2,h=6,$fn=100);



};

};




translate([-(PlasticThickness+StandardGap),-(PlasticThickness+StandardGap),-8])
Enclosure();

translate([-(PlasticThickness+StandardGap+8),-(PlasticThickness+StandardGap+11.5),77]);