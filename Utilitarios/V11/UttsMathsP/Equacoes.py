from Menu import Menu
from Base import BaseMath

class Equacoes(BaseMath):
    def __init__(self):
        """Resolve equações de primeiro e segundo grau."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Primero Grau", "Segundo Grau"]
        menu = Menu("Equações", menu_opcoes)
        while True:
            menu.desenhar()
            grau = input("Escolha uma opção: ")
            try:
                if opcao == "1":
                    a = float(input("Coeficiente a: "))
                    b = float(input("Coeficiente b: "))
                    solucao = -b / a
                    print(f"Solução da equação linear: x = {solucao}")
                    self.adicionar_historico("Equação de 1º grau", a, b, solucao)
                elif opcao == "2":
                    a = float(input("Coeficiente a: "))
                    b = float(input("Coeficiente b: "))
                    c = float(input("Coeficiente c: "))
                    discriminante = b**2 - (4 * a * c)
                    if discriminante >= 0:
                        raiz1 = (-b + self.raiz_quadrada(discriminante)) / (2 * a)
                        raiz2 = (-b - self.raiz_quadrada(discriminante)) / (2 * a)
                        print(f"As raízes são x1 = {raiz1} e x2 = {raiz2}")
                        self.adicionar_historico("Equação de 2º grau", a, b, c, raiz1, raiz2)
                    else:
                        print("Sem solução real.")
                elif opcao == "3": BaseHist.limpar_historico(self.historico)
                elif opcao == "4": self.ver_historico()
            except ValueError:
                print("Erro: Entrada inválida.")

    def adicionar_historico(self, tipo_equacao, *coeficientes):
        """Adiciona a solução ao histórico."""
        if len(coeficientes) == 3:  # Primeiro grau
            self.historico.append(f"{tipo_equacao}: a={coeficientes[0]}, b={coeficientes[1]} => x={coeficientes[2]}")
        elif len(coeficientes) == 5:  # Segundo grau
            self.historico.append(f"{tipo_equacao}: a={coeficientes[0]}, b={coeficientes[1]}, c={coeficientes[2]} => x1={coeficientes[3]}, x2={coeficientes[4]}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)
