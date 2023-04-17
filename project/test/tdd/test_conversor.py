import pytest

import os
print(os.getcwd())

from project.src.conversor import Conversor

@pytest.fixture
def conversor():
    try:
        conversor = Conversor()
    except:
        assert 0, "Es necesario crear la clase Conversor"
    return conversor


def test_fahrenheit_to_centigrados(conversor):
    assert hasattr(conversor, "fahrenheit_to_centigrados"), "La clase Conversor debe tener un método fahrenheit_to_centigrados"
    assert conversor.fahrenheit_to_centigrados(32) == 0, "32ºF son 0ºC"
    assert conversor.fahrenheit_to_centigrados(50) == 10, "50ºF son 10ºC"

def test_centigrados_to_fahrenheit(conversor):
    assert hasattr(conversor, "centigrados_to_fahrenheit"), "La clase Conversor debe tener un método centigrados_to_fahrenheit"
    assert conversor.centigrados_to_fahrenheit(0) == 32, "0ºC son 32ºF"
    assert conversor.centigrados_to_fahrenheit(10) == 50, "10ºC son 50ºF"

@pytest.mark.parametrize("data", [0, 1, 2, 3])
def test_invertir(conversor, data):
    temp = conversor.fahrenheit_to_centigrados(data)
    grados = conversor.centigrados_to_fahrenheit(temp)
    assert grados == data
    
