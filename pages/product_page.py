from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage(BasePage):
    """Класс где хранятся методы для работы со страницей товара"""

    def add_book_in_basket(self):
        """Добавляет товар в корзину"""
        button_add = self.browser.find_element(*ProductPageLocators.ADD_BOOK_BUTTON)
        button_add.click()

    def should_be_message_add(self):
        """Проверяет есть ли сообщение после добавлении книги"""
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ADD_BOOK), 'Сообщение о добавлении товара отсутствует'

    def check_price(self, price_card, price_message):
        """Сравнивает цену товара в карточке и в сообщении"""
        assert price_message == price_card, 'Цена товара в сообщении и цена на карточке товара не равны'

    def check_name_book(self, name_card, name_message):
        """Сравнивает наименование товара в карточке и в сообщении"""
        assert name_card == name_message, 'Имя товара в сообщениии и на карточке не совпадают'

    def should_be_book_in_basket(self):
        """Запускает проверку на сообщение, сравнивает цену и наименование товара"""
        self.should_be_message_add()
        self.check_name_book(self.get_name_book_card(), self.get_name_book_message())
        self.check_price(self.get_price_book_card(), self.get_price_book_message())

    def get_name_book_card(self):
        """Возвращает наименование товара из карточки"""
        name_book_card = self.browser.find_element(*ProductPageLocators.NAME_IN_CARD)
        return name_book_card.text

    def get_name_book_message(self):
        """Возвращает наименование товара из сообщения"""
        name_book_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE)
        return name_book_message.text

    def get_price_book_card(self):
        """Возвращает цену товара из карточки"""
        price_book_card = self.browser.find_element(*ProductPageLocators.PRICE_IN_CARD)
        return price_book_card.text

    def get_price_book_message(self):
        """Возвращает цену товара из сообщения"""
        price_book_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE)
        return price_book_message.text

    def should_not_be_success_message(self):
        """Проверяет отсутствие сообщения о добавлении товара"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Сообщение есть, а не должно быть'

    def should_message_success_disappeared(self):
        """Проверяет исчезнет ли элемент через заданное время"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Сообщение не исчезло через заданное время'

