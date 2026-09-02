import json
import os
import time
import datetime


def ReadJSONConfig(linename,entryname=None,config="MainConfig",DefaultMainConfig="DefaultMainConfig"): #function to read a specific entry from specified line in config
    entry = None
    handle = open(config, "r")
    for line in handle:

        if line == "" or line == "\n" or line[0] == "#" or line == None:
            continue

        dict_line = json.loads(line)
        if dict_line["class"] == linename:
            if entryname == None:
                entry = dict_line
                break
            else:
                entry = dict_line[entryname]
                break
    handle.close()

    if entry ==  None:

        handle = open(DefaultMainConfig, "r")
        for line in handle:

            if line == "" or line == "\n" or line[0] == "#" or line == None:
                continue

            dict_line = json.loads(line)
            if dict_line["class"] == linename:
                if entryname == None:
                    entry = dict_line
                    break
                else:
                    entry = dict_line[entryname]
                    break
        handle.close()
    
    if entry == None:
        #NotifyUser("0015", f"Default Config Entry Missing: {linename}, {entryname} (0015)",True)

        #try:
         #   FillingActClose()
        #except:
         #   NotifyUser("0014", f"Default Config Entry Missing; and filling actuator is not responsive (0014)",True)

        raise LookupError(f"{entryname} entry was not found in {linename} line in {config} config")
        

    return entry




def EditJSONConfig(linename,new_string,MainConfig="MainConfig"):
        handle = open(MainConfig,"r")
        newconfig = []
        for line in handle:
                    try:
                        dictline = json.loads(line)
                        if dictline["class"] == linename:
                            newconfig.append((new_string.strip("\n"))+"\n")
                        else:
                            newconfig.append(line)
                    except:
                        pass
        handle.close()

        handle = open(MainConfig,"w")
        for line in newconfig:
                    handle.write(line)
        handle.close()







def MergeJSONConfigs(MainConfig="MainConfig",DefaultMainConfig="DefaultMainConfig"):
    MergedConfig = dict()
    LinesList = []

    #print(123)

    try:
        handle = open(MainConfig,"r")
        MainConfigExist = True
    except:
        MainConfigExist = False

    if MainConfigExist:

        handle = open(MainConfig,"r")
        for line in handle:
            dictline = json.loads(line)
            MergedConfig[dictline["class"]] = dictline
            LinesList.append(dictline["class"])
        handle.close()


        handle = open(DefaultMainConfig,"r")
        for line in handle:
            dictline = json.loads(line)
            if not (dictline["class"] in LinesList):
                MergedConfig[dictline["class"]] = dictline
            else:
                for key in MergedConfig:
                    if (MergedConfig[key])["class"] == dictline["class"]:
                        for entry_key in dictline:
                            try:
                                void = (MergedConfig[key])[entry_key]
                            except:
                                (MergedConfig[key])[entry_key] = dictline[entry_key]


        handle.close()



        handle = open(MainConfig,"w")
        for key in MergedConfig:
            handle.write(  json.dumps(MergedConfig[key])  )
            handle.write("\n")
        handle.close()

    else:
        NewConfig = []
        handle = open(DefaultMainConfig, "r")
        for line in handle:
            NewConfig.append(line)
        handle.close()

        handle = open(MainConfig, "w")
        for line in NewConfig:
            handle.write(line)
        handle.close()







