import pytest
from Ejercicio_1 import bubble_sort

def test_not_a_list():
    #Arrange
    test_list = 1
    #Act
    with pytest.raises(TypeError):
        bubble_sort(test_list)
    #Assert
    assert True