from Menu import Menu
from Base import BaseHist

# --- FUNÇÕES MATEMÁTICAS ---
class FuncoesMatematicas:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Logaritmo", "Exponencial", "Seno", "Cosseno", "Tangente"]
        menu = Menu("Funções Matemáticas", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            num = float(input("Digite o número: "))
            match func:
                case "1":
                    resultado = self.logaritmo(num)
                    print(f"Logaritmo de {num}: {resultado}")
                    self.adicionar_historico("Logaritmo", num, resultado)
                case "2":
                    resultado = self.exponencial(num)
                    print(f"Exponencial de {num}: {resultado}")
                    self.adicionar_historico("Exponencial", num, resultado)
                case "3":
                    resultado = self.seno(num)
                    print(f"Seno de {num}: {resultado}")
                    self.adicionar_historico("Seno", num, resultado)
                case "4":
                    resultado = self.cosseno(num)
                    print(f"Cosseno de {num}: {resultado}")
                    self.adicionar_historico("Cosseno", num, resultado)
                case "5":
                    resultado = self.tangente(num)
                    print(f"Tangente de {num}: {resultado}")
                    self.adicionar_historico("Tangente", num, resultado)
                case "6": BaseHist.limpar_historico(self.historico)
                case "7": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, funcao, num, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{funcao} de {num} = {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

    def logaritmo(self, x, base=10):
        """Calcula o logaritmo de x na base especificada."""
        if x <= 0:
            raise ValueError("Logaritmo indefinido para valores menores ou iguais a zero.")
        return self.exponencial(self.logaritmo_base_e(x)) / self.exponencial(self.logaritmo_base_e(base))

    def logaritmo_base_e(self, x):
        """Calcula o logaritmo natural (base e) usando a série de Taylor."""
        if x <= 0:
            raise ValueError("Logaritmo indefinido para valores menores ou iguais a zero.")
        resultado = 0
        termo = (x - 1)  # Primeiro termo da série
        n = 1
        while abs(termo) > 1e-10:  # Precisão
            resultado += termo / n
            n += 1
            termo *= (x - 1) / n
        return resultado

    def exponencial(self, x):
        """Calcula e^x usando a série de Taylor."""
        resultado = 1.0
        termo = 1.0
        n = 1
        while abs(termo) > 1e-10:  # Precisão
            termo *= x / n
            resultado += termo
            n += 1
        return resultado

    def seno(self, x):
        """Calcula o seno de x usando a série de Taylor."""
        resultado = 0.0
        termo = x  # Primeiro termo da série
        n = 1
        while abs(termo) > 1e-10:  # Precisão
            resultado += termo
            termo *= -x * x / ((2 * n) * (2 * n + 1))  # Fórmula do termo seguinte
            n += 1
        return resultado

    def cosseno(self, x):
        """Calcula o cosseno de x usando a série de Taylor."""
        resultado = 0.0
        termo = 1.0  # Primeiro termo da série
        n = 1
        while abs(termo) > 1e-10:  # Precisão
            resultado += termo
            termo *= -x * x / ((2 * n - 1) * (2 * n))  # Fórmula do termo seguinte
            n += 1
        return resultado

    def tangente(self, x):
        """Calcula a tangente de x como seno/cosseno."""
        seno_val = self.seno(x)
        cosseno_val = self.cosseno(x)
        if cosseno_val == 0:
            raise ValueError("Tangente indefinida para valores onde o cosseno é zero.")
        return seno_val / cosseno_val