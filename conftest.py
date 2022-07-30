import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture
def browser(request):

    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", language)

    if browser_name == "chrome":
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox(firefox_profile=fp)

    yield browser

    browser.quit()
