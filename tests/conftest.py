import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="/Users/herm/Downloads/chromedriver")


@pytest.fixture(scope="session")
def driver():
    _driver = webdriver.Chrome(service=service)

    return _driver


