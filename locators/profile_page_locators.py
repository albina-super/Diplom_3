from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_BUTTON = By.XPATH, '//a[contains(@href, "/account")]'
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    PASSWORD_INPUT = By.XPATH, '//label[text()="Пароль"]/following-sibling::input'
    PROFILE_TITLE_LINK = By.XPATH, '//*[contains(@class, "Account_link_active")]'
    CONFIRM_LOGIN_BUTTON = By.XPATH, '//*[contains(@class, "button_button_size_medium") and text()="Войти"]'
    INVISIBLE_MODAL = By.XPATH, '//*[contains(@class, "Modal_modal_overlay__x2ZCr")]'
    ORDER_HISTORY = By.XPATH, '//a[contains(@href, "/account/order-history")]'
    LOGOUT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button") and text()="Выход"]'
    LOGIN_PAGE = By.XPATH, '//h2[text()="Вход"]'