def ReadCSV(filename, entries_to_display):
    handle = open(filename,"r")


    temperature_sensors_list = []
    pressure_sensors_list = []
    amperage_sensors_list = []
    vacuum_sensors_list = []
    dm_sensors_list = []


    time_array = []
    temperature_arrays = {}
    pressure_arrays = {}
    amperage_arrays = {}
    vacuum_arrays = {}
    dm_arrays = {}




    for line in handle:
        if "Current time" in line:    #handle first line

            splitline = line.split('\t')
            

            for element in splitline:
                if "Temp." in element:
                    temperature_sensors_list.append(element)
                    temperature_arrays[element] = []
                if "Press." in element:
                    pressure_sensors_list.append(element)
                    pressure_arrays[element] = []
                if "Amp." in element:
                    amperage_sensors_list.append(element)
                    amperage_arrays[element] = []
                if "Vac." in element:
                    vacuum_sensors_list.append(element)
                    vacuum_arrays[element] = []
                if "DM." in element:
                    dm_sensors_list.append(element)
                    dm_arrays[element] = []
            

        
        elif line == "" or line == "\n":
            pass
            



        else:  #handle other lines

    

            splitline = line.split('\t')

            
            utc_time = (datetime.datetime.fromtimestamp(time.mktime(time.strptime(splitline[0],"%Y-%b-%d %H:%M:%S")))).timestamp()
    

            time_array.append(utc_time)
            if len(time_array) > entries_to_display:
                    time_array.pop(0)

            
            i = 1

            for sensor in temperature_sensors_list:

                while splitline[i] == "" or splitline[i] == "\n" or splitline[i] == "\t":
                    i += 1


                temperature_arrays[sensor].append(float(splitline[i]))
                i += 1


                if len(temperature_arrays[sensor]) > entries_to_display:
                    temperature_arrays[sensor].pop(0)


            for sensor in pressure_sensors_list:

                
                while splitline[i] == "" or splitline[i] == "\n" or splitline[i] == "\t":
                    i += 1



                pressure_arrays[sensor].append(float(splitline[i]))
                i += 1

                if len(pressure_arrays[sensor]) > entries_to_display:
                    pressure_arrays[sensor].pop(0)

            for sensor in amperage_sensors_list:

                
                while splitline[i] == "" or splitline[i] == "\n" or splitline[i] == "\t":
                    i += 1



                amperage_arrays[sensor].append(float(splitline[i]))
                i += 1

                if len(amperage_arrays[sensor]) > entries_to_display:
                    amperage_arrays[sensor].pop(0)

            for sensor in dm_sensors_list:

                
                while splitline[i] == "" or splitline[i] == "\n" or splitline[i] == "\t":
                    i += 1



                dm_arrays[sensor].append(float(splitline[i]))
                i += 1

                if len(dm_arrays[sensor]) > entries_to_display:
                    dm_arrays[sensor].pop(0)
            

            for sensor in vacuum_sensors_list:

                
                while splitline[i] == "" or splitline[i] == "\n" or splitline[i] == "\t":
                    i += 1



                vacuum_arrays[sensor].append(float(splitline[i]))
                i += 1

                if len(vacuum_arrays[sensor]) > entries_to_display:
                    vacuum_arrays[sensor].pop(0)



    handle.close()


    return time_array, temperature_arrays, pressure_arrays, amperage_arrays, dm_arrays, vacuum_arrays




def ReadCSVAmperage(filename, entries_to_display):
    handle = open(filename,"r")


    channels_list = []
    


    time_array = []
    amperage_arrays = {}

    channels_count = 0 
    



    for line in handle:
        if "Current time" in line:    #handle first line

            splitline = line.split('\t')
            

            for element in splitline:
                if len(element) == 4:
                
                    channels_list.append(element)
                    channels_count += 1
                
            

        
        elif line == "" or line == "\n":
            pass
            



        else:  #handle other lines

    

            splitline = line.split('\t')

            
            utc_time = (datetime.datetime.fromtimestamp(time.mktime(time.strptime(splitline[0],"%Y-%b-%d %H:%M:%S")))).timestamp()
    

            time_array.append(utc_time)
            if len(time_array) > entries_to_display:
                    time_array.pop(0)

            
            i = 1

            for sensor in channels_list:

                while splitline[i] == "" or splitline[i] == "\n" or splitline[i] == "\t":
                    i += 1


                amperage_arrays[sensor].append(float(splitline[i]))
                i += 1


                if len(amperage_arrays[sensor]) > entries_to_display:
                    temperature_arrays[sensor].pop(0)


            

    handle.close()


    return time_array, amperage_arrays



if __name__ == "__main__":
        print(123)
        print(ReadCSV("b",100))


    
