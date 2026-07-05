from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_deletejournal_btn(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://theracareweb.online/landing.php")
    driver.maximize_window()

    # Click Get Started
    get_started = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "get-started-btn")
        )
    )
    get_started.click()

    # Login
    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "username")
        )
    )
    username.send_keys("2023-004")

    password = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "password")
        )
    )
    password.send_keys("Test@1234")

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Login']")
        )
    )
    login_button.click()

    # Open Journal Page
    journal_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='journal.php']//button")
        )
    )
    journal_button.click()

    delete_button = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[class='px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600 text-sm']")
        )
    )

    delete_button.click()

    yes_delete_it = wait.until(
        EC.presence_of_element_located(
            (By. CSS_SELECTOR, "button[class='swal2-confirm swal2-styled']")
        )
    )

    yes_delete_it.click()