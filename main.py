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
        
        
        
        x = 0
        x_ax = []
        
        colorlist = ['r','g','b','c','m','y','k','tab:brown']
        
       
       
            
        
            
        
        tempfig = plt.figure()
        tempax = tempfig.add_subplot(111)
        tempax.set_title("Temperature")
        tempfig.show()
        
        pressfig = plt.figure()
        pressax = pressfig.add_subplot(111)
        pressax.set_title("Pressure")
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
            
            for i in range(len(pressurelist)):
                pressurearrays[i].append(pressurelist[i])
            
            x = x+1
            x_ax.append(x)
            
            
            i = 0
        
            for array in temperaturearrays:
                tempax.plot(x_ax,array,color=colorlist[i])
                
                i += 1
                
            j = 0
            for array in pressurearrays:
                pressax.plot(x_ax,array,color=colorlist[j])
                
                j += 1
            
            
            tempax.legend(temperaturelegend)
            pressax.legend(pressurelegend)
            
            
                
            tempfig.canvas.draw()
            pressfig.canvas.draw()
            
        
        time.sleep(interval)
        
        



main()

