import pytest

from pages.locators import LoginPageLocators
from pages.login_page import LoginPage


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