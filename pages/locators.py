from selenium.webdriver.common.by import By


class MainPageLocators():
    """Класс где хранятся селекторы элементов MainPage"""
    LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """Класс, где хранятся селекторы элементов Login Page"""
    LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
