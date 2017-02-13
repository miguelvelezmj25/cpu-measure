import commands
from time import strftime

CPU_MONITOR_COMMAND = "mpstat -P ALL 1 30 | grep -E 'Average' | awk '{print $2, $3}'"

output = open("cpu_tuple_output_" + strftime("%m%d") + '_' + strftime("%H%M%S") + ".txt","w",0)
value = commands.getstatusoutput(CPU_MONITOR_COMMAND)[1]

cpu_utilizations = value.strip().split('\n')[1:]

all_stat = cpu_utilizations[0]
cpu_utilizations.remove(all_stat)
cpu_utilizations.append(all_stat)

stats_instance = ''
for cpu in cpu_utilizations:
    stats_instance += cpu.strip().split(' ')[-1] + ","

output.write(stats_instance[:-1])