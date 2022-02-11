import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Описываем параметр для ввода в коммандной строке
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language: en, ru, fr and another")


@pytest.fixture(scope='function')
def browser(request):
    # получаем параметр, который ввели в командной строке
    user_language = request.config.getoption('language')
    options = Options()
    # передаем параметр в option, инициализируем браузер с нужным языком
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    #закрываем браузер после выполнения теста
    browser.quit()

