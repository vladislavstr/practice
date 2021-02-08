import psutil
import GPUtil
from tabulate import tabulate

#number of cores
print('Physical cores', psutil.cpu_count(logical = False))
print('Total cores', psutil.cpu_count(logical = True))

#CPY frequencies
cpufreq = psutil.cpu_freq()
print(f'Max: {cpufreq.max:.2f}Mhz')
print(f'Min: {cpufreq.min:.2f}Mhz')
print(f'Current: {cpufreq.current:.2f}Mhz')

#CPU usage
print('CPU Usage Per Core')
for i, percentage in enumerate(psutil.cpu_percent(percpu = True, interval = 1)):
    print(f'Core {i}: {percentage}%')
print(f'Total CPU Usage: {psutil.cpu_percent()}%')


# RAM Info
print('')
print('#'*10, 'RAM info', '#'*10)
print('')

def get_size(bytes, suffix = '8'):
	factor = 1024
	for unit in ['', 'K', 'M', 'G', 'T', 'P']:
		if bytes < factor:
			return f'{bytes: .2f}{unit}{suffix}'
		bytes /= factor
		
svmem = psutil.virtual_memory()
print(f'Total: {get_size(svmem.total)}')
print(f'Available: {get_size(svmem.available)}')
print(f'Used: {get_size(svmem.used)}')
print(f'Percentage: {svmem.percent}%')


# GPU Info 
print('')
print('#'*10, 'GPU info', '#'*10)
print('')

def GPU_info_table():
	gpus = GPUtil.getGPUs()
	list_gpus = []
	for gpu in gpus:
		gpu_id = gpu.id
		gpu_name = gpu.name
		gpu_load = f'{gpu.load * 100}%'
		gpu_free_memory = f'{gpu.memoryFree}Mb'
		gpu_used_memory = f'{gpu.memoryUsed}Mb'
		gpu_total_memory = f'{gpu.memoryTotal}Mb'
		gpu_temperature = f'{gpu.temperature} C'
		gpu_uuid = gpu.uuid

		list_gpus.append((gpu_id,
		 gpu_name, 
		 gpu_load, 
		 gpu_free_memory, 
		 gpu_used_memory, 
		 gpu_total_memory, 
		 gpu_temperature, 
		 gpu_uuid))

	#return str(tabulate(list_gpus, headers = ('id', 'name', 'load', 'free memory', 'used memory', 'total memory', 'temperature', 'uuid'), tablefmt = 'pretty'))
	print(gpu_id)

if __name__ == "__main__":
	print(GPU_info_table)	