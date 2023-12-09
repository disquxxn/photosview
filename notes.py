import tkinter as tk #tk used as an alias
from tkinter import filedialog #sub-module used for opening file dialogs in your GUI
from PIL import Image, ImageTk # Python Imaging Library, sub-modules used for opening and displaying images.

class SimpPhotoViewer: # in oop, class is blue print for creating objects
    def __init__(self, root):
        self.root = root
        self.root.title("Simp Photo Viewer")

        #setup label to display image
        self.img_label = tk.Label(root)
        self.img_label.pack()

        #setup buttons to open images 
        self.open_btn = tk.Button(root, text="Open Image", command=self.open_image)
        self.open_btn.pack()

    def open_image(self):
        # File dialog to choose an image
        file_path = filedialog.askopenfilename()
        if file_path:
            # Open and display the image
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            self.img_label.config(image=photo)
            self.img_label.image = photo  # keep a reference

root = tk.Tk()
app = SimplePhotoViewer(root)
root.mainloop()