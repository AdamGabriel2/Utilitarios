class Menu:
    def __init__(self, titulo: str, opcoes: list[str]):
        self.titulo = titulo
        self.opcoes = opcoes
        self.largura = 50  # Define a largura máxima do menu

    def desenhar(self):
        # Linha superior
        print(f"|{'=' * (self.largura - 2)}|")
        
        # Título centralizado
        print(f"|{self.titulo.center(self.largura - 2)}|")
        
        # Opções formatadas
        i=1
        for idx, opcao in enumerate(self.opcoes, start=1):
            linha = f"{idx}. {opcao}"  # Exemplo: "1. Comprimento"
            print(f"|{linha.ljust(self.largura - 2)}|")
            i+=1
        # Linha para a opção "Voltar"
        if i>9:
            print(f"|{i}{'. Limpar Histórico'.ljust(self.largura - 4)}|")
            print(f"|{i+1}{'. Ver Histórico'.ljust(self.largura - 4)}|")
        else:
            print(f"|{i}{'. Limpar Histórico'.ljust(self.largura - 3)}|")
            print(f"|{i+1}{'. Ver Histórico'.ljust(self.largura - 3)}|")
        print(f"|{'0. Voltar'.ljust(self.largura - 2)}|")
        
        # Linha inferior
        print(f"|{'=' * (self.largura - 2)}|")
