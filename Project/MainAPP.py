from MFCReader import MFCReader
from CO2Reader import CO2Reader
import queue


MFCqueue = queue.Queue()
tempratureQueue = queue.Queue()
modbus_CSV_queue  = queue.Queue()
co2_csv = queue.Queue()
co2_queue = queue.Queue()

co2_reader = CO2Reader(co2_queue,co2_csv)
co2_reader.start()


"""
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print(f"{port}: {desc} [{hwid}]")
"""