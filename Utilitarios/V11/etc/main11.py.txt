import inspect

class Base:
    @staticmethod
    def dec_bin(numero):
        if isinstance(numero, float):
            parte_inteira = int(abs(numero))
            parte_decimal = abs(numero) - parte_inteira
            bin_inteira = bin(parte_inteira)[2:]
            bin_decimal = []
            while parte_decimal > 0 and len(bin_decimal) < 20:  # Limite para precisão
                parte_decimal *= 2
                bit = int(parte_decimal)
                bin_decimal.append(str(bit))
                parte_decimal -= bit
            resultado = f"{'-' if numero < 0 else ''}{bin_inteira}.{''.join(bin_decimal)}"
        else:
            resultado = bin(int(numero) & 0xFFFFFFFF)[2:] if numero < 0 else bin(int(numero))[2:]
        return resultado

    @staticmethod
    def dec_oct(numero):
        if isinstance(numero, float):
            parte_inteira = int(abs(numero))
            parte_decimal = abs(numero) - parte_inteira
            oct_inteira = oct(parte_inteira)[2:]
            oct_decimal = []
            while parte_decimal > 0 and len(oct_decimal) < 20:  # Limite para precisão
                parte_decimal *= 8
                bit = int(parte_decimal)
                oct_decimal.append(str(bit))
                parte_decimal -= bit
            resultado = f"{'-' if numero < 0 else ''}{oct_inteira}.{''.join(oct_decimal)}"
        else:
            resultado = oct(int(numero) & 0xFFFFFFFF)[2:] if numero < 0 else oct(int(numero))[2:]
        return resultado

    @staticmethod
    def dec_hex(numero):
        if isinstance(numero, float):
            import struct
            hexadecimal = struct.pack('>f', numero).hex()  # IEEE 754
            resultado = f"0x{hexadecimal}"
        else:
            resultado = hex(int(numero) & 0xFFFFFFFF)[2:] if numero < 0 else hex(int(numero))[2:]
        return resultado

    @staticmethod
    def bin_dec(binario):
        """Converte um número binário para decimal."""
        return int(binario, 2)

    @staticmethod
    def oct_dec(octal):
        """Converte um número octal para decimal."""
        return int(octal, 8)

    @staticmethod
    def hex_decl(hexadecimal):
        """Converte um número hexadecimal para decimal."""
        return int(hexadecimal, 16)

    @staticmethod
    def dec_para_qualquer_base(numero, base):
        """Converte um número decimal para qualquer base (2 a 36)."""
        if not (2 <= base <= 36):
            raise ValueError("Base deve estar entre 2 e 36")
        caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        while numero > 0:
            resultado = caracteres[numero % base] + resultado
            numero //= base
        return resultado or "0"

    @staticmethod
    def qualquer_base_para_dec(numero, base):
        """Converte um número de qualquer base (2 a 36) para decimal."""
        if not (2 <= base <= 36):
            raise ValueError("Base deve estar entre 2 e 36")
        return int(numero, base)

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

    def saida(self, num):
        print(f"Sistemas: Decimal: {num}, Octal: {self.dec_oct(num)}, Hexadecimal: {self.dec_hex(num)}, Binário {self.dec_bin(num)}")

    def __def__():
        nome_funcao = inspect.currentframe().f_code.co_name
        print("O nome desta função é:", nome_funcao)

class Menu:
    def __init__(self, titulo: str, opcoes: list[str]):
        self.titulo = titulo
        self.opcoes = opcoes
        self.largura = 50  # Define a largura máxima do menu

    def desenhar(self):
        # Linha superior
        print(f"|{'=' * (self.largura - 2)}|")
        
        # Título centralizado
        print(f"|{self.titulo.center(self.largura - 2)}|")
        
        # Opções formatadas
        i=1
        for idx, opcao in enumerate(self.opcoes, start=1):
            linha = f"{idx}. {opcao}"  # Exemplo: "1. Comprimento"
            print(f"|{linha.ljust(self.largura - 2)}|")
            i+=1
        # Linha para a opção "Voltar"
        print(f"|{i}{'. Ver Histórico'.ljust(self.largura - 3)}|")
        print(f"|{'0. Voltar'.ljust(self.largura - 2)}|")
        
        # Linha inferior
        print(f"|{'=' * (self.largura - 2)}|")

import json
from datetime import datetime

historico = []

def registrar_acao(classe, funcao, entrada, saida):
    """
    Registra a ação do usuário no histórico.

    Args:
        classe: Nome da classe.
        funcao: Nome da função.
        entrada: Entrada do usuário.
        saida: Saída do programa.
    """
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    acao = {
    "classe": classe,
        "funcao": funcao,
        "entrada": entrada,
        "saida": saida,
        "horario": agora
    }
    historico.append(acao)
    
def salvar_historico(nome_arquivo="historico.json"):
    """
    Salva o histórico em um arquivo JSON.

    Args:
        nome_arquivo: Nome do arquivo JSON.
    """
    with open(nome_arquivo, "w") as arquivo:
        json.dump(historico, arquivo, indent=2)


