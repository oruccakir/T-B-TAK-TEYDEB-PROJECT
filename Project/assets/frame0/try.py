# import tkinter and necessary libraries
import tkinter as tk
from PIL import Image, ImageTk
path = "C:\\Users\\orucc\\Desktop\\Coding_Projects\\TUBITAK-TEYDEB-PROJECT\\Project\\assets\\frame0\\"
class ButtonApp(tk.Tk):
    def __init__(self, image_path):
        super().__init__()

        self.title("Tkinter Button with Image")

        # Load the image with PIL and create an ImageTk.PhotoImage object
        self.photo = ImageTk.PhotoImage(Image.open(image_path))

        # Create a Button and assign the image to it
        self.button = tk.Button(self, image=self.photo, command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        print("Button clicked!")  # Replace with your desired action

# Example usage
if __name__ == "__main__":
    app = ButtonApp(path+"button_1.png")  # Replace with your image path
    app.mainloop()
