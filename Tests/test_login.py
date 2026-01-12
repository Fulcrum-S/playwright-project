import allure
import pytest


from Tests.Base_Test import BaseTest


@pytest.mark.usefixtures("setup_page_function")

class TestLogin(BaseTest):
    @allure.title("Open login page")
    @allure.description("Verify that login page opens successfully")
    @allure.severity(allure.severity_level.NORMAL)

    def test_open_login_page(self):
        with allure.step("open login page"):
            self.login_page.open_login()
        with allure.step("verify login page in title"):
            assert "Account Login" in self.login_page.page.title()

    @allure.title("Invalid login attempt")
    @allure.description("Verify error message for invalid login credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("email,password", [("wrong@test.com", "1234")])

    def test_invalid_login(self,email,password):
        with allure.step("open login page"):
             self.login_page.open_login()
        with allure.step(f"enter invalid credentials:{email},{password}"):
            self.login_page.login(email,password)
        with allure.step("verify error message"):
            assert "No match" in self.login_page.page.text_content(".alert-danger")

    @allure.title("Empty login submission")
    @allure.description("Verify error message when submitting empty login form")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("email,password", [("", ""),])

    def test_empty_login(self,email,password):
        with allure.step("Open login page"):
            self.login_page.open_login()
        with allure.step(f"Submit empty login credentials:{email},{password}"):
            self.login_page.login(email,password)
        with allure.step("verify error message"):
            assert "No match" in self.login_page.page.text_content(".alert.alert-danger.alert-dismissible")

    @allure.title("Forgot password link")
    @allure.description("Verify Forgotten Password link is visible")
    @allure.severity(allure.severity_level.MINOR)

    def test_forgot_password_link_visible(self):
        with allure.step("open login page"):
            self.login_page.open_login()
        with allure.step("verify forgotten password link"):
            assert self.login_page.is_visible("a:has-text('Forgotten Password')")

    @allure.title("Login button visibility")
    @allure.description("verify login button is visible")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_button_visible(self):
        with allure.step("open login page"):
            self.login_page.open_login()
        with allure.step("verify login button is displayed on login page"):
            assert self.login_page.is_visible(".btn.btn-primary")
