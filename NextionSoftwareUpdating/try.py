import os
import time


file_path = "drumCollectorNextion V1.1.tft"  # Replace with your file path
file_size = os.path.getsize(file_path)
print(f"The size of the file is: {file_size} bytes")

file_path = "drumCollectorNextion V1.1.tft"
CHUNK_SIZE = 4096
i = 0
with open(file_path, 'rb') as file:
     while True:
        chunk = file.read(64)  # 64 byte'lık parçalar halinde oku
        if not chunk:
            break  # Dosya sonuna gelindi
        ser.write(chunk)
        time.sleep(0.1)  

print(i)
