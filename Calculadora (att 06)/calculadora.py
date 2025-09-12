class Calculadora:
    def soma(self, a: float, b: float) -> float:
        return a + b

    def subtracao(self, a: float, b: float) -> float:
        return a - b

    def multiplicacao(self, a: float, b: float) -> float:
        return a * b

    def divisao(self, a: float, b: float) -> float:
        if b == 0:
            raise ArithmeticError("Divisão por zero não é permitida.")
        return a / b 


class CalculadoraService:
    def media(self, a: float, b: float) -> float:
        return (a + b) / 2.0

    def porcentagem(self, valor: float, percentual: float) -> float:
        return (valor * percentual) / 100.0

    def regra_de_tres(self, valor_a: float, valor_b: float, valor_c: float) -> float:
        if valor_a == 0:
            raise ArithmeticError("Valor A não pode ser zero na regra de três.")
        return (valor_b * valor_c) / valor_a


def main():
    calc = Calculadora()
    service = CalculadoraService()

    menu = """=== CALCULADORA ===
Digite a operação desejada:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Média de dois valores
6 - Porcentagem
7 - Regra de três simples
Escolha a opção: """

    try:
        opcao = int(input(menu))

        resultado = None

        if opcao == 1:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calc.soma(a, b)

        elif opcao == 2:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calc.subtracao(a, b)

        elif opcao == 3:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calc.multiplicacao(a, b)

        elif opcao == 4:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = calc.divisao(a, b)

        elif opcao == 5:
            m1 = float(input("Digite o primeiro número: "))
            m2 = float(input("Digite o segundo número: "))
            resultado = service.media(m1, m2)

        elif opcao == 6:
            valor = float(input("Digite o valor: "))
            perc = float(input("Digite a porcentagem (%): "))
            resultado = service.porcentagem(valor, perc)

        elif opcao == 7:
            valA = float(input("Digite o valor A: "))
            valB = float(input("Digite o valor B: "))
            valC = float(input("Digite o valor C: "))
            resultado = service.regra_de_tres(valA, valB, valC)

        else:
            print("Opção inválida!")
            return

        print("Resultado:", resultado)

    except ArithmeticError as e:
        print("Erro:", e)
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar números válidos.")
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")


if __name__ == "__main__":
    main()