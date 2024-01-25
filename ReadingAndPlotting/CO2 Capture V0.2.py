import multiprocessing
import threading
from datetime import datetime
import time
import serial
import csv
from filterpy.kalman import KalmanFilter
import numpy as np

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from pymodbus.client import ModbusSerialClient
from pymodbus.constants import *
from pymodbus.payload import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alpti\OneDrive\Masaüstü\CO2 Capture\CO2 Capture Python\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("600x1024")
window.configure(bg = "#C5D5FF")

canvas = Canvas(
    window,
    bg = "#C5D5FF",
    height = 1024,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    306.0,
    545.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    123.0,
    167.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=87.0,
    y=145.0,
    width=72.0,
    height=42.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    123.0,
    268.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=87.0,
    y=246.0,
    width=72.0,
    height=42.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    146.0,
    464.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=110.0,
    y=442.0,
    width=72.0,
    height=42.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    123.0,
    570.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=87.0,
    y=548.0,
    width=72.0,
    height=42.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: modbusDevices.modbusSet(modbus_set_queue),
    relief="flat"
)
button_1.place(
    x=65.0,
    y=335.0,
    width=116.0,
    height=69.0
)

def CSVrecord(CO2_CSV_queue,modbus_CSV_queue):
 
    csv_file_path = "C:\\Users\\alpti\\downloads\\" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + "_deneme_veri_log.csv"

    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Time(s)', 'CO%', 'Ar MFC (sccm)', 'CO2 MFC (sscm)', 'Temprature (°C)'])
    
    start_time = time.perf_counter()
    
    func_start_time= time.perf_counter()
    fark2 = 0
    
    while True:

        with open(csv_file_path, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                
                CO2Sensor=CO2_CSV_queue.get()
                modbus=modbus_CSV_queue.get()

                current_time = time.perf_counter()
                time_diff = current_time - start_time

                csv_writer.writerow([time_diff, CO2Sensor['CO2Percentage'],modbus['Ar'],modbus['CO2'],modbus['temprature']])   

        func_end_time=time.perf_counter()
 
        fark=(func_end_time- func_start_time)
        time_start = time.perf_counter()
        try:
            time.sleep(1- fark - fark2)
        except ValueError:
            pass
        time_stop = time.perf_counter()

        fark2 = (time_stop - time_start) - 1 + fark + fark2
        func_start_time=time.perf_counter()

def helpme(modbusClient):
    modbusClient.loop()    

class modbusDevices():
    def __init__(self,modbus_set_queue,MFCqueue, tempratureQueue, modbus_CSV_queue,):
        self.modbus_set_queue=modbus_set_queue
        self.MFCqueue=MFCqueue
        self.tempratureQueue=tempratureQueue
        self.modbus_CSV_queue=modbus_CSV_queue
        
        self.modbusClient = ModbusSerialClient(method='rtu', port = 'COM12', baudrate = 9600, bytesize = 8, parity = 'N', stopbits = 2, address=1)
        self.modbusClient.connect()

    def write_float_register (self, address: int, values: list[float] | float | int, slave: int = 0):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.BIG)
        builder.add_32bit_float(values)
        payload = builder.build()
        self.modbusClient.write_registers(address=address, values=payload, slave=slave, skip_encode=True)

    def read_float_register (self, address: int, count: int = 1, slave: int = 0):
        read= self.modbusClient.read_holding_registers(address=address, count=count,slave=slave)
        decoder = BinaryPayloadDecoder.fromRegisters(read.registers, byteorder=Endian.BIG, wordorder=Endian.BIG)
        return decoder.decode_32bit_float()
    
    def modbusSet(self):

        Ar= float(entry_1.get())
        CO2= float(entry_2.get())
        temprature= int((float(entry_3.get()))*10)
        print(temprature)

        set_data={
            'Ar' : Ar,
            'CO2' : CO2,
            'temprature' : temprature
        }
        
        self.modbus_set_queue.put(set_data)

    def loop(self):

        self.start_time= time.perf_counter()
        self.func_start_time= time.perf_counter()
        self.fark2 = 0

        while True:

            MFC_Ar_read= self.read_float_register(0,2,1)

            MFC_CO2_read= self.read_float_register(0,2,2)
            
            temprature_read= self.modbusClient.read_holding_registers(1,1,3)

            current_time = time.perf_counter()
            time_diff = current_time - self.start_time

            MFC_data = {
                'time' : time_diff,
                'Ar': MFC_Ar_read,
                'CO2': MFC_CO2_read
                }
            
            temprature_data = {
                'time' : time_diff,
                'temprature': float(temprature_read.registers[0]/10),
                }

            csv_data = {
                'Ar': MFC_Ar_read,
                'CO2': MFC_CO2_read,
                'temprature': float(temprature_read.registers[0]/10),
            }

            self.MFCqueue.put(MFC_data)
            self.tempratureQueue.put(temprature_data)
            self.modbus_CSV_queue.put(csv_data)

            if not modbus_set_queue.empty():
                
                set_data=modbus_set_queue.get()

                self.write_float_register(0x0006,set_data['Ar'],1)
                self.write_float_register(0x0006,set_data['CO2'],2)

                self.modbusClient.write_register(0x0002, set_data['temprature'], unit=3)  

            func_end_time=time.perf_counter()
    
            fark=(func_end_time- func_start_time)
            time_start = time.perf_counter()
            try:
                time.sleep(1- fark - fark2)
            except ValueError:
                pass
            time_stop = time.perf_counter()

            fark2 = (time_stop - time_start) - 1 + fark + fark2
            func_start_time=time.perf_counter()


