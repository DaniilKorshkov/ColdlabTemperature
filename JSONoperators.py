import json
import os


def ReadJSONConfig(linename,entryname,config="MainConfig"): #function to read a specific entry from specified line in config
    handle = open(config, "r")
    for line in handle:

        if line == "" or line == "\n" or line[0] == "#" or line == None:
            continue

        dict_line = json.loads(line)
        if dict_line["class"] == linename:
            entry = dict_line[entryname]
            break
    handle.close()

    if entry == None:
        raise LookupError(f"{entryname} entry was not found in {linename} line in {config} config")

    return entry






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
