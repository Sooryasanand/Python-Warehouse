import tkinter as tk
import Utils

from PIL import Image as PImage
from PIL import ImageTk


class ErrorView(tk.Frame):
    def __init__(self, ErrorName:str, ErrorDesc:str):
        self.root = Utils.Toplevel("Error")
        super().__init__(self.root)

        Utils.WinIcon(self, "./image/error_icon.png")
        self.root.geometry("500x375")
        self.pack()

        #Image Frame
        self.imageFrame = Utils.Frame(self)
        self.image_banner = Utils.Image(self.imageFrame, "./image/error.png").pack()
        self.imageFrame.pack()

        #Seprator 1
        self.seprator1 = Utils.Separator(self).pack(fill="x", padx=10, pady=10)

        #Title Frame
        self.titleFrame = Utils.Frame(self)

        self.titleFrame.grid_rowconfigure(0, weight=1)  # Top empty space
        self.titleFrame.grid_rowconfigure(1, weight=1)  # Center column
        self.titleFrame.grid_rowconfigure(2, weight=1)  # Bottom empty space

        self.title_label = tk.Label(self.titleFrame, text="Error", font="Helvetica 15 bold", fg=Utils.python_blue)
        self.title_label.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.titleFrame.pack()

        #Seprator 2
        self.seprator2 = Utils.Separator(self).pack(fill="x", padx=10, pady=20)

        #Error Frame
        self.ErrorFrame = Utils.Frame(self)
        self.error_title = tk.Label(self.ErrorFrame, text=ErrorName, font="Helvetica 15 bold", foreground="#FF0000").pack()
        self.error_desc = Utils.Label(self.ErrorFrame, ErrorDesc).pack(pady=20)
        self.ErrorFrame.pack()
        
        #Button Frame
        self.ButtonFrame = Utils.Frame(self)
        self.close_button = tk.Button(self.ButtonFrame, text="Close", command=self.close, background=Utils.python_blue, padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2").pack(fill="x", side="bottom", expand=True)
        self.ButtonFrame.pack(fill="x")

    def close(self):
        self.root.destroy()