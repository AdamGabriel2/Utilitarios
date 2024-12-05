from Menu import Menu
from Base import Base

class UttsMaths:
    def __init__(self):
        menu_opcoes=["Calculadora Completa","Tabuada","Funções Matemáticas","Calculo de Estatística","Resolver Equações","Operações com Vetores","Operações com Matrizes","Geometria","Teorema","Número Complexo"]
        while True:
            menu = Menu("Utilitários Matemáticos", menu_opcoes)
            menu.desenhar()
            escolha = input("Escolha uma opção: ")
            match escolha:
                case "0": return
                case "1": CalculadoraCompleta()
                case "2": Tabuada()
                case "3": FuncoesMatematicas()
                case "4": Estatisticas()
                case "5": Equacoes()
                case "6": OperacoesVetores()
                case "7": OperacoesMatrizes()
                case "8": Geometria()
                case "9": Teoremas()
                case "10": NumeroComplexo()
                case "11": Fracao()
                case _: print("Opção inválida. Por favor, escolha novamente.")
              
class CalculadoraCompleta(Base):
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
                case "12": self.ver_historico()
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

# --- TABUADA ---
class Tabuada:
    def __init__(self):
        """Mostra a tabuada de multiplicação para um número dado, com intervalo definido pelo usuário."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Tabuada"]
        menu = Menu("Funções Matemáticas", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            match func:
                case "1":
                    try:
                        num = int(input("Digite o número para ver sua tabuada: "))
                        inicio = int(input("Digite o início do intervalo: "))
                        fim = int(input("Digite o fim do intervalo: "))
                        for i in range(inicio, fim + 1):
                            resultado = num * i
                            print(f"{num} x {i} = {resultado}")
                            self.adicionar_historico(num, i, resultado)
                    except ValueError:
                        print("Erro: Entrada inválida.")
                case "2": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, num, i, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{num} x {i} = {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

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
                case "6": self.ver_historico()
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
        
class Estatisticas:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Calcular Média", "Calcular Mediana", "Calcular Moda", "Calcular Desvio Padrão"]
        menu = Menu("Estatísticas", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            if func == "0":
                return
            numeros = input("Digite os números separados por vírgula: ")
            lista_numeros = [float(num.strip()) for num in numeros.split(",")]
            match func:
                case "1":
                    resultado = self.calcular_media(lista_numeros)
                    print(f"Média: {resultado}")
                    self.adicionar_historico("Média", lista_numeros, resultado)
                case "2":
                    resultado = self.calcular_mediana(lista_numeros)
                    print(f"Mediana: {resultado}")
                    self.adicionar_historico("Mediana", lista_numeros, resultado)
                case "3":
                    resultado = self.calcular_moda(lista_numeros)
                    print(f"Moda: {resultado}")
                    self.adicionar_historico("Moda", lista_numeros, resultado)
                case "4":
                    resultado = self.calcular_desvio_padrao(lista_numeros)
                    print(f"Desvio Padrão: {resultado}")
                    self.adicionar_historico("Desvio Padrão", lista_numeros, resultado)
                case "5": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, funcao, numeros, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{funcao} de {numeros} = {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

    def calcular_media(self, lista):
        """Calcula a média de uma lista de números."""
        return sum(lista) / len(lista) if lista else 0

    def calcular_mediana(self, lista):
        """Calcula a mediana de uma lista de números."""
        lista.sort()
        n = len(lista)
        meio = n // 2
        if n % 2 == 0:
            return (lista[meio - 1] + lista[meio]) / 2
        else:
            return lista[meio]

    def calcular_moda(self, lista):
        """Calcula a moda de uma lista de números."""
        from collections import Counter
        contagem = Counter(lista)
        max_freq = max(contagem.values())
        modas = [num for num, freq in contagem.items() if freq == max_freq]
        return modas

    def calcular_desvio_padrao(self, lista):
        """Calcula o desvio padrão de uma lista de números."""
        media = self.calcular_media(lista)
        variancia = sum((x - media) ** 2 for x in lista) / len(lista)
        return variancia ** 0.5

class Equacoes(Base):
    def __init__(self):
        """Resolve equações de primeiro e segundo grau."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Primero Grau", "Segundo Grau"]
        menu = Menu("Equações", menu_opcoes)
        while True:
            menu.desenhar()
            grau = input("Escolha uma opção: ")
            try:
                if opcao == "1":
                    a = float(input("Coeficiente a: "))
                    b = float(input("Coeficiente b: "))
                    solucao = -b / a
                    print(f"Solução da equação linear: x = {solucao}")
                    self.adicionar_historico("Equação de 1º grau", a, b, solucao)
                elif opcao == "2":
                    a = float(input("Coeficiente a: "))
                    b = float(input("Coeficiente b: "))
                    c = float(input("Coeficiente c: "))
                    discriminante = b**2 - (4 * a * c)
                    if discriminante >= 0:
                        raiz1 = (-b + self.raiz_quadrada(discriminante)) / (2 * a)
                        raiz2 = (-b - self.raiz_quadrada(discriminante)) / (2 * a)
                        print(f"As raízes são x1 = {raiz1} e x2 = {raiz2}")
                        self.adicionar_historico("Equação de 2º grau", a, b, c, raiz1, raiz2)
                    else:
                        print("Sem solução real.")
                elif opcao == "3": self.ver_historico()
            except ValueError:
                print("Erro: Entrada inválida.")

    def adicionar_historico(self, tipo_equacao, *coeficientes):
        """Adiciona a solução ao histórico."""
        if len(coeficientes) == 3:  # Primeiro grau
            self.historico.append(f"{tipo_equacao}: a={coeficientes[0]}, b={coeficientes[1]} => x={coeficientes[2]}")
        elif len(coeficientes) == 5:  # Segundo grau
            self.historico.append(f"{tipo_equacao}: a={coeficientes[0]}, b={coeficientes[1]}, c={coeficientes[2]} => x1={coeficientes[3]}, x2={coeficientes[4]}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)
            
class OperacoesVetores:
    def __init__(self):
        """Realiza operações com vetores."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Adição", "Subtração", "Produto Escalar", "Produto Vetorial"]
        menu = Menu("Operações com Vetores", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação: ")

            tamanho = int(input("Digite o tamanho dos vetores: "))
            print("Preencha os valores do primeiro vetor:")
            vetor1 = Vetor.criar_vetor(tamanho)

            print("Preencha os valores do segundo vetor:")
            vetor2 = Vetor.criar_vetor(tamanho if opcao in ["1", "2", "3"] else 3)  # Produto vetorial exige vetores 3D
            match opcao:
                case "1":
                    self.resultado = vetor1.adicionar(vetor2)
                    self.adicionar_historico("Adição", vetor1, vetor2, self.resultado)
                case "2":
                    self.resultado = vetor1.subtrair(vetor2)
                    self.adicionar_historico("Subtração", vetor1, vetor2, self.resultado)
                case "3":
                    escalar = vetor1.produto_escalar(vetor2)
                    print(f"Resultado do Produto Escalar: {escalar}")
                    self.adicionar_historico("Produto Escalar", vetor1, vetor2, escalar)
                    continue
                case "4":
                    self.resultado = vetor1.produto_vetorial(vetor2)
                    self.adicionar_historico("Produto Vetorial", vetor1, vetor2, self.resultado)
                case "5": self.ver_historico()
                case _:
                print("Opção inválida.")
                continue

            self.vetor_resultado()

    def adicionar_historico(self, operacao, vetor1, vetor2, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{operacao}: {vetor1.componentes} e {vetor2.componentes} => {resultado.componentes}")

    def vetor_resultado(self):
        """Exibe o resultado das operações."""
        print("\nResultado:")
        self.resultado.mostrar_vetor()

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)


class Vetor:
    def __init__(self, componentes):
        self.componentes = componentes

    def mostrar_vetor(self):
        print(f"Vetor: {self.componentes}")

    def adicionar(self, outro):
        if len(self.componentes) != len(outro.componentes):
            raise ValueError("Os vetores devem ter o mesmo tamanho para serem somados.")
        resultado = [a + b for a, b in zip(self.componentes, outro.componentes)]
        return Vetor(resultado)

    def subtrair(self, outro):
        if len(self.componentes) != len(outro.componentes):
            raise ValueError("Os vetores devem ter o mesmo tamanho para serem subtraídos.")
        resultado = [a - b for a, b in zip(self.componentes, outro.componentes)]
        return Vetor(resultado)

    def produto_escalar(self, outro):
        if len(self.componentes) != len(outro.componentes):
            raise ValueError("Os vetores devem ter o mesmo tamanho para o produto escalar.")
        return sum(a * b for a, b in zip(self.componentes, outro.componentes))

    def produto_vetorial(self, outro):
        if len(self.componentes) != 3 or len(outro.componentes) != 3:
            raise ValueError("O produto vetorial só é definido para vetores 3D.")
        x1, y1, z1 = self.componentes
        x2, y2, z2 = outro.componentes
        resultado = [
            y1 * z2 - z1 * y2,
            z1 * x2 - x1 * z2,
            x1 * y2 - y1 * x2,
        ]
        return Vetor(resultado)

    @staticmethod
    def criar_vetor(tamanho):
        componentes = []
        for i in range(tamanho):
            valor = float(input(f"Insira o valor do componente {i + 1}: "))
            componentes.append(valor)
        return Vetor(componentes)


class OperacoesMatrizes:
    def __init__(self):
        """Realiza operações com matrizes."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Adição", "Multiplicação", "Transposição"]
        menu = Menu("Operações com Matrizes", menu_opcoes)
        while True:
            menu.desenhar()
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
                continue

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
                continue

            print("Segunda matriz criada:")
            self.imprimir_matriz(matriz2)

            match opcao:
                case "0":
                    return
                case "1":
                    self.resultado = matriz1.adicionar(matriz2)
                    self.adicionar_historico("Adição", matriz1, matriz2, self.resultado)
                case "2":
                    self.resultado = matriz1.multiplicar(matriz2)
                    self.adicionar_historico("Multiplicação", matriz1, matriz2, self.resultado)
                case "3":
                    self.resultado = matriz1.transpor()
                    self.adicionar_historico("Transposição", matriz1, None, self.resultado)
                case "4": self.ver_historico()

            self.matrizes_resultado()

    def adicionar_historico(self, operacao, matriz1, matriz2, resultado):
        """Adiciona a operação ao histórico."""
        if matriz2 is not None:
            self.historico.append(f"{operacao}: {matriz1.matriz} e {matriz2.matriz} => {resultado.matriz}")
        else:
            self.historico.append(f"{operacao}: {matriz1.matriz} => {resultado.matriz}")

    def matrizes_resultado(self):
        """Exibe o resultado das operações."""
        print("\nResultado:")
        self.resultado.mostrarMatriz()

    def imprimir_matriz(self, matriz):
        for linha in matriz.matriz:
            print(f"[{', '.join(map(str, linha))}],")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)


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
        
