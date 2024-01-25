# import threading
import threading
# import neccessary libraries for graphic
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class CO2GraphicMaker(threading.Thread):
    # define constructor
    def __init__(self,CO2Queue,window_app):
        # call parent contructor
        super().__init__()
        # get queue and save
        self.CO2Queue = CO2Queue
        # create and x and y list for graphic issues
        self.x_data = []
        self.y_data = []
        # get tkinter reference for plotting
        self.window_app = window_app
    
    
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
        # create the canvas figure here importan to assign master as self.window_app
        canvas = FigureCanvasTkAgg(figure=CO2_fig, master=self.window_app)
        canvas.get_tk_widget().place(x=39, y=700)

        while True:
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

            canvas.draw()
        
