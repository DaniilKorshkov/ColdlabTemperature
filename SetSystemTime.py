import subprocess
import datetime

def SetSystemTime():
	rawtime = str(subprocess.run([f"megaind", "0", "rtcrd"], capture_output=True).stdout)
	rawtime = rawtime[2:(len(rawtime)-3)]	
	rawtime = rawtime.replace("/","splitme"); rawtime = rawtime.replace(" ","splitme"); rawtime = rawtime.replace(":","splitme")
	time_array = rawtime.split("splitme")  #month,day,year,hours,minutes,seconds
	month_lookup_table = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
	month = month_lookup_table[(int(time_array[0])-1)]

	void = subprocess.run([f"sudo", "date", f'--set={time_array[1]} {month}  {int(time_array[2])+2000} {time_array[3]}:{time_array[4]}:{time_array[5]}'])
	



SetSystemTime()

# to activate:
# type 'sudo cp SetSystemTime.py /bin'
#type 'sudo crontab -e'
#add '@reboot sudo python3 /bin/SetSystemTime.py' line, press Ctrl+X 