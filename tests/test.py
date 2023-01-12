import time
import pytest
import logging

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestEskaleraPage:
    @pytest.fixture(scope='session')
    def navigate_to_login_page(self, driver):
        url = 'https://dev-feature.eskalera.com'

        logging.info(f'Navigating to {url}')
        driver.get(url)

        return driver

    def test_user_has_correct_header_information_and_employee_groups(self, navigate_to_login_page, driver):
        username_or_password_field = driver.find_element(By.TAG_NAME, "input")

        logging.info('Entering username in username field')
        username_or_password_field.send_keys("hermon.haile@gmail.com")

        continue_or_login_button = driver.find_element(By.CLASS_NAME, "MuiButton-label")

        logging.info('Clicking "Continue" button')
        continue_or_login_button.click()

        username_or_password_field_locator = 'input'
        username_or_password_field = WebDriverWait(driver, 20, (NoSuchElementException, StaleElementReferenceException,
                                                                ElementNotInteractableException)) \
            .until(expected_conditions.presence_of_element_located((By.TAG_NAME, username_or_password_field_locator)))

        logging.info('Entering password in the password field')
        username_or_password_field.send_keys("Abcd1234")

        continue_button_locator = 'MuiButton-label'
        continue_or_login_button = WebDriverWait(driver, 10, StaleElementReferenceException) \
            .until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, continue_button_locator)))

        logging.info('Clicking "Continue" button')
        continue_or_login_button.click()

        time.sleep(3)

        top_right_menu_locator = "MuiSvgIcon-root"
        top_right_menu = WebDriverWait(driver, 10, TimeoutException) \
            .until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, top_right_menu_locator)))

        logging.info("Selecting icon to open menu")
        top_right_menu[1].click()

        time.sleep(4)

        drop_down_menu_locator = "//span[normalize-space()='Admin Platform']"
        drop_down_menu = WebDriverWait(driver, 20) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, drop_down_menu_locator)))

        logging.info("Selecting 'Admin Platform' from top-right drop down menu")
        drop_down_menu.click()

        time.sleep(3)

        employee_list_selection_locator = "//div[@aria-rowindex='5']//div[@aria-colindex='1']//div[contains(text(),'Stodd  Pierce')]"
        employee_list_selection = WebDriverWait(driver, 20) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, employee_list_selection_locator)))

        logging.info("Selecting 'Stodd Pierce' from employee list")
        employee_list_selection.click()

        time.sleep(3)

        header_name = driver.find_element(By.CSS_SELECTOR,
                                          '.MuiTypography-root.MuiTypography-h3.MuiTypography-colorTextPrimary')

        assert "Stodd Pierce" in header_name.text

        last_login = driver.find_element(By.XPATH, "//div[contains(text(),'Last login')]")

        assert "-" in last_login.text

        last_invite = driver.find_element(By.XPATH, "//div[contains(text(),'Last invite')]")

        assert "Nov 27, 2022 6:00 PM" in last_invite.text

        logging.info("Scrolling to Groups section")
        ActionChains(driver).scroll_to_element(
            driver.find_element(By.CSS_SELECTOR, "button[aria-label='Edit Personal Info']"))

        time.sleep(5)

        actual_group_memberships = driver.find_elements(By.CSS_SELECTOR,
                                                        "div[aria-label*='Release backspace or delete key to remove.']")

        expected_groups = ['All', 'Sales']

        assert expected_groups[0] == actual_group_memberships[0].text \
               and expected_groups[1] == actual_group_memberships[1].text
