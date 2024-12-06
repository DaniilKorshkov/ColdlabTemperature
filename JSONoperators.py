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
