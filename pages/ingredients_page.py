from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data
from locators.ingredients_page_locators import IngredientsPageLocators
from pages.base_page import BasePage


class IngredientsPage(BasePage):

    def click_on_ingredient(self):
        element = self.driver.find_element(By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6c')]")
        ActionChains(self.driver).move_to_element(element).perform()
        self.click_to_element(IngredientsPageLocators.BUN_LINK)

    def check_modal_opened(self):
        modal_title = self.get_text_from_element(IngredientsPageLocators.DETAIL_INGREDIENT_HEADER)
        section_class = self.get_class_from_element(IngredientsPageLocators.SECTION_MODAL)

        return modal_title, section_class


    def close_modal(self):
        self.click_to_element(IngredientsPageLocators.CLOSE_MODAL_BUTTON)



    def check_modal_closed(self):
        main_page_title = self.get_text_from_element(IngredientsPageLocators.MAIN_PAGE_HEADER)
        return main_page_title


    def add_ingredients_buns(self):
        if data.BROWSER_NAME == 'chrome':
            self.drag_and_drop_chrome(IngredientsPageLocators.BUN_LINK, IngredientsPageLocators.CREATE_ORDER_PLACE)
        else:
            self.drag_and_drop_ff(IngredientsPageLocators.BUN_LINK, IngredientsPageLocators.CREATE_ORDER_PLACE)


    def get_counter(self):
        counter_ing = self.get_text_from_element(IngredientsPageLocators.COUNTER_BUNS)
        return int(counter_ing)