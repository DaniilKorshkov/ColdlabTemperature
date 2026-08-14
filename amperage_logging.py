import time
#import serial
import subprocess
import os
import serial

import math
import datetime
import json
import datetime
import serial.tools.list_ports
import usb
import CreateNewFile
import JSONoperators

#PORT = '/dev/ttyUSB0'  #"COM7"
#MKS_ADDRESS = "253"


def ReadFeed(PORT):
    #Logging.MakeLogEntry("Communication with arduino board initiated",log_name="USB_Log")

    #ports = serial.tools.list_ports.comports()
    #print(ports)


    filename = CreateNewFile.MakeNewFileArduino()

    ser = serial.Serial()
    ser.port = PORT
    ser.baudrate = 115200
    ser.timeout = 10

    

    

        

            
    try:
        ser.close()
    except:
        pass
        
    ser.open()




    while True:

        try:
            ret = ser.read_until(b"!END")
            ret = ret.decode("utf-8")
            ret = ret.replace("!START!", "").replace("!END", "")

            print(ret)
            
            tmp = ret.split("\n")
            tmp3 = []
            output = []
            for element in tmp:
                tmp2 = element.split(",")
                for element in tmp2:
                    tmp3.append(element)
            

            for element in tmp3:
                if element == "":
                    pass
                else:
                    output.append( ((element.strip("Dev[0] CURR: ")).strip("Dev[1] CURR:" )).strip("\r") )
            
            print(output)

            current_time = (datetime.datetime.now()).strftime("%Y-%h-%d %H:%M:%S")
        


            if len(output) == 8:
                log_handle = open(filename, "a")
                log_handle.write(f"{current_time}\t")
                for element in output:
                    log_handle.write(element)
                    log_handle.write("\t")
                log_handle.write("\n")
                log_handle.close()

        except:
            pass


    
    


    ser.close()



if __name__ == "__main__":
    address = JSONoperators.ReadJSONConfig("Technical","arduino_address")
    ReadFeed(address)
