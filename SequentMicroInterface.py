import subprocess
import JSONoperators as js
import datetime



def ReadTemperature(sensor_number):
    ret = str(subprocess.run([f"rtd", f"0", "readpoly5", f"{sensor_number}"], cwd="/home/pi/rtd-rpi", capture_output=True).stdout)
    ret = float(ret[2:(len(ret)-3)])
    return ret
    
    
def ReadAllTemperatures():
    ret = ""
    temperaturearray = []
    for sensor_number in js.ReadJSONConfig("RTD_options","currently_processed_ports"):
        temperature = ReadTemperature(int(sensor_number))
        temperaturearray.append(float(temperature))
        ret = ret+"\t"+str(temperature)
    ret = ret.strip("\t")
    return ret, temperaturearray
        

def RecordTemperatureToLog(filename):
    current_time = datetime.datetime.now().strftime("%Y-%h-%d %H:%M:%S")
    current_temp, temperaturearray = ReadAllTemperatures()
    
    handle = open(filename,"a")
    handle.write(f"{current_temp}")
    handle.close()
    
    return temperaturearray

def ReadVoltage(board_id, sensor_number):
    ret = str(subprocess.run([f"megaind", f"{board_id}", f"uoutrd", f"{sensor_number}"], capture_output=True).stdout)
    ret = float(ret[2:(len(ret)-3)])
    
    return ret
    
    
def ReadAllVoltages():
    ret = ""
    pressurearray = []
    polynomes = js.ReadJSONConfig("Polynomes","polynomes")
    for i in range(2):
        for j in range(4):
                voltage = ReadVoltage(i*4,(j+1))
                pressure = ((polynomes[i*4+j])[0])*voltage + ((polynomes[i*4+j])[1])
                pressurearray.append(pressure)
                ret = ret+"\t"+str(pressure)
                
    ret = ret.strip("\t")
    return ret, pressurearray


def RecordVoltageToLog(filename):
    current_volt, pressurearray = ReadAllVoltages()
    handle = open(filename,"a")
    handle.write(f"{current_volt}")
    handle.close()
    return pressurearray
    


