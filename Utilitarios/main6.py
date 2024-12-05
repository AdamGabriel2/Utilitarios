import random
from collections import Counter

class UtilitariosMatematicos:
    def menu_principal(self):
        """Exibe o menu principal e permite navegação entre diferentes funcionalidades."""
        while True:
            print("\n|============================|")
            print("|        Menu Principal      |")
            print("|1. Calculadora              |")
            print("|2. Tabuada                  |")
            print("|3. Verificar Número         |")
            print("|4. Análise de Texto         |")
            print("|5. Conversores              |")
            print("|6. Jogos Matemáticos        |")
            print("|0. Sair                     |")
            print("|============================|")
            escolha = input("Escolha uma opção: ")
            match escolha:
                case "0": 
                    print("Fim do Programa.")
                    break
                case "1":
                    c1=Calculadora()
                    c1.calculadora()
                case "2":
                    c2=Tabuada()
                    c2.tabuada()
                case "3":
                    c3=Verificacoes()
                    c3.verificar_numero()
                case "4":
                    c4=AnaliseTexto()
                    c4.analise_texto()
                case "5":
                    c5=Conversor()
                    c5.menu_principal()
                case "6":
                    c6=JogosMatematicos()
                    c6.jogos_matematicos()
                case _: print("Opção inválida. Por favor, escolha novamente.")

