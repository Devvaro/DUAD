import pytest
from Ejercicio_de_funciones_3 import sum_list

def test_sum_list_with_small_numbers():
    #arrange
    number_list= [12, 34, 56, 78]
    #act
    result = sum_list(number_list)
    #assert
    assert result == "the result of the list is: 180"

def test_sum_list_with_big_numbers():
    #arrange
    number_list= [4330, 2150, 6560, 7670, 8430, 1000]
    #act
    result = sum_list(number_list)
    #assert
    assert result == "the result of the list is: 30140"

def test_sum_list_with_negative_numbers():
    #arrange
    number_list= [-12, -34, -56, -78]
    #act
    result = sum_list(number_list)
    #assert
    assert result == "the result of the list is: -180"