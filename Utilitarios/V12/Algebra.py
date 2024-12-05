from Menu import MenuDict, MenuList

class Algebra:
    def __init__(self):
        """Exibe o menu principal de tópicos de Álgebra."""
        self.historico = []  # Lista para armazenar o histórico
        self.topicos = {
            'Básico': [
                'Expressões algébricas e simplificação',
                'Equações lineares',
                'Sistemas de equações lineares (duas variáveis)',
                'Produtos notáveis (quadrado da soma, diferença de quadrados)',
                'Fatoração algébrica'
            ],
            'Intermediário': [
                'Funções (definição, domínio e imagem)',
                'Equações quadráticas',
                'Inequações lineares e quadráticas',
                'Sistemas de inequações',
                'Funções polinomiais (análise gráfica)',
                'Matrizes e determinantes básicos'
            ],
            'Avançado': [
                'Álgebra abstrata (grupos, anéis e corpos)',
                'Matrizes avançadas (autovalores e autovetores)',
                'Transformações lineares',
                'Equações diofantinas',
                'Teoria dos polinômios (raízes e fatoração complexa)'
            ]
        }
        menu = MenuDict("Álgebra Completa", self.topicos)
        while True:
            menu.desenhar()
            opcao = input("Escolha um tópico ou operação: ")
            match opcao:
                case "0": return
                case "1": self.expressoes_algebricas()
                case "2": self.equacoes_lineares()
                case "3": self.sistemas_equacoes()
                case "4": self.produtos_notaveis()
                case "5": self.fatoracao_algebrica()
                case "6": self.funcoes_basicas()
                case "7": self.equacoes_quadraticas()
                case "8": self.inequacoes()
                case "9": self.sistemas_inequacoes()
                case "10": self.funcoes_polinomiais()
                case "11": self.matrizes_basicas()
                case "12": self.algebra_abstrata()
                case "13": self.matrizes_avancadas()
                case "14": self.transformacoes_lineares()
                case "15": self.equacoes_diofantinas()
                case "16": self.teoria_polinomios()
                case "17": self.limpar_historico()
                case "18": self.ver_historico()
                case _: print("Opção inválida, tente novamente.")

    ### Funções Básicas
    def expressoes_algebricas(self):
        print("Expressões Algébricas: Simplificação de expressões.")
        expr = input("Digite a expressão algébrica (ex.: 2x + 3x - x): ")
        # Aqui poderia integrar uma biblioteca como sympy para simplificar
        print(f"Expressão simplificada: {expr} (não implementado).")
        self.adicionar_historico("Expressões algébricas", expr)

    def equacoes_lineares(self):
        print("Equações Lineares: ax + b = 0")
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        if a == 0:
            print("Não é uma equação linear válida.")
        else:
            x = -b / a
            print(f"Solução: x = {x}")
            self.adicionar_historico("Equação Linear", f"x = {x}")

    def sistemas_equacoes(self):
        print("Sistemas de Equações Lineares: Exemplo 2x + y = 5, 3x - y = 4")
        a1, b1, c1 = map(float, input("Digite os coeficientes da 1ª equação (a b c): ").split())
        a2, b2, c2 = map(float, input("Digite os coeficientes da 2ª equação (a b c): ").split())
        det = a1 * b2 - a2 * b1
        if det == 0:
            print("O sistema não tem solução única.")
        else:
            x = (c1 * b2 - c2 * b1) / det
            y = (a1 * c2 - a2 * c1) / det
            print(f"Solução: x = {x}, y = {y}")
            self.adicionar_historico("Sistema Linear", f"x = {x}, y = {y}")

    def produtos_notaveis(self):
        print("Produtos Notáveis: Exemplos como (a+b)^2, (a-b)(a+b), etc.")
        # Exemplos com cálculos simbólicos podem ser adicionados aqui.

    def fatoracao_algebrica(self):
        print("Fatoração Algébrica: Exemplos de agrupamento, trinômios, etc.")

    ### Funções Intermediárias
    def funcoes_basicas(self):
        print("Funções: f(x) = ... Definir domínio e imagem.")

    def equacoes_quadraticas(self):
        print("Equações Quadráticas: ax^2 + bx + c = 0")
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print("Não há soluções reais.")
        elif delta == 0:
            x = -b / (2 * a)
            print(f"Solução única: x = {x}")
        else:
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            print(f"Soluções: x1 = {x1}, x2 = {x2}")
            self.adicionar_historico("Equação Quadrática", f"x1 = {x1}, x2 = {x2}")

    def inequacoes(self):
        print("Inequações Lineares e Quadráticas")

    def sistemas_inequacoes(self):
        print("Sistemas de Inequações")

    def funcoes_polinomiais(self):
        print("Funções Polinomiais e Análise Gráfica")

    def matrizes_basicas(self):
        print("Operações Básicas com Matrizes e Determinantes")

    ### Funções Avançadas
    def algebra_abstrata(self):
        print("Álgebra Abstrata: Grupos, Anéis, Corpos")

    def matrizes_avancadas(self):
        print("Matrizes Avançadas: Autovalores e Autovetores")

    def transformacoes_lineares(self):
        print("Transformações Lineares")

    def equacoes_diofantinas(self):
        print("Equações Diofantinas: ax + by = c")

    def teoria_polinomios(self):
        print("Teoria dos Polinômios: Fatoração e Raízes")

    ### Histórico
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

Algebra()