# import threading
import threading
# import csv for recording
import csv
# import time for recording obvious intervals
import time
# import datetime to save current time file
from datetime import datetime

class CSVRecorder(threading.Thread):
    def __init__(self,path,CO2_CSV_queue,modbus_CSV_queue,flag):
        # call parent constructor
        super().__init__()
        if flag:
            self.csv_file_path =path+datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + "_deneme_veri_log.csv"
        else:
            self.csv_file_path = "record.txt"
        # create self running to stop the thread
        self.isRunning = True
        # get queues to be recorded
        self.CO2_CSV_queue = CO2_CSV_queue
        self.modbus_CSV_queue = modbus_CSV_queue

    
    # overwirte run method
    def run(self):
        # open file as csv file and implement method of writing
        with open(self.csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Time(s)', 'CO%', 'Ar MFC (sccm)', 'CO2 MFC (sscm)', 'Temprature (°C)'])

        # start timer to get data in every one second
        start_time = time.perf_counter()
        # start function start time
        func_start_time= time.perf_counter()
        # get difference time 2
        difference2 = 0

        while self.isRunning:
            # open csv fike to write
            with open(self.csv_file_path, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)

                # write the necessary data
                CO2Sensor=self.CO2_CSV_queue.get()
                modbus=self.modbus_CSV_queue.get()

                current_time = time.perf_counter()
                time_diff = current_time - start_time

                csv_writer.writerow([time_diff, CO2Sensor['CO2Percentage'],modbus['Ar'],modbus['CO2'],modbus['temprature']]) 


            # hold the ending time
            func_end_time=time.perf_counter()
            # get time difference
            difference1 = (func_end_time- func_start_time)
            # hold new start time
            time_start = time.perf_counter()
            # wait exactly one second includes function working time
            try:
                time.sleep(1- difference1 - difference2)
            except ValueError:
                pass
            # hodl new stop time
            time_stop = time.perf_counter()

            # calculate the diffence2
            difference2 = (time_stop - time_start) - 1 + difference1 + difference2
            # again calculate new start time for function
            func_start_time=time.perf_counter() 