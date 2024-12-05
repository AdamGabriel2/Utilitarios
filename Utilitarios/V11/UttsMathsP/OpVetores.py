from Menu import Menu
from Base import BaseHist

class OperacoesVetores:
    def __init__(self):
        """Realiza operações com vetores."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Adição", "Subtração", "Produto Escalar", "Produto Vetorial"]
        menu = Menu("Operações com Vetores", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação: ")

            tamanho = int(input("Digite o tamanho dos vetores: "))
            print("Preencha os valores do primeiro vetor:")
            vetor1 = Vetor.criar_vetor(tamanho)

            print("Preencha os valores do segundo vetor:")
            vetor2 = Vetor.criar_vetor(tamanho if opcao in ["1", "2", "3"] else 3)  # Produto vetorial exige vetores 3D
            match opcao:
                case "1":
                    self.resultado = vetor1.adicionar(vetor2)
                    self.adicionar_historico("Adição", vetor1, vetor2, self.resultado)
                case "2":
                    self.resultado = vetor1.subtrair(vetor2)
                    self.adicionar_historico("Subtração", vetor1, vetor2, self.resultado)
                case "3":
                    escalar = vetor1.produto_escalar(vetor2)
                    print(f"Resultado do Produto Escalar: {escalar}")
                    self.adicionar_historico("Produto Escalar", vetor1, vetor2, escalar)
                    continue
                case "4":
                    self.resultado = vetor1.produto_vetorial(vetor2)
                    self.adicionar_historico("Produto Vetorial", vetor1, vetor2, self.resultado)
                case "5": BaseHist.limpar_historico(self.historico)
                case "6": self.ver_historico()
                case _:
                    print("Opção inválida.")
                    continue

            self.vetor_resultado()

    def adicionar_historico(self, operacao, vetor1, vetor2, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{operacao}: {vetor1.componentes} e {vetor2.componentes} => {resultado.componentes}")

    def vetor_resultado(self):
        """Exibe o resultado das operações."""
        print("\nResultado:")
        self.resultado.mostrar_vetor()

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

class Vetor:
    def __init__(self, componentes):
        self.componentes = componentes

    def mostrar_vetor(self):
        print(f"Vetor: {self.componentes}")

    def adicionar(self, outro):
        if len(self.componentes) != len(outro.componentes):
            raise ValueError("Os vetores devem ter o mesmo tamanho para serem somados.")
        resultado = [a + b for a, b in zip(self.componentes, outro.componentes)]
        return Vetor(resultado)

    def subtrair(self, outro):
        if len(self.componentes) != len(outro.componentes):
            raise ValueError("Os vetores devem ter o mesmo tamanho para serem subtraídos.")
        resultado = [a - b for a, b in zip(self.componentes, outro.componentes)]
        return Vetor(resultado)

    def produto_escalar(self, outro):
        if len(self.componentes) != len(outro.componentes):
            raise ValueError("Os vetores devem ter o mesmo tamanho para o produto escalar.")
        return sum(a * b for a, b in zip(self.componentes, outro.componentes))

    def produto_vetorial(self, outro):
        if len(self.componentes) != 3 or len(outro.componentes) != 3:
            raise ValueError("O produto vetorial só é definido para vetores 3D.")
        x1, y1, z1 = self.componentes
        x2, y2, z2 = outro.componentes
        resultado = [
            y1 * z2 - z1 * y2,
            z1 * x2 - x1 * z2,
            x1 * y2 - y1 * x2,
        ]
        return Vetor(resultado)

    @staticmethod
    def criar_vetor(tamanho):
        componentes = []
        for i in range(tamanho):
            valor = float(input(f"Insira o valor do componente {i + 1}: "))
            componentes.append(valor)
        return Vetor(componentes)
