from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_users_can_see_clubs_and_points(driver, live_server):
    driver.get(f"{live_server}/clubs")

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    page_source = driver.page_source

    assert "Club Test" in page_source
    assert "10" in page_source


def test_secretary_can_see_clubs_and_points(driver, live_server):
    driver.get(live_server)

    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("test@mail.com")

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    page_source = driver.page_source

    assert "Club Test" in page_source
    assert "10" in page_source
