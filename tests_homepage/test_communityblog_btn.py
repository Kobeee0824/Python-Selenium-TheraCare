from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_moodtrack_btn(driver):
    driver.get("https://theracareweb.online/landing.php")
    driver.maximize_window()

    get_started = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='get-started-btn']")
        )
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

    communityblog_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='community_blog.php']//button[@class='mt-auto bg-blue-900 text-white text-sm font-semibold py-2 px-4 rounded-md hover:bg-blue-800 transition'][normalize-space()='Get Started']")
        )
    )
    communityblog_button.click()

    communityblog_titlepage = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[@class='text-4xl font-bold mb-2']")
        )
    )

    assert communityblog_titlepage.is_displayed()
