import SequentMicroInterface as sm
import time
import datetime
import CreateNewFile
import matplotlib.pyplot as plt
import serial

import JSONoperators as js
import json
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


def vacuum_update_frame(i):

    entries_to_display = js.ReadJSONConfig("RTD_options","entriestodisplay")
    raw_time_array, temperature_arrays, pressure_arrays, amperage_arrays, vacuum_arrays = js.ReadCSV(filename,entries_to_display)
    vacax.xaxis.set_major_formatter(DateFormatter('%H-%M-%S'))
    legend_dictionary = js.ReadJSONConfig("Dictionaries","Vac_dictionary")


    time_array = [dt.datetime.fromtimestamp(element) for element in raw_time_array]
   

    vacax.cla()
    #pressax.clear()

    vacax.set_title(f"Vacuum (Pa vs time)")
    colorlist = ['r','g','b','c','m','y','k','tab:brown']
    i = 0


    vacax.set_xlabel(f'Time')
    vacax.set_ylabel("Pressure (Pa)")

    vacax.set_xscale('linear')
    vacax.set_yscale('linear')


    vacax.xaxis.grid(which='major', color='k', alpha=0.8, linestyle='--', linewidth=1)
    vacax.yaxis.grid(which='major', color='k', alpha=0.8, linestyle='--', linewidth=1)

    vacax.xaxis.grid(which='minor', color='k', alpha=0.5, linestyle=':', linewidth=0.75)
    vacax.yaxis.grid(which='minor', color='k', alpha=0.5, linestyle=':', linewidth=0.75)


    
    vacax.tick_params('x', labelrotation=90)
    
    vacuumlegend = []


    for vacuum_array_key in vacuum_arrays:


       

        vacax.plot(time_array, vacuum_arrays[vacuum_array_key], color = colorlist[i])
        try:
            if len(vacuum_arrays[vacuum_array_key]) > 0:
                vacuumlegend.append(f"{legend_dictionary[vacuum_array_key]}: {vacuum_arrays[vacuum_array_key][-1]} Pa")
            else:
                vacuumlegend.append(legend_dictionary[vacuum_array_key])
        except:
            if len(vacuum_arrays[vacuum_array_key]) > 0:
                vacuumlegend.append(f"{vacuum_array_key}: {vacuum_arrays[vacuum_array_key][-1]} Pa")
            else:
                vacuumlegend.append(vacuum_array_key)
        i += 1
    

    vacax.legend(vacuumlegend,loc=3)





def temperature_update_frame(i):

    entries_to_display = js.ReadJSONConfig("RTD_options","entriestodisplay")
    raw_time_array, temperature_arrays, pressure_arrays, amperage_arrays, vacuum_arrays = js.ReadCSV(filename,entries_to_display)
    tempax.xaxis.set_major_formatter(DateFormatter('%H-%M-%S'))
    legend_dictionary = js.ReadJSONConfig("Dictionaries","RTD_dictionary")


    time_array = [dt.datetime.fromtimestamp(element) for element in raw_time_array]
   

    tempax.cla()
    #pressax.clear()

    tempax.set_title(f"Temperature (°C vs time)")
    colorlist = ['r','g','b','c','m','y','k','tab:brown']
    i = 0


    tempax.set_xlabel(f'Time')
    tempax.set_ylabel("Temperature (°C)")

    tempax.set_xscale('linear')
    tempax.set_yscale('linear')


    tempax.xaxis.grid(which='major', color='k', alpha=0.8, linestyle='--', linewidth=1)
    tempax.yaxis.grid(which='major', color='k', alpha=0.8, linestyle='--', linewidth=1)

    tempax.xaxis.grid(which='minor', color='k', alpha=0.5, linestyle=':', linewidth=0.75)
    tempax.yaxis.grid(which='minor', color='k', alpha=0.5, linestyle=':', linewidth=0.75)


    
    tempax.tick_params('x', labelrotation=90)
    
    temperaturelegend = []


    for temperature_array_key in temperature_arrays:


       

        tempax.plot(time_array, temperature_arrays[temperature_array_key], color = colorlist[i])
        try:
            if len(temperature_arrays[temperature_array_key]) > 0:
                temperaturelegend.append(f"{legend_dictionary[temperature_array_key]}: {temperature_arrays[temperature_array_key][-1]}°C")
            else:
                temperaturelegend.append(legend_dictionary[temperature_array_key])
        except:
            if len(temperature_arrays[temperature_array_key]) > 0:
                temperaturelegend.append(f"{temperature_array_key}: {temperature_arrays[temperature_array_key][-1]}°C")
            else:
                temperaturelegend.append(temperature_array_key)
        i += 1
    

    tempax.legend(temperaturelegend,loc=3)

