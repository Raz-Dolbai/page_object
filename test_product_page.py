import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators, PromoLocators, LoginPageLocators


@pytest.mark.need_review
def test_add_book_in_basket(browser):
    link = ProductPageLocators.LINK2
    page = ProductPage(browser, link)
    page.open()
    page.add_book_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_add()


@pytest.mark.promo
@pytest.mark.parametrize("link", [*[num for num in range(10) if num != 7],
                                  pytest.param(7, marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, link):
    # при помощи параметризации узнаем какой тест падает и затем помечаем его как заведомо падающий xfail
    link = f"{PromoLocators.LINK}{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_book_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_book_in_basket()
    # page.should_be_message_add()
    # page.check_price(page.get_price_book_card(), page.get_price_book_message())
    # page.check_name_book(page.get_name_book_card(), page.get_name_book_message())


@pytest.mark.explictly_wait
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.LINK3
    page = ProductPage(browser, link)
    page.open()
    page.add_book_in_basket()
    page.should_not_be_success_message()


@pytest.mark.explictly_wait
def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.LINK3
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.explictly_wait
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.LINK3
    page = ProductPage(browser, link)
    page.open()
    page.add_book_in_basket()
    page.should_message_success_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = ProductPageLocators.LINK4
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.LINK4
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.LINK4
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_text_empty_basket()
    basket.should_not_be_items_in_basket()


@pytest.mark.user_can_add_book
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LoginPageLocators.LINK
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(*page.create_email_password())

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.LINK4
        page = ProductPage(browser, link)
        page.open()
        page.add_book_in_basket()
        page.should_be_book_in_basket()
        # page.check_price(page.get_price_book_card(), page.get_price_book_message())
        # page.check_name_book(page.get_name_book_card(), page.get_name_book_message())

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.LINK3
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
