import tkinter as tk 
from tkinter import filedialog 
from PIL import Image, ImageTk 

class SimpPhotoViewer: 
    def __init__(self, root):
        self.root = root
        self.root.title("Simp Photo Viewer")

        self.img_label = tk.Label(root)
        self.img_label.pack()

        self.open_btn = tk.Button(root, text="Open Image", command=self.open_image)
        self.open_btn.pack()

    def open_image(self):
        
        file_path = filedialog.askopenfilename()
        if file_path:

            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            self.img_label.config(image=photo)
            self.img_label.image = photo  

root = tk.Tk()
app = SimplePhotoViewer(root)
root.mainloop()
