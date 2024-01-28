from pymodbus.client import ModbusSerialClient
import time
# Seri port ve iletişim parametreleri
serial_port = 'COM12'  # Seri portu uygun şekilde güncelleyin
baudrate = 9600
bytesize = 8
parity = 'N'
stopbits = 2

# Modbus client oluştur
client = ModbusSerialClient(method='rtu', port=serial_port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits)
client.connect()

i = 1
while i<10:
    okuma=client.read_holding_registers(1,1,3)
    print(okuma.registers[0])
    i=i+1

time.sleep(1)
start = time.perf_counter()
register_address = 2
setpoint_value = 100 # Örnek bir değer, gerektiğinde bu değeri istediğiniz değer ile değiştirin

client.write_register(register_address, setpoint_value, unit=3)  
end = time.perf_counter()
print("Set time",(end-start))

while True:
    okuma=client.read_holding_registers(1,1,3)
    print(okuma.registers[0]/10)
# address 1 okuma, 2 set 