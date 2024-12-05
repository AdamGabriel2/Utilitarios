from Menu import MenuDict, MenuList

class Aritmetica:
    def __init__(self):
        """Exibe o menu principal com os tópicos organizados por níveis."""
        self.historico = []  # Lista para armazenar o histórico
        self.topicos = {
            'Básico': [
                'Operações fundamentais',
                'Propriedades dos números',
                'Fatores e múltiplos',
                'Números primos e compostos',
                'Potenciação e radiciação simples',
                'Frações, decimais e porcentagens'
            ],
            'Intermediário': [
                'Razões e proporções',
                'Média, mediana e moda',
                'Regra de três',
                'Progressões aritméticas e geométricas simples',
                'Teorema fundamental da aritmética'
            ],
            'Avançado': [
                'Sequências numéricas complexas',
                'Cálculo modular',
                'Teoremas de divisibilidade',
                'Números irracionais e transcendentes',
                'Propriedades dos números inteiros'
            ]
        }
        menu = MenuDict("Aritmetica", self.topicos)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação ou tópico: ")
            match opcao:
                case "0": return
                case "1": self.operacoes_fundamentais()
                case "2": self.propriedades_dos_numeros()
                case "3": self.fatores_e_multiplos()
                case "4": self.numeros_primos_compostos()
                case "5": self.potenciacao_radiciacao()
                case "6": self.fracoes_decimais_porcentagens()
                case "7": self.razoes_e_proporcoes()
                case "8": self.media_mediana_moda()
                case "9": self.regra_de_tres()
                case "10": self.progressao_aritmetica_geometrica()
                case "11": self.teorema_fundamental_aritmetica()
                case "12": self.sequencias_complexas()
                case "13": self.calculo_modular()
                case "14": self.teoremas_divisibilidade()
                case "15": self.numeros_irracionais_transcendentes()
                case "16": self.propriedades_inteiros()
                case "17": self.limpar_historico()
                case "18": self.ver_historico()
                case _: print("Opção inválida, tente novamente.")

    def operacoes_fundamentais(self):
        print("Operações Fundamentais: Adição, Subtração, Multiplicação e Divisão")
        menu_opcoes=["Adição","Subtração","Multiplicação","Divisão"]
        menu = MenuList("Operações Fundamentais", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação: ")
            match opcao:
                case "0": return
                case "1": self.operacao("Adição", self.adicao)
                case "2": self.operacao("Subtração", self.subtracao)
                case "3": self.operacao("Multiplicação", self.multiplicacao)
                case "4": self.operacao("Divisão", self.divisao, divisao=True)
                case _: print("Opção inválida, tente novamente.")

    def operacao(self, nome_operacao, operacao, divisao=False):
        """Realiza operações matemáticas básicas e avançadas."""
        try:
            if divisao:
                a = float(input("Entre com o dividendo: "))
                b = float(input("Entre com o divisor: "))
                if b == 0:
                    print("Erro: Divisão por zero não permitida.")
                    return
                resultado = operacao(a, b)
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
        return f"{r}"

    def subtracao(self, a, b):
        r = a - b
        return f"{r}"

    def multiplicacao(self, a, b):
        r = a * b
        return f"{r}"

    def divisao(self, a, b):
        r = a / b
        return f"{r}"

    def propriedades_dos_numeros(self):
        print("Propriedades dos Números:")
        print(" - Comutativa, Associativa, Distributiva, etc.")

    def fatores_e_multiplos(self):
        n = int(input("Digite um número para encontrar seus fatores e múltiplos: "))
        fatores = [i for i in range(1, n + 1) if n % i == 0]
        print(f"Fatores de {n}: {fatores}")
        print(f"Multiplos de {n} (até 10x): {[n * i for i in range(1, 11)]}")

    def numeros_primos_compostos(self):
        n = int(input("Digite um número: "))
        if n < 2:
            print(f"{n} não é primo.")
            return
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(f"{n} é um número composto.")
                return
        print(f"{n} é um número primo.")

    def potenciacao_radiciacao(self):
        a = float(input("Digite a base: "))
        b = float(input("Digite o expoente: "))
        resultado = a ** b
        print(f"{a} elevado a {b} é {resultado}")
        self.adicionar_historico(f"Potência de {a} elevado a {b}", resultado)

    def fracoes_decimais_porcentagens(self):
        print("Frações, Decimais e Porcentagens:")
        fracao = input("Digite uma fração (ex.: 3/4): ")
        num, den = map(float, fracao.split("/"))
        decimal = num / den
        porcentagem = decimal * 100
        print(f"Decimal: {decimal}, Porcentagem: {porcentagem:.2f}%")

    def razoes_e_proporcoes(self):
        print("Razões e Proporções: Exemplo: 2/3 = 4/6")
        a, b = map(float, input("Digite dois valores separados por espaço: ").split())
        print(f"A razão é {a}/{b} ou {a / b:.2f}")

    def media_mediana_moda(self):
        dados = list(map(float, input("Digite os números separados por espaço: ").split()))
        media = sum(dados) / len(dados)
        mediana = sorted(dados)[len(dados) // 2]
        print(f"Média: {media}, Mediana: {mediana}")

    def regra_de_tres(self):
        print("Regra de Três Simples")
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))
        c = float(input("Digite o terceiro valor: "))
        d = (b * c) / a
        print(f"O resultado é {d}")

    def progressao_aritmetica_geometrica(self):
        print("Progressões Aritméticas e Geométricas")

    def teorema_fundamental_aritmetica(self):
        print("Teorema Fundamental da Aritmética: Decomposição em fatores primos")

    def sequencias_complexas(self):
        print("Sequências Numéricas Complexas")

    def calculo_modular(self):
        a = int(input("Digite o número: "))
        b = int(input("Digite o módulo: "))
        print(f"{a} mod {b} = {a % b}")

    def teoremas_divisibilidade(self):
        print("Teoremas de Divisibilidade")

    def numeros_irracionais_transcendentes(self):
        print("Números Irracionais e Transcendentes")

    def propriedades_inteiros(self):
        print("Propriedades dos Números Inteiros")

    def limpar_historico(self):
        self.historico.clear()
        print("Histórico limpo!")

    def ver_historico(self):
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico:")
            for h in self.historico:
                print(h)

    def adicionar_historico(self, operacao, resultado):
        self.historico.append(f"{operacao}: {resultado}")

Aritmetica()