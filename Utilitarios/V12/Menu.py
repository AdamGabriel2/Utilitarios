class MenuDict:
    def __init__(self, titulo: str, topicos: dict[str, list[str]]):
        self.titulo = titulo
        self.topicos = topicos
        self.largura = 75  # Define a largura máxima do menu

    def desenhar(self):
        # Linha superior
        print(f"|{'=' * (self.largura - 2)}|")
        
        # Título centralizado
        print(f"|{self.titulo.center(self.largura - 2)}|")
        
        # Desenhar os tópicos e suas opções
        idx = 1  # Contador de opções
        for nivel, topicos in self.topicos.items():
            # Exibir o título do nível
            print(f"|{'-' * (self.largura - 2)}|")  # Separador
            nivel_titulo = f"[{nivel}]"
            print(f"|{nivel_titulo.center(self.largura - 2)}|")
            
            # Exibir os tópicos do nível
            for topico in topicos:
                linha = f"{idx}. {topico}"  # Exemplo: "1. Operações fundamentais"
                print(f"|{linha.ljust(self.largura - 2)}|")
                idx += 1

        # Opções adicionais no final do menu
        print(f"|{'-' * (self.largura - 2)}|")  # Separador
        print(f"|{f'{idx}. Limpar Histórico'.ljust(self.largura - 2)}|")
        print(f"|{f'{idx + 1}. Ver Histórico'.ljust(self.largura - 2)}|")
        print(f"|{'0. Voltar'.ljust(self.largura - 2)}|")
        
        # Linha inferior
        print(f"|{'=' * (self.largura - 2)}|")

    def mostrar_topicos(self):
        """
        Método para exibir os tópicos em formato de lista, sem a formatação
        de menu, útil para debug ou exibições simples.
        """
        for nivel, topicos in self.topicos.items():
            print(f"{nivel}:")
            for topico in topicos:
                print(f" - {topico}")

class MenuList:
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
