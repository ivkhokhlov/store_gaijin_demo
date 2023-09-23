import pytest
from selene import browser

@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://store.gaijin.net/'
    yield
    browser.quit()

@pytest.fixture(scope='session')
def user(browser_management):
    browser.open('https://store.gaijin.net/user.php')
    browser.element('#email').send_keys('xokev83191@ipnuc.com')
    browser.element('#password').send_keys('123456')
    browser.element('.input-button-main').click()
