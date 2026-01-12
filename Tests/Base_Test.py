from Pages.login_page import Login
from Pages.products_page import Products
from Pages.register_page import Register
from Pages.home_page import Homepage
from Pages.cart_page import Cart


class BaseTest:
    register_page : Register
    home_page : Homepage
    login_page: Login
    cart_page: Cart
    products_page: Products