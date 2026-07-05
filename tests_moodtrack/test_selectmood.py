from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_selectmood(driver):

    driver.get("https://theracareweb.online/landing.php")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    get_started = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='get-started-btn']")
        )
    )
    get_started.click()

    username = driver.find_element(By. XPATH, "//button[@id='get-started-btn']")
    username.send_keys("2023-004")

    password = driver.find_element(By. XPATH, "//input[@id='password']")
    password.send_keys("Test@1234")

    login_btn = driver.find_element(By. XPATH, "//button[normalize-space()='Login']")
    login_btn.click()



