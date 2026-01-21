from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).highlight()
        self.page.click(locator)

    def fill(self, locator, text):
        self.page.locator(locator).highlight()
        self.page.fill(locator, text)

    def get_text(self, locator):
        self.page.locator(locator).highlight()
        return self.page.text_content(locator)

    def is_visible(self, locator):
        return self.page.is_visible(locator)

    def press_enter(self):
        self.page.keyboard.press("Enter")

    def select_all(self,locator):
        self.page.locator(locator).highlight()
        return self.page.locator(locator).count()

    def inner_text(self,locator):
        return self.page.inner_text(locator)

    def wait_for_selector(self,locator):
        return self.page.wait_for_selector(locator)

