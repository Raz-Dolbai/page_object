import random
import time
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

    def create_email_password(self):
        """Создает пароль и email"""
        password = ''.join([str(random.randint(0, 10)) for _ in range(9)])
        email = str(time.time()) + "@fakemail.org"
        return (email, password)

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER)
        email_input.send_keys(email)
        login_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER)
        login_input.send_keys(password)
        login_confirm_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_REGISTER)
        login_confirm_input.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()

