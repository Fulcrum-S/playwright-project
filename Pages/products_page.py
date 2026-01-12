from playwright.sync_api import Page

from Pages.Base_Page import BasePage


class Products(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

    _click_s = "#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1)"
    _image = ".product-thumb button[onclick*='cart.add']"

    def select_first_product(self):
        self.click(self._click_s)

    def add_first_product_to_cart(self):
        self.click(self._image)

