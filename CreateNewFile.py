import subprocess
import JSONoperators as js

def MakeNewFile():
    
    current_directory = js.ReadJSONConfig("Technical","current_directory")

    while True:
        filename = str(input("Enter filename: "))
        type = str(subprocess.run([f"file", f"{filename}"], cwd=current_directory, capture_output=True).stdout)
        type = type[(len(filename)+4):(len(type)-3)]


        if (type == f"cannot open `{filename}' (No such file or directory)" or type == "empty" or type == "ASCII text") and filename != "MainConfig":
            break
        else:
            print("Invalid filename")
        
    subprocess.run([f"touch", f"{filename}"], cwd=current_directory)
    if type == f"cannot open `{filename}' (No such file or directory)":
        
        handle = open(filename,"a")
        handle.write(f"Current time \t\t")
        
        for sensor_number in js.ReadJSONConfig("RTD_options","currently_processed_temperature_ports"):
            handle.write(f"Temp. port {sensor_number}\t")
            
        handle.write("\t")

        for sensor_number in js.ReadJSONConfig("RTD_options", "currently_processed_voltage_ports"):
            handle.write(f"Press. port {sensor_number}\t")
        
        handle.write(f"\n\n")
        
        handle.close()
        

    return filename

