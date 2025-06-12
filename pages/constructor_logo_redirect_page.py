from locators.constructor_logo_redirect_page_locators import ConstructorLogoRedirectPageLocators
from pages.base_page import BasePage
from allure import step

class ConstructorLogoRedirectPage(BasePage):

    @step('Кликаем на лого конструктора')
    def click_to_logo(self):
        self.click_to_element(ConstructorLogoRedirectPageLocators.CONSTRUCTOR_LINK)


    @step('Получаем класс элемента логотипа')
    def get_class_of_element(self):
        element_class = self.get_class_from_element(ConstructorLogoRedirectPageLocators.CONSTRUCTOR_LINK)
        return element_class