from pages.ingredients_page import IngredientsPage


class TestIngredientsPage:


    def test_open_ingredient_modal_success(self, driver):
        ingredient = IngredientsPage(driver)
        ingredient.click_on_ingredient()
        title, section_classes = ingredient.check_modal_opened()
        assert title == 'Детали ингредиента' and 'Modal_modal_opened' in section_classes


    def test_close_ingredient_modal_success(self, driver):
        ingredient = IngredientsPage(driver)
        ingredient.click_on_ingredient()
        main_page_title = ingredient.check_modal_closed()
        assert main_page_title == "Соберите бургер"


    def test_add_ingredients_to_order_success(self, driver):
        ingredient = IngredientsPage(driver)
        ingredient.add_ingredients_buns()
        count_ingredient = ingredient.get_counter()
        assert count_ingredient == 2