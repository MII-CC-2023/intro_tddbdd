import pytest
 
from pytest_bdd import scenarios, given, when, then, parsers, scenario
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json

 
# Constants
 
APP_URL = 'http://52.90.108.163:8080/api'

# Scenarios

#scenarios('../features/api.feature')

@scenario(
    "../features/api.feature",
    "convert fahrenheit to centigrados",
)
def test_outlined():
    pass




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
    browser.get(APP_URL+'/version')
    assert "Not Found" not in browser.page_source, "La API debe atender a http://<IP>:8080/api/version"
    data = browser.find_element(By.ID, 'json')
    try:
        r = json.loads(data.text)
        version = r['result']
    except:
        assert 0, "El 'json' debe incluir un campo result con la versión"
    try:
        status = r['status']
    except:
        assert 0, "El 'json' debe incluir un campo status con valor success"
    assert version == v, "La versión no es la correcta"
    assert status == "success", "El estado no es correcto"

# When Steps

@when(parsers.parse('user invokes GET /f2c/{f}'))
def saysme_hello(browser,f):
    url = APP_URL+'/f2c/'+ f
    print(url)
    browser.get(url)
    assert "Not Found" not in browser.page_source, "La API debe atender a http://<IP>:8080/api/f2c/<N>"
    data = browser.page_source
    #print(data)



# Then Steps
 
 
@then(parsers.parse('for {f}, api returns json with result: {c}'))
def hello(browser, f, c):
    data = browser.find_element(By.ID, 'json')
    try:
        r = json.loads(data.text)
        result = r['result']
    except:
        assert 0, "El 'json' debe incluir un campo result con el resultado de la conversión"
    try:
        status = r['status']
    except:
        assert 0, "El 'json' debe incluir un campo status con valor success"
    try:
        i = r['input']
    except:
        assert 0, "El 'json' debe incluir un campo input con el valor de entrada"
    assert i == int(f), f"El valor de entrada debe ser {f}"
    assert result == float(c), f"El resultado debe ser {c}"