import os
import platform
from typing import Dict

import allure
import pytest
from playwright.sync_api import Page, sync_playwright

from Pages.cart_page import Cart
from Pages.login_page import Login
from Pages.products_page import Products
from Pages.register_page import Register
from Pages.home_page import Homepage

@pytest.fixture(scope="function")
def setup_page_function(request, page: Page):
    page.goto("https://tutorialsninja.com/demo/")
    request.cls.register_page= Register(page)
    request.cls.home_page = Homepage(page)
    request.cls.login_page = Login(page)
    request.cls.products_page = Products(page)
    request.cls.cart_page = Cart(page)




@pytest.fixture(scope="class")
def setup_page_class(request, browser):
    request.cls.page = browser.new_page()
    request.cls.page.goto("https://tutorialsninja.com/demo/")
    request.cls.register_page = Register(request.cls.page)
    request.cls.home_page = Homepage(request.cls.page)
    request.cls.login_page = Login(request.cls.page)
    request.cls.products_page = Products(request.cls.page)
    request.cls.cart_page = Cart(request.cls.page)


    yield
    request.cls.page.close()
    browser.close()




@pytest.fixture(scope="function")
  #navigate to base URL
def goto(page):
    page.goto("https://tutorialsninja.com/demo/")
    yield



@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "no_viewport": True,
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: Dict):
    """Fixture to set browser launch arguments.
    Args:
        browser_type_launch_args (dict): Browser type launch arguments.
    Returns:
        dict: Updated browser type launch arguments.
    See Also:
        https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch
    """
    return {**browser_type_launch_args, "args": ["--start-maximized"]}


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    allure_results_dir = os.getenv("ALLURE_RESULTS_DIR", "allure-results")
    os.makedirs(allure_results_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        browser_version = browser.version
        browser.close()

    env_file = os.path.join(allure_results_dir, "environment.properties")

    with open(env_file, "w") as f:
        f.write(f"Browser=Chrome\n")
        f.write(f"Browser.Version={browser_version}\n")
        f.write(f"OS={platform.system()} {platform.release()}\n")
        f.write(f"Python.Version={platform.python_version()}\n")
        f.write("Automation=Playwright\n")





@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook to attach screenshot on test failure
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Try to get a page object from the test class
        page = None
        if hasattr(item.instance, "cart_page"):
            page = item.instance.cart_page.page
        elif hasattr(item.instance, "home_page"):
            page = item.instance.home_page.page
        elif hasattr(item.instance, "login_page"):
            page = item.instance.login_page.page
        elif hasattr(item.instance, "register_page"):
            page = item.instance.register_page.page
        elif hasattr(item.instance, "products_page"):
            page = item.instance.products_page.page

        if page:
            screenshot_bytes = page.screenshot(full_page=True)
            allure.attach(
                screenshot_bytes,
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )