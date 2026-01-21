from playwright.sync_api import Page

from pages.Base_Page import BasePage


class Homepage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

    _click_acc = ".dropdown-toggle"
    _search = ".form-control.input-lg"
    _container = ".container"
    _login_menu_visible = "a:has-text('Login')"
    _logo = "#logo"
    _search_name = "[name='search']"
    _alert_success = ".alert.alert-success.alert-dismissible"
    _scroll_bar = "window.scrollTo(0, document.body.scrollHeight)"
    _dropdown_menu = "ul.dropdown-menu li a"
    _account_menu = "a[title='My Account']"
    product_layout = ".product-layout"
    _product_price = ".product-thumb .price"
    _swiper = ".swiper-wrapper .swiper-slide"

    def click_my_account(self):
        self.click(self._click_acc)

    def search_product(self, product):
        self.fill(self._search,product)
        self.press_enter()

    def search_is_visible(self):
        return self.is_visible(self._search_name)


    def container_is_visible(self):
        return self.is_visible(self._container)


    def login_is_visible(self):
        return self.is_visible(self._login_menu_visible)

    def logo_is_visible(self):
        return self.is_visible(self._logo)

    def alert_success(self):
        return self.wait_for_selector(self._alert_success)

    def scrolling_bar(self):
        self.page.evaluate(self._scroll_bar)

    def get_my_account_options(self) -> list[str]:
        self.click(self._account_menu)
        options = self.page.locator(self._dropdown_menu)
        option_texts = []

        for i in range(options.count()):
            option_texts.append(options.nth(i).inner_text().strip())

        return option_texts

    def get_featured_products_count(self):
        return self.page.locator(self.product_layout).count()

    def get_featured_product_prices(self) -> list[str]:
        price_elements = self.page.locator(self._product_price)
        prices = []

        for i in range(price_elements.count()):
            prices.append(price_elements.nth(i).inner_text().strip())

        return prices

    def get_carousel_slides_count(self):
        self.page.wait_for_selector(self._swiper, timeout=5000)
        slides = self.page.locator(self._swiper)
        return slides.count()

    def is_carousel_present(self):
        return self.get_carousel_slides_count() > 0






