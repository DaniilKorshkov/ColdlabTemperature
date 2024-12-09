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
        ret = ret+"\t"+str(ReadTemperature(int(sensor_number)))
    ret = ret.strip("\t")
    return ret
        

def RecordTemperatureToLog(filename):
    current_time = datetime.datetime.now().strftime("%Y-%h-%d %H:%M:%S")
    current_temp = ReadAllTemperatures()
    
    handle = open(filename,"a")
    handle.write(f"{current_temp}")
    handle.close()
    
    

def ReadVoltage(board_id, sensor_number):
    ret = str(subprocess.run([f"megaind", f"{board_id}", f"uoutrd", f"{sensor_number}"], capture_output=True).stdout)
    ret = float(ret[2:(len(ret)-3)])
    
    return ret
    
    
def ReadAllVoltages():
    ret = ""
    for i in range(2):
        for j in range(4):
                ret = ret+"\t"+str(ReadVoltage(i*4,(j+1)))
    ret = ret.strip("\t")
    return ret


def RecordVoltageToLog(filename):
    current_volt = ReadAllVoltages()
    handle = open(filename,"a")
    handle.write(f"{current_volt}")
    handle.close()
    


