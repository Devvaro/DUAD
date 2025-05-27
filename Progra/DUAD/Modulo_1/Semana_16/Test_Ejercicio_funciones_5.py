import pytest
from Ejercicio_de_funciones_5 import look_for_upper_and_lower

def test_with_string_with_numbers():
    #arrange
    string = "I'm 25 years old"
    #act
    result = look_for_upper_and_lower(string)
    #assert
    assert result == (1, 9)

def test_with_string_with_special_characters():
    #arrange
    string = "AeFt@#hT^&*"
    #act
    result = look_for_upper_and_lower(string)
    #assert
    assert result == (3, 3)

def test_should_return_an_error_when_input_is_not_a_string():
    #arrange
    string = 12345
    #act
    with pytest.raises(TypeError):
        look_for_upper_and_lower(string)
    #assert
    assert True