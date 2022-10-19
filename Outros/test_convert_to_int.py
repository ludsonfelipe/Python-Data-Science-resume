import pytest
from function import convert_to_int


# testing if when we have a value with dot instead of comma we have problems
def test_convert_to_dot():
    assert convert_to_int('293.93') == None, "Não aceitamos mensagens com pontos em vez de virgula"


# test if the value is correct
def test_convert_to_int():
    assert convert_to_int('294,34') == 29434


# We can put more than one assert in the function
def test_convert_to_large_int():
    value = convert_to_int('294,331234')
    assert type(value) == int,"O Tipo de dado também deu certo"
    assert value  == 294331234, "O valor deu certo"


# We can create raises for the erros
def test_value_error():
    """In this case we tried to simulate a AtributeError in the funcion, we send to the function a list value, and the expect a string value,
    so because of that, we will show the message of the error, the pytest.raises is util for that"""
    value_to_test = [3291]
    with pytest.raises(AttributeError) as message_error:
        value = convert_to_int(value_to_test)
    assert message_error.match('O valor passado para função deve ser uma string, a lista não tem o atributo replace')
    