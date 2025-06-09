from locators.order_tape_redirect_locators_page import OrderTapeRedirectLocators
from pages.base_page import BasePage


class OrderTapeRedirectPage(BasePage):

    def click_order_tape_logo(self):
        self.click_to_element(OrderTapeRedirectLocators.ORDER_TAPE_LOGO)

    def get_title_page(self):
        return self.get_text_from_element(OrderTapeRedirectLocators.TITLE_ORDER_TAPE_PAGE)