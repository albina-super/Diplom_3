import allure
from pages.constructor_logo_redirect_page import ConstructorLogoRedirectPage

class TestConstructorLogoRedirect:

    @allure.title('Тест на редирект на конструктор')
    def test_constructor_logo_redirect(self, driver):
        constructor = ConstructorLogoRedirectPage(driver)
        constructor.click_to_logo()
        element_class = constructor.get_class_of_element()
        active_class = 'AppHeader_header__link_active'
        assert  active_class in element_class

