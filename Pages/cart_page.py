from playwright.sync_api import Page

from Pages.Base_Page import BasePage


class Cart(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

    _cart= "#cart-total"
    _click_prod = ".fa.fa-shopping-cart"

    def add_iphone_to_cart(self):
        self.click(self._click_prod)

    def open_cart(self):
        self.page.click(self._cart)

    def get_cart_message(self):
        return self.page.inner_text(".text-center")

    def remove_product(self):
        self.click(".btn.btn-danger.btn-xs")

    def checkout(self):
        self.click(".fa.fa-share")