class Geometria:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = [
            "Calcular Área do Círculo",
            "Calcular Área do Retângulo",
            "Calcular Perímetro do Triângulo",
            "Calcular Volume do Cubo"
        ]
        menu = Menu("Geometria", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            match func:
                case "0":
                    return
                case "1": 
                    raio = float(input("Digite o raio do círculo: "))
                    area = self.calcular_area_circulo(raio)
                    print(f"Área do Círculo: {area}")
                    self.adicionar_historico("Área do Círculo", {"raio": raio}, area)
                case "2": 
                    largura = float(input("Digite a largura do retângulo: "))
                    altura = float(input("Digite a altura do retângulo: "))
                    area = self.calcular_area_retangulo(largura, altura)
                    print(f"Área do Retângulo: {area}")
                    self.adicionar_historico("Área do Retângulo", {"largura": largura, "altura": altura}, area)
                case "3":
                    a = float(input("Digite o comprimento do lado A: "))
                    b = float(input("Digite o comprimento do lado B: "))
                    c = float(input("Digite o comprimento do lado C: "))
                    perimetro = self.calcular_perimetro_triangulo(a, b, c)
                    print(f"Perímetro do Triângulo: {perimetro}")
                    self.adicionar_historico("Perímetro do Triângulo", {"a": a, "b": b, "c": c}, perimetro)
                case "4": 
                    lado = float(input("Digite o comprimento do lado do cubo: "))
                    volume = self.calcular_volume_cubo(lado)
                    print(f"Volume do Cubo: {volume}")
                    self.adicionar_historico("Volume do Cubo", {"lado": lado}, volume)
                case "5": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, operacao, parametros, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{operacao}: {parametros} => {resultado}")

    def calcular_area_circulo(self, raio):
        """Calcula a área de um círculo dado o raio."""
        return 3.14 * raio ** 2

    def calcular_area_retangulo(self, largura, altura):
        """Calcula a área de um retângulo dado a largura e a altura."""
        return largura * altura

    def calcular_perimetro_triangulo(self, a, b, c):
        """Calcula o perímetro de um triângulo dado os comprimentos dos lados."""
        return a + b + c

    def calcular_volume_cubo(self, lado):
        """Calcula o volume de um cubo dado o comprimento do lado."""
        return lado ** 3

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)


