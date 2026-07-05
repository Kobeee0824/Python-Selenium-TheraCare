from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def test_searchbar(driver):
    driver.get("https://theracareweb.online/landing.php")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Click Get Started
    get_started = wait.until(
        EC.presence_of_element_located(
            (By.ID, "get-started-btn")
        )
    )
    get_started.click()

    # Login
    username = wait.until(
        EC.presence_of_element_located(
            (By.ID, "username")
        )
    )
    username.send_keys("2023-004")

    time.sleep(3)
    password = wait.until(
        EC.presence_of_element_located(
            (By.ID, "password")
        )
    )
    password.send_keys("Test@1234")
    time.sleep(3)
    login_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Login']")
        )
    )
    login_button.click()
    time.sleep(3)
    # Open Journal Page
    journal_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='journal.php']//button")
        )
    )
    journal_button.click()
    time.sleep(3)
    search_bar = wait.until(
        EC.presence_of_element_located(
            (By.ID, "search-input")
        )
    )
    search_bar.send_keys("Hello World!")
    time.sleep(3)
    assert search_bar.get_attribute("value") == "Hello World!"