def CO2Sensor(CO2queue,CO2_CSV_queue): 

    kf = KalmanFilter(dim_x=2, dim_z=1) 
    kf.x = np.array([[0.], [0.]])
    kf.F = np.array([[1., 1.], [0., 1.]])
    kf.H = np.array([[1., 0.]])
    kf.P *= 10
    kf.R = 5
    kf.Q = np.array([[0.01, 0.01], [0.01, 0.01]])

    ser = serial.Serial('COM7', 57600, bytesize=8, parity='N', stopbits=1, timeout=1)

    start_time = time.perf_counter()
    
    func_start_time= time.perf_counter()
    fark2 = 0

    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
        except UnicodeDecodeError:
            pass
        
        ser.reset_input_buffer()

        telemetriSatiri = data.split(" ")

        if len(telemetriSatiri) > 8:
            try:
                percentage = round((float(telemetriSatiri[1]) * 100), 2)
            except ValueError:
                pass

            current_time = time.perf_counter()
            time_diff = current_time - start_time

            kf.predict()
            kf.update(percentage)

            data = {
            'time': time_diff,
            'value': kf.x[0]
            }
            
            csv_data = {
                'CO2Percentage' : percentage 
            }
            
            CO2queue.put(data)
            CO2_CSV_queue.put(csv_data)

            func_end_time=time.perf_counter()
 
            fark=(func_end_time- func_start_time)
            time_start = time.perf_counter()
            time.sleep(1- fark - fark2)
            time_stop = time.perf_counter()

            fark2 = (time_stop - time_start) - 1 + fark + fark2
            func_start_time=time.perf_counter()

def CO2grafik(CO2queue):

    x_data = []
    y_data = []

    CO2_fig = Figure(figsize=(5, 3), facecolor="#5198F0")
    CO2_ax = CO2_fig.add_subplot()
    CO2_ax.set_facecolor("#5198F0")
    CO2_ax.tick_params(labelsize=8, colors="white")
    CO2_fig.autofmt_xdate()

    CO2_ax.spines['top'].set_visible(False)
    CO2_ax.spines['right'].set_visible(False)

    CO2_ax.spines['bottom'].set_color("white")
    CO2_ax.spines['left'].set_color("white")

    canvas = FigureCanvasTkAgg(figure=CO2_fig, master=window)
    canvas.get_tk_widget().place(x=39, y=700)

    while True:
    
        data = CO2queue.get()
        x_data.append(data['time'])
        y_data.append(data['value'])    

        CO2_ax.cla()
        CO2_ax.plot(x_data, y_data, label='CO2', color='purple')

        CO2_fig.suptitle('CO2 Percentage', fontsize=12, color='white')
        CO2_fig.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)

        CO2_ax.set_xlabel('Time (s)', fontsize=10, color='white')
        CO2_ax.set_ylabel('CO2%', fontsize=10, color='white')

        CO2_ax.tick_params(axis='both', which='both', colors='white')

        canvas.draw()