class Teoremas:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = [
            "Teorema de Pitágoras",
            "Teorema de Tales"
        ]
        menu = Menu("Teoremas", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha um teorema: ")
            match func:
                case "0":
                    return
                case "1":
                    a = float(input("Digite o comprimento do lado A: "))
                    b = float(input("Digite o comprimento do lado B: "))
                    hipotenusa = self.teorema_pitagoras(a, b)
                    print(f"Comprimento da hipotenusa: {hipotenusa}")
                    self.adicionar_historico("Teorema de Pitágoras", {"a": a, "b": b}, hipotenusa)
                case "2":
                    # Exemplo simples do Teorema de Tales
                    a = float(input("Digite o comprimento do segmento A: "))
                    b = float(input("Digite o comprimento do segmento B: "))
                    c = float(input("Digite o comprimento do segmento C: "))
                    proporcao = self.teorema_tales(a, b, c)
                    print(f"Proporção: {proporcao}")
                    self.adicionar_historico("Teorema de Tales", {"a": a, "b": b, "c": c}, proporcao)
                case "3": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, teorema, parametros, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{teorema}: {parametros} => {resultado}")

    def teorema_pitagoras(self, a, b):
        """Calcula a hipotenusa de um triângulo retângulo."""
        return (a**2 + b**2) ** 0.5

    def teorema_tales(self, a, b, c):
        """Calcula a proporção do Teorema de Tales."""
        return (a / b) * c

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)


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
                case "6": self.ver_historico()
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
                case "5": self.ver_historico()
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

