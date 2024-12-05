from Menu import Menu
from UttsMathsP.CalcComp import CalculadoraCompleta
from UttsMathsP.Tabuada import Tabuada
from UttsMathsP.FuncMath import FuncoesMatematicas
from UttsMathsP.EsttsProb import EstatisticasProbabilidades
from UttsMathsP.Equacoes import Equacoes
from UttsMathsP.OpVetores import OperacoesVetores
from UttsMathsP.OpMatrizes import OperacoesMatrizes
from UttsMathsP.Geometria import Geometria
from UttsMathsP.Teoremas import Teoremas
from UttsMathsP.NumComplex import NumeroComplexo
from UttsMathsP.Outros import *

class UttsMaths:
    def __init__(self):
        menu_opcoes = ["Calculadora Completa", "Tabuada", "Funções Matemáticas", "Calculo de Estatística e Probabilidades", "Resolver Equações", "Operações com Vetores", "Operações com Matrizes", "Geometria", "Teorema", "Número Complexo", "Cálculo de Limites", "Fatoração de Polinômios", "Gráficos de Funções"]
        while True:
            menu = Menu("Utilitários Matemáticos", menu_opcoes)
            menu.desenhar()
            escolha = input("Escolha uma opção: ")
            match escolha:
                case "0": return
                case "1": CalculadoraCompleta()
                case "2": Tabuada()
                case "3": FuncoesMatematicas()
                case "4": EstatisticasProbabilidades()
                case "5": Equacoes()
                case "6": OperacoesVetores()
                case "7": OperacoesMatrizes()
                case "8": Geometria()
                case "9": Teoremas()
                case "10": NumeroComplexo()
                case "11": self.calcular_limite_op()
                case "12": self.fatorar_polinomio_op()
                case "13": self.plotar_funcao_op()
                case _: print("Opção inválida. Por favor, escolha novamente.")
