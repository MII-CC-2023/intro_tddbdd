import pytest
 
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver

# Constants
 
APP_URL = 'http://127.0.0.1:8080/'

# Scenarios
 
scenarios('../features/web.feature')

# Fixtures
 
@pytest.fixture
def browser():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    b = webdriver.Firefox(options=options)
    b.implicitly_wait(10)
    yield b
    b.quit()

# Given Steps
 
@given('la página principal')
def app_home(browser):
    browser.get(APP_URL)

# When Steps
 
@when('el usuario accede a ella')
def saysme_hello():
    pass

# Then Steps
 
@then(parsers.parse('se muestra el mensaje "{saludo}"'))
def hello(browser, saludo):
    assert saludo in browser.page_source
