import pytest
from selenium import webdriver
import data
from data import MAIN_PAGE_URL

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    data.BROWSER_NAME = request.param
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(MAIN_PAGE_URL)

    yield driver

    driver.quit()