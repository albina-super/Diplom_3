from allure import step
import data
from locators.ingredients_page_locators import IngredientsPageLocators
from pages.base_page import BasePage


class IngredientsPage(BasePage):

    @step('Кликаем на ингредиент')
    def click_on_ingredient(self):
        self.click_to_element(IngredientsPageLocators.BUN_LINK)


    @step('Проверяем что модалка открылась')
    def check_modal_opened(self):
        modal_title = self.get_text_from_element(IngredientsPageLocators.DETAIL_INGREDIENT_HEADER)
        section_class = self.get_class_from_element(IngredientsPageLocators.SECTION_MODAL)

        return modal_title, section_class


    @step('закрываем модалку')
    def close_modal(self):
        self.click_to_element(IngredientsPageLocators.CLOSE_MODAL_BUTTON)


    @step('Проверяем что модалка закрылась')
    def check_modal_closed(self):
        main_page_title = self.get_text_from_element(IngredientsPageLocators.MAIN_PAGE_HEADER)
        return main_page_title


    @step('Добавляем ингредиент  к заказу')
    def add_ingredients_buns(self):
        if data.BROWSER_NAME == 'chrome':
            self.drag_and_drop_chrome(IngredientsPageLocators.BUN_LINK, IngredientsPageLocators.CREATE_ORDER_PLACE)
        else:
            self.drag_and_drop_ff(IngredientsPageLocators.BUN_LINK, IngredientsPageLocators.CREATE_ORDER_PLACE)


    @step('Проверяем счетчик ингредиента')
    def get_counter(self):
        counter_ing = self.get_text_from_element(IngredientsPageLocators.COUNTER_BUNS)
        return int(counter_ing)