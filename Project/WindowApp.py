# import tkinter and necessary libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
# import Path
from pathlib import Path
# set output path
path = "C:\\Users\\orucc\\Desktop\\Coding_Projects\\TUBITAK-TEYDEB-PROJECT\\Project\\assets\\frame0\\"


class WindowApp(tk.Tk):
    def __init__(self,width,height):
        super().__init__()

        self.geometry(f"{str(width)}x{str(height)}")
        self.configure(bg="#C5D5FF")
        # assign threads
        self.threads = []

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
        self.initialize_widgets()

    def initialize_widgets(self):
        image_image_1 = PhotoImage(path+"image_1.png")
        image_1 = self.canvas.create_image(
            306.0,
            545.0,
            image=image_image_1
        )

        entry_image_1 = PhotoImage(file=path+"entry_1.png")
        entry_bg_1 = self.canvas.create_image(
            123.0,
            167.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=87.0,
            y=145.0,
            width=72.0,
            height=42.0
        )

        entry_image_2 = PhotoImage(
            file=path+"entry_2.png")
        entry_bg_2 = self.canvas.create_image(
            123.0,
            268.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=87.0,
            y=246.0,
            width=72.0,
            height=42.0
        )

        entry_image_3 = PhotoImage(
            file=path+"entry_3.png")
        entry_bg_3 = self.canvas.create_image(
            146.0,
            464.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=110.0,
            y=442.0,
            width=72.0,
            height=42.0
        )

        entry_image_4 = PhotoImage(
            file=path+"entry_4.png")
        entry_bg_4 = self.canvas.create_image(
            123.0,
            570.0,
            image=entry_image_4
        )
        entry_4 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
            x=87.0,
            y=548.0,
            width=72.0,
            height=42.0
        )

        button_image_1 = PhotoImage(
            file=path+"button_1.png")
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_1.place(
            x=65.0,
            y=335.0,
            width=116.0,
            height=69.0
        )
        
    # define a method that will be terminate program
    def on_closing(self):
        print(len (self.threads))
        for thread in self.threads:
            thread.isRunning = False
        self.destroy()

    def run(self):
        # This method starts the Tkinter event loop
        self.mainloop()

