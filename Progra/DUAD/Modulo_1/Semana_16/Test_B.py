import pytest, random
from Ejercicio_1 import bubble_sort
def test_bubble_sort_with_big_lists():
    #Arrange
    test_list = [random.randint(0, 1000) for _ in range(102)]
    #Act
    bubble_sort(test_list)
    #Assert
    assert test_list == sorted(test_list)