import pytest
from Ejercicio_de_funciones_4 import reversed_string

def test_reversed_string():
    # Arrange
    string = "Hello World"
    # Act
    result = reversed_string(string)
    # Assert
    assert result == "dlroW olleH"


def test_reversed_string_empty_string():
    # Arrange
    string = ""
    # Act
    result = reversed_string(string)
    # Assert
    assert result == "" 


def test_reversed_string_with_numbers():
    # Arrange
    string = "12345"
    # Act
    result = reversed_string(string)
    # Assert
    assert result == "54321"