from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
