import serial
import time

# Replace 'COM3' with the port to which your Nextion device is connected
serialPort = 'COM14'
baudRate =9600

# Establishing the serial connection
ser = serial.Serial(serialPort, baudRate, timeout=1)

# Give some time for the connection to establish
time.sleep(1)

try:
    # Sending a command (example: get the text of a component with .txt attribute)
    # Replace 'component_name' with your actual component's name
    
    """
    ser.write('DRAKJHSUYDGBNCJHGJKSHBDN\xFF\xFF\xFF'.encode('utf-8'))
    time.sleep(0.135)
    ser.write('connect\xFF\xFF\xFF'.encode())
    time.sleep(0.135)
    ser.write('\xFF\xFFconnect\xFF\xFF\xFF'.encode())
    """
    while True:
        response = ser.read(ser.inWaiting()).decode('utf-8')
        print(response)
        time.sleep(1)

    ser.write("t8.txt=".encode())
    ser.write("0x22".encode())
    ser.write("Alper_bebesi".encode())
    ser.write("0x22".encode())
    ser.write("0xff".encode())
    ser.write("0xff".encode())
    ser.write("0xff".encode())

    


except Exception as e:
    print("Error:", e)
finally:
    # Close the serial connection
    ser.close()

