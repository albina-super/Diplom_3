import allure
from pages.order_page import OrderPage

class TestOrderPage:

    @allure.title('Тест на создание ордера успешно')
    def test_create_order_success(self, driver, user):
        order = OrderPage(driver)
        order.login(user)
        order.create_order_and_get_order_number()
        text_of_order_created = order.check_order_created()
        assert text_of_order_created == 'Ваш заказ начали готовить'


    @allure.title('Тест на открытие детального просмотра ордера')
    def test_open_order_detail_success(self, driver):
        order = OrderPage(driver)
        class_name = order.click_to_order_and_get_class_name()
        assert "Modal_modal_opened" in class_name


    @allure.title('Тест на проверку ордера в ленте заказов')
    def test_order_in_order_tape_success(self, driver, user):
        order = OrderPage(driver)
        order.login(user)
        num = order.create_order_and_get_order_number()
        num_in_list = order.check_order_in_order_tape(num)
        assert num == num_in_list.removeprefix("#0")


    @allure.title('Тест на то чтобы ордер был "В работе"')
    def test_order_in_progress_success(self, driver, user):
        order = OrderPage(driver)
        order.login(user)
        num = order.create_order_and_get_order_number()
        order_in_progress = order.check_order_in_progress()
        assert order_in_progress == f'0{num}'


    @allure.title('Тест на проверку исполненных ордеров')
    def test_done_orders_success(self, driver, user):
        order = OrderPage(driver)
        order.login(user)
        all_time_done, today_done = order.get_done_orders_fields()
        order.create_order_and_get_order_number()
        all_time_after, today_after = order.get_done_orders_fields()
        assert int(all_time_after) != int(all_time_done)  and int(today_after) != (today_done)
