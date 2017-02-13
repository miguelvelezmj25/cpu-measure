import commands
from time import strftime

CPU_MONITOR_COMMAND = "mpstat -P ALL 1 30 | grep -E 'Average' | awk '{print $2, $3}'"

output = open("cpu_tuple_output_" + strftime("%m%d") + '_' + strftime("%H%M%S") + ".txt","w",0)
value = commands.getstatusoutput(CPU_MONITOR_COMMAND)[1]
current_time= strftime("%H:%M:%S")
output.write("time: {} | value: {}\n".format(current_time, float(value)))

