import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def api_base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def practice_url():
    return "https://rahulshettyacademy.com/AutomationPractice/"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser_instance = p.chromium.launch(headless=True)
        yield browser_instance
        browser_instance.close()


@pytest.fixture(scope="function")
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(browser_context):
    page_instance = browser_context.new_page()
    yield page_instance
    page_instance.close()
