from MFCReader import MFCReader
from CO2ReaderThread import CO2ReaderThread
from CO2GraphicMaker import CO2GraphicMaker
from MFCGraphicMaker import MFCGraphicMaker
from TempGraphicMaker import TempGraphicMaker
import queue
from WindowApp import WindowApp


MFCqueue = queue.Queue()
tempratureQueue = queue.Queue()
modbus_CSV_queue  = queue.Queue()
co2_csv = queue.Queue()
co2_queue = queue.Queue()


co2_reader = CO2ReaderThread(co2_queue,co2_csv)
co2_reader.start()

mfc_reader = MFCReader(MFCqueue,tempratureQueue,modbus_CSV_queue)
mfc_reader.start()

app = WindowApp(620,1024)

co2_maker = CO2GraphicMaker(co2_queue,app,39,700)
co2_maker.start()

mfc_make = MFCGraphicMaker(MFCqueue,app,278,112)
mfc_make.start()

temp_make = TempGraphicMaker(tempratureQueue,app,278,409)
temp_make.start()

app.run()


#for thread in threads:
#    thread.join()



"""
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print(f"{port}: {desc} [{hwid}]")
"""