from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')


class MainPageLocators():
    """Класс где хранятся селекторы элементов MainPage"""
    LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """Класс, где хранятся селекторы элементов Login Page"""
    LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL_REGISTER = (By.ID, 'id_registration-email')
    PASSWORD_REGISTER = (By.ID, 'id_registration-password1')
    CONFIRM_PASSWORD_REGISTER = (By.ID, 'id_registration-password2')
    BUTTON_REGISTER = (By.NAME, 'registration_submit')


class ProductPageLocators():
    """Класс где хранятся селекторы элементов Product Page"""
    LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    LINK2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    LINK3 = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    LINK4 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    ADD_BOOK_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_IN_CARD = (By.CSS_SELECTOR, 'div.product_main h1')
    PRICE_IN_CARD = (By.CSS_SELECTOR, 'p.price_color')
    MESSAGE_ADD_BOOK = (By.CSS_SELECTOR, 'div#messages')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-success strong')
    All_TEXT_IN_MESSAGE = (By.CSS_SELECTOR, 'div#messages strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')


class PromoLocators():
    LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
