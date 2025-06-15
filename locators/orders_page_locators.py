from selenium.webdriver.common.by import By


class OrderPageLocators:
    LOGIN_BUTTON_ON_MAIN_PAGE = By.XPATH, '//*[contains(@class, "button_button_size_large") and text()="Войти в аккаунт"]'
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    PASSWORD_INPUT = By.XPATH, '//label[text()="Пароль"]/following-sibling::input'
    CONFIRM_LOGIN_BUTTON = By.XPATH, '//*[contains(@class, "button_button_size_medium") and text()="Войти"]'
    BUN_LINK = By.XPATH, '//a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa6c")]'
    CREATE_ORDER_PLACE = By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket__list")]'
    CONFIRM_CREATE_ORDER_BUTTON = By.XPATH, '//button[contains(@class, "button_button_size_large") and text()="Оформить заказ"]'
    TEXT_OF_CREATED_ORDER = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//p[contains(text(), "Ваш заказ начали готовить")]'
    ORDER_TAPE_LOGO = By.XPATH, '//a[@href="/feed" and .//p[text()="Лента Заказов"]]'
    DETAIL_ORDER_LINK = By.XPATH, '//ul[contains(@class, "OrderFeed_list")]/li[1]//a'
    TITLE_OF_ORDER = By.XPATH, '//h2[text()="Краторный бургер"]'
    NUMBER_ORDER = By.XPATH, '//h2[contains(@class, "text_type_digits-large")]'
    NUMBER_ORDER_IN_ORDER_TAPE = By.XPATH, '//p[contains(@class, "text_type_digits-default") and text()="#0{}"]'
    NUMBER_ORDER_IN_PROGRESS = By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li'
    DONE_ORDERS_ALL_TIME = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p'
    DONE_ORDERS_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p'
    MAIN_PAGE_LINK = By.XPATH, '//a[contains(@href, "/")]'
    ORDER_DETAIL_MODAL = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
