from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_journal_btn(driver):
    driver.get("https://theracareweb.online/landing.php")
    driver.maximize_window()

    get_started = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "get-started-btn"))
    )
    get_started.click()

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username.send_keys("2023-004")

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password.send_keys("Test@1234")

    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login']"))
    )
    login_button.click()

    journal_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='journal.php']//button")
        )
    )
    journal_button.click()

    journal_titlepage = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(@class,'text-3xl')]")
        )
    )

    assert journal_titlepage.is_displayed()