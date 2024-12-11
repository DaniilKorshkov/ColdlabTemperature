import SequentMicroInterface as sm
import time
import datetime
import CreateNewFile
import matplotlib.pyplot as plt
import JSONoperators as js

def main():
    
    filename = CreateNewFile.MakeNewFile()
    

    while True:
        try:
            interval = int(input("Enter interval in seconds: "))
            assert interval > 0
            break
        except:
            print("Not a valid integer")


    temperaturearrays=[]
    for i in js.ReadJSONConfig("RTD_options","currently_processed_ports"):
        temperaturearrays.append([])
    pressurearrays = []
    for i in range(8):
        pressurearrays.append([])
        
    x = 0
    x_ax = []
        
    
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
        
        for i in range(len(temperaturelist)):
            temperaturearrays[i].append(temperaturelist[i])
        
        pressurelist = sm.RecordVoltageToLog(filename)
        handle = open(filename,"a")
        handle.write(f"\n")
        handle.close()
        
        for i in range(len(pressurelist)):
            pressurearrays[i].append(pressurelist[i])
        
        x = x+1
        x_ax.append(x)
        
        for array in temperaturearrays:
            tempax.plot(x_ax,array,color="b")
            
       
        for array in pressurearrays:
            pressax.plot(x_ax,array,color="b")
            
            
        tempfig.canvas.draw()
        pressfig.canvas.draw()
        
        
        time.sleep(interval)
        
        



main()

