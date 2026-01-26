import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True for CI
        context = browser.new_context()
        yield context
        browser.close()

def test_select_elements(browser_context):
    page = browser_context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")


    checkbox = page.locator("input#checkBoxOption1")
    checkbox.check()
    assert checkbox.is_checked()


    radio = page.locator("input[value='radio2']")
    radio.check()
    assert radio.is_checked()


    dropdown = page.locator("select#dropdown-class-example")
    dropdown.select_option("option2")
    selected_value = dropdown.input_value()
    assert selected_value == "option2"


    input_box = page.locator("input#name")
    input_box.fill("Ayush Jain")
    assert input_box.input_value() == "Ayush Jain"

    page.locator("input#alertbtn").click()
    alert = page.wait_for_event("dialog")
    assert "Ayush" in alert.message
    alert.dismiss()

    page.close()
