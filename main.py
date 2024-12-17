import SequentMicroInterface as sm
import time
import datetime
import CreateNewFile
import matplotlib.pyplot as plt
import JSONoperators as js

def main():
    
    plt.close('all')
    
    filename = CreateNewFile.MakeNewFile()
    dodisplaygraphs = js.ReadJSONConfig("RTD_options","showgraphs")
    entriestodisplay = js.ReadJSONConfig("RTD_options","entriestodisplay")
    

    while True:
        try:
            interval = int(input("Enter interval in seconds: "))
            assert interval > 0
            break
        except:
            print("Not a valid integer")



        
    if dodisplaygraphs == "True":
        
        temperaturelegend = []
        pressurelegend = []
        
        
        temperaturearrays=[]
        for i in js.ReadJSONConfig("RTD_options","currently_processed_ports"):
            temperaturearrays.append([])
            temperaturelegend.append([i])
        pressurearrays = []
        for i in range(8):
            pressurearrays.append([])
            pressurelegend.append([i+1])
        
        
        
        x_ax = []
        
        colorlist = ['r','g','b','c','m','y','k','tab:brown']
        
       
       
            
        
            
        
        tempfig = plt.figure()
        tempax = tempfig.add_subplot(111)
        tempfig.show()
        
        pressfig = plt.figure()
        pressax = pressfig.add_subplot(111)
        pressfig.show()
    
    
    while True:
        current_time = (datetime.datetime.now()).strftime("%Y-%h-%d %H:%M:%S")
        
        handle = open(filename,"a")
        handle.write(f"{current_time}\t\t")
        handle.close()
        
        temperaturelist = sm.RecordTemperatureToLog(filename)
        handle = open(filename,"a")
        handle.write(f"\t\t")
        handle.close()
        
        
        pressurelist = sm.RecordVoltageToLog(filename)
        handle = open(filename,"a")
        handle.write(f"\n")
        handle.close()
        
        if dodisplaygraphs == "True":
            
            
            
            for i in range(len(temperaturelist)):
                temperaturearrays[i].append(temperaturelist[i])
                if len(temperaturearrays[i]) > entriestodisplay:
                    void = (temperaturearrays[i]).pop(0)
            
            for i in range(len(pressurelist)):
                pressurearrays[i].append(pressurelist[i])
                if len(pressurearrays[i]) > entriestodisplay:
                    void = (pressurearrays[i]).pop(0)
            
            
            x_ax.append(datetime.datetime.now())
            
            if len(x_ax) > entriestodisplay:
                void = x_ax.pop(0)
                
                
            
            
            i = 0
            tempax.cla()
            tempax.set_title("Temperature (oC vs time)")
            for array in temperaturearrays:
                
                tempax.plot(x_ax,array,color=colorlist[i])
                
                i += 1
                
            j = 0
            pressax.cla()
            pressax.set_title("Pressure (kPa vs time)")
            for array in pressurearrays:
                pressax.plot(x_ax,array,color=colorlist[j])
                
                j += 1
            
            
            tempax.legend(temperaturelegend,loc=3)
            pressax.legend(pressurelegend,loc=3)
            
            
                
            tempfig.canvas.draw()
            pressfig.canvas.draw()
            
            
            
        
        time.sleep(interval)
        
        



main()

