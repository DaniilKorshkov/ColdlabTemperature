import SequentMicroInterface as sm
import time
import datetime
import CreateNewFile
import matplotlib.pyplot as plt

import JSONoperators as js
import atexit
import signal
import sys


def main():



    #------------------------------ initiation --------------------------------------------

    js.MergeJSONConfigs()

    atexit.register(exit_handler)
    signal.signal(signal.SIGINT, kill_handler)
    signal.signal(signal.SIGTERM, kill_handler)
    
    filename = CreateNewFile.MakeNewFile()
    
  

    while True:
        try:
            interval = int(input(f"Enter record interval in seconds: "))
            assert interval > 0
            break
        except:
            print(f"Not a valid integer")
        
        
            
            
    temperaturelegend = []

    print(f"To terminate the process, please use Ctrl+C")


        
    


    #------------------------------ infinite cycle --------------------------------------------
    
    
    while True:
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
        handle.write("\n")
        handle.close()

        
        
        time.sleep(interval)
    
        
        
def exit_handler():
    plt.close('all')

def kill_handler(*args):
    sys.exit(0)


if __name__ == "__main__":
    main()

