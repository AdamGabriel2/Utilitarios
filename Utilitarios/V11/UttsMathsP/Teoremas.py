from Menu import Menu
from Base import BaseHist

class Teoremas:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = [
            "Teorema de Pitágoras",
            "Teorema de Tales"
        ]
        menu = Menu("Teoremas", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha um teorema: ")
            match func:
                case "0":
                    return
                case "1":
                    a = float(input("Digite o comprimento do lado A: "))
                    b = float(input("Digite o comprimento do lado B: "))
                    hipotenusa = self.teorema_pitagoras(a, b)
                    print(f"Comprimento da hipotenusa: {hipotenusa}")
                    self.adicionar_historico("Teorema de Pitágoras", {"a": a, "b": b}, hipotenusa)
                case "2":
                    # Exemplo simples do Teorema de Tales
                    a = float(input("Digite o comprimento do segmento A: "))
                    b = float(input("Digite o comprimento do segmento B: "))
                    c = float(input("Digite o comprimento do segmento C: "))
                    proporcao = self.teorema_tales(a, b, c)
                    print(f"Proporção: {proporcao}")
                    self.adicionar_historico("Teorema de Tales", {"a": a, "b": b, "c": c}, proporcao)
                case "3": BaseHist.limpar_historico(self.historico)
                case "4": self.ver_historico()
                case _: print("Opção inválida.")

    def adicionar_historico(self, teorema, parametros, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{teorema}: {parametros} => {resultado}")

    def teorema_pitagoras(self, a, b):
        """Calcula a hipotenusa de um triângulo retângulo."""
        return (a**2 + b**2) ** 0.5

    def teorema_tales(self, a, b, c):
        """Calcula a proporção do Teorema de Tales."""
        return (a / b) * c

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)
