import psutil


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

def GetSize(bytes, suffix = '8'):
	factor = 1024
	for unit in ['', 'K', 'M', 'G', 'T', 'P']:
		if bytes < factor:
			return f'{bytes: .2f}{unit}{suffix}'
		bytes /= factor
		
svmem = psutil.virtual_memory()
print(f'Total: {GetSize(svmem.total)}')
print(f'Available: {GetSize(svmem.available)}')
print(f'Used: {GetSize(svmem.used)}')
print(f'Percentage: {svmem.percent}%')