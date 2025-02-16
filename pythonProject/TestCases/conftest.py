from selenium import webdriver
from pytest import fixture


@fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        driver = webdriver.Firefox()
        print("Launching FireFox Browser")
    yield driver
    driver.quit()

@fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_addoption(parser):
    parser.addoption("--browser")

