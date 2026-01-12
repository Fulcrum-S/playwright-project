import allure
import pytest


from Tests.Base_Test import BaseTest


@pytest.mark.usefixtures("setup_page_function")

class TestProducts(BaseTest):

    @allure.title("Search product")
    @allure.description("Verify product in page title")
    @allure.severity(allure.severity_level.NORMAL)

    def test_search_product(self):
        with allure.step("search for product"):
            self.home_page.search_product("Mac")
        with allure.step("verify product mac in page title"):
            assert "Mac" in self.products_page.page.title()

    @allure.title("product result in product page")
    @allure.description("Verify product is displayed for valid search")
    @allure.severity(allure.severity_level.NORMAL)

    def test_product_results_visible(self):
        with allure.step("search for product"):
            self.home_page.search_product("Mac")
        with allure.step("verify product is visible") :
            assert self.products_page.is_visible(".product-thumb")

    @allure.title("Select product")
    @allure.description("Verify product details page opens")
    @allure.severity(allure.severity_level.NORMAL)

    def test_select_product(self):
        with allure.step("search for product"):
            self.home_page.search_product("mac")
        with allure.step("select the product"):
            self.products_page.select_first_product()
        with allure.step("verify content in product page"):
            assert self.products_page.is_visible("#content")

    @allure.title("Add product to cart")
    @allure.description("Verify product is added to cart successfully")
    @allure.severity(allure.severity_level.BLOCKER)

    def test_add_product_to_cart(self):
        with allure.step("search product"):
            self.home_page.search_product("Mac")
        with allure.step("add product to cart"):
            self.products_page.add_first_product_to_cart()
        with allure.step("verify success alert"):
            assert self.home_page.page.wait_for_selector(".alert-success")

    @allure.title("Invalid product search")
    @allure.description("Verify message when searching invalid product")
    @allure.severity(allure.severity_level.MINOR)

    def test_invalid_product_search(self):
        with allure.step("search invalid product"):
            self.home_page.search_product("zzzzz")
        with allure.step("verify there is no product message"):
            assert "There is no product" in self.products_page.page.content()