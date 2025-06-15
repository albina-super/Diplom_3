from selenium.webdriver.common.by import By


class GeneralsLocators:
    DIV_OVERLAY = By.XPATH, '//*[contains(@class,  "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]'
    OVERLAY_MODAL = By.XPATH, '//section[contains(@class, "Modal_modal__P3_V5")]//div[contains(@class, "Modal_modal_overlay__x2ZCr")]'
