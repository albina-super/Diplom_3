import data
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


def script_for_click_to_ff():
    pass


class MoveToProfilePage(BasePage):

    def go_to_profile_and_login(self, params):
        self.click_to_element(ProfilePageLocators.PROFILE_BUTTON)
        self.add_text_to_element(ProfilePageLocators.EMAIL_INPUT, params['email'])
        self.add_text_to_element(ProfilePageLocators.PASSWORD_INPUT, params['password'])
        self.click_to_element(ProfilePageLocators.CONFIRM_LOGIN_BUTTON)
        if data.BROWSER_NAME == 'chrome':
            self.click_to_element(ProfilePageLocators.PROFILE_BUTTON)
        else:
            self.script_for_click_to_ff(ProfilePageLocators.PROFILE_BUTTON)



    def check_move_to_profile(self):
        text = self.get_text_from_element(ProfilePageLocators.PROFILE_TITLE_LINK)
        return text


    def click_to_order_history(self):
        self.click_to_element(ProfilePageLocators.ORDER_HISTORY)


    def logout_and_check_redirect_page(self):
        self.click_to_element(ProfilePageLocators.LOGOUT_BUTTON)
        text = self.get_text_from_element(ProfilePageLocators.LOGIN_PAGE)
        return text