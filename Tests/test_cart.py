import allure
import pytest


from Tests.Base_Test import BaseTest


@pytest.mark.usefixtures("setup_page_function")

class TestCart(BaseTest):

    @allure.title("Verify empty cart message")
    @allure.description("Verify message displayed when cart is empty")
    @allure.severity(allure.severity_level.NORMAL)

    def test_cart_empty_message(self):
        with allure.step("open cart"):
            self.cart_page.open_cart()
        with allure.step("verify empty shopping cart"):
            assert "Your shopping cart is empty!" in self.cart_page.get_cart_message()

    @allure.title("Verify cart item button")
    @allure.description("Verify cart item button is visible")
    @allure.severity(allure.severity_level.NORMAL)

    def test_cart_button_title(self):
        with allure.step("open cart"):
            self.cart_page.open_cart()
        with allure.step("verify cart item button"):
            assert self.cart_page.is_visible("#cart-total")


    @allure.title("Verify cart page title")
    @allure.description("Verify cart page title is correct")
    @allure.severity(allure.severity_level.NORMAL)

    def test_cart_page_title(self):
        with allure.step("Open cart"):
            self.cart_page.open_cart()
        with allure.step("Verify title"):
            assert "Shopping Cart" in self.cart_page.page.title()

    @allure.title("Remove product from cart")
    @allure.description("Verify product can be removed from cart")
    @allure.severity(allure.severity_level.BLOCKER)

    def test_remove_product_from_cart(self):
        with allure.step("search product mac"):
            self.home_page.search_product("Mac")
        with allure.step("add the product to the cart"):
            self.products_page.add_first_product_to_cart()
        with allure.step("open the cart"):
            self.cart_page.open_cart()
        with allure.step("remove the product from the cart"):
            self.cart_page.remove_product()
        with allure.step("verify cart is empty"):
            assert "Your shopping cart is empty!" in self.cart_page.get_cart_message()

    @allure.title("Add product to cart")
    @allure.description("Verify product can be added to cart")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_product_to_cart(self):
        with allure.step("Search product"):
            self.home_page.search_product("Mac")
        with allure.step("Add product to cart"):
            self.products_page.add_first_product_to_cart()
        with allure.step("Verify success alert"):
            assert self.home_page.page.wait_for_selector(".alert-success")