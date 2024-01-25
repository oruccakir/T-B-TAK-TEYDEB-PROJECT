# import threading
import threading
# import neccessary libraries for graphic
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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

