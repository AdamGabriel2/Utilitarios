import math

class UtilitariosMatematicos:
    def __init__(self):
        pass

    def menu_principal(self):
        while True:
            print("|============================|")
            print("|            Menu            |")
            print("|1. Calculadora              |")
            print("|2. Tabuada                  |")
            print("|3. Verificar Número         |")
            print("|4. Tamanho do texto         |")
            print("|5. Conversores              |")
            print("|0. Sair                     |")
            print("|============================|")
            opcao = input("Escolha uma opção: ")
            if opcao == "0":
                print("Fim do Programa.")
                break
            elif opcao == "1":
                self.calculadora()
            elif opcao == "2":
                self.tabuada()
            elif opcao == "3":
                self.verificar_numero()
            elif opcao == "4":
                self.tamanho_do_texto()
            elif opcao == "5":
                self.conversores()
            else:
                print("Opção inválida. Por favor, escolha novamente.")

    def calculadora(self):
        print("|============================|")
        print("|        Calculadora         |")
        print("|1. Adição                   |")
        print("|2. Subtração                |")
        print("|3. Multiplicação            |")
        print("|4. Divisão                  |")
        print("|5. Potência                 |")
        print("|6. Raiz Quadrada            |")
        print("|7. Múltiplos                |")
        print("|8. Média                    |")
        print("|9. Soma de Números          |")
        print("|10. Fatorial                |")
        print("|0. Voltar                   |")
        print("|============================|")
        opcao = input("Escolha uma operação: ")
        if opcao == "0":
            return
        operacoes = {
            "1": self.adicao,
            "2": self.subtracao,
            "3": self.multiplicacao,
            "4": self.divisao,
            "5": self.potencia,
            "6": self.raiz_quadrada,
            "7": self.verifica_multiplos,
            "8": self.media,
            "9": self.soma_numeros,
            "10": self.fatorial
        }
        operacao = operacoes.get(opcao)
        if operacao:
            operacao()
        else:
            print("Opção inválida.")

    def adicao(self):
        a, b = self._input_dois_numeros()
        print(f"A soma é: {a + b}")

    def subtracao(self):
        a, b = self._input_dois_numeros()
        print(f"O resultado é: {a - b}")

    def multiplicacao(self):
        a, b = self._input_dois_numeros()
        print(f"O produto é: {a * b}")

    def divisao(self):
        a, b = self._input_dois_numeros()
        if b != 0:
            print(f"O quociente é: {a / b}")
        else:
            print("Erro: Divisão por zero não permitida.")

    def potencia(self):
        base = int(input("Base: "))
        expoente = int(input("Expoente: "))
        print(f"O resultado é: {base ** expoente}")

    def raiz_quadrada(self):
        num = int(input("Número para raiz quadrada: "))
        print(f"A raiz quadrada é: {math.sqrt(num)}")

    def verifica_multiplos(self):
        a, b = self._input_dois_numeros()
        if a % b == 0:
            print(f"{a} é múltiplo de {b}")
        else:
            print(f"{a} não é múltiplo de {b}")

    def media(self):
        quantidade = int(input("Quantidade de números: "))
        numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(quantidade)]
        media = sum(numeros) / quantidade
        print(f"A média é: {media}")

    def soma_numeros(self):
        limite = int(input("Até qual número somar: "))
        soma = sum(range(limite + 1))
        print(f"A soma é: {soma}")

    def fatorial(self):
        num = int(input("Número para fatorial: "))
        print(f"O fatorial de {num} é: {math.factorial(num)}")

    def tabuada(self):
        num = int(input("Número para tabuada: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

    def verificar_numero(self):
        print("|============================|")
        print("|     Verificar Número       |")
        print("|1. Positivo, negativo ou zero|")
        print("|2. Primo                    |")
        print("|3. Par ou ímpar             |")
        print("|0. Voltar                   |")
        print("|============================|")
        opcao = input("Escolha uma verificação: ")
        if opcao == "0":
            return
        elif opcao == "1":
            self.verificar_positivo_negativo()
        elif opcao == "2":
            self.verificar_primo()
        elif opcao == "3":
            self.verificar_paridade()

    def verificar_positivo_negativo(self):
        num = int(input("Número: "))
        if num > 0:
            print("Positivo")
        elif num < 0:
            print("Negativo")
        else:
            print("Zero")

    def verificar_primo(self):
        num = int(input("Número: "))
        if num > 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            print("É primo")
        else:
            print("Não é primo")

    def verificar_paridade(self):
        num = int(input("Número: "))
        if num % 2 == 0:
            print("Par")
        else:
            print("Ímpar")

    def tamanho_do_texto(self):
        texto = input("Digite o texto: ")
        print(f"Tamanho do texto: {len(texto)} caracteres")

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
            }
        }

    def conversores(self):
        while True:
            print("|============================|")
            print("|         Conversores        |")
            print("|1. Comprimento              |")
            print("|2. Área                     |")
            print("|3. Volume                   |")
            print("|4. Tempo                    |")
            print("|5. Velocidade               |")
            print("|0. Voltar                   |")
            print("|============================|")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.converter("comprimento")
            elif opcao == "2":
                self.converter("área")
            elif opcao == "3":
                self.converter("volume")
            elif opcao == "4":
                self.converter("tempo")
            elif opcao == "5":
                self.u_velocidade()
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def converter(self, tipo):
        unidades = self.unidades[tipo]
        print(f"|============================|")
        print(f"| Escolha uma unidade de {tipo} |")
        for key, (nome, _) in unidades.items():
            print(f"|{key}. {nome:<24}|")
        print("|============================|")
        
        unidade_origem = input("Escolha a unidade de origem: ")
        if unidade_origem not in unidades:
            print("Unidade inválida.")
            return
        
        valor = float(input(f"Digite o valor em {unidades[unidade_origem][0]}: "))
        
        print(f"|============================|")
        print(f"| Escolha a unidade de destino|")
        for key, (nome, _) in unidades.items():
            print(f"|{key}. {nome:<24}|")
        print("|============================|")
        
        unidade_destino = input("Escolha a unidade de destino: ")
        if unidade_destino not in unidades:
            print("Unidade inválida.")
            return

        valor_em_base = valor * unidades[unidade_origem][1]
        valor_convertido = valor_em_base / unidades[unidade_destino][1]
        
        print(f"{valor} {unidades[unidade_origem][0]} é igual a {valor_convertido} {unidades[unidade_destino][0]}")

    def u_velocidade(self):
        print("Conversão entre m/s e km/h")
        valor = float(input("Digite a velocidade em m/s: "))
        kmh = valor * 3.6
        print(f"{valor} m/s é igual a {kmh} km/h")
