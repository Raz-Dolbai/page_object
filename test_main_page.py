import time
import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import MainPageLocators, LoginPageLocators, ProductPageLocators


# запуск теста
# pytest -v --tb=line --language=en test_main_page.py

@pytest.mark.main_page
def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)  # создаем объект, передаем параметры browser и ссылку
    page.open()  # открываем браузер
    page.go_to_login_page()
    # Реализация перехода на страницу login
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.main_page
def test_guest_should_see_login_link(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)  # создаем объект, передаем параметры browser и ссылку
    page.open()  # открываем браузер
    page.should_be_login_link()


@pytest.mark.login_page
def test_should_be_login_url(browser):
    link = LoginPageLocators.LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


@pytest.mark.login_page
def test_should_be_login_form(browser):
    link = LoginPageLocators.LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


@pytest.mark.login_page
def test_should_be_register_form(browser):
    link = LoginPageLocators.LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


@pytest.mark.product_page
def test_add_book_in_basket(browser):
    link = ProductPageLocators.LINK2
    page = ProductPage(browser, link)
    page.open()
    page.add_book_in_basket()
    page.solve_quiz_and_get_code()
    page.check_name_book()
    page.check_price()
    page.should_be_message_add()

