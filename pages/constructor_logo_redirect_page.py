from locators.constructor_logo_redirect_page_locators import ConstructorLogoRedirectPageLocators
from pages.base_page import BasePage


class ConstructorLogoRedirectPage(BasePage):

    def click_to_logo(self):
        self.click_to_element(ConstructorLogoRedirectPageLocators.CONSTRUCTOR_LINK)

    def get_class_of_element(self):
        element_class = self.get_class_from_element(ConstructorLogoRedirectPageLocators.CONSTRUCTOR_LINK)
        return element_class