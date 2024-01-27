from pymodbus.client import *
from pymodbus.constants import *
from pymodbus.payload import *
import time 
# Seri port ve iletişim parametreleri
serial_port = 'COM12'  # Seri portu uygun şekilde güncelleyin
baudrate = 9600
bytesize = 8
parity = 'N'
stopbits = 2

def write_float_register (address: int, values: list[float] | float | int, slave: int = 0):
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.BIG)
    builder.add_32bit_float(values)
    payload = builder.build()
    client.write_registers(address=address, values=payload, slave=slave, skip_encode=True)

def read_float_register (address: int, count: int = 1, slave: int = 0):
    read= client.read_holding_registers(address=address, count=count,slave=slave)
    decoder = BinaryPayloadDecoder.fromRegisters(read.registers, byteorder=Endian.BIG, wordorder=Endian.BIG)
    return decoder.decode_32bit_float()

# Modbus client oluştur
client = ModbusSerialClient(method='rtu', port=serial_port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits)
client.connect()

i = 0

while i<10:

    print(read_float_register(0,2,1),read_float_register(0,2,2))
    time.sleep(1)
    i=i+1


print("-------------------------------")

#client.write_register(address=0x4040, value=0, unit=1)
#client.write_register(address=0x000e, value=1, unit=1)

start = time.perf_counter()
write_float_register(6,0,1)

#client.write_register(address=0x4040, value=0, unit=2)
#client.write_register(address=0x000e, value=1, unit=2)

write_float_register(6,0,2)
end = time.perf_counter()

print(end - start)

while True:

    print(read_float_register(0,2,1),read_float_register(0,2,2))




