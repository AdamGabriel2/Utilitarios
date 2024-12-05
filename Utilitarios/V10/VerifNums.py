from Menu import Menu
from Base import Base

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
