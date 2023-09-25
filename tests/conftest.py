import pytest
import os
from dotenv import load_dotenv
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://store.gaijin.net/'
    yield
    browser.quit()


@pytest.fixture(scope='session')
def user(browser_management):
    browser.open('https://store.gaijin.net/user.php')

    login = os.getenv('GAIJIN_LOGIN')
    password = os.getenv('GAIJIN_PASSWORD')

    browser.element('#email').send_keys(login)
    browser.element('#password').send_keys(password)
    browser.element('.input-button-main').click()
