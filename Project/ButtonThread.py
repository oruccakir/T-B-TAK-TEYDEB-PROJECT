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
class ButtonThread(threading.Thread):
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
    
    def write_float_register (self,address: int, values: list[float] | float | int, slave: int = 0):
        builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.BIG)
        builder.add_32bit_float(values)
        payload = builder.build()
        self.mfc_reader.modbusClient.write_registers(address=address, values=payload, slave=slave, skip_encode=True)

    #overwrite run method
    def run(self):
        Ar = self.data["Ar"]
        CO2_value = self.data["CO2"]
        temprature = self.data["Temp"]
        ramp = self.data["Ramp"]
        print("Clicked")
        
        with self.lock:
            start = time.perf_counter()
            if len(Ar) > 0 :
                Ar= float(Ar)
                self.write_float_register(0x0006,Ar,1)
            
            if len(CO2_value) > 0:
                CO2_value= float(CO2_value)
                self.write_float_register(0x0006,CO2_value,2)
            
            if len(temprature) > 0 :
                temprature= int((float(temprature))*10)
                self.mfc_reader.modbusClient.write_register(0x0002, temprature, unit=3)
                #self.write_float_register(0x0002,temprature,3)

            end = time.perf_counter()
            print(end - start)
            
            

