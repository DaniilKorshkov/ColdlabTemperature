import subprocess
import JSONoperators as js
import datetime



def ReadTemperature(sensor_number):
    ret = str(subprocess.run([f"rtd", f"0", "readpoly5", f"{sensor_number}"], cwd="/home/pi/rtd-rpi", capture_output=True).stdout)
    ret = float(ret[2:(len(ret)-3)])
    return ret
    
    
def ReadAllTemperatures():
    ret = ""
    for sensor_number in js.ReadJSONConfig("RTD_options","currently_processed_ports"):
        ret = ret+" "+str(ReadTemperature(int(sensor_number)))+"oC"
    return ret
        

def RecordTemperatureToLog():
    current_time = datetime.datetime.now().strftime("%Y-%h-%d %H:%M:%S")
    current_temp = ReadAllTemperatures()
    
    handle = open("MainLog","a")
    handle.write(f"{current_time}: {current_temp}\n")
    handle.close()


RecordTemperatureToLog()