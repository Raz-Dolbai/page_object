from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Класс для работы со страницей товара"""

    def add_book_in_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.ADD_BOOK_BUTTON)
        button_add.click()

    def should_be_message_add(self):
        # Проверяет есть ли сообщение после добавлении книги
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ADD_BOOK), 'Сообщение о добавлении товара отсутствует'

    def check_price(self):
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE)
        price_card = self.browser.find_element(*ProductPageLocators.PRICE_IN_CARD)
        assert price_message.text == price_card.text, 'Цена товара в сообщении и цена на карточке товара не равны'

    def check_name_book(self):
        name_card = self.browser.find_element(*ProductPageLocators.NAME_IN_CARD)
        name_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE)
        assert name_card.text == name_message.text, 'Имя товара в сообщениии и на карточке не совпадают'

    def should_be_book_in_basket(self):
        self.should_be_message_add()
        self.check_name_book()
        self.check_price()
