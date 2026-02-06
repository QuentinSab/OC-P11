import pytest
import threading
import time

import server
from server import app
from unittest.mock import patch
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(autouse=True)
def reset_data(request):
    test_path = request.fspath.dirname

    if "integration" in test_path or "functional" in test_path:
        with patch("logic.logic.open", create=True):
            server.clubs = [{"name": "Club Test", "points": 10, "email": "test@mail.com"}]
            server.competitions = [{
                "name": "Spring Festival",
                "date": "2030-01-01 10:00:00",
                "numberOfPlaces": 25
            }]
            yield
    else:
        yield


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
