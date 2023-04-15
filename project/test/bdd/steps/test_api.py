import pytest
 
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json

 
# Constants
 
APP_URL = 'http://100.27.39.229:8080/myapi/'

# Scenarios
 
scenarios('../features/api.feature')

# Fixtures
 
@pytest.fixture
def browser():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    b = webdriver.Firefox(options=options)
    b.implicitly_wait(0.1)
    yield b
    b.quit()

# Given Steps
 
@given(parsers.parse('myapi version {v}'))
def app_home(browser, v):
    browser.get(APP_URL+'version')
    #data = browser.page_source
    data = browser.find_element(By.ID, 'json')
    print(data.text)
    r = json.loads(data.text)
    assert r['result'] == v

# When Steps
 
@when(parsers.parse('user invokes GET /f2c/{f}'))
def saysme_hello(browser,f):
    url = APP_URL+'f2c/'+f
    print(url)
    browser.get(APP_URL+'f2c/'+f)
    data = browser.page_source
    print(data)



# Then Steps
 
@then(parsers.parse('api returns json with result: {c}'))
def hello(browser, c):
    data = browser.find_element(By.ID, 'json')
    r = json.loads(data.text)
    assert r['result'] == float(c)