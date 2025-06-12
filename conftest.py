import pytest
from selenium import webdriver
import data
from data import MAIN_PAGE_URL, MY_USER_DATA
from methods.user_methods import UserMethods


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



@pytest.fixture
def user():
    user = UserMethods()
    user.register_user(MY_USER_DATA)
    yield MY_USER_DATA
    status, response_login = user.login_user(MY_USER_DATA)
    user.delete_user(response_login['accessToken'])
