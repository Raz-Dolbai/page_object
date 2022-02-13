
class BasePage():
    """Базовый класс для работы с драйвером, от этого класса будут унаследованы другие классы"""
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
        self.browser.get(self.url)