from playwright.sync_api import Page

from pages.Base_Page import BasePage


class HeaderArea(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)


