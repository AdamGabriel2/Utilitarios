from Menu import Menu
from Base import BaseMath, BaseHist

# --- CALCULADORA COMPLETA ---
class CalculadoraCompleta(BaseMath):
    def __init__(self):
        """Exibe o menu de operações da calculadora."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes=["Adição","Subtração","Multiplicação","Divisão","Potência","Raiz Quadrada","Fatorial","Combinação","Permutação","Derivada","Integral"]
        menu = Menu("Calculadora Completa", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação: ")
            match opcao:
                case "0": return
                case "1": self.operacao("Adição", self.adicao)
                case "2": self.operacao("Subtração", self.subtracao)
                case "3": self.operacao("Multiplicação", self.multiplicacao)
                case "4": self.operacao("Divisão", self.divisao, divisao=True)
                case "5": self.operacao("Potência", self.potencia, potencia=True)
                case "6": self.operacao("Raiz Quadrada", self.raiz_quadrada, raiz_quadrada=True)
                case "7": self.operacao_fatorial()
                case "8": self.operacao_combinacao()
                case "9": self.operacao_permutacao()
                case "10": self.calcular_derivada()
                case "11": self.calcular_integral()
                case "12": BaseHist.limpar_historico(self.historico)
                case "13": self.ver_historico()
                case _: print("Opção inválida, tente novamente.")

    def operacao_fatorial(self):
        n = int(input("Digite n: "))
        resultado = self.fatorial(n)
        print(f"Fatorial de {n}: {resultado}")
        self.adicionar_historico(f"Fatorial de {n}", resultado)

    def operacao_combinacao(self):
        n = int(input("Digite n: "))
        k = int(input("Digite k: "))
        resultado = self.combinacao(n, k)
        print(f"Combinação C({n},{k}): {resultado}")
        self.adicionar_historico(f"Combinação C({n},{k})", resultado)

    def operacao_permutacao(self):
        n = int(input("Digite n: "))
        k = int(input("Digite k: "))
        resultado = self.permutacao(n, k)
        print(f"Permutação P({n},{k}): {resultado}")
        self.adicionar_historico(f"Permutação P({n},{k})", resultado)

    def operacao(self, nome_operacao, operacao, divisao=False, potencia=False, raiz_quadrada=False):
        """Realiza operações matemáticas básicas e avançadas."""
        try:
            if divisao:
                a = float(input("Entre com o dividendo: "))
                b = float(input("Entre com o divisor: "))
                if b == 0:
                    print("Erro: Divisão por zero não permitida.")
                    return
                resultado = operacao(a, b)
            elif potencia:
                a = float(input("Entre com a base: "))
                b = float(input("Entre com o expoente: "))
                resultado = operacao(a, b)
            elif raiz_quadrada:
                num = float(input("Entre com o número: "))
                resultado = operacao(num)
            else:
                a = float(input("Entre com o primeiro número: "))
                b = float(input("Entre com o segundo número: "))
                resultado = operacao(a, b)
            
            print(f"Resultado da {nome_operacao}: {resultado}")
            self.adicionar_historico(f"{nome_operacao} de {a} e {b}", resultado)
        except ValueError:
            print("Erro: Entrada inválida.")

    def adicao(self, a, b):
        r = a + b
        return f"Sistemas: Decimal: {r}, Octal: {self.dec_oct(r)}, Hexadecimal: {self.dec_hex(r)}, Binário: {self.dec_bin(r)}"

    def subtracao(self, a, b):
        r = a - b
        return f"Sistemas: Decimal: {r}, Octal: {self.dec_oct(r)}, Hexadecimal: {self.dec_hex(r)}, Binário: {self.dec_bin(r)}"

    def multiplicacao(self, a, b):
        r = a * b
        return f"Sistemas: Decimal: {r}, Octal: {self.dec_oct(r)}, Hexadecimal: {self.dec_hex(r)}, Binário: {self.dec_bin(r)}"

    def divisao(self, a, b):
        r = a / b
        return f"Sistemas: Decimal: {r}, Octal: {self.dec_oct(r)}, Hexadecimal: {self.dec_hex(r)}, Binário: {self.dec_bin(r)}"

    def potencia(self, a, b):
        r = a ** b
        return f"Sistemas: Decimal: {r}, Octal: {self.dec_oct(r)}, Hexadecimal: {self.dec_hex(r)}, Binário: {self.dec_bin(r)}"

    def fatorial(self, n):
        """Calcula o fatorial de um número inteiro não negativo."""
        if n < 0:
            raise ValueError("Fatorial não é definido para números negativos.")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def combinacao(self, n, k):
        """Calcula a combinação de n elementos tomados k a k."""
        if k > n:
            return 0
        return self.fatorial(n) // (self.fatorial(k) * self.fatorial(n - k))

    def permutacao(self, n, k):
        """Calcula a permutação de n elementos tomados k a k."""
        if k > n:
            return 0
        return self.fatorial(n) // self.fatorial(n - k)

    def calcular_derivada(self):
        print("Cálculo de Derivada de um Polinômio: a_nx^n + a_(n-1)x^(n-1) + ... + a_0")
        n = int(input("Digite o grau do polinômio: "))
        coeficientes = []
        for i in range(n, -1, -1):
            coeficientes.append(float(input(f"Digite o coeficiente de x^{i}: ")))
        derivada = [(n - i) * coeficientes[i] for i in range(len(coeficientes) - 1)]
        derivada_str = " + ".join(f"{coef}x^{n - i - 1}" for i, coef in enumerate(derivada) if coef != 0)
        print("Derivada: ", derivada_str)
        self.adicionar_historico(f"Derivada do polinômio de grau {n}", derivada_str)

    def calcular_integral(self):
        print("Cálculo de Integral de um Polinômio: a_nx^n + a_(n-1)x^(n-1) + ... + a_0")
        n = int(input("Digite o grau do polinômio: "))
        coeficientes = []
        for i in range(n, -1, -1):
            coeficientes.append(float(input(f"Digite o coeficiente de x^{i}: ")))
        integral = [coeficientes[i] / (n - i + 1) for i in range(len(coeficientes))]
        integral_str = " + ".join(f"{coef}x^{n - i + 1}" for i, coef in enumerate(integral))
        print("Integral: ", integral_str)
        self.adicionar_historico(f"Integral do polinômio de grau {n}", integral_str)
        
    def adicionar_historico(self, operacao, resultado):
        """Adiciona uma entrada ao histórico."""
        self.historico.append(f"{operacao}: {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)
