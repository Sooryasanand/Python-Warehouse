import tkinter as tk
import Utils
from Suppliers import Suppliers

class ShopView():
    def __init__(self, root=None):
        super().__init__(root)
        self.root = Utils.Toplevel("Shop View")
        Utils.WinIcon(self, "./image/user_icon.png")
        self.root.geometry("600x300")
        self.pack()

        #Banner Frame
        self.bannerFrame = Utils.Frame(self)
        self.bannerImage = Utils.Image(self.bannerFrame, "./image/supplier.png").pack()
        self.bannerFrame.pack()

        #Seprator 1
        self.seprator1 = Utils.Separator(self).pack(fill="x", padx=10, pady=10)

        #Title Frame
        self.titleFrame = Utils.Frame(self)

        self.titleFrame.grid_rowconfigure(0, weight=1)  # Top empty space
        self.titleFrame.grid_rowconfigure(1, weight=1)  # Center column
        self.titleFrame.grid_rowconfigure(2, weight=1)  # Bottom empty space

        self.title_label = tk.Label(self.titleFrame, text="Select a Supplier", font="Helvetica 15 bold", fg=Utils.python_blue)
        self.title_label.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.titleFrame.pack()

        #Seprator 2
        self.seprator2 = Utils.Separator(self).pack(fill="x", padx=10, pady=20)
        