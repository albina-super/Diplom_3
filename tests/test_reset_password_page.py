import allure
from pages.reset_password_page import ResetPasswordPage



class TestResetPasswordPage:


    @allure.title('Тест на видимость пароль при нажатии на "глазик"')
    def test_visibility_password(self, driver, user):
        res_pass_page = ResetPasswordPage(driver)
        res_pass_page.click_reset_password_link(user)
        div_class = res_pass_page.check_visibility_of_password()
        assert 'input_status_active' in div_class
