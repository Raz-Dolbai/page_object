from selenium.webdriver.common.by import By
from .pages.main_page import MainPage

# запуск теста
# pytest -v --tb=line --language=en test_main_page.py

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # создаем объект, передаем параметры browser и ссылку
    page.open()  # открываем браузер
    page.go_to_login_page()
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # создаем объект, передаем параметры browser и ссылку
    page.open()  # открываем браузер
    page.should_be_login_link()
