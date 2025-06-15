from selenium.webdriver.common.by import By


class IngredientsPageLocators:

    BUN_LINK = By.XPATH, '//a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa6c")]'
    DETAIL_INGREDIENT_HEADER = By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified") and text()="Детали ингредиента"]'
    CLOSE_MODAL_BUTTON = By.XPATH, '//button[contains(@class, "Modal_modal__close_modified Modal_modal__close"]'
    SECTION_MODAL = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
    MAIN_PAGE_HEADER = By.XPATH, '//h1[contains(@class, "text_type_main-large") and text()="Соберите бургер"]'
    CREATE_ORDER_PLACE = By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket__list")]'
    COUNTER_BUNS = By.XPATH, '//a[contains(@href, "61c0c5a71d1f82001bdaaa6c")]//p[contains(@class, "counter_counter__num")]'