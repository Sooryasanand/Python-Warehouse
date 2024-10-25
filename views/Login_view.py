import tkinter as tk
import Utils
import Organisation
import User
from views import CustomerDashboard
from views.Manager import ManagerDashboard


class LoginView(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root or Utils.Toplevel("Login View")
        Utils.WinIcon(self.root, "./image/login_icon.png")
        self.controller = None
        self.pack()
        
        #Title
        self.titleFrame = Utils.Frame(self)

        self.titleFrame.grid_columnconfigure(0, weight=1)  # Left empty space
        self.titleFrame.grid_columnconfigure(1, weight=1)  # Center column
        self.titleFrame.grid_columnconfigure(2, weight=1)  # Right empty space
        self.titleFrame.grid_rowconfigure(0, weight=1)  # Top empty space
        self.titleFrame.grid_rowconfigure(1, weight=1)  # Center column
        self.titleFrame.grid_rowconfigure(2, weight=1)  # Bottom empty space

        self.titleLabel = Utils.Label(self.titleFrame, text="Login").grid(row=0, column=0, columnspan=3, rowspan=2, sticky="nsew", padx=10, pady=10)
        self.titleFrame.pack(ipadx=18, ipady=18)

        #Seperator
        self.seperator1 = Utils.Separator(self)
        self.seperator1.pack(fill="x")
        
        #Input
        self.inputFrame = Utils.Frame(self)

        self.inputFrame.grid_columnconfigure(0, weight=1)  # Left empty space
        self.inputFrame.grid_columnconfigure(1, weight=1)  # Center column
        self.inputFrame.grid_columnconfigure(2, weight=1)  # Right empty space
        self.inputFrame.grid_rowconfigure(0, weight=1)  # Top empty space
        self.inputFrame.grid_rowconfigure(1, weight=1)  # Center column
        self.inputFrame.grid_rowconfigure(2, weight=1)  # Bottom empty space

        self.userLabel = Utils.Label(self.inputFrame, text="Username:").grid(row=0, column=0, rowspan=1)
        self.userInput = tk.Entry(self.inputFrame, font="Helvetica 12 bold", foreground=Utils.python_blue)
        self.userInput.grid(row=0, column=1, rowspan=1)
        self.passLabel = Utils.Label(self.inputFrame, text="Password:").grid(row=1, column=0, rowspan=3)
        self.passInput = tk.Entry(self.inputFrame, font="Helvetica 12 bold", foreground=Utils.python_blue, show="*")
        self.passInput.grid(row=1, column=1, rowspan=3)

        self.userInput.bind("<KeyRelease>", self.valid_userInput)
        self.passInput.bind("<KeyRelease>", self.valid_userInput)

        self.inputFrame.pack(pady=50, padx=50)

        #Buttons
        self.buttonsFrame = Utils.Frame(self)

        self.loginButton = tk.Button(self.buttonsFrame, text="Login", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", command=self.login)
        self.loginButton.pack(side='left', expand=True, fill='x')
        self.loginButton.config(state="disabled", bg=Utils.blue_disable)
        self.exitButton = tk.Button(self.buttonsFrame, text="Exit", padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white", cursor="hand2", command=exit)
        self.exitButton.pack(side='right', expand=True, fill='x')
        self.exitButton.config(bg=Utils.python_blue)
        self.buttonsFrame.pack(fill='x', side='bottom')

    def valid_userInput(self, _):
        if self.userInput.get() and self.passInput.get():
            self.loginButton.config(state="normal", bg=Utils.python_blue)
        else:
            self.loginButton.config(state="disabled", bg=Utils.blue_disable)

    def set_controller(self, controller):
        self.controller = controller

    def login(self):
        usernameInput = self.userInput.get()
        passwordInput = self.passInput.get()
        if self.controller is not None:
            user = self.controller.login(usernameInput, passwordInput)
            if user is not None:
                self.close()
            else:
                print("Login Failed")
        else:
            print("Controller Failed")

    def close(self):
        self.root.destroy()