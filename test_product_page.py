import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators, PromoLocators


@pytest.mark.product_page
def test_add_book_in_basket(browser):
    link = ProductPageLocators.LINK2
    page = ProductPage(browser, link)
    page.open()
    page.add_book_in_basket()
    page.solve_quiz_and_get_code()
    page.check_price(page.get_price_book_card(), page.get_price_book_message())
    page.check_name_book(page.get_name_book_card(), page.get_name_book_message())


@pytest.mark.promo
@pytest.mark.parametrize("link", [*[num for num in range(2) if num != 7],
                                  pytest.param(7, marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, link):
    # при помощи параметризации узнаем какой тест падает и затем помечаем его как заведомо падающий xfail
    link = f"{PromoLocators.LINK}{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_book_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_add()
    page.should_be_book_in_basket()
    # page.check_price(page.get_price_book_card(), page.get_price_book_message())
    # page.check_name_book(page.get_name_book_card(), page.get_name_book_message())