# --- CALCULADORA ---
class Calculadora:
    def calculadora(self):
        """Exibe o menu de operações da calculadora."""
        print("\n|============================|")
        print("|        Calculadora         |")
        print("|1. Adição                   |")
        print("|2. Subtração                |")
        print("|3. Multiplicação            |")
        print("|4. Divisão                  |")
        print("|5. Potência                 |")
        print("|6. Raiz Quadrada            |")
        print("|7. Funções Avançadas        |")
        print("|8. Resolver Equação         |")
        print("|9. Operações com Matrizes   |")
        print("|0. Voltar                   |")
        print("|============================|")
        opcao = input("Escolha uma operação: ")
        match opcao:
            case "0": return
            case "1": self.operacao("Adição", self.adicao)
            case "2": self.operacao("Subtração", self.subtracao)
            case "3": self.operacao("Multiplicação", self.multiplicacao)
            case "4": self.operacao("Divisão", self.divisao, divisao=True)
            case "5": self.operacao("Potência", self.potencia, potencia=True)
            case "6": self.operacao("Raiz Quadrada", self.raiz_quadrada, raiz_quadrada=True)
            case "7": self.funcoes_avancadas()
            case "8": self.resolver_equacao()
            case "9": self.operacoes_matrizes()
            case _: print("Opção inválida, tente novamente.")

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
        except ValueError:
            print("Erro: Entrada inválida.")

    def adicao(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

    def potencia(self, a, b):
        return a ** b

    def raiz_quadrada(self, num):
        """Calcula a raiz quadrada de um número usando o método de Newton."""
        if num < 0:
            return complex(0, abs(num) ** 0.5)  # Para números negativos, retorna a parte imaginária
        x = num
        y = (x + 1) / 2
        while y < x:
            x = y
            y = (x + num / x) / 2
        return x

    def funcoes_avancadas(self):
        """Executa funções avançadas: logaritmo, exponencial, seno, cosseno, tangente, fatorial, combinação, permutação, derivada e integral."""
        print("\n|============================|")
        print("|    Funções Avançadas       |")
        print("|1. Logaritmo                |")
        print("|2. Exponencial              |")
        print("|3. Seno                     |")
        print("|4. Cosseno                  |")
        print("|5. Tangente                 |")
        print("|6. Fatorial                 |")
        print("|7. Combinação               |")
        print("|8. Permutação               |")
        print("|9. Derivada                 |")
        print("|10. Integral                |")
        print("|0. Voltar                   |")
        print("|============================|")
        func = input("Escolha uma função: ")
        try:
            if func in ["6", "7", "8"]:
                n = int(input("Digite n: "))
                match func:
                    case "7":
                        k = int(input("Digite k: "))
                        resultado = self.combinacao(n, k)
                        print(f"Combinação C({n},{k}): {resultado}")
                    case "8":
                        k = int(input("Digite k: "))
                        resultado = self.permutacao(n, k)
                        print(f"Permutação P({n},{k}): {resultado}")
                    case "6":
                        resultado = self.fatorial(n)
                        print(f"Fatorial de {n}: {resultado}")
            else:
                num = float(input("Digite o número: "))
                match func:
                    case "1": print(f"Logaritmo de {num}: {self.logaritmo(num)}")
                    case "2": print(f"Exponencial de {num}: {self.exponencial(num)}")
                    case "3": print(f"Seno de {num}: {self.seno(num)}")
                    case "4": print(f"Cosseno de {num}: {self.cosseno(num)}")
                    case "5": print(f"Tangente de {num}: {self.tangente(num)}")
                    case "9": self.calcular_derivada()
                    case "10": self.calcular_integral()
                    case _: print("Opção inválida.")
        except ValueError:
            print("Erro: Entrada inválida.")

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

    def resolver_equacao(self):
        """Resolve equações de primeiro e segundo grau."""
        print("Resolva equações do tipo ax² + bx + c = 0 (segundo grau) ou ax + b = 0 (primeiro grau)")
        grau = input("Digite '1' para primeiro grau e '2' para segundo grau: ")
        try:
            if grau == "1":
                a = float(input("Coeficiente a: "))
                b = float(input("Coeficiente b: "))
                solucao = -b / a
                print(f"Solucão da equação linear: x = {solucao}")
            elif grau == "2":
                a = float(input("Coeficiente a: "))
                b = float(input("Coeficiente b: "))
                c = float(input("Coeficiente c: "))
                discriminante = b**2 - (4 * a * c)
                if discriminante >= 0:
                    raiz1 = (-b + self.raiz_quadrada(discriminante)) / (2 * a)
                    raiz2 = (-b - self.raiz_quadrada(discriminante)) / (2 * a)
                    print(f"As raízes são x1 = {raiz1} e x2 = {raiz2}")
                else:
                    print("Sem solução real.")
        except ValueError:
            print("Erro: Entrada inválida.")

    def calcular_derivada(self):
        print("Cálculo de Derivada de um Polinômio: a_nx^n + a_(n-1)x^(n-1) + ... + a_0")
        n = int(input("Digite o grau do polinômio: "))
        coeficientes = []
        for i in range(n, -1, -1):
            coeficientes.append(float(input(f"Digite o coeficiente de x^{i}: ")))
        derivada = [(n - i) * coeficientes[i] for i in range(len(coeficientes) - 1)]
        print("Derivada: ", " + ".join(f"{coef}x^{n - i - 1}" for i, coef in enumerate(derivada) if coef != 0))
        
    def calcular_integral(self):
        print("Cálculo de Integral de um Polinômio: a_nx^n + a_(n-1)x^(n-1) + ... + a_0")
        n = int(input("Digite o grau do polinômio: "))
        coeficientes = []
        for i in range(n, -1, -1):
            coeficientes.append(float(input(f"Digite o coeficiente de x^{i}: ")))
        integral = [coeficientes[i] / (n - i + 1) for i in range(len(coeficientes))]
        print("Integral: ", " + ".join(f"{coef}x^{n - i + 1}" for i, coef in enumerate(integral)))
        
    def operacoes_matrizes(self):
        """Realiza operações com matrizes."""
        print("\n|============================|")
        print("|   Operações com Matrizes   |")
        print("|1. Adição                   |")
        print("|2. Multiplicação            |")
        print("|3. Transposição             |")
        # ... (adicione outras operações) ...
        print("|0. Voltar                   |")
        print("|============================|")

        opcao = input("Escolha uma operação: ")
        
        tamanho = input("Digite o tamanho da matriz (ex: 2x2): ")
        valor_inicial = float(input("Digite o valor inicial: "))
        tipo_progressao = input("Digite o tipo de progressão (PA ou PG): ").strip().upper()

        if tipo_progressao == 'PA':
            razao = float(input("Digite a razão da PA: "))
            matriz1 = Matriz.criar_matriz(tamanho, valor_inicial, 'PA', razao)
        elif tipo_progressao == 'PG':
            razao = float(input("Digite a razão da PG: "))
            matriz1 = Matriz.criar_matriz(tamanho, valor_inicial, 'PG', razao)
        else:
            print("Tipo de progressão inválido.")
            exit()

        print("Matriz criada:")
        self.imprimir_matriz(matriz1)

        tamanho = input("Digite o tamanho da segunda matriz (ex: 2x2): ")
        valor_inicial = float(input("Digite o valor inicial da segunda matriz: "))
        tipo_progressao = input("Digite o tipo de progressão (PA ou PG): ").strip().upper()

        if tipo_progressao == 'PA':
            razao = float(input("Digite a razão da PA: "))
            matriz2 = Matriz.criar_matriz(tamanho, valor_inicial, 'PA', razao)
        elif tipo_progressao == 'PG':
            razao = float(input("Digite a razão da PG: "))
            matriz2 = Matriz.criar_matriz(tamanho, valor_inicial, 'PG', razao)
        else:
            print("Tipo de progressão inválido.")
            exit()

        print("Segunda matriz criada:")
        self.imprimir_matriz(matriz2)

        match opcao:
            case "0":
                return
            # Realize a operação selecionada
            case "1":
                resultado = matriz1.adicionar(matriz2)
            case "2":
                resultado = matriz1.multiplicar(matriz2)
            case "3":
                resultado = matriz1.transpor()
            # ... (adicione outras operações) ...
        
    def matrizes_resultado(self):
        # Exiba o resultado
        print("\nResultado:")
        resultado.mostrarMatriz()
        
    def imprimir_matriz(self, matriz):
      for linha in matriz.matriz:
        print(f"[{', '.join(map(str, linha))}],")
        
class Matriz:
    def __init__(self, nLinhas, nColunas):
        self.nLinhas = nLinhas
        self.nColunas = nColunas
        self.matriz = [[0 for _ in range(nColunas)] for _ in range(nLinhas)]
        
    def addValores(self):
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                self.matriz[l][c] = float(input(f"Insira o valor para a Matriz em Linha: {l} e Coluna: {c}: "))
    
    def mostrarMatriz(self):
        saida = ""
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                numero = self.matriz[l][c]
                saida += f"{numero}\t"
            saida += "\n"
        print(f"\nSaida da Matriz {self.nLinhas}x{self.nColunas}:")
        print(saida)

    def transpor(self):
        transposta = Matriz(self.nColunas, self.nLinhas)
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                transposta.matriz[c][l] = self.matriz[l][c]
        return transposta

    def adicionar(self, outra):
        if self.nLinhas != outra.nLinhas or self.nColunas != outra.nColunas:
            raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")
        resultado = Matriz(self.nLinhas, self.nColunas)
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                resultado.matriz[l][c] = self.matriz[l][c] + outra.matriz[l][c]
        return resultado

    def multiplicar(self, outra):
        if self.nColunas != outra.nLinhas:
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        resultado = Matriz(self.nLinhas, outra.nColunas)
        for i in range(self.nLinhas):
            for j in range(outra.nColunas):
                resultado.matriz[i][j] = sum(self.matriz[i][k] * outra.matriz[k][j] for k in range(self.nColunas))
        return resultado

    def igual(self, outra):
        if self.nLinhas != outra.nLinhas or self.nColunas != outra.nColunas:
            return False
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                if self.matriz[l][c] != outra.matriz[l][c]:
                    return False
        return True

    @staticmethod
    def criar_matriz(tamanho, valor_inicial, progressao, razao=1):
        linhas, colunas = map(int, tamanho.split('x'))
        matriz = Matriz(linhas, colunas)
        valor_atual = valor_inicial
        
        if progressao == 'PA':
            for i in range(linhas):
                for j in range(colunas):
                    matriz.matriz[i][j] = valor_atual
                    valor_atual += razao

        elif progressao == 'PG':
            for i in range(linhas):
                for j in range(colunas):
                    matriz.matriz[i][j] = valor_atual
                    valor_atual *= razao

        return matriz

# --- VERIFICAÇÕES NUMÉRICAS ---
class Verificacoes:
    def verificar_numero(self):
        """Menu de opções para verificar propriedades de um número: paridade, primo, palíndromo, Fibonacci."""
        print("\n|==============================|")
        print("|       Verificar Número       |")
        print("|1. Positivo, negativo, zero   |")
        print("|2. Primo                      |")
        print("|3. Par, ímpar                 |")
        print("|4. Palíndromo                 |")
        print("|5. Fibonacci                  |")
        print("|6. Perfeito                   |")
        print("|7. Amigável                   |")
        print("|8. Calculo de MDC e MMC       |")
        print("|0. Voltar                     |")
        print("|==============================|")
        opcao = input("Escolha uma opção: ")
        try:
            if opcao in ["1", "2", "3", "4", "5", "6"]:
                num = int(input("Digite o número: "))
                match opcao:
                    case "1": print(f"{num} é positivo." if num > 0 else f"{num} é negativo." if num < 0 else "Zero.")
                    case "2": print(f"{num} é primo." if self.eh_primo(num) else f"{num} não é primo.")
                    case "3": print(f"{num} é par." if num % 2 == 0 else f"{num} é ímpar.")
                    case "4": print(f"{num} é palíndromo." if str(num) == str(num)[::-1] else f"{num} não é palíndromo.")
                    case "5": print(f"{num} pertence à sequência de Fibonacci." if self.eh_fibonacci(num) else f"{num} não pertence.")
                    case "6": print(f"{num} é um número perfeito. " if self.eh_perfeito(num) else f"{num} não é perfeito")
            else:
                match opcao:
                    case "7":
                        a=int(input("Insira um número: "))
                        b=int(input("Insira um número: "))
                        print(f"{a} e {b} são números amigáveis." if self.eh_amigavel(a, b) else f"{a} e {b} não são amigáveis.")
                    case "8": self.calcular_mdc_mmc()
                    case _: print("Opção inválida.")
        except ValueError:
            print("Erro: Entrada inválida.")

    def eh_primo(self, num):
        """Verifica se um número é primo."""
        if num <= 1:
            return False
        for i in range(2, int(self.raiz_quadrada(num)) + 1):
            if num % i == 0:
                return False
        return True

    def eh_fibonacci(self, num):
        """Verifica se um número pertence à sequência de Fibonacci."""
        def eh_quadrado_perfeito(x):
            s = int(self.raiz_quadrada(x))
            return s * s == x
        return eh_quadrado_perfeito(5 * num * num + 4) or eh_quadrado_perfeito(5 * num * num - 4)
        
    def eh_perfeito(self, n):
        soma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return soma_divisores == n
        
    def eh_amigavel(self, a, b):
        soma_a = sum(i for i in range(1, a) if a % i == 0)
        soma_b = sum(i for i in range(1, b) if b % i == 0)
        return soma_a == b and soma_b == a

    def calcular_mdc_mmc(self):
        """Permite o cálculo de MDC e MMC de uma lista de números fornecida pelo usuário."""
        try:
            print("\n|============================|")
            print("|    Cálculo de MDC e MMC    |")
            print("|============================|")
            numeros = list(map(int, input("Digite os números separados por espaço: ").split()))
            
            if len(numeros) < 2:
                print("Erro: Insira pelo menos dois números.")
                return
            
            mdc = self.calcular_mdc_lista(numeros)
            mmc = self.calcular_mmc_lista(numeros)
            
            print(f"MDC dos números {numeros}: {mdc}")
            print(f"MMC dos números {numeros}: {mmc}")
        except ValueError:
            print("Erro: Certifique-se de digitar apenas números inteiros separados por espaço.")

    def calcular_mdc_lista(self, numeros):
        """Calcula o MDC de uma lista de números."""
        def mdc(a, b):
            while b:
                a, b = b, a % b
            return a

        resultado = numeros[0]
        for num in numeros[1:]:
            resultado = mdc(resultado, num)
        return resultado

    def calcular_mmc_lista(self, numeros):
        """Calcula o MMC de uma lista de números."""
        def mdc(a, b):
            while b:
                a, b = b, a % b
            return a

        def mmc(a, b):
            return abs(a * b) // mdc(a, b)

        resultado = numeros[0]
        for num in numeros[1:]:
            resultado = mmc(resultado, num)
        return resultado

# --- ANÁLISE DE TEXTO ---
class AnaliseTexto:
    def analise_texto(self):
        """Contagem de palavras e caracteres no texto, e frequência de palavras e caracteres."""
        texto = input("Digite o texto para análise: ")
        palavras = texto.split()

        contador_palavras = Counter(palavras)
        contador_caracteres = Counter(texto)
        print(f"Número total de palavras: {len(palavras)}")
        print("Frequência de palavras:", dict(contador_palavras))
        print("Frequência de caracteres:", dict(contador_caracteres))
        
# --- TABUADA ---
class Tabuada:
    def tabuada(self):
        """Mostra a tabuada de multiplicação para um número dado, com intervalo definido pelo usuário."""
        try:
            num = int(input("Digite o número para ver sua tabuada: "))
            inicio = int(input("Digite o início do intervalo: "))
            fim = int(input("Digite o fim do intervalo: "))
            for i in range(inicio, fim + 1):
                print(f"{num} x {i} = {num * i}")
        except ValueError:
            print("Erro: Entrada inválida.")

# --- CONVERSORES ---
class Conversor:
    def __init__(self):
        self.unidades = {
            "comprimento": {
                "1": ("Quilômetros", 1000),
                "2": ("Metros", 1),
                "3": ("Centímetros", 0.01),
                "4": ("Milhas", 1609.34),
                "5": ("Pés", 0.3048),
                "6": ("Polegadas", 0.0254),
            },
            "área": {
                "1": ("Metro Quadrado", 1),
                "2": ("Hectare", 10000),
                "3": ("Acre", 4046.86),
                "4": ("Kilômetro Quadrado", 1000000),
                "5": ("Centímetro Quadrado", 0.0001),
                "6": ("Milha Quadrada", 2589988.11),
            },
            "volume": {
                "1": ("Metro Cúbico", 1),
                "2": ("Litro", 0.001),
                "3": ("Mililitro", 0.000001),
                "4": ("Centímetro Cúbico", 0.000001),
                "5": ("Kilômetro Cúbico", 1000000000),
                "6": ("Hectômetro Cúbico", 1000000),
            },
            "tempo": {
                "1": ("Segundos", 1),
                "2": ("Minutos", 60),
                "3": ("Horas", 3600),
                "4": ("Dias", 86400),
                "5": ("Anos", 31557600),
            },
            "velocidade": {
                "1": ("m/s", 1),
                "2": ("km/h", 3.6),
            },
            "moeda": {
                "USD": 1.0,
                "BRL": 5.25,
                "EUR": 0.85,
            },
            "temperatura": {
                "1": {
                    "nome": "Celsius",
                    "simbolo": "C",
                    "conversao": {
                        "F": lambda c: c * 9 / 5 + 32,  # Para Fahrenheit
                        "K": lambda c: c + 273.15,     # Para Kelvin
                        "R": lambda c: (c + 273.15) * 9 / 5,  # Para Rankine
                    },
                },
                "2": {
                    "nome": "Fahrenheit",
                    "simbolo": "F",
                    "conversao": {
                        "C": lambda f: (f - 32) * 5 / 9,           # Para Celsius
                        "K": lambda f: (f - 32) * 5 / 9 + 273.15,  # Para Kelvin
                        "R": lambda f: f + 459.67,                 # Para Rankine
                    },
                },
                "3": {
                    "nome": "Kelvin",
                    "simbolo": "K",
                    "conversao": {
                        "C": lambda k: k - 273.15,                 # Para Celsius
                        "F": lambda k: (k - 273.15) * 9 / 5 + 32,  # Para Fahrenheit
                        "R": lambda k: k * 9 / 5,                  # Para Rankine
                    },
                },
                "4": {
                    "nome": "Rankine",
                    "simbolo": "R",
                    "conversao": {
                        "C": lambda r: (r - 491.67) * 5 / 9,       # Para Celsius
                        "F": lambda r: r - 459.67,                 # Para Fahrenheit
                        "K": lambda r: r * 5 / 9,                  # Para Kelvin
                    },
                },
            },
            "pressao": {
                "1": ("Pascal", 1),
                "2": ("Bar", 100000),
                "3": ("Atmosfera", 101325),
                "4": ("Milímetro de Mercúrio", 133.322),
                "5": ("Torr", 133.322),
                "6": ("PSI", 6894.76),
                "7": ("Kilopascal", 1000),
            },
            "massa": {
                "1": ("Quilograma", 1),
                "2": ("Grama", 0.001),
                "3": ("Miligrama", 0.000001),
                "4": ("Libra", 0.453592),
                "5": ("Onça", 0.0283495),
                "6": ("Tonelada", 1000),
            },
            "energia": {
                "1": ("Joule", 1),
                "2": ("Kilojoule", 1000),
                "3": ("Caloria", 4.184),
                "4": ("Kilocaloria", 4184),
                "5": ("Watt-hora", 3600),
                "6": ("Kilowatt-hora", 3600000),
                "7": ("BTU", 1055.06),
                "8": ("Erg", 1e-7),
            },
            "dados": {
                "1": ("Byte", 1),
                "2": ("Kilobyte", 1024),
                "3": ("Megabyte", 1024**2),
                "4": ("Gigabyte", 1024**3),
                "5": ("Terabyte", 1024**4),
                "6": ("Bit", 1/8),
                "7": ("Kilobit", 1024 / 8),
                "8": ("Megabit", (1024**2) / 8),
                "9": ("Gigabit", (1024**3) / 8),
                "10": ("Terabit", (1024**4) / 8),
            },
            "forca": {
                "1": ("Newton", 1),
                "2": ("Libra-força", 4.44822),
                "3": ("Dina", 1e-5),
            },
            "angulo": {
                "1": ("Grau", 1),
                "2": ("Minuto de Arco", 1/60),
                "3": ("Segundo de Arco", 1/3600),
                "4": ("Radianos", 57.2958),
            },
            "densidade": {
                "1": ("Quilograma por metro cúbico", 1),
                "2": ("Grama por centímetro cúbico", 1000),
                "3": ("Libra por pé cúbico", 16.0185),
            },
            "frequencia": {
                "1": ("Hertz", 1),
                "2": ("Kilohertz", 1000),
                "3": ("Megahertz", 1_000_000),
                "4": ("Gigahertz", 1_000_000_000),
            },
            "iluminancia": {
                "1": ("Lux", 1),
                "2": ("Foot-candle", 10.764),
            },
            "luminancia": {
                "1": ("Candela por metro quadrado", 1),
                "2": ("Foot-lambert", 3.426),
                "3": ("Nit", 1),
            },
            "potencia": {
                "1": ("Watt", 1),
                "2": ("Cavalo-vapor", 745.7),
                "3": ("BTU/h", 0.293071),
            },
            "eletricidade": {
                "1": ("Ampere", 1),
                "2": ("Volt", 1),
                "3": ("Ohm", 1),
                "4": ("Farad", 1),
                "5": ("Coulomb", 1),
                "6": ("Watt-hora", 3600),
                "7": ("Quilowatt-hora", 3600000),
            },
            "radioatividade": {
                "1": ("Becquerel", 1),
                "2": ("Curie", 3.7e10),
                "3": ("Gray", 1),
                "4": ("Sievert", 1),
            },
            "velocidade_angular": {
                "1": ("Radianos por segundo", 1),
                "2": ("RPM", 2 * 3.14159 / 60),
            },
            "fluxo_massa": {
                "1": ("Quilograma por segundo", 1),
                "2": ("Libra por segundo", 0.453592),
            },
        }

    def menu_principal(self):
        while True:
            print("|============================|")
            print("|         Conversores        |")
            print("|1. Conversão de Unidades    |")
            print("|2. Conversão de Moeda       |")
            print("|0. Sair                     |")
            print("|============================|")
            opcao = input("Escolha uma opção: ")
            match opcao:
                case "1": self.conversores_unidades()
                case "2": self.conversao_moeda()
                case "0": break
                case _: print("Opção inválida. Tente novamente.")

    def conversores_unidades(self):
        while True:
            print("|============================|")
            print("|         Conversores        |")
            print("|1. Comprimento              |")
            print("|2. Área                     |")
            print("|3. Volume                   |")
            print("|4. Tempo                    |")
            print("|5. Velocidade               |")
            print("|6. Temperatura              |")
            print("|7. Pressão                  |")
            print("|8. Massa                    |")
            print("|9. Energia                  |")
            print("|10. Dados                   |")
            print("|11. Força                   |")
            print("|12. Ângulo                  |")
            print("|13. Densidade               |")
            print("|14. Frequência              |")
            print("|15. Iluminância             |")
            print("|16. Luminância              |")
            print("|17. Potência                |")
            print("|18. Eletricidade            |")
            print("|19. Radioatividade          |")
            print("|20. Velocidade Angular      |")
            print("|21. Fluxo de Massa          |")
            print("|0. Voltar                   |")
            print("|============================|")
            opcao = input("Escolha uma opção: ")
            match opcao:
                case "1": self.converter("comprimento")
                case "2": self.converter("área")
                case "3": self.converter("volume")
                case "4": self.converter("tempo")
                case "5": self.converter("velocidade")
                case "6": self.converter_temperatura()
                case "7": self.converter("pressao")
                case "8": self.converter("massa")
                case "9": self.converter("energia")
                case "10": self.converter("dados")
                case "11": self.converter("forca")
                case "12": self.converter("angulo")
                case "13": self.converter("densidade")
                case "14": self.converter("frequencia")
                case "15": self.converter("iluminancia")
                case "16": self.converter("luminancia")
                case "17": self.converter("potencia")
                case "18": self.converter("eletricidade")
                case "19": self.converter("radioatividade")
                case "20": self.converter("velocidade_angular")
                case "21": self.converter("fluxo_massa")
                case "0": break
                case _: print("Opção inválida. Tente novamente.")

    def converter(self, tipo):
        unidades = self.unidades[tipo]
        print(f"|============================|")
        print(f"| Escolha uma unidade de {tipo} |")
        for key, (nome, _) in self.unidades.items():
            print(f"|{key}. {nome:<24}|")
        print("|0. Sair                     |")
        print("|============================|")
        
        unidade_origem = input("Escolha a unidade de origem: ")
        if unidade_origem==0:
            self.conversores_unidades()
        elif unidade_origem not in unidades:
            print("Unidade inválida.")
            return

        valor = float(input(f"Digite o valor em {unidades[unidade_origem][0]}: "))
        
        # Converte para a unidade base e calcula para todas as unidades
        valor_em_base = valor * unidades[unidade_origem][1]
        print(f"\nConversão de {valor} {unidades[unidade_origem][0]} para todas as unidades disponíveis:")
        for key, (nome, fator) in unidades.items():
            valor_convertido = valor_em_base / fator
            print(f"{valor_convertido} {nome}")
            
    def converter_temperatura(self):
        unidades = self.unidades["temperatura"]
        print(f"|============================|")
        print(f"| Escolha uma unidade de temperatura |")
        for key, unidade in unidades.items():
            print(f"|{key}. {unidade['nome']:<24}|")
        print("|0. Sair                     |")
        print("|============================|")
        
        unidade_origem = input("Escolha a unidade de origem: ")
        if unidade_origem == "0":
            print("Saindo...")
            return
        elif unidade_origem not in unidades:
            print("Unidade inválida.")
            return

        valor = float(input(f"Digite o valor em {unidades[unidade_origem]['nome']}: "))
        
        print(f"\nConversão de {valor} {unidades[unidade_origem]['simbolo']} para todas as unidades disponíveis:")
        for key, unidade_destino in unidades.items():
            if key == unidade_origem:
                continue  # Pula a unidade de origem
            # Realiza a conversão utilizando a função correspondente
            conversao_func = unidades[unidade_origem]["conversao"][unidade_destino["simbolo"]]
            valor_convertido = conversao_func(valor)
            print(f"{valor_convertido:.2f} {unidade_destino['nome']} ({unidade_destino['simbolo']})")


    def conversao_moeda(self):
        valor = float(input("Digite o valor em moeda: "))
        origem = input("Moeda de origem (USD, BRL, EUR): ")
        destino = input("Moeda de destino (USD, BRL, EUR): ")
        if origem in self.unidades["moeda"] and destino in self.unidades["moeda"]:
            valor_convertido = valor * (self.unidades["moeda"][destino] / self.unidades["moeda"][origem])
            print(f"Resultado: {valor} {origem} = {valor_convertido:.2f} {destino}")
        else:
            print("Erro: Moeda inválida.")

# --- JOGOS MATEMÁTICOS ---
class JogosMatematicos:
    def quiz_matematico(self):
        print("Escolha a dificuldade: ")
        dificuldade = input("1. Fácil (1-10)\n2. Médio (1-50)\n3. Difícil (1-100): ")
        intervalo = {"1": 10, "2": 50, "3": 100}.get(dificuldade, 10)
        operacao = input("Escolha a operação (soma, subtracao, multiplicacao, divisao): ").lower()
        pontos = 0

        for _ in range(5):
            num1 = random.randint(1, intervalo)
            num2 = random.randint(1, intervalo)
            if operacao == "soma":
                resposta_correta = num1 + num2
                simbolo = "+"
            elif operacao == "subtracao":
                resposta_correta = num1 - num2
                simbolo = "-"
            elif operacao == "multiplicacao":
                resposta_correta = num1 * num2
                simbolo = "*"
            elif operacao == "divisao" and num2 != 0:
                resposta_correta = num1 // num2
                simbolo = "/"
            else:
                print("Operação inválida.")
                return

            resposta_usuario = int(input(f"Quanto é {num1} {simbolo} {num2}? "))
            if resposta_usuario == resposta_correta:
                print("Correto!")
                pontos += 1
            else:
                print(f"Incorreto. A resposta correta é {resposta_correta}.")
        print(f"Pontuação final: {pontos}/5")

    def sudoku_basico(self):
        tabuleiro = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

    while True:
        print_tabuleiro()
        try:
            x = int(input("Linha (0-8) ou -1 para sair: "))
            if x == -1:
                break
            y = int(input("Coluna (0-8): "))
            valor = int(input("Valor (1-9): "))

            if eh_valido(x, y, valor):
                tabuleiro[x][y] = valor
                print("Valor inserido!")
            else:
                print("Movimento inválido!")
        except (ValueError, IndexError):
            print("Entrada inválida! Tente novamente.")
            
    def print_tabuleiro(self):
        for linha in tabuleiro:
            print(" ".join(str(x) if x != 0 else "." for x in linha))
        print()  # Linha em branco para separação

    def eh_valido(self, x, y, valor):
        # Verifica linha e coluna
        for i in range(9):
            if tabuleiro[x][i] == valor or tabuleiro[i][y] == valor:
                return False
        
        # Verifica o quadrante 3x3
        quad_x = (x // 3) * 3
        quad_y = (y // 3) * 3
        for i in range(quad_x, quad_x + 3):
            for j in range(quad_y, quad_y + 3):
                if tabuleiro[i][j] == valor:
                    return False
        
        return True

    def jogos_matematicos(self):
        print("\n|============================|")
        print("|    Jogos Matemáticos       |")
        print("|1. Quiz                     |")
        print("|2. Sudoku                   |")
        print("|0. Voltar                   |")
        print("|============================|")
        opcao = input("Escolha uma função: ")
        match opcao:
            case "1": self.quiz_matematico()
            case "2": self.sudoku_basico()
            case _: print("Opção inválida.")

app = UtilitariosMatematicos()
app.menu_principal()