def amperage_update_frame(i):

    entries_to_display = js.ReadJSONConfig("RTD_options","entriestodisplay")
    raw_time_array, temperature_arrays, pressure_arrays, amperage_arrays, vacuum_arrays = js.ReadCSV(filename,entries_to_display)
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
            if len(amperage_arrays[amperage_array_key]) > 0:
                amperagelegend.append(f"{legend_dictionary[amperage_array_key]}: {amperage_arrays[amperage_array_key][-1]} A")
            else:
                amperagelegend.append(f"{legend_dictionary[amperage_array_key]}")
        except:
            if len(amperage_arrays[amperage_array_key]) > 0:
                amperagelegend.append(f"{amperage_array_key}: {amperage_arrays[amperage_array_key][-1]} A")
            else:
                amperagelegend.append(f"{amperage_array_key}")
        i += 1
    

    ampax.legend(amperagelegend,loc=3)


def pressure_update_frame(i):

    entries_to_display = js.ReadJSONConfig("RTD_options","entriestodisplay")
    raw_time_array, temperature_arrays, pressure_arrays, amperage_arrays, vacuum_arrays = js.ReadCSV(filename,entries_to_display)
    pressax.xaxis.set_major_formatter(DateFormatter('%H-%M-%S'))
    legend_dictionary = js.ReadJSONConfig("Dictionaries","Press_dictionary")


    time_array = [dt.datetime.fromtimestamp(element) for element in raw_time_array]
   

    pressax.cla()
    #pressax.clear()

    pressax.set_title(f"Pressure (torr vs time)")
    colorlist = ['r','g','b','c','m','y','k','tab:brown']
    i = 0


    pressax.set_xlabel(f'Time')
    pressax.set_ylabel("Pressure (torr)")

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
            if len(pressure_arrays[pressure_array_key]) > 0:
                pressurelegend.append(f"{legend_dictionary[pressure_array_key]}: {pressure_arrays[pressure_array_key][-1]} torr")
            else:
                pressurelegend.append(legend_dictionary[pressure_array_key])
        except:
            if len(pressure_arrays[pressure_array_key]) > 0:
                temperaturelegend.append(f"{temperature_array_key}: {temperature_arrays[temperature_array_key][-1]} torr")
            else:
                pressurelegend.append(pressure_array_key)
        i += 1
    

    pressax.legend(pressurelegend,loc=3)



def initiate_frame():

    

    if do_temperature:
        global tempfig, tempax, tempani
        tempfig = plt.figure()
        tempax = tempfig.add_subplot(111)
        tempani = FuncAnimation(tempfig, temperature_update_frame, interval=1000)

    if do_pressure:
        global pressfig, pressax, pressani
        pressfig = plt.figure()
        pressax = pressfig.add_subplot(111)
        pressani = FuncAnimation(pressfig, pressure_update_frame, interval=1000)

    if do_amperage:
        global ampfig, ampax, ampani
        ampfig = plt.figure()
        ampax = ampfig.add_subplot(111)
        ampani = FuncAnimation(ampfig, amperage_update_frame, interval=1000)

    if do_vacuum:
        global vacfig, vacax, vacani
        vacfig = plt.figure()
        vacax = vacfig.add_subplot(111)
        vacani = FuncAnimation(vacfig, vacuum_update_frame, interval=1000)

    plt.show(block=False)


def modify_config_from_preset():
    print("Select settings preset: ")
    i = 1
    presets_list = js.ReadJSONConfig("Presets","Presets_list")
    for element in presets_list:
        print(f"{i}) {element["preset_name"]}")
        i+=1

    while True:
        try:
            selection = int(input("Enter preset number: "))
            assert selection > 0
            assert selection < (len(presets_list) + 1)
            print(f"Option {selection} selected")
            break
        except:
            print("Invalid selection")


    old_line_json = js.ReadJSONConfig("RTD_options")

    old_line_json["currently_processed_temperature_ports"] = (presets_list[selection-1])["currently_processed_temperature_ports"]
    old_line_json["currently_processed_voltage_ports"] = (presets_list[selection-1])["currently_processed_voltage_ports"]
    old_line_json["currently_processed_amperage_ports"] = (presets_list[selection-1])["currently_processed_amperage_ports"]
    old_line_json["currently_processed_vacuum_ports"] = (presets_list[selection-1])["currently_processed_vacuum_ports"]


    new_line = json.dumps(old_line_json)

    js.EditJSONConfig("RTD_options", new_line)



def main():



    #------------------------------ initiation --------------------------------------------

    js.MergeJSONConfigs()
    modify_config_from_preset()

    global do_amperage, do_pressure, do_temperature, do_vacuum


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

    currently_processed_vacuum_ports = js.ReadJSONConfig("RTD_options","currently_processed_vacuum_ports")
    if len(currently_processed_vacuum_ports) > 0:
        do_vacuum = True
    else:
        do_vacuum = False

    assert (do_amperage or do_pressure or do_temperature or do_vacuum)

    while True:
        inputline = str(input("Display graphs(y/n): "))
        if inputline.lower()[0] == "y":
            display_graphs = True
            break
        elif inputline.lower()[0] == "n":
            display_graphs = False
            break
        else:
            print("Invalid input")



    

    atexit.register(exit_handler)
    signal.signal(signal.SIGINT, kill_handler)
    signal.signal(signal.SIGTERM, kill_handler)

    
    global filename




    while True:
        filename = CreateNewFile.MakeNewFile()
        
        with open(filename,"r") as file_handle:
            for line in file_handle:
                first_line = line
                break

