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
                    c2=Outros()
                    c2.tabuada()
                case "3":
                    c3=Verificacoes()
                    c3.verificar_numero()
                case "4":
                    c4=Outros()
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
        """Executa funções avançadas: logaritmo, exponencial, seno, cosseno, tangente, fatorial, combinação e permutação."""
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

# --- VERIFICAÇÕES NUMÉRICAS ---
class Verificacoes:
    def verificar_numero(self):
        """Menu de opções para verificar propriedades de um número: paridade, primo, palíndromo, Fibonacci."""
        print("\n|============================|")
        print("|      Verificar Número      |")
        print("|1. Positivo, negativo, zero |")
        print("|2. Primo                    |")
        print("|3. Par, ímpar               |")
        print("|4. Palíndromo               |")
        print("|5. Fibonacci                |")
        print("|0. Voltar                   |")
        print("|============================|")
        opcao = input("Escolha uma opção: ")
        try:
            num = int(input("Digite o número: "))
            match opcao:
                case "1": print(f"{num} é positivo." if num > 0 else f"{num} é negativo." if num < 0 else "Zero.")
                case "2": print(f"{num} é primo." if self.eh_primo(num) else f"{num} não é primo.")
                case "3": print(f"{num} é par." if num % 2 == 0 else f"{num} é ímpar.")
                case "4": print(f"{num} é palíndromo." if str(num) == str(num)[::-1] else f"{num} não é palíndromo.")
                case "5": print(f"{num} pertence à sequência de Fibonacci." if self.eh_fibonacci(num) else f"{num} não pertence.")
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


# --- Outras Classes ---
class Outros:
    # --- ANÁLISE DE TEXTO ---
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
        
# --- JOGOS MATEMÁTICOS ---
class JogosMatematicos:
    def jogos_matematicos(self):
        """Menu para jogos matemáticos: desafios de tabuada."""
        print("\n|============================|")
        print("|     Jogos Matemáticos      |")
        print("|1. Quiz de Tabuada          |")
        print("|0. Voltar                   |")
        print("|============================|")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1": self.quiz_tabuada()
            case _: print("Opção inválida.")

    def quiz_tabuada(self):
        """Jogo de tabuada para testar conhecimento de multiplicação."""
        pontos = 0
        for _ in range(5):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            resposta_correta = num1 * num2
            resposta_usuario = int(input(f"Quanto é {num1} x {num2}? "))
            if resposta_usuario == resposta_correta:
                print("Correto!")
                pontos += 1
            else:
                print(f"Incorreto. A resposta correta é {resposta_correta}.")
        print(f"Pontuação final: {pontos}/5")

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
                "1": ("Celsius", "C"),
                "2": ("Fahrenheit", "F"),
                "3": ("Kelvin", "K"),
            },
            "pressao": {
                "1": ("Pascal", 1),
                "2": ("Bar", 100000),
                "3": ("Atmosfera", 101325),
                "4": ("Milímetro de Mercúrio", 133.322),
            },
            "massa": {
                "1": ("Quilograma", 1),
                "2": ("Grama", 0.001),
                "3": ("Miligrama", 0.000001),
                "4": ("Libra", 0.453592),
                "5": ("Onça", 0.0283495),
            },
            "energia": {
                "1": ("Joule", 1),
                "2": ("Kilojoule", 1000),
                "3": ("Caloria", 4.184),
                "4": ("Kilocaloria", 4184),
                "5": ("Watt-hora", 3600),
                "6": ("Kilowatt-hora", 3600000),
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
            }
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
            print("|0. Voltar                   |")
            print("|============================|")
            opcao = input("Escolha uma opção: ")
            match opcao:
                case "1": self.converter("comprimento")
                case "2": self.converter("área")
                case "3": self.converter("volume")
                case "4": self.converter("tempo")
                case "5": self.u_velocidade()
                case "6": self.converter_temperatura()
                case "7": self.converter_pressao()
                case "8": self.converter("massa")
                case "9": self.converter("energia")
                case "10": self.converter("dados")
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

    def u_velocidade(self):
        print("Conversão entre m/s e km/h")
        valor = float(input("Digite a velocidade em m/s: "))
        kmh = valor * 3.6
        print(f"{valor} m/s é igual a {kmh} km/h")

    def conversao_moeda(self):
        valor = float(input("Digite o valor em moeda: "))
        origem = input("Moeda de origem (USD, BRL, EUR): ")
        destino = input("Moeda de destino (USD, BRL, EUR): ")
        if origem in self.unidades["moeda"] and destino in self.unidades["moeda"]:
            valor_convertido = valor * (self.unidades["moeda"][destino] / self.unidades["moeda"][origem])
            print(f"Resultado: {valor} {origem} = {valor_convertido:.2f} {destino}")
        else:
            print("Erro: Moeda inválida.")

    def converter_temperatura(self):
        print("|====================================|")
        print("| Escolha uma unidade de temperatura |")
        print("|1. Celsius                          |")
        print("|2. Fahrenheit                       |")
        print("|3. Kelvin                           |")
        print("|0. Sair                             |")
        print("|====================================|")
        unidade_origem = input("Escolha a unidade de origem: ")
        valor = float(input("Digite o valor: "))
        
        # Conversões para todas as unidades de temperatura
        if unidade_origem == "1":  # Celsius
            fahrenheit = (valor * 9/5) + 32
            kelvin = valor + 273.15
            print(f"{valor} °C é igual a {fahrenheit} °F e {kelvin} K")
        elif unidade_origem == "2":  # Fahrenheit
            celsius = (valor - 32) * 5/9
            kelvin = celsius + 273.15
            print(f"{valor} °F é igual a {celsius} °C e {kelvin} K")
        elif unidade_origem == "3":  # Kelvin
            celsius = valor - 273.15
            fahrenheit = (celsius * 9/5) + 32
            print(f"{valor} K é igual a {celsius} °C e {fahrenheit} °F")
        else:
            print("Unidade inválida.")

    def converter_pressao(self):
        print("|================================|")
        print("| Escolha uma unidade de pressão |")
        print("|1. Pascal                       |")
        print("|2. Bar                          |")
        print("|3. Atmosfera                    |")
        print("|4. Milímetro de Mercúrio        |")
        print("|0. Sair                         |")
        print("|================================|")
        unidade_origem = input("Escolha a unidade de origem: ")
        if unidade_origem not in self.unidades["pressao"]:
            print("Unidade inválida.")
            return
        
        valor = float(input("Digite o valor: "))
        valor_em_base = valor * self.unidades["pressao"][unidade_origem][1]
        
        print(f"\nConversão de {valor} {self.unidades['pressao'][unidade_origem][0]} para todas as unidades disponíveis:")
        for key, (nome, fator) in self.unidades["pressao"].items():
            valor_convertido = valor_em_base / fator
            print(f"{valor_convertido} {nome}")

app = UtilitariosMatematicos()
app.menu_principal()

