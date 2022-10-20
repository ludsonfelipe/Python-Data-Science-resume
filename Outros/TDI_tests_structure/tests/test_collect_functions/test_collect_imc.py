# Objetivos
# receber 3 inputs
# criamos 3 tipos de testes 
# - Bad arguments (argumentos que testam error)| Special arguments (Argumentos que testam resultados impossiveis) | Normal arguments (argumentos que testam resultados possiveis)
# dentro de cada classe, vai ter varios testes para uma função

import pytest
from TDI_tests_structure.functions_to_projects.collect_functions.collect_imc import collect_name 
#, collect_info
collect_name('test')
"""class TestCollectName(object):
    # Normal Tests
    def test_name_capitalize(self):
        actual = collect_name('JoN')
        expected = 'jon'
        assert actual == expected, f'actual value: {actual} expected value: {expected}'

    def test_name_strip(self):
        actual = collect_name(' felipe ')
        expected = 'felipe'
        assert actual == expected, f'actual value: {actual} expected value: {expected}'

    def test_only_first_name(self):
        actual = collect_name('felipe souza')
        expected = 'felipe'
        assert actual == expected, f'actual value: {actual} expected value: {expected}'

    # Special Tests
    def test_name_size(self):
        actual = collect_name('Fe')
        assert actual is None, f'actual value:{actual} expected None'

    def test_name_alphabet(self):
        actual = collect_name('#$!Lipe')
        assert actual is None, f'actual value:{actual} expected None'
    
    # Bad Test
    def test_name_is_not_string(self):
        with pytest.raises(AttributeError) as message_error:
            actual = collect_name(3121)
        assert message_error.match('The input needs to be a string')
        """



