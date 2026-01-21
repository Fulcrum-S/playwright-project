from playwright.sync_api import Page

from pages.Base_Page import BasePage


class Register(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)


    _account = ".fa.fa-user"
    _click = "#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a"
    _name = "#input-firstname"
    _last_name = "#input-lastname"
    _email = "#input-email"
    _password = "#input-password"
    _phone = "#input-telephone"
    _confirm = "#input-confirm"
    _click_final = ".btn.btn-primary"
    _affirm = "[name = 'agree']"
    _choose = "[name = 'newsletter']"
    _alert = ".alert-danger"
    _alert_danger = ".alert.alert-danger.alert-dismissible"
    _confirm_name = "[name='confirm']"
    _value = "[value='Continue']"
    _fill_first_name = "[name='firstname']"
    _continue_confirm = "[value='Continue']"

    def open_register(self):
        self.click(self._account)
        self.click(self._click)

    def register(self,name, last_name, phone, email, password, confirm):

        self.fill(self._name, name)
        self.fill(self._last_name, last_name)
        self.fill(self._email, email)
        self.fill(self._phone, phone)
        self.fill(self._password, password)
        self.fill(self._confirm, confirm)
        self.click(self._affirm)
        self.click(self._click_final)

    def alert_visible(self):
        return self.is_visible(self._alert)


    def alert_danger_visible(self):
        return self.is_visible(self._alert_danger)


    def confirm_is_visible(self):
        return self.is_visible(self._confirm_name)


    def value_visible(self):
        return self.is_visible(self._value)

    def fill_first_name(self,test):
        self.fill(self._fill_first_name, test)

    def click_continue(self):
        self.click(self._value)

    def wait_for_confirm(self):
        return self.page.wait_for_selector(self._confirm_name)

    def wait_for_continue(self):
        return self.page.wait_for_selector(self._continue_confirm)


