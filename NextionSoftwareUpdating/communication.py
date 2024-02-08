import serial
import time
import os

import numpy as np
# Replace 'COM3' with the port to which your Nextion device is connected
serialPort = 'COM15'
baudRate =921600
file_path = "update.tft"
CHUNK_SIZE = 4096  # 4 KB
file_path =  "update.tft"
answer=""
# Establishing the serial connection
ser = serial.Serial(serialPort, baudRate)

# Give some time for the connection to establish
time.sleep(1)

def calculate_package_number(file_path):
    i=0
    with open(file_path, 'rb') as file:
     while True:
        chunk = file.read(CHUNK_SIZE)  # 64 byte'lık parçalar halinde oku
        if not chunk:
            print(chunk)
            break  # Dosya sonuna gelindi
        i = i +1
    
    return i

file_size = os.path.getsize(file_path)
packet_num = calculate_package_number(file_path)
ser.set_buffer_size(file_size*2)
print(packet_num)

def uploadUpdateMode():
    message = f"upload,{file_size},{packet_num}"
    ser.write(message.encode())
    time.sleep(0.1)

def getfilecontentasList(file_path):
    i = 0
    list = []
    with open(file_path, 'rb') as file:
        while True:
            temp_list = []
            chunk = file.read(CHUNK_SIZE)
            if not chunk:
                break 
            temp_list.append(chunk)
            list.append(temp_list)
            
    return list
                


# Function to send data in chunks
def send_in_chunks(file_path=file_path):
    with open(file_path, 'rb') as file:
        chunk = file.read(CHUNK_SIZE)
        ser.write(chunk)
        time.sleep(1)  # Give the Arduino time to process the data


try:
    list = getfilecontentasList(file_path)
    print(len(list))
    uploadUpdateMode()
    while ser.in_waiting == 0:
        pass
    answer = ser.readline().decode('utf-8').strip()
    print(answer)
    i=0
    if answer == "done":
        with open(file_path,'rb') as file:
            while True:
                chunk = file.read(1)
                chunk = tuple(chunk)
                if not chunk:
                    break
                ser.write(bytes(chunk))
                print(bytes(chunk))
                i=i+1
                #time.sleep(0.05)

    print(f"My jobe is done{i}")
        
except Exception as e:
    print("Error:", e)
finally:
    # Close the serial connection
    ser.close()


