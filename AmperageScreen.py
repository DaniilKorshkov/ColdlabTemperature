import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import JSONoperators as js
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter
import datetime as dt

def update_frame(i):

    entries_to_display = js.ReadJSONConfig("RTD_options","entriestodisplay")
    raw_time_array, temperature_arrays, pressure_arrays, amperage_arrays = js.ReadCSV(filename,entries_to_display)
    ampax.xaxis.set_major_formatter(DateFormatter('%H-%M-%S'))
    legend_dictionary = js.ReadJSONConfig("Dictionaries","Amp_dictionary")


    time_array = [dt.datetime.fromtimestamp(element) for element in raw_time_array]
   

    ampax.cla()
    #pressax.clear()

    ampax.set_title(f"Amperage vs time")
    colorlist = ['r','g','b','c','m','y','k','tab:brown']
    i = 0


    ampax.set_xlabel(f'Time')
    ampax.set_ylabel("Amperage")

    ampax.set_xscale('linear')
    ampax.set_yscale('linear')


    ampax.xaxis.grid(which='major', color='k', alpha=0.8, linestyle='--', linewidth=1)
    ampax.yaxis.grid(which='major', color='k', alpha=0.8, linestyle='--', linewidth=1)

    ampax.xaxis.grid(which='minor', color='k', alpha=0.5, linestyle=':', linewidth=0.75)
    ampax.yaxis.grid(which='minor', color='k', alpha=0.5, linestyle=':', linewidth=0.75)


    
    ampax.tick_params('x', labelrotation=90)
    
    amperagelegend = []


    for amperage_array_key in amperage_arrays:


       

        ampax.plot(time_array, amperage_arrays[amperage_array_key], color = colorlist[i])
        try:
            amperagelegend.append(legend_dictionary[amperage_array_key])
        except:
            amperagelegend.append(amperage_array_key)
        i += 1
    

    ampax.legend(amperagelegend,loc=3)



    #for pressure_array in pressure_arrays:
     #   pressax.plot(time_array, pressure_array)
    




def initiate_frame(input_filename):

    
    global filename
    filename = input_filename

    
    global ampfig
    ampfig = plt.figure()

    global ampax
    ampax = ampfig.add_subplot(111)








    ani = FuncAnimation(ampfig, update_frame, interval=1000)







def initiate():

    while True:
        input_filename = str(input("Enter filename: "))
        try:
            handle = open(input_filename,"r")
            handle.close
            break
        except:
            print("Invalid filename")

    
    initiate_frame(input_filename)

if __name__ == "__main__":
    initiate()
