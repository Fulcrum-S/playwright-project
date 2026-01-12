from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from Pages.Base_Page import BasePage


class NextComponent(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)



    def next(self):
        self.click()


