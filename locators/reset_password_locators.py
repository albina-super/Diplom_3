from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    PROFILE_BUTTON = By.XPATH, '//*[contains(@href, "/account")]'
    RESET_PASSWORD_LINK = By.XPATH, '//*[contains(@class, "Auth_link") and text()="Восстановить пароль"]'
    RESET_PASSWORD_EMAIL_INPUT = By.XPATH, '//*[contains(@class, "text_type_main-default") and @type="text"]'
    RESET_PASSWORD_CONFIRM_BUTTON = By.XPATH, '//*[contains(@class, "button_button_size_medium") and text()="Восстановить"]'
    VISIBILITY_PASSWORD_BUTTON = By.XPATH, '//*[contains(@class, "input__icon-action")]'
    PASSWORD_INPUT = By.XPATH, '//*[contains(@class, "text_type_main-default") and @type="password"]'
    DIV_INPUT = By.XPATH, '//div[contains(@class, "input_status_active")]'

