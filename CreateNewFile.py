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

        for sensor_number in js.ReadJSONConfig("RTD_options", "currently_processed_amperage_ports"):
            handle.write(f"Amp. port {sensor_number}\t")
        
        handle.write(f"\n")
        
        handle.close()
        

    return filename




def WriteFirstLineInNewFileArduino(path):
    with open(path,"a") as handle:
        handle.write(f"Current time\t")
        handle.write(f"P0CH1\tP0CH2\tP0CH3\tP0CH4\tP1CH1\tP1CH2\tP1CH3\tP1CH4\n")
        
            
        
        handle.write(f"\n")
    
    


def MakeNewFileArduino():
    
    operating_system = sys.platform
    current_directory = js.ReadJSONConfig("Technical","current_directory")


    if operating_system == 'linux':

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
            
            WriteFirstLineInNewFileArduino(filename)
            

        return filename

    
    else:

       
   


        #For windows specify directory: r"C:\Users\COLDlab6\Desktop\tpbdeposition"
        while True:
            filename = input("Enter filename (e.g., data.txt): ").strip()
            
            if filename == "MainConfig" or not filename:
                print("Invalid filename.")
            else:
                break
                
            # Combine directory and filename into an absolute path
        full_path = os.path.join(current_directory, filename)
        
        # Check if the file already exists
        if os.path.exists(full_path):
            pass
        else:
            # File does not exist, which is what we want
            WriteFirstLineInNewFile(full_path)

        
        return full_path



