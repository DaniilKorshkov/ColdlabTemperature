import numpy
import JSONoperators as js
import json

def main():

    channels = []
    pressure_arrays_dictionary = {}
    voltage_arrays_dictionary = {}

    with open("CalibrationSheet.csv", "r") as handle:
        for line in handle:
            if "CH" in line:
                splitline = line.split("\t")
                for element in splitline:
                    if not element.strip("\n") in channels:
                        channels.append(element.strip("\n"))
            
            else:
                channel_counter = 0
                splitline = line.split("\t")
                
                try:
                    pressure_arrays_dictionary[channels[channel_counter]].append(float(splitline[channel_counter]  ))
                except:
                    pressure_arrays_dictionary[channels[channel_counter]] = []
                    pressure_arrays_dictionary[channels[channel_counter]].append(float(splitline[channel_counter]  ))

                try:
                    voltage_arrays_dictionary[channels[channel_counter]].append(float(splitline[channel_counter+1]  ))
                except:
                    voltage_arrays_dictionary[channels[channel_counter]] = []
                    voltage_arrays_dictionary[channels[channel_counter]].append(float(splitline[channel_counter+1]  ))
                

                channel_counter+=1


    print(channels)
    print(pressure_arrays_dictionary)
    print(voltage_arrays_dictionary)


    old_calibration_cfg = js.ReadJSONConfig("Polynomes")


    for key in channels:
        calibration_coefficients = numpy.polyfit(voltage_arrays_dictionary[key], pressure_arrays_dictionary[key],1)
        (old_calibration_cfg["polynomes"])[int(key.strip("CH"))] = [float(calibration_coefficients[0]),  float(calibration_coefficients[1])]

    
    new_string = json.dumps(old_calibration_cfg)
    js.EditJSONConfig("Polynomes",new_string)
    


main()