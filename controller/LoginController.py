from NoSuchUserException import NoSuchUserException
from Organisation import Organisation
from views.Login_view import LoginView
from views.Error_view import ErrorView


class LoginController:
    def __init__(self, root):
        self.model = Organisation()

    def login(self, username, password):
        try:
            user = self.model.users.validate_user(username=username, password=password)
            self.model.logged_in_user = user
            return user
        except NoSuchUserException:
            ErrorView("NoSuchUserException", "Invalid Credentials")
            