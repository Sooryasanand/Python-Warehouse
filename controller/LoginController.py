from Organisation import Organisation
from views.Login_view import LoginView


class LoginController:
    def __init__(self, root):
        self.model = Organisation()

        self.loginView = LoginView(root)
        self.loginView.set_controller(self)

    def login(self, username, password):
        if self.model.users.validate_user(username=username, password=password):
            print("User Logged In")
            return True
        else:
            print("User not logged in")
            return False