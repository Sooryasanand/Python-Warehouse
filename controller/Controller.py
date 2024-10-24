from NoSuchUserException import NoSuchUserException
from Organisation import Organisation
from views.Login_view import LoginView
from views.Manager import ManagerDashboard
from views import CustomerDashboard
import User
from Manager import Manager
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
            if isinstance(self.model.logged_in_user, Manager):
                ManagerDashboard.ManagerDashboardView(self.model.logged_in_user.get_first_name(), self)
            else:
                CustomerDashboard.CustomerDashboardView(self.model.logged_in_user.get_first_name(), self)
            return user
        except NoSuchUserException:
            ErrorView("NoSuchUserException", "Invalid Credentials")


    def open_manager_dashboard(self, manager):
        print(f"Opening Manager dashboard for {manager.username}")

    def open_customer_dashboard(self, customer):
        print(f"Opening Customer dashboard for (customer.username)")

    def makeCart(self, supplier):
        self.cart = Cart.Cart(supplier, Organisation.logged_in_user)
        return self.cart
    
    def addOrder(self, order):
        self.cart.add_order(order)

    def addOrderHistory(self, cart):
        self.model.logged_in_user.add_purchase(cart)

    def getOrderHistory(self):
        return self.model.logged_in_user.purchases

    def addProductToCart(self, product):
        self.cartView.populate_treeview()

    def setCart(self, cartView):
        self.cartView = cartView

    def getManagerSupplier(self):
        return self.model.logged_in_user.suppliers.suppliers
            