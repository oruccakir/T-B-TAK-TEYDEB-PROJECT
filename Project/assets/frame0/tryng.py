import tkinter as tk
from PIL import Image, ImageTk
path = "C:\\Users\\orucc\\Desktop\\Coding_Projects\\TUBITAK-TEYDEB-PROJECT\\Project\\assets\\frame0\\"
"""


root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Load the image
image = Image.open(path+"image_1.png")
photo = ImageTk.PhotoImage(image)

# Add image to canvas
canvas.create_image(200, 200, image=photo)

root.mainloop()
"""

class ImageApp(tk.Tk):
    def __init__(self, image_path):
        super().__init__()

        self.title("Tkinter Image Viewer")
        self.geometry("500x500")  # Adjust the size as per your image

        # Create a Canvas Widget
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()

        # Load the image with PIL and add to canvas
        self.load_image(image_path)

    def load_image(self, path):
        # Load the image
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)

        # Keep a reference to the image to prevent garbage collection
        self.image = photo

        # Add image to canvas
        self.canvas.create_image(250, 250, image=photo)  # Center position

# Example usage
if __name__ == "__main__":
    app = ImageApp(path+"image_1.png")
    app.mainloop()
