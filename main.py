import SequentMicroInterface as sm
import time
import datetime
import CreateNewFile

def main():
    
    filename = CreateNewFile.MakeNewFile()
    

    while True:
        try:
            interval = int(input("Enter interval in seconds: "))
            assert interval > 0
            break
        except:
            print("Not a valid integer")



    while True:
        current_time = (datetime.datetime.now()).strftime("%Y-%h-%d %H:%M:%S")
        
        handle = open(filename,"a")
        handle.write(f"{current_time}\t\t")
        handle.close()
        
        sm.RecordTemperatureToLog(filename)
        handle = open(filename,"a")
        handle.write(f"\t\t")
        handle.close()
        sm.RecordVoltageToLog(filename)
        handle = open(filename,"a")
        handle.write(f"\n")
        handle.close()
        time.sleep(interval)



main()

