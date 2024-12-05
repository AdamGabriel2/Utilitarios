from Menu import Menu
from Base import BaseMath, BaseHist

# --- CONVERSORES ---
class ConvUni(BaseMath):
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
        
        menu_opcoes = ["Conversão de Unidades", "Conversão de Moeda", "Adicionar Unidade Personalizada"]
        menu = Menu("Conversores", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma opção: ")
            match opcao:
                case "1": self.conversores_unidades()
                case "2": self.conversao_moeda()
                case "3": self.adicionar_unidade_personalizada()
                case "4": self.mostrar_historico()
                case "5": BaseHist.limpar_historico(self.historico)
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
                case "22": BaseHist.limpar_historico(self.historico)
                case "23": self.ver_historico()
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
            
