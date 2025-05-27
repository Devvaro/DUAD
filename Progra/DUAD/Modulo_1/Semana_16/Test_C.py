import pytest
from Ejercicio_1 import bubble_sort

def test_empty_list():
    #Arrange
    test_list = []
    #Act
    bubble_sort(test_list)
    #Assert
    assert test_list == []