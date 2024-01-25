# import threading
import threading
# import neccessary libraries for graphic
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class TempGraphicMaker(threading.Thread):
    # define constructor
    def __init__(self,temperatureQueue,window_app,x,y):
        # call parent contructor
        super().__init__()
        # get queue and save temp queue
        self.temperatureQueue = temperatureQueue
        # create x data and temperature data list
        self.x_data = []
        self.temperature_data = []
        # get windows app
        self.window_app = window_app
        # get graphic x and y values
        self.x = x
        self.y = y
        # set isRunning as True
        self.isRunning = True

    def run(self):
        # create graphic figures
        temprature_fig = Figure(figsize=(3.2, 2.3), facecolor="#5198F0")
        temprature_ax = temprature_fig.add_subplot()
        temprature_ax.set_facecolor("#5198F0")
        temprature_ax.tick_params(labelsize=8, colors="white")
        temprature_fig.autofmt_xdate()

        temprature_ax.spines['top'].set_visible(False)
        temprature_ax.spines['right'].set_visible(False)

        temprature_ax.spines['bottom'].set_color("white")
        temprature_ax.spines['left'].set_color("white")
        # create the canvas figure here important to assign master as self.window_app
        canvas = FigureCanvasTkAgg(figure=temprature_fig, master=self.window_app)
        canvas.get_tk_widget().place(x=278, y=409)

        while self.isRunning:
            # get the data
            temprature= self.temperatureQueue.get()
        
            self.x_data.append(temprature['time'])
            self.temperature_data.append(temprature['temprature'])
            
            temprature_ax.cla()
        
            temprature_ax.plot(self.x_data, self.temperature_data, label='temprature', color='firebrick')

            temprature_fig.subplots_adjust(left=0.18, right=0.95, top=0.9, bottom=0.2)

            temprature_ax.set_xlabel('Time (s)', fontsize=10, color='white')
            temprature_ax.set_ylabel('Temprature °C', fontsize=10, color='white')

            temprature_ax.tick_params(axis='both', which='both', colors='white')

            try:
                canvas.draw()
            except:
                pass
        
        print("TEMP Reader Terminated")
