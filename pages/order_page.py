import data
from locators.general_locators import GeneralsLocators
from locators.orders_page_locators import OrderPageLocators
from pages.base_page import BasePage
from allure import step

class OrderPage(BasePage):


    @step('Логинимся под юзером')
    def login(self, data):
        self.click_to_element(OrderPageLocators.LOGIN_BUTTON_ON_MAIN_PAGE)
        self.add_text_to_element(OrderPageLocators.EMAIL_INPUT, data['email'])
        self.add_text_to_element(OrderPageLocators.PASSWORD_INPUT, data['password'])
        self.click_to_element(OrderPageLocators.CONFIRM_LOGIN_BUTTON)


    @step('Создаем ордер и получаем его идентификатор')
    def create_order_and_get_order_number(self):
        if data.BROWSER_NAME == 'chrome':
            self.drag_and_drop_chrome(OrderPageLocators.BUN_LINK, OrderPageLocators.CREATE_ORDER_PLACE)
        else:
            self.drag_and_drop_ff(OrderPageLocators.BUN_LINK, OrderPageLocators.CREATE_ORDER_PLACE)

        self.wait_for_invisibility_of_element(GeneralsLocators.DIV_OVERLAY)
        self.click_to_element(OrderPageLocators.CONFIRM_CREATE_ORDER_BUTTON)
        number_order = self.get_actual_text_after_loading(OrderPageLocators.NUMBER_ORDER)
        self.wait_for_invisibility_of_element(GeneralsLocators.DIV_OVERLAY)
        return number_order


    @step('проверяем что ордер создался')
    def check_order_created(self):
        confirmed_text = self.get_text_from_element(OrderPageLocators.TEXT_OF_CREATED_ORDER)
        return confirmed_text


    @step('кликаем на ордер и получаем заголовок-название')
    def click_to_order_and_get_class_name(self):
        self.wait_for_invisibility_of_element(GeneralsLocators.DIV_OVERLAY)
        self.click_to_element(OrderPageLocators.ORDER_TAPE_LOGO)
        self.scroll_to_element(OrderPageLocators.DETAIL_ORDER_LINK)
        self.click_to_element(OrderPageLocators.DETAIL_ORDER_LINK)
        class_name = self.get_class_from_element(OrderPageLocators.ORDER_DETAIL_MODAL)
        return class_name


    @step('проверяем ордер в ленте заказов')
    def check_order_in_order_tape(self, number):
        self.press_esc()
        self.wait_for_invisibility_of_element(GeneralsLocators.OVERLAY_MODAL)
        self.click_to_element(OrderPageLocators.ORDER_TAPE_LOGO)
        formated_order_num_locator = self.format_locators(OrderPageLocators.NUMBER_ORDER_IN_ORDER_TAPE, number)
        self.click_to_element(formated_order_num_locator)
        order_num = self.get_text_from_element(formated_order_num_locator)
        return order_num


    @step('проверяем что ордер находится в работе')
    def check_order_in_progress(self):
        self.press_esc()
        self.wait_for_invisibility_of_element(GeneralsLocators.OVERLAY_MODAL)
        self.click_to_element(OrderPageLocators.ORDER_TAPE_LOGO)
        self.wait_for_invisibility_of_element(GeneralsLocators.DIV_OVERLAY)
        order_num = self.get_text_when_presence(OrderPageLocators.NUMBER_ORDER_IN_PROGRESS, "Все текущие заказы готовы!")
        return order_num


    @step('получаем кол-во исполненных орежров за все время и за сегодня')
    def get_done_orders_fields(self):
        self.press_esc()
        self.wait_for_invisibility_of_element(GeneralsLocators.DIV_OVERLAY)
        self.wait_for_invisibility_of_element(GeneralsLocators.OVERLAY_MODAL)
        self.click_to_element(OrderPageLocators.ORDER_TAPE_LOGO)
        self.wait_for_invisibility_of_element(GeneralsLocators.DIV_OVERLAY)
        all_time = self.get_text_from_element(OrderPageLocators.DONE_ORDERS_ALL_TIME)
        today = self.get_text_from_element(OrderPageLocators.DONE_ORDERS_TODAY)
        self.click_to_element(OrderPageLocators.MAIN_PAGE_LINK)
        return all_time, today