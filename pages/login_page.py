from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Класс где хранятся методы для работы со страницей авторизации и регистрации"""

    def should_be_login_page(self):
        """Проверяет URL=URL login, присутствие форм: регистрации и авторизации"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяет текущий URL с login URL"""
        assert "login" in self.browser.current_url, "It is not a login page"

    def should_be_login_form(self):
        """Проверяет есть ли форма с авторизацией"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        """Проверяет есть ли форма с регистрацией"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
