from Menu import Menu

# --- JOGOS ---
class Jogos:
    def quiz_matematico(self):
        print("Escolha a dificuldade: ")
        dificuldade = input("1. Fácil (1-10)\n2. Médio (1-50)\n3. Difícil (1-100): ")
        intervalo = {"1": 10, "2": 50, "3": 100}.get(dificuldade, 10)
        operacao = input("Escolha a operação (soma, subtracao, multiplicacao, divisao): ").lower()
        pontos = 0

        for _ in range(5):
            num1 = random.randint(1, intervalo)
            num2 = random.randint(1, intervalo)
            if operacao == "soma":
                resposta_correta = num1 + num2
                simbolo = "+"
            elif operacao == "subtracao":
                resposta_correta = num1 - num2
                simbolo = "-"
            elif operacao == "multiplicacao":
                resposta_correta = num1 * num2
                simbolo = "*"
            elif operacao == "divisao" and num2 != 0:
                resposta_correta = num1 // num2
                simbolo = "/"
            else:
                print("Operação inválida.")
                return

            resposta_usuario = int(input(f"Quanto é {num1} {simbolo} {num2}? "))
            if resposta_usuario == resposta_correta:
                print("Correto!")
                pontos += 1
            else:
                print(f"Incorreto. A resposta correta é {resposta_correta}.")
        print(f"Pontuação final: {pontos}/5")

    def sudoku_basico(self):
        self.tabuleiro = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

        while True:
            self.print_tabuleiro()
            try:
                x = int(input("Linha (0-8) ou -1 para sair: "))
                if x == -1:
                    break
                y = int(input("Coluna (0-8): "))
                valor = int(input("Valor (1-9): "))

                if self.eh_valido(x, y, valor):
                    self.tabuleiro[x][y] = valor
                    print("Valor inserido!")
                else:
                    print("Movimento inválido!")
            except (ValueError, IndexError):
                print("Entrada inválida! Tente novamente.")
            
    def print_tabuleiro(self):
        for linha in self.tabuleiro:
            print(" ".join(str(x) if x != 0 else "." for x in linha))
        print()  # Linha em branco para separação

    def eh_valido(self, x, y, valor):
        # Verifica linha e coluna
        for i in range(9):
            if self.tabuleiro[x][i] == valor or self.tabuleiro[i][y] == valor:
                return False
        
        # Verifica o quadrante 3x3
        quad_x = (x // 3) * 3
        quad_y = (y // 3) * 3
        for i in range(quad_x, quad_x + 3):
            for j in range(quad_y, quad_y + 3):
                if self.tabuleiro[i][j] == valor:
                    return False
        
        return True

    def __init__(self):
        menu_opcoes=["Quiz","Sudoku",]
        menu = Menu("Jogos", menu_opcoes)
        menu.desenhar()
        opcao = input("Escolha uma função: ")
        match opcao:
            case "1": self.quiz_matematico()
            case "2": self.sudoku_basico()
            case _: print("Opção inválida.")

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"

    def menu_jogo_da_velha(self):
        print("\n|=============================|")
        print("|1. Iniciar Jogo              |")
        print("|0. Voltar                    |")
        print("|=============================|")
        func = input("Escolha uma opção: ")

        if func == "1":
            self.iniciar_jogo()
        elif func == "0":
            return
        else:
            print("Opção inválida.")

    def iniciar_jogo(self):
        for _ in range(9):
            self.imprimir_tabuleiro()
            linha = int(input(f"Jogador {self.jogador_atual}, escolha a linha (0-2): "))
            coluna = int(input(f"Jogador {self.jogador_atual}, escolha a coluna (0-2): "))
            if self.fazer_jogada(linha, coluna):
                if self.verificar_vencedor():
                    self.imprimir_tabuleiro()
                    print(f"Jogador {self.jogador_atual} venceu!")
                    return
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
        self.imprimir_tabuleiro()
        print("Empate!")

    def fazer_jogada(self, linha, coluna):
        """Faz a jogada do jogador atual."""
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            return True
        else:
            print("Casa já ocupada! Tente novamente.")
            return False

    def verificar_vencedor(self):
        """Verifica se houve um vencedor."""
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != " ":
                return True
        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != " ":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return True
        return False

    def imprimir_tabuleiro(self):
        """Imprime o tabuleiro do jogo da velha."""
        for linha in self.tabuleiro:
            print(" | ".join(linha))
            print("-" * 9)

class SudokuSolver:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def menu_sudoku(self):
        print("\n|============================|")
        print("|1. Resolver Sudoku           |")
        print("|0. Voltar                   |")
        print("|=============================|")
        func = input("Escolha uma opção: ")

        if func == "1":
            if self.resolver():
                print("Sudoku resolvido:")
                self.imprimir_tabuleiro()
            else:
                print("Não foi possível resolver o Sudoku.")
        elif func == "0":
            return
        else:
            print("Opção inválida.")

    def resolver(self):
        """Resolve o Sudoku usando backtracking."""
        for i in range(9):
            for j in range(9):
                if self.tabuleiro[i][j] == 0:  # Encontrar uma célula vazia
                    for num in range(1, 10):
                        if self.eh_valido(i, j, num):
                            self.tabuleiro[i][j] = num
                            if self.resolver():
                                return True
                            self.tabuleiro[i][j] = 0  # Backtrack
                    return False
        return True

    def eh_valido(self, linha, coluna, num):
        """Verifica se um número pode ser colocado na célula."""
        for x in range(9):
            if self.tabuleiro[linha][x] == num or self.tabuleiro[x][coluna] == num:
                return False
        # Verificar a subgrade 3x3
        start_row, start_col = 3 * (linha // 3), 3 * (coluna // 3)
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[start_row + i][start_col + j] == num:
                    return False
        return True

    def imprimir_tabuleiro(self):
        """Imprime o tabuleiro de Sudoku."""
        for linha in self.tabuleiro:
            print(" ".join(str(num) for num in linha))
