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
