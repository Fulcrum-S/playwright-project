from playwright.sync_api import Page

from Pages.Base_Page import BasePage


class Login(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

    _account = ".fa.fa-user"
    _click_it = ".dropdown.open li:nth-child(2)>a"
    _email = "#input-email"
    _password = "#input-password"
    _click = "#content div input:nth-child(3)"

    def open_login(self):
        self.click(self._account)
        self.click(self._click_it)

    def login(self, email, password):
        self.fill(self._email,email)
        self.fill(self._password,password)
        self.click(self._click)



