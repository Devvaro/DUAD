import pytest
from Ejercicio_1 import bubble_sort
def test_bubble_sort_with_small_lists():
    #Arrange
    test_list = [3, 4, 8 , 6, 7, 10]
    #Act
    bubble_sort(test_list)
    #Assert
    assert test_list == [3, 4, 6, 7, 8, 10] 

