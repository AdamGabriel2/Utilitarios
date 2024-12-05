from Menu import MenuDict, MenuList

class Trigonometria:
    def __init__(self):
        """Exibe o menu principal com os tópicos organizados por níveis."""
        self.historico = []  # Lista para armazenar o histórico
        self.topicos = {
            'Básico': [
                'Razões trigonométricas (seno, cosseno, tangente)',
                'Triângulos retângulos',
                'Propriedades dos ângulos',
                'Teorema de Pitágoras',
                'Simetria e transformações básicas'
            ],
            'Intermediário': [
                'Geometria analítica (reta, circunferência e parábola)',
                'Trigonometria básica (seno, cosseno, tangente)',
                'Relações métricas no triângulo retângulo',
                'Teorema dos cossenos e dos senos',
                'Polígonos regulares e irregulares'
            ],
            'Avançado': [
                'Geometria diferencial (curvatura e superfícies)',
                'Topologia básica (conjuntos abertos e fechados)',
                'Geometria projetiva',
                'Geometrias não-euclidianas',
                'Aplicações de vetores em geometria'
            ]
        }
        menu = MenuDict("Trigonometria", self.topicos)
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
