import allure
import pytest


from Tests.Base_Test import BaseTest


@pytest.mark.usefixtures("setup_page_function")

class TestHome(BaseTest):

    @allure.title("Verify home page title")
    @allure.description("Verify that home page title contains 'Your Store'")
    @allure.severity(allure.severity_level.CRITICAL)

    def test_home_title(self):
        with allure.step("Get home page title"):
            title= self.home_page.page.title()
        with allure.step("Verify title"):
            assert "Your Store" in title

    @allure.title("Verify logo visibility")
    @allure.description("Verify that the site logo is visible on home page")
    @allure.severity(allure.severity_level.NORMAL)

    def test_logo_visible(self):
        with allure.step("Check logo visibility"):
            assert self.home_page.is_visible("#logo")

    @allure.title("Verify search box visibility")
    @allure.description("Verify that search input field is displayed")
    @allure.severity(allure.severity_level.NORMAL)

    def test_search_box_visible(self):
        with allure.step("check search box visibility"):
            assert self.home_page.is_visible("[name='search']")

    @allure.title("Verify My Account menu")
    @allure.description("Verify My Account menu shows Login option")
    @allure.severity(allure.severity_level.MINOR)

    def test_my_account_menu_visible(self):
        with allure.step("Open My Account menu"):
            self.home_page.click_my_account()
        with allure.step("Verify Login option is visible"):
            assert self.home_page.is_visible("a:has-text('Login')")

    @allure.title("Verify footer exists")
    @allure.description("Verify footer section exists on home page")
    @allure.severity(allure.severity_level.MINOR)

    def test_container_container(self):
        with allure.step("scroll to container"):
            self.home_page.page.evaluate(
                "window.scrollTo(0, document.body.scrollHeight)"
            )
        with allure.step("Verify footer visibility"):
            assert self.home_page.is_visible(".container")

