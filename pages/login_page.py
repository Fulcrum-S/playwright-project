from playwright.sync_api import Page

from pages.Base_Page import BasePage


class Login(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

    _account = ".fa.fa-user"
    _click_it = ".dropdown.open li:nth-child(2)>a"
    _email = "#input-email"
    _password = "#input-password"
    _click = "#content div input:nth-child(3)"
    _button = ".btn.btn-primary"
    _password_visible = "a:has-text('Forgotten Password')"
    _error_message = ".alert.alert-danger.alert-dismissible"
    _alert_danger = ".alert-danger"

    def open_login(self):
        self.click(self._account)
        self.click(self._click_it)

    def login(self, email, password):
        self.fill(self._email,email)
        self.fill(self._password,password)
        self.click(self._click)

    def password_visible(self):

        return self.is_visible(self._password_visible)

    def is_login_button_visible(self):
        return self.is_visible(self._button)


    def error_visible(self):
        return self.page.text_content(self._error_message)

    def alert_danger_content(self):
        return self.page.text_content(self._alert_danger)


