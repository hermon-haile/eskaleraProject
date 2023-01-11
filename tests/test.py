import pytest
import logging

from pages.login_page.page_object import LoginPage


class TestEsklaeraPage:
    @pytest.fixture(scope='session')
    def set_up(self, driver):
        url = 'https://dev-feature.eskalera.com'

        logging.info(f'Navigating to {url}')
        driver.get(url)

        return driver

    @pytest.mark.login
    def test_user