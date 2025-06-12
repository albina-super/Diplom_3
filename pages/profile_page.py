from locators.general_locators import GeneralsLocators
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from allure import step

class MoveToProfilePage(BasePage):

    @step('Ждем пока закроется модалка')
    def wait_invisible_element(self):
        self.wait_for_invisibility_of_element(GeneralsLocators.DIV_OVERLAY)


    @step('Идем в профиль и логинимся')
    def go_to_profile_and_login(self, params):
        self.click_to_element(ProfilePageLocators.PROFILE_BUTTON)
        self.add_text_to_element(ProfilePageLocators.EMAIL_INPUT, params['email'])
        self.add_text_to_element(ProfilePageLocators.PASSWORD_INPUT, params['password'])
        self.click_to_element(ProfilePageLocators.CONFIRM_LOGIN_BUTTON)
        self.wait_invisible_element()
        self.click_to_element(ProfilePageLocators.PROFILE_BUTTON)


    @step('проверяем что попали на страницу профиля')
    def check_move_to_profile(self):
        text = self.get_text_from_element(ProfilePageLocators.PROFILE_TITLE_LINK)
        return text


    @step('кликаем на историю ордеров')
    def click_to_order_history(self):
        self.wait_invisible_element()
        self.click_to_element(ProfilePageLocators.ORDER_HISTORY)


    @step('делаем логаут и проверяем страницу на которую нас перекинет')
    def logout_and_check_redirect_page(self):
        self.wait_invisible_element()
        self.click_to_element(ProfilePageLocators.LOGOUT_BUTTON)
        text = self.get_text_from_element(ProfilePageLocators.LOGIN_PAGE)
        return text