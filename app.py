import psutil
from psutil._common import bytes2human
import math
import sqlite3
import os

class SystemInfo:
    def __init__(self) -> None:
        self.cpu_count = psutil.cpu_count()
        self.cpu_freq = psutil.cpu_freq()
        self.cpu_load = psutil.getloadavg()
        self.memory = psutil.virtual_memory()
        self.disk = psutil.disk_usage('/')
        self.con = sqlite3.connect("database.db")
        self.cur = self.con.cursor()

    def CallInfo(self):
        print('Welcome to System Info')
        print('======================')

        print(f'CPU Cores: {self.cpu_count}')
        print(f'CPU Frequency: {math.trunc(self.cpu_freq.current)} Hz')
        print(f'CPU Load: {math.trunc(self.cpu_load[0] / self.cpu_count * 100)}%')

        print(f'Memory: {self.memory.percent}%')
    
        print(f'Disk Free Space: {bytes2human(self.disk.free)}')

    def InitDb(self):
        if os.path.exists("database.db"):
            self.cur.execute("""
                            INSERT INTO stats VALUES (23, 43.4, 23, 2)
                            """)
            self.con.commit()
        else:
            self.cur.execute("CREATE TABLE stats(count, fequency, load, memory, disk)")

SysInstance = SystemInfo()
SysInstance.CallInfo()
SysInstance.InitDb()
