from Menu import Menu
from Base import BaseHist

class Financas:
    def __init__(self):
        self.historico = []  # Lista para armazenar o histórico
        menu_opcoes = ["Calculadora Financeira", "Simulador Financeiro", "Simulador de Empréstimos", "Simulador de Investimentos"]
        menu = Menu("Finanças", menu_opcoes)
        while True:
            menu.desenhar()
            opcao = input("Escolha uma opção: ")
            match opcao:
                case "0": return
                case "1": CalculadoraFinanceira(self.historico)
                case "2": SimuladorFinanceiro(self.historico)
                case "3": self.simulador_emprestimos_op()
                case "4": self.simulador_investimentos_op()
                case "5": BaseHist.limpar_historico(self.historico)
                case "6": self.ver_historico()
                case _: print("Opção inválida. Tente novamente.")

    def simulador_emprestimos_op(self):
        principal = float(input("Digite o valor do empréstimo: "))
        taxa = float(input("Digite a taxa de juros (em %): "))
        anos = int(input("Digite o número de anos: "))
        pagamento_mensal, total_pago, juros_totais = self.simulador_emprestimos(principal, taxa, anos)
        print(f"Pagamento Mensal: {pagamento_mensal:.2f}")
        print(f"Total Pago: {total_pago:.2f}")
        print(f"Juros Totais: {juros_totais:.2f}")
        self.adicionar_historico("Simulador de Empréstimos", f"Pagamento Mensal: {pagamento_mensal:.2f}, Total Pago: {total_pago:.2f}, Juros Totais: {juros_totais:.2f}")

    def simulador_investimentos_op(self):
        capital_inicial = float(input("Digite o capital inicial: "))
        taxa = float(input("Digite a taxa de juros (em %): ")) / 100
        anos = int(input("Digite o número de anos: "))
        aportes = float(input("Digite o valor dos aportes anuais (ou 0 se não houver): "))
        montante = self.simulador_investimentos(capital_inicial, taxa, anos, aportes)
        print(f"Montante após {anos} anos: {montante:.2f}")
        self.adicionar_historico("Simulador de Investimentos", f"Montante: {montante:.2f}")

    def simulador_emprestimos(self, principal, taxa, anos):
        """Calcula os pagamentos mensais e juros totais de um empréstimo."""
        taxa_mensal = taxa / 12 / 100
        n = anos * 12
        pagamento_mensal = principal * taxa_mensal / (1 - (1 + taxa_mensal) ** -n)
        total_pago = pagamento_mensal * n
        juros_totais = total_pago - principal
        return pagamento_mensal, total_pago, juros_totais

    def simulador_investimentos(self, capital_inicial, taxa, anos, aportes=0):
        """Simula o crescimento de um investimento ao longo do tempo."""
        montante = capital_inicial
        for ano in range(1, anos + 1):
            montante = montante * (1 + taxa) + aportes
        return montante

class CalculadoraFinanceira:
    def __init__(self, historico):
        self.historico = historico
        menu_opcoes = ["Calcular ROI", "Calcular Margem de Lucro"]
        menu = Menu("Calculadora Financeira", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            match func:
                case "1":
                    investimento = float(input("Digite o investimento inicial: "))
                    retorno = float(input("Digite o retorno total: "))
                    resultado = self.calcular_roi(investimento, retorno)
                    print(f"ROI: {resultado}%")
                    self.adicionar_historico("Calcular ROI", resultado)
                case "2":
                    receita = float(input("Digite a receita total: "))
                    custo = float(input("Digite o custo total: "))
                    resultado = self.calcular_margem_lucro(receita, custo)
                    print(f"Margem de Lucro: {resultado}%")
                    self.adicionar_historico("Calcular Margem de Lucro", resultado)
                case _: 
                    print("Opção inválida.")

    def calcular_roi(self, investimento, retorno):
        """Calcula o Retorno sobre Investimento (ROI)."""
        return ((retorno - investimento) / investimento) * 100

    def calcular_margem_lucro(self, receita, custo):
        """Calcula a margem de lucro."""
        return ((receita - custo) / receita) * 100 if receita else 0

    def adicionar_historico(self, operacao, resultado):
        """Adiciona uma entrada ao histórico."""
        self.historico.append(f"{operacao}: {resultado}%")

class SimuladorFinanceiro:
    def __init__(self, historico):
        self.historico = historico
        menu_opcoes = ["Calcular Juros Compostos", "Calcular Investimento Futuro", "Calcular Valor Presente"]
        menu = Menu("Simulador Financeiro", menu_opcoes)
        while True:
            menu.desenhar()
            func = input("Escolha uma função: ")
            match func:
                case "1":
                    capital = float(input("Digite o capital inicial: "))
                    taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                    tempo = float(input("Digite o tempo (em anos): "))
                    resultado = self.calcular_juros_compostos(capital, taxa, tempo)
                    print(f"Juros Compostos: {resultado}")
                    self.adicionar_historico("Calcular Juros Compostos", resultado)
                case "2":
                    capital = float(input("Digite o capital inicial: "))
                    taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                    tempo = float(input("Digite o tempo (em anos): "))
                    resultado = self.calcular_investimento_futuro(capital, taxa, tempo)
                    print(f"Investimento Futuro: {resultado}")
                    self.adicionar_historico("Calcular Investimento Futuro", resultado)
                case "3":
                    montante = float(input("Digite o montante: "))
                    taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                    tempo = float(input("Digite o tempo (em anos): "))
                    resultado = self.calcular_valor_presente(montante, taxa, tempo)
                    print(f"Valor Presente: {resultado}")
                    self.adicionar_historico("Calcular Valor Presente", resultado)
                case _: 
                    print("Opção inválida.")

    def calcular_juros_compostos(self, capital, taxa, tempo):
        """Calcula o montante total com juros compostos."""
        return capital * (1 + taxa) ** tempo

    def calcular_investimento_futuro(self, capital, taxa, tempo):
        """Calcula o valor futuro do investimento."""
        return self.calcular_juros_compostos(capital, taxa, tempo)

    def calcular_valor_presente(self, montante, taxa, tempo):
        """Calcula o valor presente dado um montante futuro."""
        return montante / ((1 + taxa) ** tempo)

    def adicionar_historico(self, operacao, resultado):
        """Adiciona uma entrada ao histórico."""
        self.historico.append(f"{operacao}: {resultado}")
