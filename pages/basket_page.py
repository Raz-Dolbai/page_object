from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_text_empty_basket(self):
        """Проверят есть ли сообщение Ваша корзина пуста"""
        text_in_basket = self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET)
        assert text_in_basket, 'Сообщение о том, что корзина пуста отсутствует'

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Не должно быть покупок в корзине'
