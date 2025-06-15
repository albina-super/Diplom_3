import allure

from pages.ingredients_page import IngredientsPage


class TestIngredientsPage:

    @allure.title('Тест на открытие модалки ингредиента')
    def test_open_ingredient_modal_success(self, driver):
        ingredient = IngredientsPage(driver)
        ingredient.click_on_ingredient()
        title, section_classes = ingredient.check_modal_opened()
        assert title == 'Детали ингредиента' and 'Modal_modal_opened' in section_classes


    @allure.title('Тест на закрытие модалки ингредиента')
    def test_close_ingredient_modal_success(self, driver):
        ingredient = IngredientsPage(driver)
        ingredient.click_on_ingredient()
        main_page_title = ingredient.check_modal_closed()
        assert main_page_title == "Соберите бургер"


    @allure.title('Тест на перетаскивание ингредиента в заказ')
    def test_add_ingredients_to_order_success(self, driver):
        ingredient = IngredientsPage(driver)
        ingredient.add_ingredients_buns()
        count_ingredient = ingredient.get_counter()
        assert count_ingredient == 2