import tkinter as tk
from tkinter import ttk
import Utils
from views.add_view import AddView
import Product
import Cart

class ViewCart(tk.Frame):
    def __init__(self, supplier, controller, cart):
        self.root = Utils.Toplevel("View Cart")
        super().__init__(self.root)
        Utils.WinIcon(self.root, "./image/cart_icon.png")
        self.root.geometry("600x600")
        self.pack()
        self.controller = controller
        self.cart = cart

        #Title Banner
        self.bannerFrame = tk.Frame(self)
        self.bannerImage = Utils.Image(self.bannerFrame, "./image/cart.png").pack(fill="x")
        self.bannerFrame.pack(fill="x")

        #Separator1
        self.separator1 = ttk.Separator(self).pack(fill="x", pady=10)

        #Title Frame
        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack(fill="x")

        self.title_label = tk.Label(self.titleFrame, text=f"Your Cart", font="Helvetica 15 bold", fg=Utils.python_blue)
        self.title_label.pack(pady=10)

        #Separator2
        self.separator2 = ttk.Separator(self).pack(fill="x", pady=20)

        # TreeView
        self.style = ttk.Style()

        self.style.map("Treeview", 
                       background=[("selected", Utils.python_blue)],
                       foreground=[("selected", "white")])

        columns = ('Name', 'Stock')
        self.tree = ttk.Treeview(self, columns=columns, show='headings', height=10, selectmode='extended')
        
        self.tree.heading('Name', text='Name')
        self.tree.heading('Stock', text='Stock')

        self.tree.column('Name', width=250)
        self.tree.column('Stock', width=100)

        for order in cart.orders:
            self.tree.insert('', tk.END, values=(order.product.name, order.quantity))

        self.tree.bind("<<TreeviewSelect>>", self.valid_userInput)

        self.tree.pack(padx=20, pady=10, fill="both", expand=True)

        # Separator3
        self.separator3 = ttk.Separator(self).pack(fill="x", pady=10)

        #Buttons
        self.buttonsFrame = Utils.Frame(self)

        self.removeButton = tk.Button(self.buttonsFrame, text="Remove", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.remove)
        self.removeButton.pack(side='left', expand=True, fill='x')
        self.removeButton.config(state="disabled", bg=Utils.blue_disable)
        self.closeButton = tk.Button(self.buttonsFrame, text="Cancel", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.close)
        self.closeButton.pack(side='right', expand=True, fill='x')
        self.buttonsFrame.pack(fill='x', side='bottom', pady=[32, 0])

    def valid_userInput(self, _):
        if len(self.tree.selection()):
            self.removeButton.config(state="normal", bg=Utils.python_blue)
        else:
            self.removeButton.config(state="disabled", bg=Utils.blue_disable)

    def remove(self):
        selected_items = self.tree.selection()
        for item in selected_items:
            product_name = self.tree.item(item, 'values')[0]
            order_to_remove = None
            for order in self.cart.orders:
                if order.product.name == product_name:
                    order_to_remove = order
                    break

            if order_to_remove:
                self.cart.remove_order(order_to_remove)
                self.tree.delete(item)


    def close(self):
        self.root.destroy()