import tkinter as tk
import Utils


class CustomerDashboardView(tk.Frame):
    def __init__(self):
        self.root = Utils.Toplevel("Customer Dashboard")
        super().__init__(self.root)
        self.root.geometry("600x300")
        self.pack()

