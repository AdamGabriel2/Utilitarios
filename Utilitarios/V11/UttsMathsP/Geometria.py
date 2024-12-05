from Menu import Menu
from Base import BaseHist

class Geometria:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = [
            "Calcular Área do Círculo",
            "Calcular Área do Retângulo",
            "Calcular Perímetro do Triângulo",
            "Calcular Volume do Cubo",
            "Calcular Área do Trapézio",
            "Calcular Área do Losango",
            "Calcular Volume do Cilindro",
            "Calcular Volume da Esfera",
            "Calcular Diagonal do Retângulo",
            "Calcular Distância entre Dois Pontos",
            "Calcular Área do Triângulo",
            "Transladar Ponto",
            "Rotacionar Ponto",
            "Refletir Ponto",
        ]
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
                    largura = float(input("Digite a largura do retângulo: "))
                    altura = float(input("Digite a altura do retângulo: "))
                    diagonal = self.calcular_diagonal_retangulo(largura, altura)
                    print(f"Diagonal do Retângulo: {diagonal}")
                    self.adicionar_historico("Diagonal do Retângulo", {"largura": largura, "altura": altura}, diagonal)
                case "10":
                    x1 = float(input("Digite x1: "))
                    y1 = float(input("Digite y1: "))
                    x2 = float(input("Digite x2: "))
                    y2 = float(input("Digite y2: "))
                    distancia = self.calcular_distancia_pontos((x1, y1), (x2, y2))
                    print(f"Distância entre os pontos: {distancia}")
                    self.adicionar_historico("Distância entre Pontos", {"ponto1": (x1, y1), "ponto2": (x2, y2)}, distancia)
                case "11":
                    base = float(input("Digite a base do triângulo: "))
                    altura = float(input("Digite a altura do triângulo: "))
                    area = self.calcular_area_triangulo(base, altura)
                    print(f"Área do Triângulo: {area}")
                    self.adicionar_historico("Área do Triângulo", {"base": base, "altura": altura}, area)
                case "12":
                    ponto = (float(input("Digite a coordenada x do ponto: ")), float(input("Digite a coordenada y do ponto: ")))
                    dx = float(input("Digite o deslocamento em x: "))
                    dy = float(input("Digite o deslocamento em y: "))
                    ponto_transladado = self.transladar(ponto, dx, dy)
                    print(f"Ponto Transladado: {ponto_transladado}")
                    self.adicionar_historico("Translação de Ponto", {"ponto": ponto, "dx": dx, "dy": dy}, ponto_transladado)
                case "13":
                    ponto = (float(input("Digite a coordenada x do ponto: ")), float(input("Digite a coordenada y do ponto: ")))
                    angulo = float(input("Digite o ângulo de rotação (em graus): "))
                    ponto_rotacionado = self.rotacionar(ponto, angulo)
                    print(f"Ponto Rotacionado: {ponto_rotacionado}")
                    self.adicionar_historico("Rotação de Ponto", {"ponto": ponto, "angulo": angulo}, ponto_rotacionado)
                case "14":
                    ponto = (float(input("Digite a coordenada x do ponto: ")), float(input("Digite a coordenada y do ponto: ")))
                    eixo = input("Digite o eixo de reflexão (x ou y): ")
                    ponto_refletido = self.refletir(ponto, eixo)
                    print(f"Ponto Refletido: {ponto_refletido}")
                    self.adicionar_historico("Reflexão de Ponto", {"ponto": ponto, "eixo": eixo}, ponto_refletido)
                case "15": BaseHist.limpar_historico(self.historico)
                case "16": self.ver_historico()
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

    def calcular_diagonal_retangulo(self, largura, altura):
        """Calcula a diagonal de um retângulo."""
        return (largura ** 2 + altura ** 2) ** 0.5

    def calcular_distancia_pontos(self, ponto1, ponto2):
        """Calcula a distância entre dois pontos."""
        return ((ponto2[0] - ponto1[0]) ** 2 + (ponto2[1] - ponto1[1]) ** 2) ** 0.5

    def calcular_area_triangulo(self, base, altura):
        """Calcula a área de um triângulo."""
        return (base * altura) / 2
