import pytest
from selenium import webdriver


@pytest.fixture()
def setup_fixture(request):
    username = "testuser@example.com"
    password = "test123"
    username_nok = "testusers"
    password_nok = "test"
    print("Initiating web driver")
    driver = webdriver.Chrome(executable_path="..\\web_drivers\\chromedriver.exe")
    driver.get("http://testapp.galenframework.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password
    request.cls.username_nok = username_nok
    request.cls.password_nok = password_nok

    yield driver
    driver.close()
