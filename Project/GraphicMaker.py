# import threading
import threading
# import neccessary libraries for graphic
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class CO2GraphicMaker(threading.Thread):
    # define constructor
    def __init__(self,CO2Queue,window_app,x,y):
        # call parent contructor
        super().__init__()
        # get queue and save
        self.CO2Queue = CO2Queue
        # create and x and y list for graphic issues
        self.x_data = []
        self.y_data = []
        # get tkinter reference for plotting
        self.window_app = window_app
        # get Co2 graphc x and y values
        self.x = x
        self.y = y
        # set isRunning as True
        self.isRunning = True
    
    
    # overwrite run method
    def run(self):
        # create graphic figures
        CO2_fig = Figure(figsize=(5, 3), facecolor="#5198F0")
        CO2_ax = CO2_fig.add_subplot()
        CO2_ax.set_facecolor("#5198F0")
        CO2_ax.tick_params(labelsize=8, colors="white")
        CO2_fig.autofmt_xdate()

        CO2_ax.spines['top'].set_visible(False)
        CO2_ax.spines['right'].set_visible(False)
        CO2_ax.spines['bottom'].set_color("white")
        CO2_ax.spines['left'].set_color("white")
        # create the canvas figure here important to assign master as self.window_app
        canvas = FigureCanvasTkAgg(figure=CO2_fig, master=self.window_app)
        canvas.get_tk_widget().place(x=self.x, y=self.y)

        while self.isRunning :
            # get the data from queue
            data = self.CO2Queue.get()
            # append files to necessary list as time and value
            self.x_data.append(data['time'])
            self.y_data.append(data['value']) 
            # finally draw the graphic
            CO2_ax.cla()
            CO2_ax.plot(self.x_data, self.y_data, label='CO2', color='purple')

            CO2_fig.suptitle('CO2 Percentage', fontsize=12, color='white')
            CO2_fig.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15)

            CO2_ax.set_xlabel('Time (s)', fontsize=10, color='white')
            CO2_ax.set_ylabel('CO2%', fontsize=10, color='white')

            CO2_ax.tick_params(axis='both', which='both', colors='white')

            try:
                canvas.draw()
            except:
                pass
            

        print("CO2 Maker Terminated")


class MFCGraphicMaker(threading.Thread):
    # define constructor
    def __init__(self,MFCQueue,window_app,x,y):
        # call parent contructor
        super().__init__()
        # get queue and save MFC queue
        self.MFCQueue = MFCQueue
        # create and x and y list for graphic issues
        self.x_data = []
        self.Ar_data = []
        self.CO2_data = []
        # get window app
        self.window_app = window_app
        # get graphic x and y values
        self.x = x
        self.y = y
        # set isRunning as True
        self.isRunning = True

    # overwrite the run method
    def run(self):
        # create graphic figures
        MFC_fig = Figure(figsize=(3.2, 2.3), facecolor="#5198F0")
        MFC_ax = MFC_fig.add_subplot()
        MFC_ax.set_facecolor("#5198F0")
        MFC_ax.tick_params(labelsize=8, colors="white")
        MFC_fig.autofmt_xdate()
        MFC_ax.spines['top'].set_visible(False)
        MFC_ax.spines['right'].set_visible(False)
        MFC_ax.spines['bottom'].set_color("white")
        MFC_ax.spines['left'].set_color("white")
        # create the canvas figure here important to assign master as self.window_app
        canvas = FigureCanvasTkAgg(figure=MFC_fig, master=self.window_app)
        canvas.get_tk_widget().place(x=self.x, y=self.y)

        while self.isRunning:

            # get the data
            gaz= self.MFCQueue.get()
            
            self.x_data.append(gaz['time'])
            self.Ar_data.append(gaz['Ar'])
            self.CO2_data.append(gaz['CO2'])

            MFC_ax.cla()
        
            MFC_ax.plot(self.x_data, self.CO2_data, label='CO2', color='orange')
            MFC_ax.plot(self.x_data, self.Ar_data, label='Ar', color='purple')

            MFC_fig.subplots_adjust(left=0.20, right=0.95, top=0.9, bottom=0.2)

            MFC_ax.set_xlabel('Time (s)', fontsize=10, color='white')
            MFC_ax.set_ylabel('sscm', fontsize=10, color='white')

            MFC_ax.tick_params(axis='both', which='both', colors='white')

            MFC_ax.legend(loc='upper left', fontsize=8, frameon=False, facecolor="#5198F0", labelcolor='white')

            try:
                canvas.draw()
            except:
                pass
        
        print("MFC Maker Terminated")


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
        
        
