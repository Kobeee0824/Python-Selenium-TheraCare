from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_viewjournal(driver):
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

    journal_entry = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/div[contains(@class,'flex min-h-screen')]/div[contains(@class,'flex-1 lg:ml-64 ml-0 w-full pb-40')]/main[contains(@class,'flex flex-col w-full p-0')]/div[@id='entries-container']/div[3]")
        )
    )

    journal_entry.click()

