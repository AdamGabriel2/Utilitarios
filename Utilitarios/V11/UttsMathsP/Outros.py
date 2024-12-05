import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def calcular_limite_op(self):
    funcao_str = input("Digite a função (em termos de x): ")
    variavel = 'x'
    ponto = float(input("Digite o ponto para calcular o limite: "))
    limite = self.calcular_limite(eval(funcao_str), variavel, ponto)
    print(f"Limite de {funcao_str} em {ponto}: {limite}")

def calcular_limite(self, funcao, variavel, ponto):
    x = sp.symbols(variavel)
    limite = sp.limit(funcao(x), x, ponto)
    return limite

def fatorar_polinomio_op(self):
    polinomio_str = input("Digite o polinômio (em termos de x): ")
    fatorado = self.fatorar_polinomio(eval(polinomio_str))
    print(f"Fatoração de {polinomio_str}: {fatorado}")

def fatorar_polinomio(self, polinomio):
    x = sp.symbols('x')
    fatorado = sp.factor(polinomio(x))
    return fatorado

def plotar_funcao_op(self):
    funcao_str = input("Digite a função (em termos de x): ")
    intervalo = list(map(float, input("Digite o intervalo (início, fim): ").split(',')))
    self.plotar_funcao(eval(funcao_str), intervalo)

def plotar_funcao(self, funcao, intervalo, pontos=100):
    x = np.linspace(intervalo[0], intervalo[1], pontos)
    y = funcao(x)
    plt.plot(x, y, label=str(funcao))
    plt.title("Gráfico da Função")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()
