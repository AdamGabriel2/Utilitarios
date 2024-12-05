from Menu import Menu
from Base import BaseHist

class Algoritmos:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = [
            "Bubble Sort", "Quick Sort", "Merge Sort", 
            "Insertion Sort", "Selection Sort", "Heap Sort", "Radix Sort",
            "Busca Linear", "Busca Binária", 
            "Busca em Largura (BFS)", "Busca em Profundidade (DFS)",
            "Lista Ligada", "Pilha", "Fila"
        ]
        menu = Menu("Algoritmos", menu_opcoes)

        while True:
            menu.desenhar()
            opcao = input("Escolha uma operação: ")
            match opcao:
                case "0": return
                case "1": self.bubble_sort_op()
                case "2": self.quick_sort_op()
                case "3": self.merge_sort_op()
                case "4": self.insertion_sort_op()
                case "5": self.selection_sort_op()
                case "6": self.heap_sort_op()
                case "7": self.radix_sort_op()
                case "8": self.busca_linear_op()
                case "9": self.busca_binaria_op()
                case "10": self.busca_largura_op()
                case "11": self.busca_profundidade_op()
                case "12": self.lista_ligada_op()
                case "13": self.pilha_op()
                case "14": self.fila_op()
                case "15": BaseHist.limpar_historico(self.historico)
                case "16": self.ver_historico()
                case _: print("Opção inválida, tente novamente.")

    def _obter_lista(self, mensagem):
        """Obtém uma lista de números a partir da entrada do usuário."""
        entrada = input(mensagem)
        return [float(num) for num in entrada.split(",")]

    def bubble_sort_op(self):
        lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
        resultado = self.bubble_sort(lista)
        print(f"Lista Ordenada com Bubble Sort: {resultado}")
        self.adicionar_historico("Bubble Sort", resultado)

    @staticmethod
    def bubble_sort(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista
    
    def quick_sort_op(self):
        lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
        resultado = self.quick_sort(lista)
        print(f"Lista Ordenada com Quick Sort: {resultado}")
        self.adicionar_historico("Quick Sort", resultado)

    @staticmethod
    def quick_sort(lista):
        if len(lista) <= 1:
            return lista
        else:
            pivo = lista[len(lista) // 2]
            esquerda = [x for x in lista if x < pivo]
            meio = [x for x in lista if x == pivo]
            direita = [x for x in lista if x > pivo]
            return Algoritmos.quick_sort(esquerda) + meio + Algoritmos.quick_sort(direita)

    def merge_sort_op(self):
        lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
        resultado = self.merge_sort(lista)
        print(f"Lista Ordenada com Merge Sort: {resultado}")
        self.adicionar_historico("Merge Sort", resultado)

    @staticmethod
    def merge_sort(lista):
        if len(lista) > 1:
            meio = len(lista) // 2
            esquerda = lista[:meio]
            direita = lista[meio:]

            Algoritmos.merge_sort(esquerda)
            Algoritmos.merge_sort(direita)

            i = j = k = 0
            while i < len(esquerda) and j < len(direita):
                if esquerda[i] < direita[j]:
                    lista[k] = esquerda[i]
                    i += 1
                else:
                    lista[k] = direita[j]
                    j += 1
                k += 1

            while i < len(esquerda):
                lista[k] = esquerda[i]
                i += 1
                k += 1

            while j < len(direita):
                lista[k] = direita[j]
                j += 1
                k += 1

        return lista

    def insertion_sort_op(self):
        lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
        resultado = self.insertion_sort(lista)
        print(f"Lista Ordenada com Insertion Sort: {resultado}")
        self.adicionar_historico("Insertion Sort", resultado)

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def selection_sort_op(self):
        lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
        resultado = self.selection_sort(lista)
        print(f"Lista Ordenada com Selection Sort: {resultado}")
        self.adicionar_historico("Selection Sort", resultado)

    @staticmethod
    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def heap_sort_op(self):
        lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
        resultado = self.heap_sort(lista)
        print(f"Lista Ordenada com Heap Sort: {resultado}")
        self.adicionar_historico("Heap Sort", resultado)

    @staticmethod
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Algoritmos.heapify(arr, n, largest)

    @staticmethod
    def heap_sort(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            Algoritmos.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            Algoritmos.heapify(arr, i, 0)
        return arr

    def radix_sort_op(self):
        lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
        resultado = Algoritmos.radix_sort(lista)
        print(f"Lista Ordenada com Radix Sort: {resultado}")
        self.adicionar_historico("Radix Sort", resultado)

    @staticmethod
    def radix_sort(arr):
        max1 = max(arr)
        exp = 1
        while max1 // exp > 0:
            Algoritmos.counting_sort(arr, exp)
            exp *= 10
        return arr

    @staticmethod
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1

        for i in range(n):
            arr[i] = output[i]

    def busca_linear_op(self):
        lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
        alvo = float(input("Digite o número a ser buscado: "))
        resultado = self.busca_linear(lista, alvo)
        print(f"Resultado da Busca Linear: {'Encontrado na posição ' + str(resultado) if resultado != -1 else 'Não encontrado'}")
        self.adicionar_historico("Busca Linear", f"Alvo: {alvo}, Resultado: {resultado}")

    @staticmethod
    def busca_linear(lista, alvo):
        for i, valor in enumerate(lista):
            if valor == alvo:
                return i
        return -1

    def busca_binaria_op(self):
        lista = self._obter_lista("Insira uma lista de números (separados por vírgula): ")
        alvo = float(input("Digite o número a ser buscado: "))
        resultado = self.busca_binaria(lista, alvo)
        print(f"Resultado da Busca Binária: {'Encontrado na posição ' + str(resultado) if resultado != -1 else 'Não encontrado'}")
        self.adicionar_historico("Busca Binária", f"Alvo: {alvo}, Resultado: {resultado}")

    @staticmethod
    def busca_binaria(lista, alvo):
        lista.sort()  # Certifique-se de que a lista esteja ordenada
        baixo, alto = 0, len(lista) - 1
        while baixo <= alto:
            meio = (baixo + alto) // 2
            if lista[meio] < alvo:
                baixo = meio + 1
            elif lista[meio] > alvo:
                alto = meio - 1
            else:
                return meio
        return -1

    def busca_largura_op(self):
        grafo = self._obter_grafo()
        inicio = input("Digite o vértice de início: ")
        resultado = self.bfs(grafo, inicio)
        print(f"Nós visitados na Busca em Largura: {resultado}")
        self.adicionar_historico("Busca em Largura", f"Início: {inicio}, Visitados: {resultado}")

    @staticmethod
    def bfs(grafo, inicio):
        visitados = set()
        fila = [inicio]
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                visitados.add(vertice)
                fila.extend(set(grafo[vertice]) - visitados)
        return visitados

    def busca_profundidade_op(self):
        grafo = self._obter_grafo()
        inicio = input("Digite o vértice de início: ")
        resultado = self.dfs(grafo, inicio)
        print(f"Nós visitados na Busca em Profundidade: {resultado}")
        self.adicionar_historico("Busca em Profundidade", f"Início: {inicio}, Visitados: {resultado}")

    @staticmethod
    def dfs(grafo, vertice, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                Algoritmos.dfs(grafo, vizinho, visitados)
        return visitados

    def lista_ligada_op(self):
        lista = ListaLigada()
        while True:
            acao = input("Escolha uma ação (adicionar/imprimir/sair): ")
            if acao == "adicionar":
                dado = input("Digite o valor a ser adicionado: ")
                lista.adicionar(dado)
                self.adicionar_historico("Lista Ligada", f"Adicionado: {dado}")
            elif acao == "imprimir":
                lista.imprimir()
            elif acao == "sair":
                break
            else:
                print("Ação inválida.")

    def pilha_op(self):
        pilha = Pilha()
        while True:
            acao = input("Escolha uma ação (empilhar/desempilhar/sair): ")
            if acao == "empilhar":
                valor = input("Digite o valor a ser empilhado: ")
                pilha.empilhar(valor)
                self.adicionar_historico("Pilha", f"Empilhado: {valor}")
            elif acao == "desempilhar":
                valor = pilha.desempilhar()
                print(f"Desempilhado: {valor}")
            elif acao == "sair":
                break
            else:
                print("Ação inválida.")

    def fila_op(self):
        fila = Fila()
        while True:
            acao = input("Escolha uma ação (enfileirar/desenfileirar/sair): ")
            if acao == "enfileirar":
                valor = input("Digite o valor a ser enfileirado: ")
                fila.enfileirar(valor)
                self.adicionar_historico("Fila", f"Enfileirado: {valor}")
            elif acao == "desenfileirar":
                valor = fila.desenfileirar()
                print(f"Desenfileirado: {valor}")
            elif acao == "sair":
                break
            else:
                print("Ação inválida.")

    def adicionar_historico(self, operacao, resultado):
        """Adiciona uma entrada ao histórico."""
        self.historico.append(f"{operacao}: {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def imprimir(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")

class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        return self.itens.pop() if not self.vazia() else None

    def vazia(self):
        return len(self.itens) == 0

class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        return self.itens.pop(0) if not self.vazia() else None

    def vazia(self):
        return len(self.itens) == 0
