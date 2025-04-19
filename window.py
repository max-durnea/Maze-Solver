from tkinter import Tk, Canvas
from PIL import Image
import os
class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("My Window")
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.running = True
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def close(self):
        self.running = False
        self.root.quit()  

    def wait_for_close(self):
        while self.running:
            self.redraw()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def save_canvas_as_image(self, filename="maze.ps"):
        # Save the canvas to a PostScript file (ps format)
        # Find the next available file name (mazeX.png)
        file_number = 1
        while True:
            filename = f"maze{file_number}.png"
            filename = os.path.join("maze", filename)
            if not os.path.exists(filename):  # Check if the file already exists
                break
            file_number += 1
        #save the canvas as a Postscript file inside the maze folder
        if not os.path.exists("maze"):
            os.makedirs("maze")
        self.canvas.postscript(file=filename)
        print(f"Canvas saved as {filename}")
        
        # Optionally, convert it to PNG using Pillow
        try:
            img = Image.open(filename)
            img.save(filename.replace(".ps", ".png"))
            print(f"Canvas saved as {filename.replace('.ps', '.png')}")
        except ImportError:
            print("Pillow library is not installed. Cannot convert to PNG.")