# ---------------- verify that same data poins are logged ---------------------
        checkstring = "Current time \t\t"
        for sensor_number in js.ReadJSONConfig("RTD_options","currently_processed_temperature_ports"):
            checkstring+=f"Temp. port {sensor_number}\t"
            
        if do_temperature:
            checkstring+=("\t")

        for sensor_number in js.ReadJSONConfig("RTD_options", "currently_processed_voltage_ports"):
            checkstring+=f"Press. port {sensor_number}\t"
        
        if do_pressure:
            checkstring+=("\t")

        for sensor_number in js.ReadJSONConfig("RTD_options", "currently_processed_amperage_ports"):
            checkstring+=f"Amp. port {sensor_number}\t"

        if do_amperage:
            checkstring+=("\t")

        for sensor_number in js.ReadJSONConfig("RTD_options", "currently_processed_vacuum_ports"):
            checkstring+=f"Vac. port {sensor_number}\t"
        
        checkstring+="\n"

        
        if first_line == checkstring:
            break
        else:
            print("Different preset logged into this file")


    if do_amperage:

       
        arduino_found = False
        for i in range(100):
            if not arduino_found:
                try:
                    PORT = f"/dev/ttyACM{i}"
                    ser = serial.Serial()
                    ser.port = PORT
                    ser.baudrate = 115200
                    ser.timeout = 10

                    try:
                        ser.close()
                    except:
                        pass
                        
                    ser.open()
                    arduino_found = True
                    break
                except:
                    pass
        
        if not arduino_found:
            raise Exception("Arduino not found")

    
    if do_vacuum:

        vac_found = False
        for i in range(100):
            if not vac_found_found:
                try:
                    VAC_PORT = f"/dev/ttyUSB{i}"

                    vac_ser = serial.Serial()
                    vac_ser.port = VAC_PORT
                    vac_ser.baudrate = 9600
                    vac_ser.timeout = 10

                    try:
                        vac_ser.close()
                    except:
                        pass
                        
                    vac_ser.open()

                    vac_found = True
                    break
                except:
                    pass
        
        if not vac_found:
            raise Exception("Vacuum controller not found")
    
  

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

        
        

        
        if do_vacuum:

            ret = vac_ser.readline().decode("utf-8").strip()
            

            print(f"Vacuum reading {ret}")
            
            
            vacuum_output = []

            tmp = ret.split(",")

            try:
                for i in range(6):
                    vacuum_output.append(tmp[(2*i + 1)])
            
            except:
                vacuum_output = []
           

        else:
            vacuum_output = []
        

        #-------------------------- Appending log file --------------------------------------

        if (datetime.datetime.now().timestamp() > interval + last_cycle_time) and ( (not do_amperage) or ( do_amperage and len(amperage_output) == 8)) and ( (not do_vacuum) or ( do_vacuum and len(vacuum_output) == 6)  ):


            current_time = (datetime.datetime.now()).strftime("%Y-%h-%d %H:%M:%S")

            if do_temperature:
                void, temperaturelist = sm.ReadAllTemperatures()
            else:
                temperaturelist = []

            if do_pressure:
                void, pressurelist = sm.ReadAllVoltages()
            else:
                pressurelist = []
        

            handle = open(filename, "a")
            handle.write(f"{current_time}\t\t")
            for element in temperaturelist:
                handle.write(f"{element}\t")
            if do_temperature:
                handle.write("\t")
            for element in pressurelist:
                handle.write(f"{element}\t")
            if do_pressure:
                handle.write("\t")

            i = 1
            for element in amperage_output:
                if i in currently_processed_amperage_ports:
                    handle.write(f"{element}\t")

                i+=1
            if do_amperage:
                handle.write("\t")

            i = 1
            for element in vacuum_output:
                if i in currently_processed_vacuum_ports:
                    handle.write(f"{element}\t")

                i+=1 
                        
            handle.write("\n")
            handle.close()

            
            
            

            last_cycle_time = datetime.datetime.now().timestamp()

        
        plt.pause(0.01)
        
        
    
        
        
def exit_handler():
    plt.close('all')
    try:
        ser.close()
    except:
        pass

    try:
        vac_ser.close()
    except:
        pass    

def kill_handler(*args):
    sys.exit(0)
    try:
        ser.close()
    except:
        pass

    try:
        vac_serser.close()
    except:
        pass

if __name__ == "__main__":
    main()

