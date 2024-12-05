from Menu import Menu
from Base import BaseHist

class NumeroComplexo:
    def __init__(self):
        r1 = float(input("Parte real do primeiro número complexo: "))
        i1 = float(input("Parte imaginária do primeiro número complexo: "))
        r2 = float(input("Parte real do segundo número complexo: "))
        i2 = float(input("Parte imaginária do segundo número complexo: "))

        self.z1 = NumeroComplexoIndividual(r1, i1)
        self.z2 = NumeroComplexoIndividual(r2, i2)
        self.historico = []  # Lista para armazenar o histórico

        menu_opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Módulo do primeiro número"]
        menu = Menu("Número Complexo", menu_opcoes)
        while True:
            menu.desenhar()
            escolha = input("Opção: ")
            match escolha:
                case "1":
                    resultado = self.z1.soma(self.z2)
                    resultado.exibir()
                    self.adicionar_historico("Soma", self.z1, self.z2, resultado)
                case "2":
                    resultado = self.z1.subtracao(self.z2)
                    resultado.exibir()
                    self.adicionar_historico("Subtração", self.z1, self.z2, resultado)
                case "3":
                    resultado = self.z1.multiplicacao(self.z2)
                    resultado.exibir()
                    self.adicionar_historico("Multiplicação", self.z1, self.z2, resultado)
                case "4":
                    resultado = self.z1.divisao(self.z2)
                    resultado.exibir()
                    self.adicionar_historico("Divisão", self.z1, self.z2, resultado)
                case "5":
                    print(f"Módulo: {self.z1.modulo()}")
                case "6": BaseHist.limpar_historico(self.historico)
                case "7": self.ver_historico()
                case _:
                    print("Opção inválida.")

    def adicionar_historico(self, operacao, z1, z2, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{operacao}: {z1.exibir()} e {z2.exibir()} => {resultado.exibir()}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

class NumeroComplexoIndividual:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def exibir(self):
        sinal = '+' if self.imaginario >= 0 else '-'
        return f"{self.real} {sinal} {abs(self.imaginario)}i"

    def soma(self, outro):
        real = self.real + outro.real
        imaginario = self.imaginario + outro.imaginario
        return NumeroComplexoIndividual(real, imaginario)

    def subtracao(self, outro):
        real = self.real - outro.real
        imaginario = self.imaginario - outro.imaginario
        return NumeroComplexoIndividual(real, imaginario)

    def multiplicacao(self, outro):
        real = self.real * outro.real - self.imaginario * outro.imaginario
        imaginario = self.real * outro.imaginario + self.imaginario * outro.real
        return NumeroComplexoIndividual(real, imaginario)

    def divisao(self, outro):
        denominador = outro.real ** 2 + outro.imaginario ** 2
        real = (self.real * outro.real + self.imaginario * outro.imaginario) / denominador
        imaginario = (self.imaginario * outro.real - self.real * outro.imaginario) / denominador
        return NumeroComplexoIndividual(real, imaginario)

    def modulo(self):
        return (self.real ** 2 + self.imaginario ** 2) ** 0.5
