import tkinter as tk
import Utils
from views.Login_view import LoginView
from views.CustomerDashboard import CustomerDashboardView
from views.Error_view import ErrorView


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()

        LoginWindow = Utils.Toplevel("Login")
        LoginWindow.geometry("600x300")

        loginView = LoginView(LoginWindow)
        loginView.pack(expand=True, fill='both')

        ErrorView("NoSuchUserException", "Invalid User")


if __name__ == "__main__":
    app = Application()
    app.mainloop() 

