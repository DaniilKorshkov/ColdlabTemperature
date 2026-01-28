import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import JSONoperators as js
import matplotlib.ticker as ticker

def update_frame(i):
    time_array, temperature_arrays, pressure_arrays = js.ReadCSV('b',1000)

    tempax.clear()
    #pressax.clear()

    tempax.set_title(f"Temperature (oC vs time)")
    colorlist = ['r','g','b','c','m','y','k','tab:brown']
    i = 0


    tempax.set_xlabel(f'Time')
    tempax.set_ylabel("Temperature oC")
    #tempax.xaxis.grid(which='major', color='k', alpha=0.8, linestyle='--', linewidth=1)
    #tempax.yaxis.grid(which='major', color='k', alpha=0.8, linestyle='--', linewidth=1)

    #tempax.xaxis.grid(which='minor', color='k', alpha=0.5, linestyle=':', linewidth=0.75)
    #tempax.yaxis.grid(which='minor', color='k', alpha=0.5, linestyle=':', linewidth=0.75)


    tempax.xaxis.set_major_locator(ticker.MaxNLocator(5))
    tempax.yaxis.set_major_locator(ticker.MaxNLocator(5))
    tempax.tick_params('x', labelrotation=90)
    
    temperaturelegend = []


    for temperature_array_key in temperature_arrays:
        tempax.plot(time_array, temperature_arrays[temperature_array_key], color = colorlist[i])
        temperaturelegend.append(temperature_array_key)
        i += 1
    

    tempax.legend(temperaturelegend,loc=3)



    #for pressure_array in pressure_arrays:
     #   pressax.plot(time_array, pressure_array)
    




def initiate_frame(filename):
    
    global tempfig
    tempfig = plt.figure()
    #pressfig = plt.figure()

    global tempax
    tempax = tempfig.add_subplot(111)
    #pressax = pressfig.add_subplot(111)








    ani = FuncAnimation(tempfig, update_frame, interval=1000)
    plt.show()


if __name__ == "__main__":
    initiate_frame('b')