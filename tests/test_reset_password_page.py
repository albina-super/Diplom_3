from data import USER_DATA
from pages.reset_password_page import ResetPasswordPage



class TestResetPasswordPage:


    def test_visibility_password(self, driver):
        res_pass_page = ResetPasswordPage(driver)
        res_pass_page.click_reset_password_link(USER_DATA)
        div_class = res_pass_page.check_visibility_of_password()
        assert 'input_status_active' in div_class
