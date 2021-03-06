import pytest
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators


# запуск теста
# pytest -v --tb=line --language=en test_main_page.py

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MainPageLocators.LINK
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_text_empty_basket()
    basket.should_not_be_items_in_basket()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = MainPageLocators.LINK
        page = MainPage(browser, link)  # создаем объект, передаем параметры browser и ссылку
        page.open()  # открываем браузер
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = MainPageLocators.LINK
        page = MainPage(browser, link)  # создаем объект, передаем параметры browser и ссылку
        page.open()  # открываем браузер
        page.go_to_login_page()
        # Реализация перехода на страницу login
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
