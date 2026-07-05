from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_addjournal_btn(driver):

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

    # Click Add Journal
    add_journal_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".add-journal-btn")
        )
    )
    add_journal_btn.click()

    # Wait for modal to appear
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "journalModal")
        )
    )

    # Enter title
    title = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "journal-title")
        )
    )
    title.clear()
    title.send_keys("Hello")

    # Enter journal body
    body = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "journal-body")
        )
    )
    body.clear()
    body.send_keys("Hello World!")

    # Click Save
    save_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn-save")
        )
    )
    save_btn.click()

    # Optional: Wait for modal to disappear after save
    wait.until(
        EC.invisibility_of_element_located(
            (By.ID, "journalModal")
        )
    )