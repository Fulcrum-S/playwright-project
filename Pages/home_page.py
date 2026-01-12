from playwright.sync_api import Page

from Pages.Base_Page import BasePage


class Homepage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

    _click_acc = ".dropdown-toggle"
    _search = ".form-control.input-lg"


    def click_my_account(self):
        self.click(self._click_acc)

    def search_product(self, product):
        self.fill(self._search,product)
        self.press_enter()
