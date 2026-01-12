from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_email(driver, live_server):
    driver.get(live_server)

    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("invalid@email")

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    error = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "flash-error"))
    )

    assert "Email invalide" in error.text
