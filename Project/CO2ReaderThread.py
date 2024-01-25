# import threading
import threading
# import serial for connection
import serial
# import kalman filter to filtering the data
from filterpy.kalman import KalmanFilter
# import numpy for filtering
import numpy as np
# import time to time management
import time

# create CO2 Reader class
class CO2ReaderThread(threading.Thread):
    def __init__(self,CO2Queue,CO2_CSV_queue):
        super().__init__()
        # get queues as intances of this class will be used in run method
        self.CO2Queue = CO2Queue
        self.CO2_CSV_queue = CO2_CSV_queue
        # create kalman filter instances for data filtering
        self.kf_filter = KalmanFilter(dim_x=2, dim_z=1) 
        self.kf_filter.x = np.array([[0.], [0.]])
        self.kf_filter.F = np.array([[1., 1.], [0., 1.]])
        self.kf_filter.H = np.array([[1., 0.]])
        self.kf_filter.P *= 10
        self.kf_filter.R = 5
        self.kf_filter.Q = np.array([[0.01, 0.01], [0.01, 0.01]])
        # create serial connection object to communication
        self.ser_comm = serial.Serial('COM13', 57600, bytesize=8, parity='N', stopbits=1, timeout=1)

    
    def run(self):
        # start timer to get data in every one second
        start_time = time.perf_counter()
        # start function start time
        func_start_time= time.perf_counter()
        # get difference time 2
        difference2 = 0

        while True:
            # try data reading from serial connection
            try:
                data = self.ser_comm.readline().decode('utf-8').strip()
            except UnicodeDecodeError:
                pass

            # important here we need to reset the buffer to just taking necessary samples
            self.ser_comm.reset_input_buffer()

            # get the data as telemetri row
            telemeter_row = data.split(" ")

            # if telemeter row length greater than eight then make progress otherwise not
            if len(telemeter_row) > 8:
                try:
                    # get the data as percentage
                    percentage = round((float(telemeter_row[1]) * 100), 2)
                except ValueError:
                    pass

                # get current time and the time difference
                current_time = time.perf_counter()
                time_diff = current_time - start_time

                # implement calman filter to comng data
                self.kf_filter.predict()
                # update the filter
                self.kf_filter.update(percentage)

                print(percentage)
                
                # get the data as dictionary
                data = {'time': time_diff,'value': self.kf_filter.x[0]}
                # get csv data
                csv_data = {'CO2Percentage' : percentage }

                # put CO2 data to queue
                self.CO2Queue.put(data)
                # put csv data
                self.CO2_CSV_queue.put(csv_data)

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
