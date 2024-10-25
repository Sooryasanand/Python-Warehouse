import tkinter as tk
from tkinter import ttk
import Utils
import Cart
import Order
from InvalidQuantityException import InvalidQuantityException
from views.Error_view import ErrorView

class AddView(tk.Frame):
    def __init__(self, product, controller):
        self.root = Utils.Toplevel("Cart")
        super().__init__(self.root)
        Utils.WinIcon(self.root, "./image/cart_icon.png")
        self.root.geometry("600x400")
        self.pack()
        self.product = product
        self.controller = controller

        #Title Banner
        self.bannerFrame = tk.Frame(self)
        self.bannerImage = Utils.Image(self.bannerFrame, "./image/cart.png").pack(fill="x")
        self.bannerFrame.pack(fill="x")

        #Separator1
        self.separator1 = ttk.Separator(self).pack(fill="x", pady=10)

        #Title Frame
        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack(fill="x")

        self.title_label = tk.Label(self.titleFrame, text=f"Adding {product.name}", font="Helvetica 15 bold", fg=Utils.python_blue)
        self.title_label.pack(pady=10)

        #Input Frame
        self.inputFrame = Utils.Frame(self)
        self.quantityLabel = Utils.Label(self.inputFrame, text="Stock:").grid(row=0, column=0, rowspan=1)
        self.quantityInput = tk.Entry(self.inputFrame, font="Helvetica 12 bold", foreground=Utils.python_blue)
        self.quantityInput.grid(row=0, column=1, rowspan=1)
        self.inputFrame.pack()

        #Buttons 
        self.buttonsFrame = Utils.Frame(self)
        self.addButton = tk.Button(self.buttonsFrame, text="Add", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.submit_order)
        self.addButton.pack(side='left', expand=True, fill='x')
        self.buttonsFrame.pack(fill='x', side='bottom', pady=(20, 0))

    def submit_order(self):
        try:
            # Fetch the quantity from the input field
            quantity = self.quantityInput.get()

            # Check if the input is valid
            if not quantity.isdigit() or int(quantity) <= 0 or int(quantity) > self.product.stock:
                raise InvalidQuantityException()

            # Convert the quantity to integer
            order = Order.Order(self.product, int(quantity))
            
            # Add the order to the cart
            self.controller.addOrder(order)

            # Update product stock
            self.product.stock -= int(quantity)
            print(f"Updated product stock for {self.product.name}: {self.product.stock}")

            self.root.destroy()
        except InvalidQuantityException:
            ErrorView("InvalidQuantityException", "Invalid Quantity")


    