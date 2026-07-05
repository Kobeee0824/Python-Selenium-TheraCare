from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dropdown(driver):

    wait = WebDriverWait(driver,10)

    driver.get("https://theracareweb.online/landing.php")
    driver.maximize_window()

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

    password = wait.until(
        EC.presence_of_element_located(
            (By.ID, "password")
        )
    )
    password.send_keys("Test@1234")

    login_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Login']")
        )
    )
    login_button.click()

    # Open Journal Page
    journal_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='journal.php']//button")
        )
    )
    journal_button.click()

    dropdown = wait.until(
        EC.presence_of_element_located(
            (By.ID, "date-filter")
        )
    )

    # Turn the dropdown element into a Selenium Select object
    select = Select(dropdown)

    # Go through each option in the dropdown
    for option in select.options:

        # Get the text of the option and remove extra spaces
        text = option.text.strip()

        # Skip if the option is empty
        if text:
            # Click/select this option
            select.select_by_visible_text(text)

            # Check if the selected option matches what we clicked
            assert select.first_selected_option.text.strip() == text