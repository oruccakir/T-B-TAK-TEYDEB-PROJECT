# import tkinter and necessary libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from PIL import Image, ImageTk
# import Path
from pathlib import Path
# set output path
path = "C:\\Users\\orucc\\Desktop\\Coding_Projects\\TUBITAK-TEYDEB-PROJECT\\Project\\assets\\frame0\\"
from ButtonThread import ButtonThread
from MFCReader import MFCReader

class WindowApp(tk.Tk):
    def __init__(self,mfc_reader,lock):
        super().__init__()
        self.mfc_reader = mfc_reader
        self.lock = lock
        width = 600
        height = 1024
        self.geometry(f"{str(width)}x{str(height)}")
        self.configure(bg="#C5D5FF")

        # ad closing protocol
        self.protocol("WM_DELETE_WINDOW",self.on_closing)

        self.canvas = Canvas(
            self,
            bg="#C5D5FF",
            height=1024,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.load_image(path+"image_1.png",306,545)
       
        # Create and place entry widgets
        self.entry1 = tk.Entry(
            master=self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )

        self.entry1.place(
            x=87.0,
            y=145.0,
            width=72.0,
            height=42.0
        )

        self.entry2 = tk.Entry(
            master=self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry2.place(
            x=87.0,
            y=246.0,
            width=72.0,
            height=42.0
        )

        self.entry3 = tk.Entry(
            master=self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry3.place(
            x=87.0,
            y=442.0,
            width=72.0,
            height=42.0
        )

        self.entry4= tk.Entry(
            master = self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry4.place(
            x=87.0,
            y=548.0,
            width=72.0,
            height=42.0
        )

        self.photo = ImageTk.PhotoImage(Image.open(path + "button_1.png"))

        self.button = tk.Button(
            master=self,
            image = self.photo,
            command=self.on_click
        )

        self.button.place(
            x=65.0,
            y=335.0,
            width=116.0,
            height=69.0
        )



    def load_image(self, path,x,y):
        # Load the image
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)

        # Keep a reference to the image to prevent garbage collection
        self.image = photo

        # Add image to canvas
        self.canvas.create_image(x, y, image=photo)  # Center position
        
    # define a method that will be terminate program
    def on_closing(self):
        print("Program Terminated")
        self.destroy()
    
    def on_click(self):
        Ar = self.entry1.get()
        CO2_value = self.entry2.get()
        temprature = self.entry3.get()
        ramp = self.entry4.get()
        data = {
            "Ar":Ar,
            "CO2":CO2_value,
            "Temp":temprature,
            "Ramp":ramp
        }
        butt = ButtonThread(self.mfc_reader,data,self.lock)
        butt.start()

    def run(self):
        # This method starts the Tkinter event loop
        self.mainloop()

