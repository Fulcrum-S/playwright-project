from playwright.sync_api import Page

from pages.Base_Page import BasePage


class Cart(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

    _cart= "#cart-total"
    _click_prod = ".fa.fa-shopping-cart"
    _txt_message = "#content > p"
    _remove = ".fa.fa-times-circle"
    _checkout = ".fa.fa-share"
    _cart_visible = "#cart-total"
    _view_cart = "#cart > ul > li:nth-child(2) > div > p > a:nth-child(1) > strong"
    _txt_center = "#cart > ul > li > p"



    def cart_visible(self):
        return self.is_visible(self._cart_visible)

    def open_cart(self):
        self.page.click(self._cart)

    def get_cart_message(self):
        return self.page.inner_text(self._txt_center)

    def remove_product(self):
        self.click(self._remove)

    def checkout(self):
        self.click(self._checkout)

    def view_cart(self):
        self.click(self._view_cart)

    def shopping_cart_message(self):
        return self.page.inner_text(self._txt_message)

