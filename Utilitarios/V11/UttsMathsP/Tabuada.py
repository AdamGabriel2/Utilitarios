from Menu import Menu
from Base import BaseHist

# --- TABUADA ---
class Tabuada:
    def __init__(self):
        """Mostra a tabuada de multiplicação para um número dado, com intervalo definido pelo usuário."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Tabuada"]
        menu = Menu("Funções Matemáticas", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            match func:
                case "1":
                    try:
                        num = int(input("Digite o número para ver sua tabuada: "))
                        inicio = int(input("Digite o início do intervalo: "))
                        fim = int(input("Digite o fim do intervalo: "))
                        for i in range(inicio, fim + 1):
                            resultado = num * i
                            print(f"{num} x {i} = {resultado}")
                            self.adicionar_historico(num, i, resultado)
                    except ValueError:
                        print("Erro: Entrada inválida.")
                case "2": BaseHist.limpar_historico(self.historico)
                case "3": self.ver_historico()
                case _: 
                    print("Opção inválida.")

    def adicionar_historico(self, num, i, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{num} x {i} = {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)