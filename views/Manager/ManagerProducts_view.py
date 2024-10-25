import tkinter as tk
from tkinter import ttk
import Utils
from views.Manager.Managing_view import Managing

class ManagerProducts(tk.Frame):
    def __init__(self, cart, supplier, controller):
        self.root = Utils.Toplevel(f"Supplier: {supplier.name}")
        super().__init__(self.root)
        Utils.WinIcon(self.root, "./image/supplier_icon.png")
        self.root.geometry("600x685")
        self.controller = controller
        self.cart = cart
        self.supplier = supplier
        self.pack()

        #Title Banner
        self.bannerFrame = tk.Frame(self)
        self.bannerImage = Utils.Image(self.bannerFrame, "./image/supplier.png").pack(fill="x")
        self.bannerFrame.pack(fill="x")

        #Separator1
        self.separator1 = ttk.Separator(self).pack(fill="x", pady=10)

        #Title Frame
        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack(fill="x")

        self.title_label = tk.Label(self.titleFrame, text=f"Welcome to {supplier.name} (Total Profit: {supplier.profit:.2f})", font="Helvetica 15 bold", fg=Utils.python_blue)
        self.title_label.pack(pady=10)

        #Separator2
        self.separator2 = ttk.Separator(self).pack(fill="x", pady=20)

        #checkbox
        self.checkbox_var = tk.BooleanVar()

        # Create the Checkbutton (checkbox)
        self.checkbox = tk.Checkbutton(self, text="Filter by available", variable=self.checkbox_var, command=self.checkbox_filter)
        self.checkbox.pack(pady=10)

        #Separator3
        self.separator3 = ttk.Separator(self).pack(fill="x", pady=20)


        #TreeView
        self.style = ttk.Style()

        columns = ('Name', 'Price', 'Stock')
        self.tree = ttk.Treeview(self, columns=columns, show='headings', height=10, selectmode='none')

        self.tree.heading('Name', text='Name')
        self.tree.heading('Price', text='Price')
        self.tree.heading('Stock', text='Stock')

        self.tree.column('Name', width=250)
        self.tree.column('Price', width=100)
        self.tree.column('Stock', width=100)

        self.populate_treeview()

        self.tree.pack(padx=20, pady=10, fill="both", expand=True)

        self.tree.bind("<<TreeviewSelect>>", self.disable_select)

        # Separator4
        self.separator4 = ttk.Separator(self).pack(fill="x", pady=10)

        #Buttons
        self.buttonsFrame = Utils.Frame(self)
        self.manageButton = tk.Button(self.buttonsFrame, text="Manage", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.manage_button)
        self.manageButton.pack(side='left', expand=True, fill='x')
        self.orderButton = tk.Button(self.buttonsFrame, text="Order", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.order_button)
        self.orderButton.pack(side='left', expand=True, fill='x')
        self.closeButton = tk.Button(self.buttonsFrame, text="Close", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.close)
        self.closeButton.pack(side='right', expand=True, fill='x')
        self.buttonsFrame.pack(fill='x', side='bottom', pady=[30, 0])

    def disable_select(self, event):
        return "break"
    
    def checkbox_filter(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        if self.checkbox_var.get():
            products = self.supplier.products.get_available_products()
        else:
            products = self.supplier.products.get_all_products()
        
        for product in products:
            self.tree.insert('', tk.END, values=(product.name, f"${product.price:.2f}", product.stock))

    
    def populate_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for product in self.supplier.products.get_all_products():
            if product.stock > 0:
                self.tree.insert('', tk.END, values=(product.name, f"${product.price:.2f}", product.stock))

    def refresh_treeview(self):
        self.populate_treeview()

    def manage_button(self):
        Managing(self.root, self.supplier, self.controller, self.refresh_treeview)

    def order_button(self):
        from views.Cart_view import CartView
        CartView(self.supplier, self.controller, self, self.refresh_treeview)

    def close(self):
        self.root.destroy()
