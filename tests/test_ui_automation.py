import pytest


@pytest.mark.ui
@pytest.mark.playwright
def test_checkbox_selection(page, practice_url):
    page.goto(practice_url)
    checkbox = page.locator("input#checkBoxOption1")
    checkbox.check()
    assert checkbox.is_checked()


@pytest.mark.ui
@pytest.mark.playwright
def test_radio_button_selection(page, practice_url):
    page.goto(practice_url)
    radio = page.locator("input[value='radio2']")
    radio.check()
    assert radio.is_checked()


@pytest.mark.ui
@pytest.mark.playwright
def test_dropdown_selection(page, practice_url):
    page.goto(practice_url)
    dropdown = page.locator("select#dropdown-class-example")
    dropdown.select_option("option2")
    selected_value = dropdown.input_value()
    assert selected_value == "option2"


@pytest.mark.ui
@pytest.mark.playwright
def test_input_field_text(page, practice_url):
    page.goto(practice_url)
    input_box = page.locator("input#name")
    input_box.fill("Ayush Jain")
    assert input_box.input_value() == "Ayush Jain"


@pytest.mark.ui
@pytest.mark.playwright
def test_alert_dialog(page, practice_url):
    page.goto(practice_url)
    input_box = page.locator("input#name")
    input_box.fill("Ayush")
    
    def handle_dialog(dialog):
        assert "Ayush" in dialog.message
        dialog.dismiss()
    
    page.on("dialog", handle_dialog)
    page.locator("input#alertbtn").click()
    page.wait_for_timeout(500)


@pytest.mark.ui
@pytest.mark.playwright
def test_all_ui_elements(page, practice_url):
    page.goto(practice_url)
    
    checkbox = page.locator("input#checkBoxOption1")
    checkbox.check()
    assert checkbox.is_checked()
    
    radio = page.locator("input[value='radio2']")
    radio.check()
    assert radio.is_checked()
    
    dropdown = page.locator("select#dropdown-class-example")
    dropdown.select_option("option2")
    assert dropdown.input_value() == "option2"
    
    input_box = page.locator("input#name")
    input_box.fill("Ayush Jain")
    assert input_box.input_value() == "Ayush Jain"
