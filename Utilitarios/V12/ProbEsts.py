from Menu import MenuDict, MenuList

class ProbEsts:
    def __init__(self):
        """Exibe o menu principal com os tópicos organizados por níveis."""
        self.historico = []  # Lista para armazenar o histórico
        self.topicos = {
            'Básico': [
                'Conceitos de probabilidade',
                'Eventos mutuamente exclusivos',
                'Experimentos simples (cara ou coroa, dados)',
                'Média, mediana e moda'
            ],
            'Intermediário': [
                'Distribuições de probabilidade (binomial, normal)',
                'Variância e desvio padrão',
                'Análise combinatória (arranjos, combinações, permutações)',
                'Tabelas de frequência e histogramas'
            ],
            'Avançado': [
                'Estatística inferencial (intervalo de confiança, testes de hipótese)',
                'Regressão e correlação',
                'Distribuições avançadas (Poisson, t-Student, chi-quadrado)',
                'Análise multivariada',
                'aProbabilidade condicional e teorema de Bayes'
            ]
        }
        menu = MenuDict("Probabilidade e Estatistica", self.topicos)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação ou tópico: ")
            match opcao:
                case "0": return
                case "1": self.
                case "2": self.
                case "3": self.
                case "4": self.
                case "5": self.
                case "6": self.
                case "7": self.
                case "8": self.
                case "9": self.
                case "10": self.
                case "11": self.
                case "12": self.
                case "13": self.
                case "14": self.
                case "15": self.
                case "16": self.
                case "17": self.limpar_historico()
                case "18": self.ver_historico()
                case _: print("Opção inválida, tente novamente.")
