from NoSuchUserException import NoSuchUserException
from Organisation import Organisation
from views.Login_view import LoginView
from views.Error_view import ErrorView
import Cart


class Controller:
    def __init__(self, root):
        self.model = Organisation()
        self.cart = None

    def login(self, username, password):
        try:
            user = self.model.users.validate_user(username=username, password=password)
            self.model.logged_in_user = user
            return user
        except NoSuchUserException:
            ErrorView("NoSuchUserException", "Invalid Credentials")

    def makeCart(self, supplier):
        self.cart = Cart.Cart(supplier, Organisation.logged_in_user)
        return self.cart
        
    def addOrder(self, order):
        self.cart.add_order(order)
            