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
        self.InitDb()

    def CallInfo(self):
        print('Welcome to System Info')
        print('======================')

        print(f'CPU Cores: {self.cpu_count}')
        print(f'CPU Frequency: {math.trunc(self.cpu_freq.current)} Hz')
        print(f'CPU Load: {math.trunc(self.cpu_load[0] / self.cpu_count * 100)}%')

        print(f'Memory: {self.memory.percent}%')
    
        print(f'Disk Free Space: {bytes2human(self.disk.free)}')

    def InitDb(self):
        self.cur.execute("""
                         CREATE TABLE IF NOT EXISTS stats (
                         count INTEGER,
                         frequency REAL,
                         load REAL,
                         memory REAL,
                         disk REAL
                         )
                    """)
        self.con.commit()

    def InsertStats(self):
        self.cur.execute(
            "INSERT INTO stats (count, frequency, load, memory, disk) values (?, ?, ?, ?, ?)",
            (self.cpu_count, self.cpu_freq.current, self.cpu_load[0], self.memory.percent, self.disk.free)
        )
        self.con.commit()


SysInstance = SystemInfo()
SysInstance.CallInfo()
SysInstance.InsertStats()
