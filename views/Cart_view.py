import tkinter as tk
from tkinter import ttk
import Utils
from views.add_view import AddView
from views.ViewCart_view import ViewCart
from views.Products_view import ProductView
import Product
import Order

class CartView(tk.Frame):
    def __init__(self, supplier, controller, products_view, refresh_treeview):
        self.root = Utils.Toplevel("Cart")
        super().__init__(self.root)
        Utils.WinIcon(self.root, "./image/cart_icon.png")
        self.root.geometry("600x650")
        self.pack()
        self.controller = controller
        self.supplier = supplier
        self.cart = self.controller.makeCart(self.supplier)
        self.refresh_treeview = refresh_treeview
        self.products_view = products_view
        self.controller.setCart(self)


        #Title Banner
        self.bannerFrame = tk.Frame(self)
        self.bannerImage = Utils.Image(self.bannerFrame, "./image/cart.png").pack(fill="x")
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

        # TreeView
        self.style = ttk.Style()

        self.style.map("Treeview", 
                       background=[("selected", Utils.python_blue)],
                       foreground=[("selected", "white")])

        columns = ('Name', 'Price', 'Stock')

        self.tree = ttk.Treeview(self, columns=columns, show='headings', height=10, selectmode='extended')
        
        self.tree.heading('Name', text='Name')
        self.tree.heading('Price', text='Price')
        self.tree.heading('Stock', text='Stock')

        self.tree.column('Name', width=250)
        self.tree.column('Price', width=100)
        self.tree.column('Stock', width=100)

        self.populate_treeview()

        self.tree.bind("<<TreeviewSelect>>", self.valid_userInput)

        self.tree.pack(padx=20, pady=10, fill="both", expand=True)

        # Separator3
        self.separator3 = ttk.Separator(self).pack(fill="x", pady=10)

        #Buttons
        self.buttonsFrame = Utils.Frame(self)

        self.addButton = tk.Button(self.buttonsFrame, text="Add", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.add_Button)
        self.addButton.pack(side='left', expand=True, fill='x')
        self.addButton.config(state="disabled", bg=Utils.blue_disable)
        self.viewButton = tk.Button(self.buttonsFrame, text="View", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.viewCart)
        self.viewButton.pack(side='right', expand=True, fill='x')
        self.cancelButton = tk.Button(self.buttonsFrame, text="Cancel", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.close)
        self.cancelButton.pack(side='left', expand=True, fill='x')
        self.checkoutButton = tk.Button(self.buttonsFrame, text="Checkout", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.checkout)
        self.checkoutButton.pack(side='right', expand=True, fill='x')
        self.buttonsFrame.pack(fill='x', side='bottom', pady=30)
    
    def valid_userInput(self, _):
        if len(self.tree.selection()):
            self.addButton.config(state="normal", bg=Utils.python_blue)
        else:
            self.addButton.config(state="disabled", bg=Utils.blue_disable)

    def populate_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for product in self.supplier.products.products:
            self.tree.insert('', tk.END, values=(product.name, f"${product.price:.2f}", product.stock))

    def add_Button(self):
        selected_items = self.tree.selection()
        for item in selected_items:
            product_info = self.tree.item(item, 'values')
            product = Product.Product(product_info[0], float(product_info[1][1:]), int(product_info[2]))
            AddView(product, self.controller)
            self.tree.delete(item)

    def viewCart(self):
        ViewCart(self.supplier, self.controller, self.cart)

    def close(self):
        self.root.destroy()

    def checkout(self):
        self.controller.addOrderHistory(self.cart)
        self.supplier.process_cart(self.cart)
        if self.refresh_treeview:
            print("refresh treeview is set and valid")
            self.refresh_treeview()
        self.tree.delete(*self.tree.get_children())
        self.root.destroy()
         
    
