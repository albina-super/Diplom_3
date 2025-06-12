import allure

from pages.order_tape_logo_redirect_page import OrderTapeRedirectPage


class TestOrderTapeLogoRedirect:

    @allure.title('Тест на редирект ленты заказов')
    def test_order_tape_logo_redirect(self, driver):
        order_tape = OrderTapeRedirectPage(driver)
        order_tape.click_order_tape_logo()
        text = order_tape.get_title_page()
        assert text == "Лента заказов"
