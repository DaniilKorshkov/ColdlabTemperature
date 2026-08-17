import SequentMicroInterface as sm
import time
import datetime
import CreateNewFile
import matplotlib.pyplot as plt

import JSONoperators as js
import atexit
import signal
import sys

import TemperatureScreen
import PressureScreen
import AmperageScreen


def main():



    #------------------------------ initiation --------------------------------------------


    currently_processed_amperage_ports = js.ReadJSONConfig("RTD_options","currently_processed_amperage_ports")
    if len(currently_processed_amperage_ports > 0):
        do_amperage = True
    else:
        do_amperage = False

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

    
    
    filename = CreateNewFile.MakeNewFile()

    if do_amperage:

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
        
        
            
            
    temperaturelegend = []


    last_cycle_time = 0

    print(f"To terminate the process, please use Ctrl+C")



    if display_graphs:
        TemperatureScreen.initiate_frame(filename)
        PressureScreen.initiate_frame(filename)
        AmperageScreen.initiate_frame(filename)
        
    


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

        if (datetime.datetime.now().timestamp() > interval + last_cycle_time) and (len(amperage_output) == 8:):


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

            
                log_handle = open(filename, "a")
                log_handle.write(f"{current_time}\t")
                for element in output:
                    log_handle.write(element)
                    log_handle.write("\t")
            


            last_cycle_time = datetime.datetime.now().timestamp()

        
        
        
    
        
        
def exit_handler():
    plt.close('all')
    ser.close()

def kill_handler(*args):
    sys.exit(0)
    ser.close()

if __name__ == "__main__":
    main()

