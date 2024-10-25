import tkinter as tk
import Utils
from Suppliers import Suppliers
from views.Manager.ManagerProducts_view import ManagerProducts

class ManageSupplierView(tk.Frame):
    def __init__(self, controller):
        self.root = Utils.Toplevel("Supllier List")
        super().__init__(self.root)
        Utils.WinIcon(self.root, "./image/supplier_icon.png")
        self.root.geometry("600x660")
        self.controller = controller
        self.pack()

        self.suppliers_data = Suppliers()
        self.suppliers_data.seed_data()

        #Banner Frame
        self.bannerFrame = Utils.Frame(self)
        self.bannerImage = Utils.Image(self.bannerFrame, "./image/supplier.png").pack()
        self.bannerFrame.pack()

        #Seprator 1
        self.seprator1 = Utils.Separator(self).pack(fill="x", pady=10)

        #Title Frame
        self.titleFrame = Utils.Frame(self)

        self.titleFrame.grid_rowconfigure(0, weight=1)  # Top empty space
        self.titleFrame.grid_rowconfigure(1, weight=1)  # Center column
        self.titleFrame.grid_rowconfigure(2, weight=1)  # Bottom empty space

        self.title_label = tk.Label(self.titleFrame, text="Select a Supplier", font="Helvetica 15 bold", fg=Utils.python_blue)
        self.title_label.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.titleFrame.pack()

        #Seprator 2
        self.seprator2 = Utils.Separator(self).pack(fill="x", pady=20)

        #List Box
        self.supplier_listbox = tk.Listbox(self, height=20, width=600, font="Helvetica 10")
        self.supplier_listbox.pack(padx=10, ipady=5)

        for supplier in self.controller.getManagerSupplier():
            self.supplier_listbox.insert(tk.END, f"{supplier.name} ({supplier.region}), ({supplier.address})")


        #Buttons
        self.buttonsFrame = Utils.Frame(self)
        self.loginButton = tk.Button(self.buttonsFrame, text="Shop", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.show_products)
        self.loginButton.pack(side='left', expand=True, fill='x')
        self.exitButton = tk.Button(self.buttonsFrame, text="Close", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", bg=Utils.python_blue, command=self.close)
        self.exitButton.pack(side='right', expand=True, fill='x')
        self.buttonsFrame.pack(fill='x', side='bottom', pady=(27, 0))

    def view_supplier(self):
        # Get selected supplier
        selected_index = self.supplier_listbox.curselection()
        if selected_index:
            selected_supplier = self.controller.getManagerSupplier()[selected_index[0]]
            print(f"Viewing {selected_supplier.name}, located at {selected_supplier.address}.")
        else:
            print("No supplier selected.")

    def show_products(self):
        selected_index = self.supplier_listbox.curselection()
        if selected_index:
            selected_supplier = self.controller.getManagerSupplier()[selected_index[0]]
            ManagerProducts(self.root, selected_supplier, self.controller)
            self.close()
        else:
            print("Selection Error, Please select a supplier.")
        
    def close(self):
        self.root.destroy()