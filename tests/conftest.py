import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Update path to location of downloaded chromedriver
path = ''
service = Service(executable_path=path)


@pytest.fixture(scope="session")
def driver():
    _driver = webdriver.Chrome(service=service)

    return _driver


