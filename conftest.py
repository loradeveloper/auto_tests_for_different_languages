import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru", help='Choose language: ru or other')


@pytest.fixture
def language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser(request, language):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test...")
        options = OptionsChrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        options = OptionsFirefox()
        options.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
