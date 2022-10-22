import sys
my_project = 'C:\\Users\\felip\\Desktop\\github\\estudos_felipe\\Outros\\TDI_tests_structure'
paths = sys.path.append(my_project)

# Objetivos
# receber 3 inputs
# criamos 3 tipos de testes 
# - Bad arguments (argumentos que testam error)| Special arguments (Argumentos que testam resultados impossiveis) | Normal arguments (argumentos que testam resultados possiveis)
# dentro de cada classe, vai ter varios testes para uma função


from functions_to_projects.collect_functions.collect_imc import collect_name,collect_metrics,others

import pytest

# we can import three kinds of functions from the same file in the same test file, but we need to separate it in class
class TestCollectName(object):
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
    
    def test_name_wrong_input(self):
        actual = collect_name(31221)
        assert actual is None, f'actual value:{actual} expected None'
    
    # Bad Test
    def test_name_is_not_string(self):
        with pytest.raises(TypeError) as message_error:
            actual = collect_name()
        assert message_error.match(r"collect_name\(\) missing 1 required positional argument: 'name'")
    
# other example of metrics
class TestCollectMetrics(object):
    def test_weight_type(self):
        actual = collect_metrics(65.4,1.60)
        expected = (65.4,1.60)
        assert actual == expected, f'actual value: {actual} expected value: {expected}'

    def test_height(self):
        actual = collect_metrics(1001,1.75)
        expected = 'O peso inserido na calculadora não pode ser maior que 1000 ou menor que 0.1'
        assert actual == expected, f'actual value: {actual} expected value: {expected}'

    def test_weight(self):
        actual = collect_metrics(20,4)
        expected = 'A altura inserida na calculadora não pode ser maior que 3 metros ou menor que 0.1'
        assert actual == expected, f'actual value: {actual} expected value: {expected}'

    def test_weight(self):
        with pytest.raises(TypeError) as message_error:
            actual = collect_metrics()
        
        assert message_error.match(r"collect_metrics\(\) missing 2 required positional arguments: 'weight' and 'height'")


# This decorators is utils when we need to accept a fail test, that we havent written yet
@pytest.mark.xfail(reason='fuction not implemented yet') # we can use @pytest.mark.skipif too, if we know which kind of problems we will receive, @pytest.mark.skipif(sys.version_info > (3, 3), reason = 'requeries python in a version below 3.3')
class TestOthers(object):
    def test_others(self):
        actual = others('outra info')
        expected = 'outra info'
        assert actual == expected, f'actual value: {actual} expected value {expected}'