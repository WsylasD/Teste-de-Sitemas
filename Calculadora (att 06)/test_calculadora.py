import pytest
from calculadora import Calculadora, CalculadoraService

# Fixture para instanciar a calculadora
@pytest.fixture
def calc():
    return Calculadora()

@pytest.fixture
def service():
    return CalculadoraService()


# === TESTES CALCULADORA ===

def test_soma(calc):
    assert calc.soma(2, 3) == 5
    assert calc.soma(4.5, -3) == 1.5
    assert calc.soma(-10, -35) == -45
    assert pytest.approx(calc.soma(5.5, -4.4), 0.0001) == 1.1
    assert pytest.approx(calc.soma(-1.1, -2.5), 0.0001) == -3.6

def test_subtracao(calc):
    assert calc.subtracao(5, 3) == 2
    assert calc.subtracao(0, 5) == -5
    assert calc.subtracao(-15, -5) == -10
    assert pytest.approx(calc.subtracao(2.1, -9.3), 0.0001) == 11.4
    assert pytest.approx(calc.subtracao(-1.2, 3.3), 0.0001) == -4.5

def test_multiplicacao(calc):
    assert calc.multiplicacao(4, 3) == 12
    assert calc.multiplicacao(-2, 3) == -6
    assert pytest.approx(calc.multiplicacao(-6.1, 7.5), 0.0001) == -45.75
    assert calc.multiplicacao(-4, -5) == 20
    assert pytest.approx(calc.multiplicacao(4.5, 3.6), 0.0001) == 16.2

def test_divisao(calc):
    assert calc.divisao(10, 5) == 2
    assert calc.divisao(4, 2) == 2
    assert calc.divisao(-8.5, 2.5) == -3.4
    assert calc.divisao(3.8, -1.9) == -2
    assert calc.divisao(-9, -3) == 3

def test_divisao_por_zero(calc):
    with pytest.raises(ArithmeticError) as excinfo:
        calc.divisao(10, 0)
    assert str(excinfo.value) == "Divisão por zero não é permitida."

    with pytest.raises(ArithmeticError) as excinfo:
        calc.divisao(-5, 0)
    assert str(excinfo.value) == "Divisão por zero não é permitida."

    with pytest.raises(ArithmeticError) as excinfo:
        calc.divisao(7.5, 0)
    assert str(excinfo.value) == "Divisão por zero não é permitida."


# === TESTES CALCULADORA SERVICE ===

def test_media(service):
    assert pytest.approx(service.media(3.0, 4.0), 0.0001) == 3.5

def test_porcentagem(service):
    assert pytest.approx(service.porcentagem(200.0, 10.0), 0.0001) == 20.0
    assert pytest.approx(service.porcentagem(50.0, 50.0), 0.0001) == 25.0

def test_regra_de_tres(service):
    assert pytest.approx(service.regra_de_tres(2.0, 5.0, 4.0), 0.0001) == 10.0

def test_regra_de_tres_valor_a_zero_levanta_erro(service):
    with pytest.raises(ArithmeticError) as excinfo:
        service.regra_de_tres(0.0, 5.0, 4.0)
    assert str(excinfo.value) == "Valor A não pode ser zero na regra de três."