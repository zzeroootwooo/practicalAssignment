import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_challenging_dom_page(driver):
    driver.get("https://the-internet.herokuapp.com/challenging_dom")

    WebDriverWait(driver, 10).until(EC.title_contains("The Internet"))

    assert "The Internet" in driver.title

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#content > div > h3"))
    )
    assert element.text == "Challenging DOM"

    screenshot_path = os.path.join(
        os.getcwd(), "challenging_dom_screenshot.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at {screenshot_path}")

    element_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.example > h3"))
    )
    assert element_2.text == "Challenging DOM"

    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    assert table.is_displayed(), "Table is not visible"

    blue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button"))
    )
    assert blue_button.is_displayed(), "Blue button is not visible"

    green_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button.success"))
    )
    assert green_button.is_displayed(), "Green button is not visible"

    red_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button.alert"))
    )
    assert red_button.is_displayed(), "Red button is not visible"

    screenshot_path_after_button_check = os.path.join(
        os.getcwd(), "challenging_dom_after_button_check.png")
    driver.save_screenshot(screenshot_path_after_button_check)
    print(f"Screenshot saved at {screenshot_path_after_button_check}")

    table_headers = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table th"))
    )
    expected_headers = ["Lorem", "Ipsum", "Dolor",
                        "Sit", "Amet", "Diceret", "Action"]
    actual_headers = [header.text for header in table_headers]
    assert actual_headers == expected_headers, f"Table headers do not match. Expected: {expected_headers}, Got: {actual_headers}"

    final_screenshot_path = os.path.join(
        os.getcwd(), "challenging_dom_final.png")
    driver.save_screenshot(final_screenshot_path)
    print(f"Final screenshot saved at {final_screenshot_path}")
