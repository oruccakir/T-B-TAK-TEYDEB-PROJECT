# import threading and process
import threading
import multiprocessing
# import modbusClient
from pymodbus.client import ModbusSerialClient
# import necessary functions for ModbusSerial connection
from pymodbus.constants import *
from pymodbus.payload import *
# to thread and button lock jobs import necessary class
from MFCReader import MFCReader
import time

# create button thread class
class ButtonThread(multiprocessing.Process):
    def __init__(self,mfc_reader,data,lock):
        # call parent constructor
        super().__init__()
        # get lock object
        self.lock = lock
        # get mfc reader
        self.mfc_reader = mfc_reader
        # get running info
        self.isRunning = True
        # isClicked
        self.isClicked = False
        # get data 
        self.data = data
    
    #overwrite run method
    def run(self):
        Ar = self.data["Ar"]
        CO2_value = self.data["CO2"]
        temprature = self.data["Temp"]
        ramp = self.data["Ramp"]
        print("Clicked")
        
        print("Thread")

        with self.lock:
            start = time.perf_counter()
            if len(Ar) > 0:
                Ar= float(Ar)
                builder1 = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.BIG)
                builder1.add_32bit_float(Ar)
                payload1 = builder1.build()
                self.mfc_reader.modbusClient.write_registers(address=0x0006, values=payload1, unit=1, skip_encode=True)  

            if len(CO2_value) > 0:
                CO2_value= float(CO2_value)
                builder2 = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.BIG)
                builder2.add_32bit_float(CO2_value)
                payload2 = builder2.build()
                self.mfc_reader.modbusClient.write_registers(address=0x0006, values=payload2, unit=2, skip_encode=True)  
            if len(temprature) > 0:
                temprature= int((float(temprature))*10)
                self.mfc_reader.modbusClient.write_register(0x0002, temprature, unit=3)

            end = time.perf_counter()
            
            print(end - start)
            pass
        
        
        print(Ar, CO2_value, temprature)

