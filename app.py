import psutil
from psutil._common import bytes2human
import math
import sqlite3
import plotext as plt

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
        
        self.Menu()

    def Menu(self):
        print("========Menu==========")
        print("(1) Check Data in Db")
        print("(2) Check Stats in a Diagram")
        print("(3) Draw Plot")
        choose = input("Please choose an option")
        print(type(choose))

        match choose:
            case '1':
                print("You choose Add Data")
            case '2':
                self.GetStats()
            case '3':
                self.DrawPlot(self.GetStats())
            case _:
                print('none')
                

    def DrawPlot(self, data):
        plt.xlabel('# Data Recorded')
        plt.ylabel('Hz')
        
        data_hz = data
        data_time = list(range(1, len(data) + 1))

        plt.plot(data_time, data_hz)

        plt.canvas_color('black')
        plt.axes_color('gray+')
        plt.title("CPU Frequency")
        plt.show()

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

    def GetStats(self):
        x = self.cur.execute("SELECT frequency FROM stats")
        res = x.fetchall()
        res_list = [item[0] for item in res]
        return res_list


SysInstance = SystemInfo()
SysInstance.CallInfo()
SysInstance.InsertStats()
