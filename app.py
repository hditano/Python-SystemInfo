import psutil
from psutil._common import bytes2human
import math

def CallInfo():
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    cpu_load = psutil.getloadavg()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print('Welcome to System Info')
    print('======================')

    print(f'CPU Cores: {cpu_count}')
    print(f'CPU Frequency: {math.trunc(cpu_freq[0])} Hz')
    print(f'CPU Load: {math.trunc(cpu_load[0] / cpu_count * 100)}%')

    print(f'Memory: {math.trunc(memory[2])}%')

    print(f'Disk Free Space: {bytes2human(disk[2])}')

CallInfo()