def MFCgrafik(MFCqueue):
    
    Ar_data = []
    CO2_data = []
    x_data=[]

    MFC_fig = Figure(figsize=(3.2, 2.3), facecolor="#5198F0")
    MFC_ax = MFC_fig.add_subplot()
    MFC_ax.set_facecolor("#5198F0")
    MFC_ax.tick_params(labelsize=8, colors="white")
    MFC_fig.autofmt_xdate()

    MFC_ax.spines['top'].set_visible(False)
    MFC_ax.spines['right'].set_visible(False)

    MFC_ax.spines['bottom'].set_color("white")
    MFC_ax.spines['left'].set_color("white")

    canvas = FigureCanvasTkAgg(figure=MFC_fig, master=window)
    canvas.get_tk_widget().place(x=278, y=112)

    while True:

        gaz= MFCqueue.get()

        x_data.append(gaz['time'])
        Ar_data.append(gaz['Ar'])
        CO2_data.append(gaz['CO2'])

        MFC_ax.cla()
       
        MFC_ax.plot(x_data, CO2_data, label='CO2', color='orange')
        MFC_ax.plot(x_data, Ar_data, label='Ar', color='purple')

        MFC_fig.subplots_adjust(left=0.20, right=0.95, top=0.9, bottom=0.2)

        MFC_ax.set_xlabel('Time (s)', fontsize=10, color='white')
        MFC_ax.set_ylabel('sscm', fontsize=10, color='white')

        MFC_ax.tick_params(axis='both', which='both', colors='white')

        MFC_ax.legend(loc='upper left', fontsize=8, frameon=False, facecolor="#5198F0", labelcolor='white')

        canvas.draw()

def tempratureGrafik(tempratureQueue):
    temprature_data = []
    x_data=[]

    temprature_fig = Figure(figsize=(3.2, 2.3), facecolor="#5198F0")
    temprature_ax = temprature_fig.add_subplot()
    temprature_ax.set_facecolor("#5198F0")
    temprature_ax.tick_params(labelsize=8, colors="white")
    temprature_fig.autofmt_xdate()

    temprature_ax.spines['top'].set_visible(False)
    temprature_ax.spines['right'].set_visible(False)

    temprature_ax.spines['bottom'].set_color("white")
    temprature_ax.spines['left'].set_color("white")

    canvas = FigureCanvasTkAgg(figure=temprature_fig, master=window)
    canvas.get_tk_widget().place(x=278, y=409)

    while True:

        temprature= tempratureQueue.get()
        
        x_data.append(temprature['time'])
        temprature_data.append(temprature['temprature'])
        
        temprature_ax.cla()
       
        temprature_ax.plot(x_data, temprature_data, label='temprature', color='firebrick')

        temprature_fig.subplots_adjust(left=0.18, right=0.95, top=0.9, bottom=0.2)

        temprature_ax.set_xlabel('Time (s)', fontsize=10, color='white')
        temprature_ax.set_ylabel('Temprature °C', fontsize=10, color='white')

        temprature_ax.tick_params(axis='both', which='both', colors='white')

        canvas.draw()


if __name__ == "__main__":

    CO2queue = multiprocessing.Queue()
    MFCqueue = multiprocessing.Queue()
    tempratureQueue = multiprocessing.Queue()

    CO2_CSV_queue = multiprocessing.Queue()
    modbus_CSV_queue = multiprocessing.Queue()

    modbus_set_queue = multiprocessing.Queue()

    
    device=modbusDevices(modbus_set_queue,MFCqueue, tempratureQueue, modbus_CSV_queue)
 

    CO2SensorProcess = multiprocessing.Process(target=CO2Sensor, args=(CO2queue, CO2_CSV_queue,))
    modbusDevicesProcess = multiprocessing.Process(target=helpme, args=(device,))
    CSVprocess = multiprocessing.Process(target=CSVrecord, args=(CO2_CSV_queue, modbus_CSV_queue,))

    CO2SensorProcess.start()
    modbusDevicesProcess.start()
    CSVprocess.start()

    ## Main process threadleri -> Grafikler
    CO2grafikThread = threading.Thread(target=CO2grafik, args=(CO2queue,))
    CO2grafikThread.start()

    MFCgrafikThread = threading.Thread(target=MFCgrafik, args=(MFCqueue,))
    MFCgrafikThread.start()

    tempratureGrafikThread = threading.Thread(target=tempratureGrafik, args=(tempratureQueue,)) 
    tempratureGrafikThread.start()

    window.resizable(False, False)
    window.mainloop()

    try:
        pass

    except KeyboardInterrupt:
        CO2SensorProcess.terminate()
        modbusDevicesProcess.terminate()
        print("Program terminated.")