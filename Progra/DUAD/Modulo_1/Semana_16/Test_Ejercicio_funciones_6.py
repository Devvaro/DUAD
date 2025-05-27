import pytest
from Ejercicio_de_funciones_6 import sort_list

def test_sort_list_should_not_work_with_numbers():
    #arrange
    number_list=[6,2,3,4,5]
    #act
    with pytest.raises(ValueError):
        result=sort_list(number_list)
    #assert
    assert True

def test_should_not_work_if_input_is_not_a_list():
    #arrange
    "6,2,Apple,Banana,Watermelon"
    #act
    with pytest.raises(TypeError):
        result = sort_list(list)
    #assert
    assert True

def test_sort_list_with_empty_list():
    #arrange
    list=[]
    #act
    result = sort_list(list)
    #assert
    assert result == []