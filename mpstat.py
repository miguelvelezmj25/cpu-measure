import commands
from time import strftime

CPU_MONITOR_COMMAND = "mpstat 1 1 | grep -o M..all........ | sed -e 's/M  all   //'"

output = open("cpu_output_" + strftime("%m%d") + '_' + strftime("%H%M%S") + ".txt","w",0)

while True:
	value = commands.getstatusoutput(CPU_MONITOR_COMMAND)[1]

	if len(value) > 0:
		current_time= strftime("%H:%M:%S")
		output.write("time: {} | value: {}\n".format(current_time, float(value)))

