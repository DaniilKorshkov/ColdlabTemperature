import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import JSONoperators as js
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter
import datetime as dt

def update_frame(i):

    entries_to_display = js.ReadJSONConfig("RTD_options","entriestodisplay")
    raw_time_array, temperature_arrays, pressure_arrays = js.ReadCSV(filename,entries_to_display)
    pressax.xaxis.set_major_formatter(DateFormatter('%H-%M-%S'))
    legend_dictionary = js.ReadJSONConfig("Dictionaries","Press_dictionary")


    time_array = [dt.datetime.fromtimestamp(element) for element in raw_time_array]
   

    pressax.cla()
    #pressax.clear()

    pressax.set_title(f"Pressure (torr?? vs time)")
    colorlist = ['r','g','b','c','m','y','k','tab:brown']
    i = 0


    pressax.set_xlabel(f'Time')
    pressax.set_ylabel("Pressure torr")

    pressax.set_xscale('linear')
    pressax.set_yscale('linear')


    pressax.xaxis.grid(which='major', color='k', alpha=0.8, linestyle='--', linewidth=1)
    pressax.yaxis.grid(which='major', color='k', alpha=0.8, linestyle='--', linewidth=1)

    pressax.xaxis.grid(which='minor', color='k', alpha=0.5, linestyle=':', linewidth=0.75)
    pressax.yaxis.grid(which='minor', color='k', alpha=0.5, linestyle=':', linewidth=0.75)


    
    pressax.tick_params('x', labelrotation=90)
    
    pressurelegend = []


    for pressure_array_key in pressure_arrays:


       

        pressax.plot(time_array, pressure_arrays[pressure_array_key], color = colorlist[i])
        try:
            pressurelegend.append(legend_dictionary[pressure_array_key])
        except:
            pressurelegend.append(pressure_array_key)
        i += 1
    

    pressax.legend(pressurelegend,loc=3)



    #for pressure_array in pressure_arrays:
     #   pressax.plot(time_array, pressure_array)
    




def initiate_frame():

    while True:
        input_filename = str(input("Enter filename: "))
        try:
            handle = open(input_filename,"r")
            handle.close
            break
        except:
            print("Invalid filename")

    
    global filename
    filename = input_filename

    
    global pressfig
    pressfig = plt.figure()
    #pressfig = plt.figure()

    global pressax
    pressax = pressfig.add_subplot(111)
    #pressax = pressfig.add_subplot(111)








    ani = FuncAnimation(tempfig, update_frame, interval=1000)
    plt.show()


if __name__ == "__main__":
    initiate_frame()
