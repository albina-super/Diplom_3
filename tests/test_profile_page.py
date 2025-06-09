from data import USER_DATA, ORDER_HISTORY_URL, MAIN_PAGE_URL
from pages.profile_page import MoveToProfilePage


class TestMoveToProfile:

    def test_move_to_profile(self, driver):
        profile = MoveToProfilePage(driver)
        profile.go_to_profile_and_login(USER_DATA)
        profile_title_header = profile.check_move_to_profile()
        assert profile_title_header == 'Профиль'

    def test_order_history_from_profile(self, driver):
        profile = MoveToProfilePage(driver)
        profile.go_to_profile_and_login(USER_DATA)
        profile.click_to_order_history()
        assert profile.get_current_url() == f'{MAIN_PAGE_URL}{ORDER_HISTORY_URL}'


    def test_logout_page(self, driver):
        profile = MoveToProfilePage(driver)
        profile.go_to_profile_and_login(USER_DATA)
        text_page = profile.logout_and_check_redirect_page()
        assert text_page == 'Вход'


