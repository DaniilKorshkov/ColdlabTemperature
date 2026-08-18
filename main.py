import SequentMicroInterface as sm
import time
import datetime
import CreateNewFile
import matplotlib.pyplot as plt
import serial

import JSONoperators as js
import atexit
import signal
import sys

import TemperatureScreen
import PressureScreen
import AmperageScreen




import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import JSONoperators as js
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter
import datetime as dt







def initiate_frame():

    

    
    global filename
    

    
    global tempfig
    tempfig = plt.figure()
    #pressfig = plt.figure()

    global tempax
    tempax = tempfig.add_subplot(111)
    #pressax = pressfig.add_subplot(111)

    global pressfig
    pressfig = plt.figure()
    #pressfig = plt.figure()

    global pressax
    pressax = pressfig.add_subplot(111)

    
    global ampfig
    ampfig = plt.figure()

    global ampax
    ampax = ampfig.add_subplot(111)






    pressani = FuncAnimation(pressfig, TemperatureScreen.update_frame, interval=1000)
    tempani = FuncAnimation(tempfig, PressureScreen.update_frame, interval=1000)
    ampani = FuncAnimation(ampfig, AmperageScreen.update_frame, interval=1000)


    plt.show()











def main():



    #------------------------------ initiation --------------------------------------------


    currently_processed_amperage_ports = js.ReadJSONConfig("RTD_options","currently_processed_amperage_ports")
    if len(currently_processed_amperage_ports) > 0:
        do_amperage = True
    else:
        do_amperage = False

    currently_processed_pressure_ports = js.ReadJSONConfig("RTD_options","currently_processed_voltage_ports")
    if len(currently_processed_pressure_ports) > 0:
        do_pressure = True
    else:
        do_pressure = False

    
    currently_processed_temperature_ports = js.ReadJSONConfig("RTD_options","currently_processed_temperature_ports")
    if len(currently_processed_temperature_ports) > 0:
        do_temperature = True
    else:
        do_temperature = False

    while True:
        inputline = str(input("Display graphs(y/n): "))
        if inputline.lower() == "y":
            display_graphs = True
            break
        elif inputline.lower() == "n":
            display_graphs = False
            break
        else:
            print("Invalid input")



    js.MergeJSONConfigs()

    atexit.register(exit_handler)
    signal.signal(signal.SIGINT, kill_handler)
    signal.signal(signal.SIGTERM, kill_handler)

    
    global filename
    filename = CreateNewFile.MakeNewFile()

    if do_amperage:

        PORT = js.ReadJSONConfig("Technical","arduino_address")

        ser = serial.Serial()
        ser.port = PORT
        ser.baudrate = 115200
        ser.timeout = 10

        try:
            ser.close()
        except:
            pass
            
        ser.open()
    
  

    while True:
        try:
            interval = int(input(f"Enter record interval in seconds: "))
            assert interval > 0
            break
        except:
            print(f"Not a valid integer")
        
        
            
            
   


    last_cycle_time = 0

    print(f"To terminate the process, please use Ctrl+C")



    if display_graphs:
       initiate_frame()
    


    #------------------------------ infinite cycle --------------------------------------------
    
    
    while True:

        
        if do_amperage:

            ret = ser.read_until(b"!END")
            ret = ret.decode("utf-8")
            ret = ret.replace("!START!", "").replace("!END", "")

            print(f"Amperage reading {ret}")
            
            tmp = ret.split("\n")
            tmp3 = []
            amperage_output = []
            for element in tmp:
                tmp2 = element.split(",")
                for element in tmp2:
                    tmp3.append(element)
            

            for element in tmp3:
                if element == "":
                    pass
                else:
                    amperage_output.append( ((element.strip("Dev[0] CURR: ")).strip("Dev[1] CURR:" )).strip("\r") )

        else:
            amperage_output = []
        

        #-------------------------- Appending log file --------------------------------------

        if (datetime.datetime.now().timestamp() > interval + last_cycle_time) and ( (not do_amperage) or ( do_amperage and len(amperage_output) == 8)):


            current_time = (datetime.datetime.now()).strftime("%Y-%h-%d %H:%M:%S")
            tempertaurelogentry, temperaturelist = sm.ReadAllTemperatures()
            pressurelogentry, pressurelist = sm.ReadAllVoltages()
        

            handle = open(filename, "a")
            handle.write(f"{current_time}\t\t")
            for element in temperaturelist:
                handle.write(f"{element}\t")
            handle.write("\t")
            for element in pressurelist:
                handle.write(f"{element}\t")

            i = 1
            for element in amperage_output:
                if i in currently_processed_amperage_ports:
                    handle.write(f"{element}\t")

                i+=1             
            handle.write("\n")
            handle.close()

            
            
            


            last_cycle_time = datetime.datetime.now().timestamp()

        
        
        
    
        
        
def exit_handler():
    plt.close('all')
    try:
        ser.close()
    except:
        pass    

def kill_handler(*args):
    sys.exit(0)
    try:
        ser.close()
    except:
        pass

if __name__ == "__main__":
    main()

