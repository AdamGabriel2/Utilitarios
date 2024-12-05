from Menu import Menu

class Financas:
    def __init__(self):
        menu_opcoes=["Calculadora Financeira","Simulador Financeiro"]
        menu = Menu("Financas", menu_opcoes)
        menu.desenhar()
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "0": return
            case "1": CalculadoraFinanceira()
            case "2": SimuladorFinanceiro()
            case _: print("Opção inválida. Tente novamente.")

class CalculadoraFinanceira:
    def __init__(self):
        menu_opcoes=["Calcular ROI","Calcular Margem de Lucro"]
        menu = Menu("Calculadora Financeira", menu_opcoes)
        menu.desenhar()
        func = input("Escolha uma função: ")
        match func:
            case "1":
                investimento = float(input("Digite o investimento inicial: "))
                retorno = float(input("Digite o retorno total: "))
                print(f"ROI: {self.calcular_roi(investimento, retorno)}%")
            case "2":
                receita = float(input("Digite a receita total: "))
                custo = float(input("Digite o custo total: "))
                print(f"Margem de Lucro: {self.calcular_margem_lucro(receita, custo)}%")
            case _: 
                print("Opção inválida.")

    def calcular_roi(self, investimento, retorno):
        """Calcula o Retorno sobre Investimento (ROI)."""
        return ((retorno - investimento) / investimento) * 100

    def calcular_margem_lucro(self, receita, custo):
        """Calcula a margem de lucro."""
        return ((receita - custo) / receita) * 100 if receita else 0

class SimuladorFinanceiro:
    def __init__(self):
        menu_opcoes = ["Calcular Juros Compostos","Calcular Investimento Futuro","Calcular Valor Presente"]
        menu = Menu("Simulador Financeiro", menu_opcoes)
        menu.desenhar()
        func = input("Escolha uma função: ")
        match func:
            case "1":
                capital = float(input("Digite o capital inicial: "))
                taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                tempo = float(input("Digite o tempo (em anos): "))
                print(f"Juros Compostos: {self.calcular_juros_compostos(capital, taxa, tempo)}")
            case "2":
                capital = float(input("Digite o capital inicial: "))
                taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                tempo = float(input("Digite o tempo (em anos): "))
                print(f"Investimento Futuro: {self.calcular_investimento_futuro(capital, taxa, tempo)}")
            case "3":
                montante = float(input("Digite o montante: "))
                taxa = float(input("Digite a taxa de juros (em %): ")) / 100
                tempo = float(input("Digite o tempo (em anos): "))
                print(f"Valor Presente: {self.calcular_valor_presente(montante, taxa, tempo)}")
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
