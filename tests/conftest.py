import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10.0
    driver_options = webdriver.ChromeOptions()
    #driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    yield
    browser.quit()

