import tkinter as tk
from tkinter import ttk
import Utils

class OrderHistory(tk.Frame):
    def __init__(self, controller):
        self.root = Utils.Toplevel("Order History")
        super().__init__(self.root)
        Utils.WinIcon(self.root, "./image/user_icon.png")
        self.root.geometry("600x600")
        self.controller = controller
        self.pack()

        #Banner Frame
        self.bannerFrame = Utils.Frame(self)
        self.bannerImage = Utils.Image(self.bannerFrame, "./image/user.png").pack()
        self.bannerFrame.pack()

        #Seprator 1
        self.seprator1 = Utils.Separator(self).pack(fill="x", pady=10)

        #Title Frame
        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack(fill="x")

        self.title_label = tk.Label(self.titleFrame, text="Order History", font="Helvetica 15 bold", fg=Utils.python_blue)
        self.title_label.pack(pady=10)

        #Seprator 2
        self.seprator2 = Utils.Separator(self).pack(fill="x", pady=30)

        self.table_frame = Utils.Frame(self)
        columns = ("History")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show='headings', height=10, selectmode='none')
        self.tree.heading('History', text='History')
        self.tree.column('History', width=500)
        self.update_treeview()
        self.tree.pack(padx=20, pady=10, fill="both", expand=True)
        self.table_frame.pack()

        #Button
        self.buttonsFrame = Utils.Frame(self)
        self.addButton = tk.Button(self.buttonsFrame, text="Close", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.close)
        self.addButton.pack(side='left', expand=True, fill='x')
        self.buttonsFrame.pack(fill='x', side='bottom', pady=(20, 0))

    def update_treeview(self):
        for cart in self.controller.getOrderHistory():
            print(cart.supplier.region)
            self.tree.insert('', tk.END, values=(f"{cart.supplier.region}:",))
            for order in cart.orders:
                print(order.product.name)
                print(order.quantity)
                self.tree.insert('', tk.END, values=(f"{order.product.name} ({order.quantity})",))
            self.tree.insert("", tk.END, values=(f"Total cost: ${cart.get_total_cost()}",))

    def close(self):
        self.root.destroy()

        