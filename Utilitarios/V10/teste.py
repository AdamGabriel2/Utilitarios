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
        for idx, opcao in enumerate(self.opcoes, start=1):
            linha = f"{idx}. {opcao}"  # Exemplo: "1. Comprimento"
            print(f"|{linha.ljust(self.largura - 2)}|")
        
        # Opção "Ver Histórico" estilizada
        print(f"|{len(self.opcoes) + 1}. Ver Histórico".ljust(self.largura - 1) + '|')
        
        # Linha para a opção "Voltar"
        print(f"|{'0. Voltar'.ljust(self.largura - 2)}|")
        
        # Linha inferior
        print(f"|{'=' * (self.largura - 2)}|")

menu_opcoes = ["Utilitários Matemáticos","Verificadores de Números","Utilitários de Texto","Conversores de Unidades","Finanças","Jogos"]
menu = Menu("Menu Principal", menu_opcoes)
menu.desenhar()
menu_opcoes=["Calculadora Completa","Tabuada","Funções Matemáticas","Calculo de Estatística","Resolver Equações","Operações com Vetores","Operações com Matrizes","Geometria","Teorema","Número Complexo"]
menu = Menu("Utilitários Matemáticos", menu_opcoes)
menu.desenhar()
menu_opcoes=["Adição","Subtração","Multiplicação","Divisão","Potência","Raiz Quadrada","Fatorial","Combinação","Permutação","Derivada","Integral"]
menu = Menu("Calculadora Completa", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Tabuada"]
menu = Menu("Tabuada", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Logaritmo", "Exponencial", "Seno", "Cosseno", "Tangente"]
menu = Menu("Funções Matemáticas", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Calcular Média", "Calcular Mediana", "Calcular Moda", "Calcular Desvio Padrão"]
menu = Menu("Estatísticas", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Primero Grau", "Segundo Grau"]
menu = Menu("Equações", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Adição", "Subtração", "Produto Escalar", "Produto Vetorial"]
menu = Menu("Operações com Vetores", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Adição", "Multiplicação", "Transposição"]
menu = Menu("Operações com Matrizes", menu_opcoes)
menu.desenhar()
menu_opcoes = [
"Calcular Área do Círculo","Calcular Área do Retângulo","Calcular Perímetro do Triângulo","Calcular Volume do Cubo"]
menu = Menu("Geometria", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Teorema de Pitágoras","Teorema de Tales"]
menu = Menu("Teoremas", menu_opcoes)
menu_opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Módulo do primeiro número"]
menu = Menu("Número Complexo", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
menu = Menu("Fração", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Positivo, Negativo, Zero", "Primo", "Par, Ímpar", "Palíndromo", "Fibonacci", "Perfeito", "Amigável", "Cálculo de MDC e MMC", "Listar Fibonacci até N", "Listar Números Perfeitos até N", "Contar Dígitos de um Número", "Listar Números Primos até N", "Mágico", "Triangular", "Catalan", "Quadrado Perfeito", "Cubo Perfeito", "Número Abundante/Deficiente", "Número de Harshad","Mostrar Histórico"]
menu = Menu("Verificar Número", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Conversão de Unidades", "Conversão de Moeda", "Adicionar Unidade Personalizada"]
menu = Menu("Conversores", menu_opcoes)
menu.desenhar()
menu_opcoes=["Comprimento","Área","Volume","Tempo","Velocidade","Temperatura","Pressão","Massa", "Energia","Dados","Força","Ângulo","Densidade","Frequência","Iluminância","Luminância", "Potência","Eletricidade","Radioatividade","Velocidade Angular","Fluxo de Massa"]
menu = Menu("Conversores", menu_opcoes)
menu.desenhar()
menu_opcoes=["Analise de Texto"]
menu = Menu("Utilitários de Texto", menu_opcoes)
menu.desenhar()
menu_opcoes=["Calculadora Financeira","Simulador Financeiro"]
menu = Menu("Financas", menu_opcoes)
menu.desenhar()
menu_opcoes=["Calcular ROI","Calcular Margem de Lucro"]
menu = Menu("Calculadora Financeira", menu_opcoes)
menu.desenhar()
menu_opcoes = ["Calcular Juros Compostos","Calcular Investimento Futuro","Calcular Valor Presente"]
menu = Menu("Simulador Financeiro", menu_opcoes)
menu.desenhar()
menu_opcoes=["Quiz","Sudoku"]
menu = Menu("Jogos", menu_opcoes)
menu.desenhar()

