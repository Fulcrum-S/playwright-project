from pages.login_page import Login
from pages.products_page import Products
from pages.register_page import Register
from pages.home_page import Homepage
from pages.cart_page import Cart


class BaseTest:
    register_page : Register
    home_page : Homepage
    login_page: Login
    cart_page: Cart
    products_page: Products