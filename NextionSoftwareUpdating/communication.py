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
    ser.write('DRAKJHSUYDGBNCJHGJKSHBDNÿÿÿ'.encode())
    time.sleep(0.135)
    ser.write('connectÿÿÿ'.encode())
    time.sleep(0.135)
    ser.write('ÿÿconnectÿÿÿ'.encode())

    while True:
        response = ser.read(ser.inWaiting())
        time.sleep(1)


except Exception as e:
    print("Error:", e)
finally:
    # Close the serial connection
    ser.close()

