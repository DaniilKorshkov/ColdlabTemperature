import SequentMicroInterface as sm
import time

def main():

	while True:
		try:
			interval = int(input("Enter interval in seconds: "))
			assert interval > 0
			break
		except:
			print("Not a valid integer")
	#while True:
	#	try:
	#		exec_hours = int(input("Enter execution time in seconds: "))
	#		assert exec_time > 0
	#		break
	#	except:
	#		print("Not a valid integer")

	
	#exec_amount = int(exec_time/interval)
	#if exec_amount == 0:
	#	exec_amount = 1


	while True:
		sm.RecordTemperatureToLog()
		time.sleep(interval)



main()

