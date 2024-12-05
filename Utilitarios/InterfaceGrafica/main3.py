import tkinter as tk
from tkinter import ttk, messagebox


class VerifNumsApp:
    def __init__(self, master):
        self.master = master
        master.title("Verificar Propriedades de Números")
        master.geometry("600x500")
        master.configure(bg="#f0f0f0")

        self.label = ttk.Label(master, text="Verificar Propriedades de Números", font=("Arial", 16))
        self.label.pack(pady=20)

        self.menu_opcoes = [
            "Positivo, Negativo ou Zero",
            "Primo",
            "Par ou Ímpar",
            "Palíndromo",
            "Fibonacci",
            "Perfeito",
            "Amigável",
            "Cálculo de MDC e MMC",
        ]

        # Criando botões para cada funcionalidade
        for i, opcao in enumerate(self.menu_opcoes):
            ttk.Button(master, text=opcao, command=lambda idx=i: self.handle_option(idx)).pack(pady=5)

    def handle_option(self, opcao_idx):
        """Chamadas para funções baseadas na opção escolhida."""
        match opcao_idx:
            case 0: self.create_number_window("Positivo, Negativo ou Zero", verificar_positivo_negativo_zero)
            case 1: self.create_number_window("Verificar Número Primo", verificar_primo)
            case 2: self.create_number_window("Par ou Ímpar", verificar_par_ou_impar)
            case 3: self.create_number_window("Verificar Palíndromo", verificar_palindromo)
            case 4: self.create_number_window("Verificar Fibonacci", verificar_fibonacci)
            case 5: self.create_number_window("Verificar Número Perfeito", verificar_perfeito)
            case 6: self.create_dual_number_window("Verificar Números Amigáveis", verificar_amigavel)
            case 7: self.create_number_window("Cálculo de MDC e MMC (separe os números com espaço)", calcular_mdc_mmc)

    # Criação de janelas auxiliares
    def create_number_window(self, title, command):
        window = tk.Toplevel(self.master)
        window.title(title)
        window.geometry("400x300")

        ttk.Label(window, text="Digite um número:").pack(pady=5)
        entry = ttk.Entry(window)
        entry.pack()

        resultado = tk.StringVar()

        def execute_command():
            user_input = entry.get()
            resultado.set(command(user_input))

        ttk.Button(window, text="Verificar", command=execute_command).pack(pady=10)
        ttk.Label(window, textvariable=resultado, font=("Arial", 12)).pack()

    def create_dual_number_window(self, title, command):
        window = tk.Toplevel(self.master)
        window.title(title)
        window.geometry("400x300")

        ttk.Label(window, text="Digite o primeiro número:").pack(pady=5)
        entry1 = ttk.Entry(window)
        entry1.pack()

        ttk.Label(window, text="Digite o segundo número:").pack(pady=5)
        entry2 = ttk.Entry(window)
        entry2.pack()

        resultado = tk.StringVar()

        def execute_command():
            num1 = entry1.get()
            num2 = entry2.get()
            resultado.set(command(num1, num2))

        ttk.Button(window, text="Verificar", command=execute_command).pack(pady=10)
        ttk.Label(window, textvariable=resultado, font=("Arial", 12)).pack()


# Funções de Verificação
def verificar_positivo_negativo_zero(user_input):
    try:
        num = int(user_input)
        if num > 0:
            return f"{num} é positivo."
        elif num < 0:
            return f"{num} é negativo."
        else:
            return f"{num} é zero."
    except ValueError:
        return "Entrada inválida!"


def verificar_primo(user_input):
    try:
        num = int(user_input)
        return f"{num} é primo." if eh_primo(num) else f"{num} não é primo."
    except ValueError:
        return "Entrada inválida!"


def verificar_par_ou_impar(user_input):
    try:
        num = int(user_input)
        return f"{num} é par." if num % 2 == 0 else f"{num} é ímpar."
    except ValueError:
        return "Entrada inválida!"


def verificar_palindromo(user_input):
    try:
        num = int(user_input)
        return f"{num} é palíndromo." if str(num) == str(num)[::-1] else f"{num} não é palíndromo."
    except ValueError:
        return "Entrada inválida!"


def verificar_fibonacci(user_input):
    try:
        num = int(user_input)
        return f"{num} pertence à sequência de Fibonacci." if eh_fibonacci(num) else f"{num} não pertence."
    except ValueError:
        return "Entrada inválida!"


def verificar_perfeito(user_input):
    try:
        num = int(user_input)
        return f"{num} é um número perfeito." if eh_perfeito(num) else f"{num} não é perfeito."
    except ValueError:
        return "Entrada inválida!"


def verificar_amigavel(num1, num2):
    try:
        a, b = int(num1), int(num2)
        return f"{a} e {b} são números amigáveis." if eh_amigavel(a, b) else f"{a} e {b} não são amigáveis."
    except ValueError:
        return "Entrada inválida!"


def calcular_mdc_mmc(user_input):
    try:
        numeros = list(map(int, user_input.split()))
        if len(numeros) < 2:
            return "Insira pelo menos dois números."
        mdc = calcular_mdc_lista(numeros)
        mmc = calcular_mmc_lista(numeros)
        return f"MDC: {mdc}, MMC: {mmc}"
    except ValueError:
        return "Entrada inválida!"


# Funções Auxiliares
def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def eh_fibonacci(num):
    def eh_quadrado_perfeito(x):
        s = int(x**0.5)
        return s * s == x

    return eh_quadrado_perfeito(5 * num * num + 4) or eh_quadrado_perfeito(5 * num * num - 4)


def eh_perfeito(n):
    soma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return soma_divisores == n


def eh_amigavel(a, b):
    soma_a = sum(i for i in range(1, a) if a % i == 0)
    soma_b = sum(i for i in range(1, b) if b % i == 0)
    return soma_a == b and soma_b == a


def calcular_mdc_lista(numeros):
    def mdc(a, b):
        while b:
            a, b = b, a % b
        return a

    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mdc(resultado, num)
    return resultado


def calcular_mmc_lista(numeros):
    def mdc(a, b):
        while b:
            a, b = b, a % b
        return a

    def mmc(a, b):
        return abs(a * b) // mdc(a, b)

    resultado = numeros[0]
    for num in numeros[1:]:
        resultado = mmc(resultado, num)
    return resultado


# Inicializar o programa
root = tk.Tk()
app = VerifNumsApp(root)
root.mainloop()
