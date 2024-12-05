from Menu import Menu
from Base import BaseHist

class Fracao:
    def __init__(self):
        n1 = int(input("Numerador da primeira fração: "))
        d1 = int(input("Denominador da primeira fração: "))
        n2 = int(input("Numerador da segunda fração: "))
        d2 = int(input("Denominador da segunda fração: "))

        self.f1 = FracaoIndividual(n1, d1)
        self.f2 = FracaoIndividual(n2, d2)
        self.historico = []  # Lista para armazenar o histórico

        menu_opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
        menu = Menu("Fração", menu_opcoes)
        while True:
            menu.desenhar()
            escolha = input("Opção: ")
            match escolha:
                case "1":
                    resultado = self.f1.soma(self.f2)
                    resultado.exibir()
                    self.adicionar_historico("Soma", self.f1, self.f2, resultado)
                case "2":
                    resultado = self.f1.subtracao(self.f2)
                    resultado.exibir()
                    self.adicionar_historico("Subtração", self.f1, self.f2, resultado)
                case "3":
                    resultado = self.f1.multiplicacao(self.f2)
                    resultado.exibir()
                    self.adicionar_historico("Multiplicação", self.f1, self.f2, resultado)
                case "4":
                    resultado = self.f1.divisao(self.f2)
                    resultado.exibir()
                    self.adicionar_historico("Divisão", self.f1, self.f2, resultado)
                case "5": BaseHist.limpar_historico(self.historico)
                case "6": self.ver_historico()
                case _:
                    print("Opção inválida.")

    def adicionar_historico(self, operacao, f1, f2, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{operacao}: {f1.exibir()} e {f2.exibir()} => {resultado.exibir()}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

class FracaoIndividual:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ZeroDivisionError("Denominador não pode ser zero.")
        self.numerador = numerador
        self.denominador = denominador

    def exibir(self):
        return f"{self.numerador}/{self.denominador}"

    def soma(self, outra):
        novo_numerador = self.numerador * outra.denominador + self.denominador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return FracaoIndividual(novo_numerador, novo_denominador).simplificar()

    def subtracao(self, outra):
        novo_numerador = self.numerador * outra.denominador - self.denominador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return FracaoIndividual(novo_numerador, novo_denominador).simplificar()

    def multiplicacao(self, outra):
        novo_numerador = self.numerador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return FracaoIndividual(novo_numerador, novo_denominador).simplificar()

    def divisao(self, outra):
        novo_numerador = self.numerador * outra.denominador
        novo_denominador = self.denominador * outra.numerador
        return FracaoIndividual(novo_numerador, novo_denominador).simplificar()

    def simplificar(self):
        def calcular_mdc(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        mdc = calcular_mdc(self.numerador, self.denominador)
        return FracaoIndividual(self.numerador // mdc, self.denominador // mdc)
