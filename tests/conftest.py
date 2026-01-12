import pytest
import threading
import time

from server import app
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def live_server():
    thread = threading.Thread(target=app.run, kwargs={"port": 5000, "use_reloader": False})
    thread.daemon = True
    thread.start()
    time.sleep(1)
    yield "http://127.0.0.1:5000"


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "test"
    with app.test_client() as client:
        yield client
