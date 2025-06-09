from selenium.webdriver.common.by import By


class ConstructorLogoRedirectPageLocators:

    CONSTRUCTOR_LINK = By.XPATH, '//a[@href="/" and .//p[text()="Конструктор"]]'