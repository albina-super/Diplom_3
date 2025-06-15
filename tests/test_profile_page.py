import allure
from data import ORDER_HISTORY_URL, MAIN_PAGE_URL
from pages.profile_page import MoveToProfilePage


class TestMoveToProfile:

    @allure.title('Тест на переход в профиль')
    def test_move_to_profile(self, driver, user):
        profile = MoveToProfilePage(driver)
        profile.go_to_profile_and_login(user)
        profile_title_header = profile.check_move_to_profile()
        assert profile_title_header == 'Профиль'


    @allure.title('Тест на проверку перехода истории заказов')
    def test_order_history_from_profile(self, driver, user):
        profile = MoveToProfilePage(driver)
        profile.go_to_profile_and_login(user)
        profile.click_to_order_history()
        assert profile.get_current_url() == f'{MAIN_PAGE_URL}{ORDER_HISTORY_URL}'


    @allure.title('Тест на логаут')
    def test_logout_page(self, driver, user):
        profile = MoveToProfilePage(driver)
        profile.go_to_profile_and_login(user)
        text_page = profile.logout_and_check_redirect_page()
        assert text_page == 'Вход'