class Utilitarios:
    def __init__(self):
        menu_opcoes = ["Utilitários Matemáticos","Verificadores de Números","Utilitários de Texto","Conversores de Unidades","Finanças","Jogos","Algoritmos"]
        while True:
            menu = Menu("Menu Principal", menu_opcoes)
            menu.desenhar()
            escolha = input("Escolha uma opção: ")
            match escolha:
                case "0": 
                    print("Fim do Programa.")
                    break
                case "1": UttsMaths()
                case "2": VerifNums()
                case "3": UttsTexto()
                case "4": ConvUni()
                case "5": Financas()
                case "6": Jogos()
                case "7": Algoritmos()
                case _: print("Opção inválida. Por favor, escolha novamente.")

class UttsMaths:
    def __init__(self):
        menu_opcoes=["Calculadora Completa","Tabuada","Funções Matemáticas","Calculo de Estatística e Probabilidades","Resolver Equações","Operações com Vetores","Operações com Matrizes","Geometria","Teorema","Número Complexo"]
        while True:
            menu = Menu("Utilitários Matemáticos", menu_opcoes)
            menu.desenhar()
            escolha = input("Escolha uma opção: ")
            match escolha:
                case "0": return
                case "1": CalculadoraCompleta()
                case "2": Tabuada()
                case "3": FuncoesMatematicas()
                case "4": EstatisticasProbabilidades
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
        
