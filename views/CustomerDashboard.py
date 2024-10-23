import tkinter as tk
import Utils
from views.Shop_view import ShopView


class CustomerDashboardView(tk.Frame):
    def __init__(self, username, controller):
        self.root = Utils.Toplevel("Customer Dashboard")
        super().__init__(self.root)
        Utils.WinIcon(self.root, "./image/user_icon.png")
        self.root.geometry("600x300")
        self.controller = controller
        self.pack()

        #Banner Frame
        self.bannerFrame = Utils.Frame(self)
        self.bannerImage = Utils.Image(self.bannerFrame, "./image/user.png").pack()
        self.bannerFrame.pack()

        #Seprator 1
        self.seprator1 = Utils.Separator(self).pack(fill="x", pady=10)

        #Title Frame
        self.titleFrame = Utils.Frame(self)

        self.titleFrame.grid_rowconfigure(0, weight=1)  # Top empty space
        self.titleFrame.grid_rowconfigure(1, weight=1)  # Center column
        self.titleFrame.grid_rowconfigure(2, weight=1)  # Bottom empty space

        self.title_label = tk.Label(self.titleFrame, text=f"Welcome to Customer Dashboard {username}", font="Helvetica 15 bold", fg=Utils.python_blue)
        self.title_label.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.titleFrame.pack()

        #Seprator 2
        self.seprator2 = Utils.Separator(self).pack(fill="x", pady=30)

        #Buttons Frame
        self.buttonsFrame = Utils.Frame(self)
        self.buttonsFrame.columnconfigure(0, weight=1)
        self.buttonsFrame.columnconfigure(1, weight=1)
        self.buttonsFrame.columnconfigure(2, weight=1)
        self.shopButton = tk.Button(self.buttonsFrame, text="Shop", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.shopView)
        self.shopButton.grid(row=0, column=0, sticky="EW")
        self.orderHisButton = tk.Button(self.buttonsFrame, text="Order History", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue)
        self.orderHisButton.grid(row=0, column=1, sticky="EW")
        self.close = tk.Button(self.buttonsFrame, text="Close", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", command=exit, bg=Utils.python_blue)
        self.close.grid(row=0, column=2, sticky="EW")
        
        self.buttonsFrame.pack(fill='x', expand=True, side='bottom')

    def shopView(self):
        ShopView(self.controller)




