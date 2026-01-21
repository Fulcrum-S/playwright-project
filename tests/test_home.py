import allure
import pytest


from tests.Base_Test import BaseTest


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
            assert self.home_page.logo_is_visible()

    @allure.title("Verify search box visibility")
    @allure.description("Verify that search input field is displayed")
    @allure.severity(allure.severity_level.NORMAL)

    def test_search_box_visible(self):
        with allure.step("check search box visibility"):
            assert self.home_page.search_is_visible()

    @allure.title("Verify My Account menu")
    @allure.description("Verify My Account menu opens and shows Login option")
    @allure.severity(allure.severity_level.MINOR)

    def test_my_account_menu_visible(self):
        with allure.step("Open My Account menu"):
            self.home_page.click_my_account()
        with allure.step("Verify Login option is visible"):
            assert self.home_page._login_menu_visible

    @allure.title("Verify footer exists")
    @allure.description("Verify footer section exists on home page")
    @allure.severity(allure.severity_level.MINOR)

    def test_container_container(self):
        with allure.step("scroll to container"):
            self.home_page.scrolling_bar()
        with allure.step("Verify footer visibility"):
            assert self.home_page.container_is_visible()

    @allure.title("Verify My Account dropdown options")
    @allure.description("Verify My Account dropdown contains options")
    @allure.severity(allure.severity_level.NORMAL)

    def test_my_account_dropdown_options(self):
        with allure.step("Get My Account dropdown options"):
            options = self.home_page.get_my_account_options()
        with allure.step("Verify at least two options exist"):
            assert len(options) >= 2

    @allure.title("Verify featured products exist")
    @allure.description("Verify home page displays featured products")
    @allure.severity(allure.severity_level.NORMAL)

    def test_featured_products_exist(self):
        with allure.step("Get featured products count"):
            products_count = self.home_page.get_featured_products_count()
        with allure.step("Verify featured products are displayed"):
            assert products_count > 0

    @allure.title("Verify homepage main carousel exists")
    @allure.description("The homepage should have a main carousel with at least one slide")
    @allure.severity(allure.severity_level.MINOR)

    def test_homepage_carousel_exists(self):
        with allure.step("Check if homepage carousel has slides"):
            result = self.home_page.is_carousel_present()
            assert result is True
