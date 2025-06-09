from selenium.webdriver.common.by import By


class OrderTapeRedirectLocators:
    ORDER_TAPE_LOGO = By.XPATH, '//a[@href="/feed" and .//p[text()="Лента Заказов"]]'
    TITLE_ORDER_TAPE_PAGE = By.XPATH, '//h1[text()="Лента заказов"]'