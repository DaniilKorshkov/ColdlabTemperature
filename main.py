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
    dodisplaygraphs = js.ReadJSONConfig("RTD_options","showgraphs")
    entriestodisplay = js.ReadJSONConfig("RTD_options","entriestodisplay")
    refreshtime = js.ReadJSONConfig("RTD_options","refreshtime")
    plt_backend = js.ReadJSONConfig("Technical","plt_backend")

    if dodisplaygraphs == "True":
        plt.switch_backend(plt_backend)
    

    while True:
        try:
            interval = int(input(f"Enter record interval in seconds: "))
            assert interval > 0
            break
        except:
            print(f"Not a valid integer")
        
        
            
            
    print(f"To terminate the process, please use Ctrl+C")



        
    if dodisplaygraphs == "True":
        pressurearrays, temperaturearrays = initiate_frame()



        
        
    refreshtick = int(interval/refreshtime)
    if refreshtick < 1:
        refreshtick = 1
    refreshcounter = refreshtick
        
    


    #------------------------------ infinite cycle --------------------------------------------
    
    
    while True:
        current_time = (datetime.datetime.now()).strftime("%Y-%h-%d %H:%M:%S")
        
        #handle = open(filename,"a")
        #handle.write(f"{current_time}\t\t")
        #handle.close()
        
        tempertaurelogentry, temperaturelist = sm.ReadAllTemperatures()
        #temperaturelist = sm.RecordTemperatureToLog(filename)
        #handle = open(filename,"a")
        #handle.write(f"\t\t")
        #handle.close()
        
        
        pressurelogentry, pressurelist = sm.ReadAllVoltages()
        #pressurelist = sm.RecordVoltageToLog(filename)
        #handle = open(filename,"a")
        #handle.write(f"\n")
        #handle.close()
        
        if refreshcounter >= refreshtick:
            refreshcounter = 0

            handle = open(filename, "a")
            handle.write(f"{current_time}\t\t")
            for element in temperaturelist:
                handle.write(f"{element}\t")
            handle.write("\t")
            for element in pressurelist:
                handle.write(f"{element}\t")
            handle.write("\n")
            handle.close()

            #sm.RecordTemperatureToLog(tempertaurelogentry, filename)
            #sm.RecordVoltageToLog(pressurelogentry, filename)





        refreshcounter += 1
        
        
        if dodisplaygraphs == "True":
            update_frame(temperaturearrays, pressurearrays, temperaturelist, pressurelist)
            
            
            
            
        
        #time.sleep(interval)
        time.sleep(refreshtime)
    
        
        
def exit_handler():
    plt.close('all')

def kill_handler(*args):
    sys.exit(0)


if __name__ == "__main__":
    main()




def initiate_frame():




    #----------------------------   Produce X and Y arrays to display  ------------------------------------------




    temperaturelegend = []
    pressurelegend = []
    
    
    temperaturearrays=[]
    for i in js.ReadJSONConfig(f"RTD_options",f"currently_processed_temperature_ports"):
        temperaturearrays.append([])
        temperaturelegend.append([i])
    pressurearrays = []
    for i in js.ReadJSONConfig(f"RTD_options",f"currently_processed_voltage_ports"):
        pressurearrays.append([])
        pressurelegend.append([i+1])
    
    
    
    x_ax = []
    
    colorlist = ['r','g','b','c','m','y','k','tab:brown']
    
    
    
        
    #----------------------------------   Render temperature graph frame   ------------------------------------
        
    
    tempfig = plt.figure()
    tempax = tempfig.add_subplot(111)
    tempfig.show()


    #----------------------------------   Render pressure graph frame   ------------------------------------

    
    pressfig = plt.figure()
    pressax = pressfig.add_subplot(111)
    pressfig.show()

    return pressurearrays, temperaturearrays



def update_frame(temperaturearrays, pressurearrays, temperaturelist, pressurelist):


    #----------------------------   Produce X and Y arrays to display  ------------------------------------------



    for i in range(len(temperaturelist)):
        temperaturearrays[i].append(temperaturelist[i])
        if len(temperaturearrays[i]) > entriestodisplay:
            void = (temperaturearrays[i]).pop(0)  #reduce array length to 'entriestodisplay'
            
    for i in range(len(pressurelist)):
        pressurearrays[i].append(pressurelist[i])
        if len(pressurearrays[i]) > entriestodisplay:
            void = (pressurearrays[i]).pop(0)  #reduce array length to 'entriestodisplay'
    
    
    x_ax.append(datetime.datetime.now())
    
    if len(x_ax) > entriestodisplay:
        void = x_ax.pop(0)
        
        
    #----------------------------------   Render temperature graph frame   ------------------------------------



    
    i = 0
    tempax.cla()
    tempax.set_title(f"Temperature (oC vs time)")
    for array in temperaturearrays:
        
        tempax.plot(x_ax,array,color=colorlist[i])
        
        i += 1


    tempax.legend(temperaturelegend,loc=3)
    tempfig.canvas.draw()

    
    #----------------------------------   Render pressure graph frame   ------------------------------------

        
    j = 0
    pressax.cla()
    pressax.set_title(f"Pressure (kPa vs time)")
    for array in pressurearrays:
        pressax.plot(x_ax,array,color=colorlist[j])
        
        j += 1
    

    
    
    pressax.legend(pressurelegend,loc=3)
    pressfig.canvas.draw()