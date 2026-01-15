import allure
import pytest


from Tests.Base_Test import BaseTest


@pytest.mark.usefixtures("setup_page_function")

class TestRegister(BaseTest):

    @allure.title("Open register page")
    @allure.description("Verify that register account page opens")
    @allure.severity(allure.severity_level.NORMAL)

    def test_open_register_page(self):
        with allure.step("open register page"):
            self.register_page.open_register()
        with allure.step("verify register page opens"):
            assert "Register Account" in self.register_page.page.title()


    @allure.title("Submit empty register credentials")
    @allure.description("Verify validation errors for empty register credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("name,last_name,phone,email,password,confirm",[("", "", "", "", "", "")])
    def test_register_empty_credentials(self,name,last_name,phone,email,password,confirm):
        with allure.step("open register page"):
            self.register_page.open_register()
        with allure.step("enter empty credentials"):
            self.register_page.register(name, last_name, phone, email, password, confirm)
        with allure.step("verify error message"):
            assert self.register_page.is_visible(".alert-danger")

    @allure.title("Privacy policy required")
    @allure.description("Verify privacy policy must be accepted")
    @allure.severity(allure.severity_level.CRITICAL)

    def test_privacy_policy_required(self):
        with allure.step("Open register page"):
            self.register_page.open_register()
        with allure.step("fill in first name field"):
            self.register_page.fill("[name='firstname']", "Test")
        with allure.step("Submit without accepting policy"):
            self.register_page.page.click("[value='Continue']")
        with allure.step("verify validation error"):
            assert self.register_page.is_visible(".alert.alert-danger.alert-dismissible")

    @allure.title("Confirm password field visibility")
    @allure.description("Verify confirm password field is present")
    @allure.severity(allure.severity_level.MINOR)

    def test_confirm_password_visible(self):
        with allure.step("open register page"):
            self.register_page.open_register()
        with allure.step("verify confirm password button is visible"):
            assert self.register_page.is_visible("[name='confirm']")

    @allure.title("Continue button visibility")
    @allure.description("Verify Continue button is displayed")
    @allure.severity(allure.severity_level.NORMAL)

    def test_continue_button_visible(self):
        with allure.step("open register page"):
            self.register_page.open_register()
        with allure.step("verify continue button"):
            assert self.register_page.is_visible("[value='Continue']")