class EstatisticasProbabilidades(CalculadoraCompleta):
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Calcular Média","Calcular Mediana","Calcular Moda","Calcular Desvio Padrão","Probabilidade Simples","Probabilidade Composta","Distribuição Normal (aproximada)","Distribuição Binomial","Distribuição de Poisson","Ver Histórico"]
        menu = Menu("Estatísticas e Probabilidades", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            if func == "0":
                return
            match func:
                case "1":
                    numeros = input("Digite os números separados por vírgula: ")
                    lista_numeros = [float(num.strip()) for num in numeros.split(",")]
                    resultado = self.calcular_media(lista_numeros)
                    print(f"Média: {resultado}")
                    self.adicionar_historico("Média", lista_numeros, resultado)
                case "2":
                    numeros = input("Digite os números separados por vírgula: ")
                    lista_numeros = [float(num.strip()) for num in numeros.split(",")]
                    resultado = self.calcular_mediana(lista_numeros)
                    print(f"Mediana: {resultado}")
                    self.adicionar_historico("Mediana", lista_numeros, resultado)
                case "3":
                    numeros = input("Digite os números separados por vírgula: ")
                    lista_numeros = [float(num.strip()) for num in numeros.split(",")]
                    resultado = self.calcular_moda(lista_numeros)
                    print(f"Moda: {resultado}")
                    self.adicionar_historico("Moda", lista_numeros, resultado)
                case "4":
                    numeros = input("Digite os números separados por vírgula: ")
                    lista_numeros = [float(num.strip()) for num in numeros.split(",")]
                    resultado = self.calcular_desvio_padrao(lista_numeros)
                    print(f"Desvio Padrão: {resultado}")
                    self.adicionar_historico("Desvio Padrão", lista_numeros, resultado)
                case "5":
                    eventos = int(input("Digite o número de eventos: "))
                    total = int(input("Digite o total de eventos possíveis: "))
                    resultado = self.probabilidade_simples(eventos, total)
                    print(f"Probabilidade Simples: {resultado}")
                    self.adicionar_historico("Probabilidade Simples", {"eventos": eventos, "total": total}, resultado)
                case "6":
                    probabilidades = input("Digite as probabilidades separadas por vírgula: ")
                    lista_probabilidades = [float(p.strip()) for p in probabilidades.split(",")]
                    resultado = self.probabilidade_composta(lista_probabilidades)
                    print(f"Probabilidade Composta: {resultado}")
                    self.adicionar_historico("Probabilidade Composta", lista_probabilidades, resultado)
                case "7":
                    media = float(input("Digite a média: "))
                    desvio_padrao = float(input("Digite o desvio padrão: "))
                    x = float(input("Digite o valor de x: "))
                    resultado = self.distribuicao_normal(x, media, desvio_padrao)
                    print(f"Distribuição Normal: {resultado}")
                    self.adicionar_historico("Distribuição Normal", {"x": x, "media": media, "desvio_padrao": desvio_padrao}, resultado)
                case "8":
                    n = int(input("Digite o número de tentativas (n): "))
                    k = int(input("Digite o número de sucessos (k): "))
                    p = float(input("Digite a probabilidade de sucesso (p): "))
                    resultado = self.distribuicao_binomial(n, k, p)
                    print(f"Distribuição Binomial: {resultado}")
                    self.adicionar_historico("Distribuição Binomial", {"n": n, "k": k, "p": p}, resultado)
                case "9":
                    k = int(input("Digite o número de ocorrências (k): "))
                    lambda_ = float(input("Digite o parâmetro lambda: "))
                    resultado = self.distribuicao_poisson(k, lambda_)
                    print(f"Distribuição de Poisson: {resultado}")
                    self.adicionar_historico("Distribuição de Poisson", {"k": k, "lambda": lambda_}, resultado)
                case "10": self.ver_historico()
                case _: print("Opção inválida.")

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
        contagem = {}
        for num in lista:
            contagem[num] = contagem.get(num, 0) + 1
        max_freq = max(contagem.values())
        modas = [num for num, freq in contagem.items() if freq == max_freq]
        return modas

    def calcular_desvio_padrao(self, lista):
        """Calcula o desvio padrão de uma lista de números."""
        media = self.calcular_media(lista)
        variancia = sum((x - media) ** 2 for x in lista) / len(lista)
        return variancia ** 0.5

    def probabilidade_simples(self, eventos, total):
        """Calcula a probabilidade simples de um evento."""
        return eventos / total if total > 0 else 0

    def probabilidade_composta(self, probabilidades):
        """Calcula a probabilidade composta de eventos independentes."""
        resultado = 1
        for p in probabilidades:
            resultado *= p
        return resultado

    def distribuicao_normal(self, x, media, desvio_padrao):
        """Calcula a distribuição normal (aproximada) para um valor x."""
        # Aproximação da função densidade da normal
        constante = 1 / (desvio_padrao * (2 * 3.14) ** 0.5)
        exp_part = -0.5 * ((x - media) / desvio_padrao) ** 2
        return constante * (2.718 ** exp_part)

    def distribuicao_binomial(self, n, k, p):
        """Calcula a distribuição binomial."""
        combinacao = self.combinacao(n, k)
        return combinacao * (p ** k) * ((1 - p) ** (n - k))

    def distribuicao_poisson(self, k, lambda_):
        """Calcula a distribuição de Poisson."""
        return (lambda_ ** k * (2.718 ** -lambda_)) / self.fatorial(k)

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
        menu_opcoes = ["Calcular Área do Círculo","Calcular Área do Retângulo","Calcular Perímetro do Triângulo","Calcular Volume do Cubo","Calcular Área do Trapézio","Calcular Área do Losango","Calcular Volume do Cilindro","Calcular Volume da Esfera","Transladar Ponto","Rotacionar Ponto","Refletir Ponto"]
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
                case "5":
                    base_maior = float(input("Digite a base maior do trapézio: "))
                    base_menor = float(input("Digite a base menor do trapézio: "))
                    altura = float(input("Digite a altura do trapézio: "))
                    area = self.area_trapezio(base_maior, base_menor, altura)
                    print(f"Área do Trapézio: {area}")
                    self.adicionar_historico("Área do Trapézio", {"base_maior": base_maior, "base_menor": base_menor, "altura": altura}, area)
                case "6":
                    diagonal_maior = float(input("Digite a diagonal maior do losango: "))
                    diagonal_menor = float(input("Digite a diagonal menor do losango: "))
                    area = self.area_losango(diagonal_maior, diagonal_menor)
                    print(f"Área do Losango: {area}")
                    self.adicionar_historico("Área do Losango", {"diagonal_maior": diagonal_maior, "diagonal_menor": diagonal_menor}, area)
                case "7":
                    raio = float(input("Digite o raio do cilindro: "))
                    altura = float(input("Digite a altura do cilindro: "))
                    volume = self.volume_cilindro(raio, altura)
                    print(f"Volume do Cilindro: {volume}")
                    self.adicionar_historico("Volume do Cilindro", {"raio": raio, "altura": altura}, volume)
                case "8":
                    raio = float(input("Digite o raio da esfera: "))
                    volume = self.volume_esfera(raio)
                    print(f"Volume da Esfera: {volume}")
                    self.adicionar_historico("Volume da Esfera", {"raio": raio}, volume)
                case "9":
                    ponto = (float(input("Digite a coordenada x do ponto: ")), float(input("Digite a coordenada y do ponto: ")))
                    dx = float(input("Digite o deslocamento em x: "))
                    dy = float(input("Digite o deslocamento em y: "))
                    ponto_transladado = self.transladar(ponto, dx, dy)
                    print(f"Ponto Transladado: {ponto_transladado}")
                    self.adicionar_historico("Translação de Ponto", {"ponto": ponto, "dx": dx, "dy": dy}, ponto_transladado)
                case "10":
                    ponto = (float(input("Digite a coordenada x do ponto: ")), float(input("Digite a coordenada y do ponto: ")))
                    angulo = float(input("Digite o ângulo de rotação (em graus): "))
                    ponto_rotacionado = self.rotacionar(ponto, angulo)
                    print(f"Ponto Rotacionado: {ponto_rotacionado}")
                    self.adicionar_historico("Rotação de Ponto", {"ponto": ponto, "angulo": angulo}, ponto_rotacionado)
                case "11":
                    ponto = (float(input("Digite a coordenada x do ponto: ")), float(input("Digite a coordenada y do ponto: ")))
                    eixo = input("Digite o eixo de reflexão (x ou y): ")
                    ponto_refletido = self.refletir(ponto, eixo)
                    print(f"Ponto Refletido: {ponto_refletido}")
                    self.adicionar_historico("Reflexão de Ponto", {"ponto": ponto, "eixo": eixo}, ponto_refletido)
                case "12": self.ver_historico()
                case _: print("Opção inválida.")

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

    def area_trapezio(self, base_maior, base_menor, altura):
        """Calcula a área de um trapézio."""
        return (base_maior + base_menor) * altura / 2

    def area_losango(self, diagonal_maior, diagonal_menor):
        """Calcula a área de um losango."""
        return (diagonal_maior * diagonal_menor) / 2

    def volume_cilindro(self, raio, altura):
        """Calcula o volume de um cilindro."""
        return 3.14 * raio ** 2 * altura

    def volume_esfera(self, raio):
        """Calcula o volume de uma esfera."""
        return (4/3) * 3.14 * raio ** 3

    def transladar(self, ponto, dx, dy):
        """Translada um ponto dado um deslocamento em x e y."""
        return (ponto[0] + dx, ponto[1] + dy)

    def rotacionar(self, ponto, angulo):
        """Rotaciona um ponto em torno da origem."""
        rad = angulo * (3.14 / 180)  # Converte graus para radianos
        x_novo = ponto[0] * self.cos(rad) - ponto[1] * self.sin(rad)
        y_novo = ponto[0] * self.sin(rad) + ponto[1] * self.cos(rad)
        return (x_novo, y_novo)

    def refletir(self, ponto, eixo):
        """Reflete um ponto em torno de um eixo."""
        if eixo == 'x':
            return (ponto[0], -ponto[1])
        elif eixo == 'y':
            return (-ponto[0], ponto[1])
        return ponto

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

    def sin(self, rad):
        """Cálculo do seno sem usar a biblioteca math."""
        return rad - (rad**3)/6 + (rad**5)/120  # Aproximação de Taylor

    def cos(self, rad):
        """Cálculo do cosseno sem usar a biblioteca math."""
        return 1 - (rad**2)/2 + (rad**4)/24  # Aproximação de Taylor


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

class UttsTexto:
    def __init__(self):
        menu_opcoes=["Analise de Texto"]
        menu = Menu("Utilitários de Texto", menu_opcoes)
        menu.desenhar()
        escolha = input("Escolha uma opção: ")
        match escolha:
            case "0": return
            case "1": AnaliseTexto()
            case _: print("Opção inválida. Por favor, escolha novamente.")

# --- ANÁLISE DE TEXTO ---
class AnaliseTexto:
    def __init__(self):
        """Contagem de palavras e caracteres no texto, e frequência de palavras e caracteres."""
        texto = input("Digite o texto para análise: ")
        palavras = texto.split()

        contador_palavras = Counter(palavras)
        contador_caracteres = Counter(texto)
        print(f"Número total de palavras: {len(palavras)}")
        print("Frequência de palavras:", dict(contador_palavras))
        print("Frequência de caracteres:", dict(contador_caracteres))

class VerifNums(Base):
    def __init__(self):
        """Menu de opções para verificar propriedades de um número: paridade, primo, palíndromo, Fibonacci, etc."""
        self.historico = []  # Inicializa o histórico
        menu_opcoes = [
            "Positivo, Negativo, Zero", "Primo", "Par, Ímpar", "Palíndromo", 
            "Fibonacci", "Perfeito", "Amigável", "Cálculo de MDC e MMC", 
            "Listar Fibonacci até N", "Listar Números Perfeitos até N", 
            "Contar Dígitos de um Número", "Listar Números Primos até N", 
            "Mágico", "Triangular", "Catalan", "Quadrado Perfeito", 
            "Cubo Perfeito", "Número Abundante/Deficiente", "Número de Harshad",
            "Mostrar Histórico"  # Opção para mostrar o histórico
        ]
        menu = Menu("Verificar Número", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma opção: ")
            try:
                if opcao == "0": return
                elif opcao in ["1", "2", "3", "4", "5", "6", "11", "13", "14", "15", "16", "17", "18", "19"]:
                    num = int(input("Digite o número: "))
                    resultado = ""
                    match opcao:
                        case "1": resultado = f"{num} é positivo." if num > 0 else f"{num} é negativo." if num < 0 else "Zero."
                        case "2": resultado = f"{num} é primo." if self.eh_primo(num) else f"{num} não é primo."
                        case "3": resultado = f"{num} é par." if num % 2 == 0 else f"{num} é ímpar."
                        case "4": resultado = f"{num} é palíndromo." if str(num) == str(num)[::-1] else f"{num} não é palíndromo."
                        case "5": resultado = f"{num} pertence à sequência de Fibonacci." if self.eh_fibonacci(num) else f"{num} não pertence."
                        case "6": resultado = f"{num} é um número perfeito." if self.eh_perfeito(num) else f"{num} não é perfeito."
                        case "11": resultado = f"Número de dígitos no número '{num}': {self.contar_digitos(num)}"
                        case "13": resultado = f"{num} é um número mágico" if self.eh_numero_magico(num) else f"{num} não é mágico"
                        case "14": resultado = f"{num} é um número triangular" if self.eh_numero_triangulo(num) else f"{num} não é triangular"
                        case "15": resultado = f"{num} é um número de Catalan" if self.eh_numero_catalan(num) else f"{num} não é um número de Catalan."
                        case "16": resultado = f"{num} é um quadrado perfeito." if self.eh_quadrado_perfeito(num) else f"{num} não é um quadrado perfeito."
                        case "17": resultado = f"{num} é um cubo perfeito." if self.eh_cubo_perfeito(num) else f"{num} não é um cubo perfeito."
                        case "18": resultado = f"{num} é um número {self.classificar_numero(num)}."
                        case "19": resultado = f"{num} é um número de Harshad." if self.eh_harshad(num) else f"{num} não é um número de Harshad."
                    
                    # Armazenar resultado no histórico
                    self.historico.append(f"{resultado} (Número: {num})")
                    print(resultado)

                elif opcao in ["9", "10", "12"]:
                    match opcao:
                        case "9": self.listar_fibonacci()
                        case "10": self.listar_numeros_perfeitos()
                        case "12": self.listar_primos_intervalo()
                else:
                    match opcao:
                        case "7":
                            a = int(input("Insira um número: "))
                            b = int(input("Insira um número: "))
                            resultado = f"{a} e {b} são números amigáveis." if self.eh_amigavel(a, b) else f"{a} e {b} não são amigáveis."
                            self.historico.append(resultado)
                            print(resultado)
                        case "8": self.calcular_mdc_mmc()
                        case "20": self.mostrar_historico()  # Adiciona opção para mostrar histórico
                        case _: print("Opção inválida.")
            except ValueError as e:
                print("Erro: Entrada inválida. Por favor, insira números inteiros.")

    def mostrar_historico(self):
        """Mostra o histórico das operações realizadas."""
        print("\nHistórico de Operações:")
        for entrada in self.historico:
            print(f"- {entrada}")
        print()  # Linha em branco para melhor separação

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
        """Verifica se um número é perfeito."""
        soma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return soma_divisores == n
        
    def eh_amigavel(self, a, b):
        """Verifica se dois números são amigáveis."""
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
            
            resultado = f"MDC dos números {numeros}: {mdc}\nMMC dos números {numeros}: {mmc}"
            self.historico.append(resultado)  # Armazenar no histórico
            print(resultado)
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
        
    def contar_digitos(self, num):
        """Conta o número de dígitos em um número."""
        return len(str(abs(num)))

    def listar_fibonacci(self):
        """Lista os números de Fibonacci até um número N fornecido pelo usuário."""
        n = int(input("Até qual número deseja listar os Fibonacci? "))
        fib = [0, 1]
        while fib[-1] + fib[-2] <= n:
            fib.append(fib[-1] + fib[-2])
        print(f"Números de Fibonacci até {n}: {fib}")
        self.historico.append(f"Fibonacci até {n}: {fib}")  # Armazenar no histórico

    def listar_numeros_perfeitos(self):
        """Lista os números perfeitos até um número N fornecido pelo usuário."""
        n = int(input("Até qual número deseja listar os números perfeitos? "))
        perfeitos = []
        for i in range(1, n + 1):
            if self.eh_perfeito(i):
                perfeitos.append(i)
        print(f"Números perfeitos até {n}: {perfeitos}")
        self.historico.append(f"Números perfeitos até {n}: {perfeitos}")  # Armazenar no histórico

    def listar_primos_intervalo(self):
        """Lista os números primos em um intervalo fornecido pelo usuário."""
        inicio = int(input("Digite o início do intervalo: "))
        fim = int(input("Digite o fim do intervalo: "))
        primos = [num for num in range(inicio, fim + 1) if self.eh_primo(num)]
        print(f"Números primos entre {inicio} e {fim}: {primos}")
        self.historico.append(f"Números primos entre {inicio} e {fim}: {primos}")  # Armazenar no histórico

    def eh_numero_magico(self, num):
        """Verifica se um número é mágico."""
        while num >= 10:
            num = sum(int(d) for d in str(num))
        return num == 1

    def eh_numero_triangulo(self, num):
        """Verifica se um número é triangular."""
        n = int(((-1 + (1 + 8 * num) ** 0.5) / 2))
        return n * (n + 1) // 2 == num

    def eh_numero_catalan(self, num):
        """Verifica se um número é um número de Catalan."""
        n = 0
        catalan = 1
        while catalan < num:
            n += 1
            catalan = (2 * (2 * n + 1) * catalan) // (n + 2)
        return catalan == num

    def eh_quadrado_perfeito(self, num):
        """Verifica se um número é um quadrado perfeito."""
        raiz = int(num ** 0.5)
        return raiz * raiz == num

    def eh_cubo_perfeito(self, num):
        """Verifica se um número é um cubo perfeito."""
        raiz = int(num ** (1/3))
        return raiz * raiz * raiz == num

    def classificar_numero(self, n):
        """Classifica um número como perfeito, abundante ou deficiente."""
        soma_divisores = sum(i for i in range(1, n) if n % i == 0)
        if soma_divisores == n:
            return "Perfeito"
        elif soma_divisores > n:
            return "Abundante"
        else:
            return "Deficiente"

    def eh_harshad(self, num):
        """Verifica se um número é um número de Harshad."""
        soma_digitos = sum(int(d) for d in str(num))
        return num % soma_digitos == 0

# --- CONVERSORES ---
class ConvUni(Base):
    def __init__(self):
        self.historico = []  # Para armazenar o histórico de conversões
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
                "7": ("Micrograma", 1e-6),  # Adicionando microgramas
                "8": ("Tonelada métrica", 1000),  # Adicionando toneladas métricas
            },
            "energia": {
                "1": ("Joule", 1),
                "2": ("Kilojoule", 1000),
                "3": ("Caloria", 4.184),
                "4": ("Kilocaloria", 4184),
                "5": ("Watt-hora", 3600),
                "6": ("Joules por segundo (Watts)", 1),  # Adicionando Watts
                "7": ("Calorias por segundo", 4.184),  # Adicionando calorias por segundo
                "8": ("Kilowatt-hora", 3600000),
                "9": ("BTU", 1055.06),
                "10": ("Erg", 1e-7),
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
        
        menu_opcoes = ["Conversão de Unidades", "Conversão de Moeda", "Adicionar Unidade Personalizada", "Mostrar Histórico"]
        menu = Menu("Conversores", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma opção: ")
            match opcao:
                case "1": self.conversores_unidades()
                case "2": self.conversao_moeda()
                case "3": self.adicionar_unidade_personalizada()
                case "4": self.mostrar_historico()
                case "0": break
                case _: print("Opção inválida. Tente novamente.")

    def adicionar_unidade_personalizada(self):
        tipo = input("Digite o tipo da unidade (ex: massa, energia): ")
        nome = input("Digite o nome da nova unidade: ")
        fator = float(self.obter_input_float("Digite o fator de conversão para a unidade base: "))
        
        if tipo in self.unidades:
            novo_id = str(len(self.unidades[tipo]) + 1)
            self.unidades[tipo][novo_id] = (nome, fator)
            print("Unidade adicionada com sucesso!")
        else:
            print("Tipo de unidade inválido.")

    def obter_input_float(self, mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                
    def mostrar_historico(self):
        print("Histórico de Conversões:")
        for entrada in self.historico:
            valor, unidade, conversoes = entrada
            print(f"{valor} {unidade} convertido para:")
            for conv in conversoes:
                print(f"  - {conv[0]} {conv[1]}")

    def conversores_unidades(self):
        while True:
            menu_opcoes=["Comprimento","Área","Volume","Tempo","Velocidade","Temperatura","Pressão","Massa",
                         "Energia","Dados","Força","Ângulo","Densidade","Frequência","Iluminância","Luminância",
                         "Potência","Eletricidade","Radioatividade","Velocidade Angular","Fluxo de Massa",]
            menu = Menu("Conversores", menu_opcoes)
            menu.desenhar()
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
        for key, (nome, _) in unidades.items():
            print(f"|{key}. {nome:<24}|")
        print("|0. Sair                     |")
        print("|============================|")
        
        unidade_origem = input("Escolha a unidade de origem: ")
        if unidade_origem == "0":
            self.conversores_unidades()
            return
        elif unidade_origem not in unidades:
            print("Unidade inválida.")
            return

        valor = self.obter_input_float(f"Digite o valor em {unidades[unidade_origem][0]}: ")
        
        # Converte para a unidade base e calcula para todas as unidades
        valor_em_base = valor * unidades[unidade_origem][1]
        self.historico.append((valor, unidades[unidade_origem][0], []))  # Adiciona ao histórico

        print(f"\nConversão de {valor} {unidades[unidade_origem][0]} para todas as unidades disponíveis:")
        for key, (nome, fator) in unidades.items():
            valor_convertido = valor_em_base / fator
            self.historico[-1][2].append((valor_convertido, nome))  # Armazena a conversão
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
            return
        elif unidade_origem not in unidades:
            print("Unidade inválida.")
            return

        valor = self.obter_input_float(f"Digite o valor em {unidades[unidade_origem]['nome']}: ")
        
        print(f"\nConversão de {valor} {unidades[unidade_origem]['simbolo']} para todas as unidades disponíveis:")
        for key, unidade_destino in unidades.items():
            if key == unidade_origem:
                continue  # Pula a unidade de origem
            # Realiza a conversão utilizando a função correspondente
            conversao_func = unidades[unidade_origem]["conversao"][unidade_destino["simbolo"]]
            valor_convertido = conversao_func(valor)
            print(f"{valor_convertido:.2f} {unidade_destino['nome']} ({unidade_destino['simbolo']})")

    def conversao_moeda(self):
        valor = self.obter_input_float("Digite o valor em moeda: ")
        origem = input("Moeda de origem (USD, BRL, EUR): ")
        destino = input("Moeda de destino (USD, BRL, EUR): ")
        if origem in self.unidades["moeda"] and destino in self.unidades["moeda"]:
            valor_convertido = valor * (self.unidades["moeda"][destino] / self.unidades["moeda"][origem])
            print(f"Resultado: {valor} {origem} = {valor_convertido:.2f} {destino}")
        else:
            print("Erro: Moeda inválida.")
            
class Financas:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Calculadora Financeira", "Simulador Financeiro"]
        menu = Menu("Finanças", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma opção: ")
            match opcao:
                case "0": return
                case "1": CalculadoraFinanceira(self.historico)
                case "2": SimuladorFinanceiro(self.historico)
                case _: print("Opção inválida. Tente novamente.")

class CalculadoraFinanceira:
    def __init__(self, historico):
        self.historico = historico
        menu_opcoes = ["Calcular ROI", "Calcular Margem de Lucro"]
        menu = Menu("Calculadora Financeira", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            match func:
                case "1":
                    investimento = float(input("Digite o investimento inicial: "))
                    retorno = float(input("Digite o retorno total: "))
                    resultado = self.calcular_roi(investimento, retorno)
                    print(f"ROI: {resultado}%")
                    self.adicionar_historico("Calcular ROI", resultado)
                case "2":
                    receita = float(input("Digite a receita total: "))
                    custo = float(input("Digite o custo total: "))
                    resultado = self.calcular_margem_lucro(receita, custo)
                    print(f"Margem de Lucro: {resultado}%")
                    self.adicionar_historico("Calcular Margem de Lucro", resultado)
                case "3":
                    self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def calcular_roi(self, investimento, retorno):
        """Calcula o Retorno sobre Investimento (ROI)."""
        return ((retorno - investimento) / investimento) * 100

    def calcular_margem_lucro(self, receita, custo):
        """Calcula a margem de lucro."""
        return ((receita - custo) / receita) * 100 if receita else 0

    def adicionar_historico(self, operacao, resultado):
        """Adiciona uma entrada ao histórico."""
        self.historico.append(f"{operacao}: {resultado}%")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

class SimuladorFinanceiro:
    def __init__(self, historico):
        self.historico = historico
        menu_opcoes = ["Calcular Juros Compostos", "Calcular Investimento Futuro", "Calcular Valor Presente"]
        menu = Menu("Simulador Financeiro", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            match func:
                case "1":
                    capital = float(input("Digite o capital inicial: "))
                    taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                    tempo = float(input("Digite o tempo (em anos): "))
                    resultado = self.calcular_juros_compostos(capital, taxa, tempo)
                    print(f"Juros Compostos: {resultado}")
                    self.adicionar_historico("Calcular Juros Compostos", resultado)
                case "2":
                    capital = float(input("Digite o capital inicial: "))
                    taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                    tempo = float(input("Digite o tempo (em anos): "))
                    resultado = self.calcular_investimento_futuro(capital, taxa, tempo)
                    print(f"Investimento Futuro: {resultado}")
                    self.adicionar_historico("Calcular Investimento Futuro", resultado)
                case "3":
                    montante = float(input("Digite o montante: "))
                    taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                    tempo = float(input("Digite o tempo (em anos): "))
                    resultado = self.calcular_valor_presente(montante, taxa, tempo)
                    print(f"Valor Presente: {resultado}")
                    self.adicionar_historico("Calcular Valor Presente", resultado)
                case "4":
                    self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def calcular_juros_compostos(self, capital, taxa, tempo):
        """Calcula o montante total com juros compostos."""
        return capital * (1 + taxa) ** tempo

    def calcular_investimento_futuro(self, capital, taxa, tempo):
        """Calcula o valor futuro do investimento."""
        return self.calcular_juros_compostos(capital, taxa, tempo)

    def calcular_valor_presente(self, montante, taxa, tempo):
        """Calcula o valor presente dado um montante futuro."""
        return montante / ((1 + taxa) ** tempo)

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

# --- JOGOS ---
class Jogos:
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
        self.tabuleiro = [
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
            self.print_tabuleiro()
            try:
                x = int(input("Linha (0-8) ou -1 para sair: "))
                if x == -1:
                    break
                y = int(input("Coluna (0-8): "))
                valor = int(input("Valor (1-9): "))

                if self.eh_valido(x, y, valor):
                    self.tabuleiro[x][y] = valor
                    print("Valor inserido!")
                else:
                    print("Movimento inválido!")
            except (ValueError, IndexError):
                print("Entrada inválida! Tente novamente.")
            
    def print_tabuleiro(self):
        for linha in self.tabuleiro:
            print(" ".join(str(x) if x != 0 else "." for x in linha))
        print()  # Linha em branco para separação

    def eh_valido(self, x, y, valor):
        # Verifica linha e coluna
        for i in range(9):
            if self.tabuleiro[x][i] == valor or self.tabuleiro[i][y] == valor:
                return False
        
        # Verifica o quadrante 3x3
        quad_x = (x // 3) * 3
        quad_y = (y // 3) * 3
        for i in range(quad_x, quad_x + 3):
            for j in range(quad_y, quad_y + 3):
                if self.tabuleiro[i][j] == valor:
                    return False
        
        return True

    def __init__(self):
        menu_opcoes=["Quiz","Sudoku",]
        menu = Menu("Jogos", menu_opcoes)
        menu.desenhar()
        opcao = input("Escolha uma função: ")
        match opcao:
            case "1": self.quiz_matematico()
            case "2": self.sudoku_basico()
            case _: print("Opção inválida.")

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"

    def menu_jogo_da_velha(self):
        print("\n|=============================|")
        print("|1. Iniciar Jogo              |")
        print("|0. Voltar                    |")
        print("|=============================|")
        func = input("Escolha uma opção: ")

        if func == "1":
            self.iniciar_jogo()
        elif func == "0":
            return
        else:
            print("Opção inválida.")

    def iniciar_jogo(self):
        for _ in range(9):
            self.imprimir_tabuleiro()
            linha = int(input(f"Jogador {self.jogador_atual}, escolha a linha (0-2): "))
            coluna = int(input(f"Jogador {self.jogador_atual}, escolha a coluna (0-2): "))
            if self.fazer_jogada(linha, coluna):
                if self.verificar_vencedor():
                    self.imprimir_tabuleiro()
                    print(f"Jogador {self.jogador_atual} venceu!")
                    return
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
        self.imprimir_tabuleiro()
        print("Empate!")

    def fazer_jogada(self, linha, coluna):
        """Faz a jogada do jogador atual."""
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            return True
        else:
            print("Casa já ocupada! Tente novamente.")
            return False

    def verificar_vencedor(self):
        """Verifica se houve um vencedor."""
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != " ":
                return True
        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != " ":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return True
        return False

    def imprimir_tabuleiro(self):
        """Imprime o tabuleiro do jogo da velha."""
        for linha in self.tabuleiro:
            print(" | ".join(linha))
            print("-" * 9)

class SudokuSolver:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def menu_sudoku(self):
        print("\n|============================|")
        print("|1. Resolver Sudoku           |")
        print("|0. Voltar                   |")
        print("|=============================|")
        func = input("Escolha uma opção: ")

        if func == "1":
            if self.resolver():
                print("Sudoku resolvido:")
                self.imprimir_tabuleiro()
            else:
                print("Não foi possível resolver o Sudoku.")
        elif func == "0":
            return
        else:
            print("Opção inválida.")

    def resolver(self):
        """Resolve o Sudoku usando backtracking."""
        for i in range(9):
            for j in range(9):
                if self.tabuleiro[i][j] == 0:  # Encontrar uma célula vazia
                    for num in range(1, 10):
                        if self.eh_valido(i, j, num):
                            self.tabuleiro[i][j] = num
                            if self.resolver():
                                return True
                            self.tabuleiro[i][j] = 0  # Backtrack
                    return False
        return True

    def eh_valido(self, linha, coluna, num):
        """Verifica se um número pode ser colocado na célula."""
        for x in range(9):
            if self.tabuleiro[linha][x] == num or self.tabuleiro[x][coluna] == num:
                return False
        # Verificar a subgrade 3x3
        start_row, start_col = 3 * (linha // 3), 3 * (coluna // 3)
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[start_row + i][start_col + j] == num:
                    return False
        return True

    def imprimir_tabuleiro(self):
        """Imprime o tabuleiro de Sudoku."""
        for linha in self.tabuleiro:
            print(" ".join(str(num) for num in linha))

class Algoritmos:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Bubble Sort", "Quick Sort", "Merge Sort", "Busca Linear", "Busca Binária"]
        menu = Menu("Algoritmos", menu_opcoes)

        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação: ")
            match opcao:
                case "0": return
                case "1":
                    lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
                    resultado = self.bubble_sort(lista)
                    print(f"Lista Ordenada com Bubble Sort: {resultado}")
                    self.adicionar_historico("Bubble Sort", resultado)
                case "2":
                    lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
                    resultado = self.quick_sort(lista)
                    print(f"Lista Ordenada com Quick Sort: {resultado}")
                    self.adicionar_historico("Quick Sort", resultado)
                case "3":
                    lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
                    resultado = self.merge_sort(lista)
                    print(f"Lista Ordenada com Merge Sort: {resultado}")
                    self.adicionar_historico("Merge Sort", resultado)
                case "4":
                    lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
                    alvo = float(input("Digite o número a ser buscado: "))
                    resultado = self.busca_linear(lista, alvo)
                    print(f"Resultado da Busca Linear: {'Encontrado na posição ' + str(resultado) if resultado != -1 else 'Não encontrado'}")
                    self.adicionar_historico("Busca Linear", f"Alvo: {alvo}, Resultado: {resultado}")
                case "5":
                    lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
                    alvo = float(input("Digite o número a ser buscado: "))
                    resultado = self.busca_binaria(lista, alvo)
                    print(f"Resultado da Busca Binária: {'Encontrado na posição ' + str(resultado) if resultado != -1 else 'Não encontrado'}")
                    self.adicionar_historico("Busca Binária", f"Alvo: {alvo}, Resultado: {resultado}")
                case "6":
                    self.ver_historico()
                case _:
                    print("Opção inválida, tente novamente.")

    def _obter_lista(self, mensagem):
        """Obtém uma lista de números a partir da entrada do usuário."""
        entrada = input(mensagem)
        return [float(num) for num in entrada.split(",")]

    @staticmethod
    def bubble_sort(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    @staticmethod
    def quick_sort(lista):
        if len(lista) <= 1:
            return lista
        else:
            pivo = lista[len(lista) // 2]
            esquerda = [x for x in lista if x < pivo]
            meio = [x for x in lista if x == pivo]
            direita = [x for x in lista if x > pivo]
            return Algoritmos.quick_sort(esquerda) + meio + Algoritmos.quick_sort(direita)

    @staticmethod
    def merge_sort(lista):
        if len(lista) > 1:
            meio = len(lista) // 2
            esquerda = lista[:meio]
            direita = lista[meio:]

            Algoritmos.merge_sort(esquerda)
            Algoritmos.merge_sort(direita)

            i = j = k = 0
            while i < len(esquerda) and j < len(direita):
                if esquerda[i] < direita[j]:
                    lista[k] = esquerda[i]
                    i += 1
                else:
                    lista[k] = direita[j]
                    j += 1
                k += 1

            while i < len(esquerda):
                lista[k] = esquerda[i]
                i += 1
                k += 1

            while j < len(direita):
                lista[k] = direita[j]
                j += 1
                k += 1

        return lista

    @staticmethod
    def busca_linear(lista, alvo):
        for i, valor in enumerate(lista):
            if valor == alvo:
                return i
        return -1

    @staticmethod
    def busca_binaria(lista, alvo):
        lista.sort()  # Certifique-se de que a lista esteja ordenada
        baixo, alto = 0, len(lista) - 1
        while baixo <= alto:
            meio = (baixo + alto) // 2
            if lista[meio] < alvo:
                baixo = meio + 1
            elif lista[meio] > alvo:
                alto = meio - 1
            else:
                return meio
        return -1

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
                
app=Utilitarios()