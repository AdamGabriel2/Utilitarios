from Menu import Menu
from Base import BaseHist

class OperacoesMatrizes:
    def __init__(self):
        """Realiza operações com matrizes."""
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Adição", "Multiplicação", "Transposição"]
        menu = Menu("Operações com Matrizes", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação: ")

            tamanho = input("Digite o tamanho da matriz (ex: 2x2): ")
            valor_inicial = float(input("Digite o valor inicial: "))
            tipo_progressao = input("Digite o tipo de progressão (PA ou PG): ").strip().upper()

            if tipo_progressao == 'PA':
                razao = float(input("Digite a razão da PA: "))
                matriz1 = Matriz.criar_matriz(tamanho, valor_inicial, 'PA', razao)
            elif tipo_progressao == 'PG':
                razao = float(input("Digite a razão da PG: "))
                matriz1 = Matriz.criar_matriz(tamanho, valor_inicial, 'PG', razao)
            else:
                print("Tipo de progressão inválido.")
                continue

            print("Matriz criada:")
            self.imprimir_matriz(matriz1)

            tamanho = input("Digite o tamanho da segunda matriz (ex: 2x2): ")
            valor_inicial = float(input("Digite o valor inicial da segunda matriz: "))
            tipo_progressao = input("Digite o tipo de progressão (PA ou PG): ").strip().upper()

            if tipo_progressao == 'PA':
                razao = float(input("Digite a razão da PA: "))
                matriz2 = Matriz.criar_matriz(tamanho, valor_inicial, 'PA', razao)
            elif tipo_progressao == 'PG':
                razao = float(input("Digite a razão da PG: "))
                matriz2 = Matriz.criar_matriz(tamanho, valor_inicial, 'PG', razao)
            else:
                print("Tipo de progressão inválido.")
                continue

            print("Segunda matriz criada:")
            self.imprimir_matriz(matriz2)

            match opcao:
                case "0":
                    return
                case "1":
                    self.resultado = matriz1.adicionar(matriz2)
                    self.adicionar_historico("Adição", matriz1, matriz2, self.resultado)
                case "2":
                    self.resultado = matriz1.multiplicar(matriz2)
                    self.adicionar_historico("Multiplicação", matriz1, matriz2, self.resultado)
                case "3":
                    self.resultado = matriz1.transpor()
                    self.adicionar_historico("Transposição", matriz1, None, self.resultado)
                case "4": BaseHist.limpar_historico(self.historico)
                case "5": self.ver_historico()

            self.matrizes_resultado()

    def adicionar_historico(self, operacao, matriz1, matriz2, resultado):
        """Adiciona a operação ao histórico."""
        if matriz2 is not None:
            self.historico.append(f"{operacao}: {matriz1.matriz} e {matriz2.matriz} => {resultado.matriz}")
        else:
            self.historico.append(f"{operacao}: {matriz1.matriz} => {resultado.matriz}")

    def matrizes_resultado(self):
        """Exibe o resultado das operações."""
        print("\nResultado:")
        self.resultado.mostrarMatriz()

    def imprimir_matriz(self, matriz):
        for linha in matriz.matriz:
            print(f"[{', '.join(map(str, linha))}],")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

class Matriz:
    def __init__(self, nLinhas, nColunas):
        self.nLinhas = nLinhas
        self.nColunas = nColunas
        self.matriz = [[0 for _ in range(nColunas)] for _ in range(nLinhas)]

    def addValores(self):
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                self.matriz[l][c] = float(input(f"Insira o valor para a Matriz em Linha: {l} e Coluna: {c}: "))

    def mostrarMatriz(self):
        saida = ""
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                numero = self.matriz[l][c]
                saida += f"{numero}\t"
            saida += "\n"
        print(f"\nSaida da Matriz {self.nLinhas}x{self.nColunas}:")
        print(saida)

    def transpor(self):
        transposta = Matriz(self.nColunas, self.nLinhas)
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                transposta.matriz[c][l] = self.matriz[l][c]
        return transposta

    def adicionar(self, outra):
        if self.nLinhas != outra.nLinhas or self.nColunas != outra.nColunas:
            raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")
        resultado = Matriz(self.nLinhas, self.nColunas)
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                resultado.matriz[l][c] = self.matriz[l][c] + outra.matriz[l][c]
        return resultado

    def multiplicar(self, outra):
        if self.nColunas != outra.nLinhas:
            raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        resultado = Matriz(self.nLinhas, outra.nColunas)
        for i in range(self.nLinhas):
            for j in range(outra.nColunas):
                resultado.matriz[i][j] = sum(self.matriz[i][k] * outra.matriz[k][j] for k in range(self.nColunas))
        return resultado

    def igual(self, outra):
        if self.nLinhas != outra.nLinhas or self.nColunas != outra.nColunas:
            return False
        for l in range(self.nLinhas):
            for c in range(self.nColunas):
                if self.matriz[l][c] != outra.matriz[l][c]:
                    return False
        return True

    @staticmethod
    def criar_matriz(tamanho, valor_inicial, progressao, razao=1):
        linhas, colunas = map(int, tamanho.split('x'))
        matriz = Matriz(linhas, colunas)
        valor_atual = valor_inicial

        if progressao == 'PA':
            for i in range(linhas):
                for j in range(colunas):
                    matriz.matriz[i][j] = valor_atual
                    valor_atual += razao

        elif progressao == 'PG':
            for i in range(linhas):
                for j in range(colunas):
                    matriz.matriz[i][j] = valor_atual
                    valor_atual *= razao

        return matriz
   