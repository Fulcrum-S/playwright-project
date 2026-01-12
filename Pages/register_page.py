from playwright.sync_api import Page

from Pages.Base_Page import BasePage


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




