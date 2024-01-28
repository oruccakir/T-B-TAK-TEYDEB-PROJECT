from GraphicMaker import *
from Reader import *
import threading
import queue
from WindowApp import WindowApp
from CSVRecorder import CSVRecorder

path="C:\\Users\\orucc\\Desktop\\Coding_Projects\\TUBITAK-TEYDEB-PROJECT\\Project\\"

# create lock object
lock = threading.Lock()

MFCqueue = queue.Queue()
tempratureQueue = queue.Queue()
modbus_CSV_queue  = queue.Queue()
co2_csv = queue.Queue()
co2_queue = queue.Queue()



co2_reader = CO2ReaderThread(co2_queue,co2_csv)
co2_reader.start()

mfc_reader = MFCReader(MFCqueue,tempratureQueue,modbus_CSV_queue,lock,0.05)
mfc_reader.start()

app = WindowApp(mfc_reader,lock)

co2_maker = CO2GraphicMaker(co2_queue,app,39,700)
co2_maker.start()
mfc_make = MFCGraphicMaker(MFCqueue,app,278,112)
mfc_make.start()

temp_make = TempGraphicMaker(tempratureQueue,app,278,409)
temp_make.start()

csv_recorder = CSVRecorder(path,co2_csv,modbus_CSV_queue,True)
csv_recorder.start()

app.run()

co2_reader.isRunning = False
mfc_reader.isRunning = False
csv_recorder.isRunning = False