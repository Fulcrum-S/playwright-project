import allure
import pytest


from tests.Base_Test import BaseTest


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
            assert self.products_page.first_product_visible()

    @allure.title("Select product")
    @allure.description("Verify product details page opens")
    @allure.severity(allure.severity_level.NORMAL)

    def test_select_product(self):
        with allure.step("search for product"):
            self.home_page.search_product("mac")
        with allure.step("select the product"):
            self.products_page.select_first_product()
        with allure.step("verify content in product page"):
            assert self.products_page.content_visible()


    @allure.title("Invalid product search")
    @allure.description("Verify message when searching invalid product")
    @allure.severity(allure.severity_level.MINOR)

    def test_invalid_product_search(self):
        with allure.step("search invalid product"):
            self.home_page.search_product("zzzzz")
        with allure.step("verify there is no product message"):
            assert "There is no product" in self.products_page.page.content()

    @allure.title("Verify product names are valid")
    @allure.description("All displayed products must have valid names")
    @allure.severity(allure.severity_level.NORMAL)

    def test_product_names_are_valid(self):
        with allure.step("Search for product"):
            self.home_page.search_product("Mac")
        with allure.step("Get product names"):
            product_names = self.products_page.get_product_names()
        with allure.step("Verify all product names are valid"):
            all_names_valid = True
            for name in product_names:
                if len(name) <= 1:
                    all_names_valid = False
                    break

            assert all_names_valid is True

    @allure.title("Verify search results count")
    @allure.description("Search should return results")
    @allure.severity(allure.severity_level.CRITICAL)

    def test_search_results_count(self):
        with allure.step("Search for product"):
            self.home_page.search_product("Mac")
        with allure.step("Get search results count"):
            results_count = self.products_page.get_products_count()
        with allure.step("Verify search returned results"):
            assert results_count > 0

    @allure.title("Verify all product names are valid")
    @allure.description("All products returned by search must have non-empty names")
    @allure.severity(allure.severity_level.NORMAL)

    def test_all_product_names_are_valid(self):
        with allure.step("Search for products"):
            self.home_page.search_product("Mac")
        with allure.step("Check all product names are valid"):
            result = self.products_page.all_product_names_valid()
            assert result is True

