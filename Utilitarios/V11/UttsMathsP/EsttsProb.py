from Menu import Menu
from Base import BaseHist
from UttsMathsP.CalcComp import CalculadoraCompleta

class EstatisticasProbabilidades(CalculadoraCompleta):
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Calcular Média","Calcular Mediana","Calcular Moda","Calcular Desvio Padrão","Probabilidade Simples","Probabilidade Composta","Distribuição Normal (aproximada)","Distribuição Binomial","Distribuição de Poisson"]
        menu = Menu("Estatísticas e Probabilidades", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            if func == "0":
                return
            match func:
                case "1":
                    numeros = input("Digite os números separados por vírgula: ")
                    lista_numeros = [float(num.strip()) for num in numeros.split(",")]
                    resultado = self.calcular_media(lista_numeros)
                    print(f"Média: {resultado}")
                    self.adicionar_historico("Média", lista_numeros, resultado)
                case "2":
                    numeros = input("Digite os números separados por vírgula: ")
                    lista_numeros = [float(num.strip()) for num in numeros.split(",")]
                    resultado = self.calcular_mediana(lista_numeros)
                    print(f"Mediana: {resultado}")
                    self.adicionar_historico("Mediana", lista_numeros, resultado)
                case "3":
                    numeros = input("Digite os números separados por vírgula: ")
                    lista_numeros = [float(num.strip()) for num in numeros.split(",")]
                    resultado = self.calcular_moda(lista_numeros)
                    print(f"Moda: {resultado}")
                    self.adicionar_historico("Moda", lista_numeros, resultado)
                case "4":
                    numeros = input("Digite os números separados por vírgula: ")
                    lista_numeros = [float(num.strip()) for num in numeros.split(",")]
                    resultado = self.calcular_desvio_padrao(lista_numeros)
                    print(f"Desvio Padrão: {resultado}")
                    self.adicionar_historico("Desvio Padrão", lista_numeros, resultado)
                case "5":
                    eventos = int(input("Digite o número de eventos: "))
                    total = int(input("Digite o total de eventos possíveis: "))
                    resultado = self.probabilidade_simples(eventos, total)
                    print(f"Probabilidade Simples: {resultado}")
                    self.adicionar_historico("Probabilidade Simples", {"eventos": eventos, "total": total}, resultado)
                case "6":
                    probabilidades = input("Digite as probabilidades separadas por vírgula: ")
                    lista_probabilidades = [float(p.strip()) for p in probabilidades.split(",")]
                    resultado = self.probabilidade_composta(lista_probabilidades)
                    print(f"Probabilidade Composta: {resultado}")
                    self.adicionar_historico("Probabilidade Composta", lista_probabilidades, resultado)
                case "7":
                    media = float(input("Digite a média: "))
                    desvio_padrao = float(input("Digite o desvio padrão: "))
                    x = float(input("Digite o valor de x: "))
                    resultado = self.distribuicao_normal(x, media, desvio_padrao)
                    print(f"Distribuição Normal: {resultado}")
                    self.adicionar_historico("Distribuição Normal", {"x": x, "media": media, "desvio_padrao": desvio_padrao}, resultado)
                case "8":
                    n = int(input("Digite o número de tentativas (n): "))
                    k = int(input("Digite o número de sucessos (k): "))
                    p = float(input("Digite a probabilidade de sucesso (p): "))
                    resultado = self.distribuicao_binomial(n, k, p)
                    print(f"Distribuição Binomial: {resultado}")
                    self.adicionar_historico("Distribuição Binomial", {"n": n, "k": k, "p": p}, resultado)
                case "9":
                    k = int(input("Digite o número de ocorrências (k): "))
                    lambda_ = float(input("Digite o parâmetro lambda: "))
                    resultado = self.distribuicao_poisson(k, lambda_)
                    print(f"Distribuição de Poisson: {resultado}")
                    self.adicionar_historico("Distribuição de Poisson", {"k": k, "lambda": lambda_}, resultado)
                case "10": BaseHist.limpar_historico(self.historico)
                case "11": self.ver_historico()
                case _: print("Opção inválida.")

    def adicionar_historico(self, funcao, numeros, resultado):
        """Adiciona a operação ao histórico."""
        self.historico.append(f"{funcao} de {numeros} = {resultado}")

    def ver_historico(self):
        """Exibe o histórico de operações."""
        if not self.historico:
            print("Histórico vazio.")
        else:
            print("Histórico de operações:")
            for entry in self.historico:
                print(entry)

    def calcular_media(self, lista):
        """Calcula a média de uma lista de números."""
        return sum(lista) / len(lista) if lista else 0

    def calcular_mediana(self, lista):
        """Calcula a mediana de uma lista de números."""
        lista.sort()
        n = len(lista)
        meio = n // 2
        if n % 2 == 0:
            return (lista[meio - 1] + lista[meio]) / 2
        else:
            return lista[meio]

    def calcular_moda(self, lista):
        """Calcula a moda de uma lista de números."""
        contagem = {}
        for num in lista:
            contagem[num] = contagem.get(num, 0) + 1
        max_freq = max(contagem.values())
        modas = [num for num, freq in contagem.items() if freq == max_freq]
        return modas

    def calcular_desvio_padrao(self, lista):
        """Calcula o desvio padrão de uma lista de números."""
        media = self.calcular_media(lista)
        variancia = sum((x - media) ** 2 for x in lista) / len(lista)
        return variancia ** 0.5

    def probabilidade_simples(self, eventos, total):
        """Calcula a probabilidade simples de um evento."""
        return eventos / total if total > 0 else 0

    def probabilidade_composta(self, probabilidades):
        """Calcula a probabilidade composta de eventos independentes."""
        resultado = 1
        for p in probabilidades:
            resultado *= p
        return resultado

    def distribuicao_normal(self, x, media, desvio_padrao):
        """Calcula a distribuição normal (aproximada) para um valor x."""
        # Aproximação da função densidade da normal
        constante = 1 / (desvio_padrao * (2 * 3.14) ** 0.5)
        exp_part = -0.5 * ((x - media) / desvio_padrao) ** 2
        return constante * (2.718 ** exp_part)

    def distribuicao_binomial(self, n, k, p):
        """Calcula a distribuição binomial."""
        combinacao = self.combinacao(n, k)
        return combinacao * (p ** k) * ((1 - p) ** (n - k))

    def distribuicao_poisson(self, k, lambda_):
        """Calcula a distribuição de Poisson."""
        return (lambda_ ** k * (2.718 ** -lambda_)) / self.fatorial(k)
