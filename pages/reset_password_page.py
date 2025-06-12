from locators.general_locators import GeneralsLocators
from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage
from allure import step


class ResetPasswordPage(BasePage):


    @step('кликаем на забыли пароль')
    def click_reset_password_link(self, data):
        self.click_to_element(ResetPasswordLocators.PROFILE_BUTTON)
        self.click_to_element(ResetPasswordLocators.RESET_PASSWORD_LINK)
        self.add_text_to_element(ResetPasswordLocators.RESET_PASSWORD_EMAIL_INPUT, data['email'])
        self.click_to_element(ResetPasswordLocators.RESET_PASSWORD_CONFIRM_BUTTON)
        self.add_text_to_element(ResetPasswordLocators.PASSWORD_INPUT, data['password'])
        self.wait_for_invisibility_of_element(GeneralsLocators.DIV_OVERLAY)
        self.click_to_element(ResetPasswordLocators.VISIBILITY_PASSWORD_BUTTON)


    @step('проверяем что поле пароля подсветилось и пароль виден')
    def check_visibility_of_password(self):
        return self.get_class_from_element(ResetPasswordLocators.DIV_INPUT)


