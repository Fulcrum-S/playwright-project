from playwright.sync_api import Page

from pages.Base_Page import BasePage


class Products(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

    _click_first_product = "#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1)"
    _image_of_first_product = ".product-thumb button[onclick*='cart.add']"
    _content_visible = "#content"
    _first_product_visible = ".product-thumb"
    _product_layout = ".product-layout"
    _product_caption = ".product-thumb.caption.h4 a"

    def select_first_product(self):
        self.click(self._click_first_product)

    def add_first_product_to_cart(self):
        self.click(self._image_of_first_product)

    def content_visible(self):
        return self.is_visible(self._content_visible)

    def first_product_visible(self):
        return self.is_visible(self._first_product_visible)

    def get_product_names(self):
        products = self.page.locator(self._product_caption)
        names = []

        for i in range(products.count()):
            names.append(products.nth(i).inner_text().strip())

        return names

    def get_products_count(self):
        return self.page.locator(self._product_layout).count()

    def all_product_names_valid(self):
        names = self.get_product_names()
        return len(names) > 0 and all(len(name) > 1 for name in names)

