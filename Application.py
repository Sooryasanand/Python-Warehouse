import tkinter as tk
import Utils
from views.Login_view import LoginView
from views.CustomerDashboard import CustomerDashboardView
from views.Error_view import ErrorView
from controller.Controller import Controller


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()

        LoginWindow = Utils.Toplevel("Login")
        LoginWindow.geometry("600x300")

        loginView = LoginView(LoginWindow)
        loginController = Controller(loginView)
        loginView.set_controller(loginController)

        loginView.pack(expand=True, fill='both')

if __name__ == "__main__":
    app = Application()
    app.mainloop() 