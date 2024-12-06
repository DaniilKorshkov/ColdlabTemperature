import SequentMicroInterface as sm
import time
import datetime

def main():

    while True:
        try:
            interval = int(input("Enter interval in seconds: "))
            assert interval > 0
            break
        except:
            print("Not a valid integer")



    while True:
        current_time = (datetime.datetime.now()).strftime("%Y-%h-%d %H:%M:%S")
        
        handle = open("MainLog","a")
        handle.write(f"{current_time}\t\t")
        handle.close()
        
        sm.RecordTemperatureToLog()
        handle = open("MainLog","a")
        handle.write(f"\t\t")
        handle.close()
        sm.RecordVoltageToLog()
        handle = open("MainLog","a")
        handle.write(f"\n")
        handle.close()
        time.sleep(interval)



main()

