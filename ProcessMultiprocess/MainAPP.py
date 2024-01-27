from MFCReader import MFCReader
from CO2ReaderThread import CO2ReaderThread
from CO2GraphicMaker import CO2GraphicMaker
from MFCGraphicMaker import MFCGraphicMaker
from TempGraphicMaker import TempGraphicMaker
from ButtonThread import ButtonThread
import queue
from WindowApp import WindowApp
import time
from CSVRecorder import CSVRecorder
import threading
import multiprocessing
path="C:\\Users\\orucc\\Desktop\\Coding_Projects\\TUBITAK-TEYDEB-PROJECT\\Project\\"
"""

# create lock object
lock = threading.Lock()

MFCqueue = queue.Queue()
tempratureQueue = queue.Queue()
modbus_CSV_queue  = queue.Queue()
co2_csv = queue.Queue()
co2_queue = queue.Queue()



co2_reader = CO2ReaderThread(co2_queue,co2_csv)
co2_reader.start()

mfc_reader = MFCReader(MFCqueue,tempratureQueue,modbus_CSV_queue,lock)
mfc_reader.start()

app = WindowApp(mfc_reader,lock)

co2_maker = CO2GraphicMaker(co2_queue,app,39,700)
co2_maker.start()

mfc_make = MFCGraphicMaker(MFCqueue,app,278,112)
mfc_make.start()

temp_make = TempGraphicMaker(tempratureQueue,app,278,409)
temp_make.start()

csv_recorder = CSVRecorder(path,co2_csv,modbus_CSV_queue,False)
csv_recorder.start()

app.run()

co2_reader.isRunning = False
mfc_reader.isRunning = False
csv_recorder.isRunning = False

"""


if __name__ == '__main__':
    MFCqueue = multiprocessing.Queue()
    tempratureQueue = multiprocessing.Queue()
    modbus_CSV_queue  = multiprocessing.Queue()
    co2_csv = multiprocessing.Queue()
    co2_queue = multiprocessing.Queue()


    co2_reader = CO2ReaderThread(co2_queue,co2_csv)
    co2_reader.start()






"""
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print(f"{port}: {desc} [{hwid}]")
"""