import tkinter as tk
from tkinter import ttk
import Utils
import Product

class Managing(tk.Frame):
    def __init__(self, cart, supplier, controller, refresh_callback):
        self.root = Utils.Toplevel(f"Managing")
        super().__init__(self.root)
        Utils.WinIcon(self.root, "./image/supplier_icon.png")
        self.root.geometry("600x536")
        self.controller = controller
        self.cart = cart
        self.supplier = supplier
        self.refresh_callback = refresh_callback
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

        self.title_label = tk.Label(self.titleFrame, text=f"Edit Supplier", font="Helvetica 15 bold", fg=Utils.python_blue)
        self.title_label.pack(pady=10)

        #Separator2
        self.separator2 = ttk.Separator(self).pack(fill="x", pady=20)

        #Listbox
        self.listboxFrame = tk.Frame(self)
        self.listbox = tk.Listbox(self.listboxFrame, height=10)
        self.populate_listbox()
        self.listbox.pack(padx=20, pady=10, fill="both", expand=True)
        self.listboxFrame.pack(fill="x")
        self.listbox.bind("<<ListboxSelect>>", lambda event: self.update_button_state())

        # Separator4
        self.separator4 = ttk.Separator(self).pack(fill="x", pady=10)

        #Buttons
        self.buttonsFrame = Utils.Frame(self)
        self.removeButton = tk.Button(self.buttonsFrame, text="Remove", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.remove_product)
        self.removeButton.pack(side='left', expand=True, fill='x')
        self.delistButton = tk.Button(self.buttonsFrame, text="Delist", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.delist_product)
        self.delistButton.pack(side='left', expand=True, fill='x')
        self.closeButton = tk.Button(self.buttonsFrame, text="Close", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.close)
        self.closeButton.pack(side='right', expand=True, fill='x')
        self.buttonsFrame.pack(fill='x', side='bottom', pady=[30, 0])



    def update_button_state(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            available_products = self.supplier.products.get_all_products()
            selected_product = available_products[selected_index[0]]
            if not selected_product.is_available():
                self.delistButton.config(state="disabled", bg=Utils.blue_disable)
            else:
                self.delistButton.config(state="normal", bg=Utils.python_blue)
    
    def populate_listbox(self):
        self.listbox.delete(0, tk.END)

        for product in self.supplier.products.get_all_products():
            self.listbox.insert(tk.END, f"{product.name} at ${product.price:.2f} ({product.stock})")

    def remove_product(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            available_products = self.supplier.products.get_all_products()
            selected_product = available_products[selected_index[0]]
            self.supplier.products.remove_product(selected_product)
            self.listbox.delete(selected_index)
            if self.refresh_callback:
                self.refresh_callback()
                
        else:
            print("Selection Error, Please select a product.")

    def delist_product(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            available_products = self.supplier.products.get_all_products()
            selected_product = available_products[selected_index[0]]
            selected_product.delist()
            self.update_button_state()
        else:
            print("Selection Error, Please select a product.")

    def refresh_listbox(self):
        self.populate_listbox()

    def close(self):
        self.root.destroy()
