import tkinter as tk
from tkinter import ttk, messagebox
import math
from collections import Counter

class App:
    def __init__(self, master):
        self.master = master
        master.title("Utilitários")
        master.geometry("600x500")
        master.configure(bg="#f0f0f0")

        # Creating the menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Main Menu Options
        self.utilitarios_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Menu Principal", menu=self.utilitarios_menu)

        # Adding options to the menu
        self.utilitarios_menu.add_command(label="Matemática Avançada", command=self.show_mat_avancados)
        self.utilitarios_menu.add_separator()
        self.utilitarios_menu.add_command(label="Sair", command=master.quit)

        # Main frames (for each functionality)
        self.frames = {
            "mat_avancados": ttk.Frame(master, padding="10"),
        }

        # Welcome message
        self.label_welcome = ttk.Label(master, text="Bem-vindo ao Programa de Utilitários!", font=("Arial", 16))
        self.label_welcome.pack(pady=20)

    def hide_frames(self):
        """Hides all active frames before displaying the next one."""
        for frame in self.frames.values():
            frame.pack_forget()

    def show_frame(self, frame_key):
        """Shows the specified frame."""
        self.hide_frames()
        frame = self.frames[frame_key]
        frame.pack(fill="both", expand=True, pady=20)

    def show_mat_avancados(self):
        self.show_frame("mat_avancados")
        frame = self.frames["mat_avancados"]
        self.clear_frame(frame)

        ttk.Label(frame, text="Utilitários Matemáticos Avançados", font=("Arial", 14)).pack(pady=10)

        # Buttons for each advanced functionality
        ttk.Button(frame, text="Calculadora Avançada", command=self.show_calculadora_avancada).pack(pady=5)
        ttk.Button(frame, text="Funções Matemáticas", command=self.show_funcoes_matematicas).pack(pady=5)
        ttk.Button(frame, text="Cálculo de Estatística", command=self.show_estatisticas).pack(pady=5)
        ttk.Button(frame, text="Resolver Equações", command=self.show_equacoes).pack(pady=5)
        ttk.Button(frame, text="Operações com Matrizes", command=self.show_operacoes_matrizes).pack(pady=5)
        ttk.Button(frame, text="Geometria", command=self.show_geometria).pack(pady=5)
        ttk.Button(frame, text="Teoremas", command=self.show_teoremas).pack(pady=5)

    def placeholder(self):
        """Message for functionality in development."""
        messagebox.showinfo("Em breve", "Essa funcionalidade será implementada em breve!")

    def clear_frame(self, frame):
        """Removes all widgets from a frame."""
        for widget in frame.winfo_children():
            widget.destroy()

    # Advanced Calculator
    def show_calculadora_avancada(self):
        def calcular():
            op = opcoes_var.get()
            try:
                n = int(entrada_n.get())
                k = int(entrada_k.get()) if entrada_k.get() else None
                if op == "Fatorial":
                    resultado.set(math.factorial(n))
                elif op == "Combinação":
                    resultado.set(self.combinacao(n, k))
                elif op == "Permutação":
                    resultado.set(self.permutacao(n, k))
                elif op == "Derivada":
                    self.calcular_derivada()
                elif op == "Integral":
                    self.calcular_integral()
                else:
                    resultado.set("Opção inválida.")
            except Exception as e:
                resultado.set(f"Erro: {e}")

        janela = tk.Toplevel(self.master)
        janela.title("Calculadora Avançada")
        janela.geometry("400x300")
        ttk.Label(janela, text="Escolha uma operação:", font=("Arial", 12)).pack(pady=10)
        opcoes_var = tk.StringVar(value="Fatorial")
        opcoes = ["Fatorial", "Combinação", "Permutação", "Derivada", "Integral"]
        ttk.OptionMenu(janela, opcoes_var, *opcoes).pack()

        ttk.Label(janela, text ="Digite n:").pack(pady=5)
        entrada_n = ttk.Entry(janela)
        entrada_n.pack()

        ttk.Label(janela, text="Digite k (se necessário):").pack(pady=5)
        entrada_k = ttk.Entry(janela)
        entrada_k.pack()

        resultado = tk.StringVar(value="")
        ttk.Button(janela, text="Calcular", command=calcular).pack(pady=10)
        ttk.Label(janela, textvariable=resultado, font=("Arial", 12)).pack()

    def combinacao(self, n, k):
        """Calcula a combinação de n elementos tomados k a k."""
        if k > n:
            return 0
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    def permutacao(self, n, k):
        """Calcula a permutação de n elementos tomados k a k."""
        if k > n:
            return 0
        return math.factorial(n) // math.factorial(n - k)

    def calcular_derivada(self):
        # Implementar a lógica para calcular a derivada
        pass

    def calcular_integral(self):
        # Implementar a lógica para calcular a integral
        pass

    # Mathematical Functions
    def show_funcoes_matematicas(self):
        def calcular():
            op = opcoes_var.get()
            try:
                num = float(entrada_num.get())
                if op == "Logaritmo":
                    base = float(entrada_base.get()) if entrada_base.get() else 10
                    resultado.set(self.logaritmo(num, base))
                elif op == "Exponencial":
                    resultado.set(self.exponencial(num))
                elif op == "Seno":
                    resultado.set(self.seno(num))
                elif op == "Cosseno":
                    resultado.set(self.cosseno(num))
                elif op == "Tangente":
                    resultado.set(self.tangente(num))
                else:
                    resultado.set("Opção inválida.")
            except Exception as e:
                resultado.set(f"Erro: {e}")

        janela = tk.Toplevel(self.master)
        janela.title("Funções Matemáticas")
        janela.geometry("400x300")
        ttk.Label(janela, text="Escolha uma função:", font=("Arial", 12)).pack(pady=10)
        opcoes_var = tk.StringVar(value="Logaritmo")
        opcoes = ["Logaritmo", "Exponencial", "Seno", "Cosseno", "Tangente"]
        ttk.OptionMenu(janela, opcoes_var, *opcoes).pack()

        ttk.Label(janela, text="Digite o número:").pack(pady=5)
        entrada_num = ttk.Entry(janela)
        entrada_num.pack()

        ttk.Label(janela, text="Base (para logaritmo, opcional):").pack(pady=5)
        entrada_base = ttk.Entry(janela)
        entrada_base.pack()

        resultado = tk.StringVar(value="")
        ttk.Button(janela, text="Calcular", command=calcular).pack(pady=10)
        ttk.Label(janela, textvariable=resultado, font=("Arial", 12)).pack()

    def logaritmo(self, x, base=10):
        """Calcula o logaritmo de x na base especificada."""
        if x <= 0:
            raise ValueError("Logaritmo indefinido para valores menores ou iguais a zero.")
        return math.log(x, base)

    def exponencial(self, x):
        """Calcula e^x usando a série de Taylor."""
        return math.exp(x)

    def seno(self, x):
        """Calcula o seno de x usando a série de Taylor."""
        return math.sin(x)

    def cosseno(self, x):
        """Calcula o cosseno de x usando a série de Taylor."""
        return math.cos(x)

    def tangente(self, x):
        """Calcula a tangente de x como seno/cosseno."""
        return math.tan(x)

    # Statistics
    def show_estatisticas(self):
        def calcular():
            func = opcoes_var.get()
            numeros = entrada_numeros.get()
            lista_numeros = [float(num.strip()) for num in numeros.split(",")]
            if func == "Calcular Média":
                resultado.set(self.calcular_media(lista_numeros))
            elif func == "Calcular Mediana":
                resultado.set(self.calcular_mediana(lista_numeros))
            elif func == "Calcular Moda":
                resultado.set(self.calcular_moda(lista_numeros))
            elif func == "Calcular Desvio Padrão":
                resultado.set(self.calcular_desvio_padrao(lista_numeros))
            else:
                resultado.set("Opção inválida.")

        janela = tk.Toplevel(self.master)
        janela.title("Estatísticas")
        janela.geometry("400x300")
        ttk.Label(janela, text="Escolha uma função:", font=("Arial", 12)).pack(pady=10)
        opcoes_var = tk.StringVar(value="Calcular Média")
        opcoes = ["Calcular Média", "Calcular Mediana", "Calcular Moda", "Calcular Desvio Padrão"]
        ttk.OptionMenu(janela, opcoes_var, *opcoes).pack()

        ttk.Label(janela, text="Digite os números separados por vírgula:").pack(pady=5)
        entrada_numeros = ttk.Entry(janela)
        entrada_numeros.pack()

        resultado = tk.StringVar(value="")
        ttk.Button(janela, text="Calcular", command=calcular).pack(pady=10)
        ttk.Label(janela, textvariable=resultado, font=("Arial", 12)).pack()

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
        contagem = Counter(lista)
        max_freq = max(contagem.values())
        modas = [num for num, freq in contagem.items() if freq == max_freq]
        return modas

    def calcular_desvio_padrao(self, lista):
        """Calcula o desvio padrão de uma lista de números."""
        media = self.calcular_media(lista)
        variancia = sum((x - media) ** 2 for x in lista) / len(lista)
        return variancia ** 0.5

    # Equations
    def show_equacoes(self):
        def resolver():
            grau = grau_var.get()
            try:
                if grau == "1":
                    a = float(entrada_a.get())
                    b = float(entrada_b.get())
                    solucao = -b / a
                    resultado.set(f"Solução da equação linear: x = {solucao}")
                elif grau == "2":
                    a = float(entrada_a.get())
                    b = float(entrada_b.get())
                    c = float(entrada_c.get())
                    discriminante = b**2 - (4 * a * c)
                    if discriminante >= 0:
                        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
                        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
                        resultado.set(f"As raízes são x1 = {raiz1} e x2 = {raiz2}")
                    else:
                        resultado.set("Sem solução real.")
            except ValueError:
                resultado.set("Erro: Entrada inválida.")

        janela = tk.Toplevel(self.master)
        janela.title("Resolver Equações")
        janela.geometry("400x300")
        ttk.Label(janela, text="Escolha o grau da equação:", font=("Arial", 12)).pack(pady=10)
        grau_var = tk.StringVar(value="1")
        ttk.Radiobutton(janela, text="Primeiro grau", variable=grau_var, value="1").pack()
        ttk.Radiobutton(janela, text="Segundo grau", variable=grau_var, value="2").pack()

        ttk.Label(janela, text="Coeficientes:").pack(pady=5)
        entrada_a = ttk.Entry(janela)
        entrada_a.pack()
        entrada_b = ttk.Entry(janela)
        entrada_b.pack()
        entrada_c = ttk.Entry(janela)
        entrada_c.pack()

        resultado = tk.StringVar(value="")
        ttk.Button(janela, text="Resolver", command=resolver).pack(pady=10)
        ttk.Label(janela, textvariable=resultado, font=("Arial", 12)).pack()

    # Matrix Operations
    def show_operacoes_matrizes(self):
        def realizar_operacao():
            # Implementar a lógica para operações com matrizes
            pass

        janela = tk.Toplevel(self.master)
        janela.title("Operações com Matrizes")
        janela.geometry("400x300")
        ttk.Label(janela , text="Escolha a operação com matrizes:", font=("Arial", 12)).pack(pady=10)
        opcoes_var = tk.StringVar(value="Adição")
        opcoes = ["Adição", "Multiplicação", "Transposição"]
        ttk.OptionMenu(janela, opcoes_var, *opcoes).pack()

        ttk.Label(janela, text="Digite o tamanho da matriz (ex: 2x2):").pack(pady=5)
        entrada_tamanho = ttk.Entry(janela)
        entrada_tamanho.pack()

        ttk.Label(janela, text="Digite o valor inicial:").pack(pady=5)
        entrada_valor_inicial = ttk.Entry(janela)
        entrada_valor_inicial.pack()

        ttk.Button(janela, text="Realizar Operação", command=realizar_operacao).pack(pady=10)

    # Geometry
    def show_geometria(self):
        def calcular_area():
            func = opcoes_var.get()
            if func == "Área do Círculo":
                raio = float(entrada_raio.get())
                resultado.set(self.calcular_area_circulo(raio))
            elif func == "Área do Retângulo":
                largura = float(entrada_largura.get())
                altura = float(entrada_altura.get())
                resultado.set(self.calcular_area_retangulo(largura, altura))
            elif func == "Perímetro do Triângulo":
                a = float(entrada_a.get())
                b = float(entrada_b.get())
                c = float(entrada_c.get())
                resultado.set(self.calcular_perimetro_triangulo(a, b, c))
            elif func == "Volume do Cubo":
                lado = float(entrada_lado.get())
                resultado.set(self.calcular_volume_cubo(lado))

        janela = tk.Toplevel(self.master)
        janela.title("Geometria")
        janela.geometry("400x300")
        ttk.Label(janela, text="Escolha uma função:", font=("Arial", 12)).pack(pady=10)
        opcoes_var = tk.StringVar(value="Área do Círculo")
        opcoes = ["Área do Círculo", "Área do Retângulo", "Perímetro do Triângulo", "Volume do Cubo"]
        ttk.OptionMenu(janela, opcoes_var, *opcoes).pack()

        # Inputs for different calculations
        entrada_raio = ttk.Entry(janela)
        entrada_largura = ttk.Entry(janela)
        entrada_altura = ttk.Entry(janela)
        entrada_a = ttk.Entry(janela)
        entrada_b = ttk.Entry(janela)
        entrada_c = ttk.Entry(janela)
        entrada_lado = ttk.Entry(janela)

        resultado = tk.StringVar(value="")
        ttk.Button(janela, text="Calcular", command=calcular_area).pack(pady=10)
        ttk.Label(janela, textvariable=resultado, font=("Arial", 12)).pack()

    def calcular_area_circulo(self, raio):
        """Calcula a área de um círculo dado o raio."""
        return math.pi * raio ** 2

    def calcular_area_retangulo(self, largura, altura):
        """Calcula a área de um retângulo dado a largura e a altura."""
        return largura * altura

    def calcular_perimetro_triangulo(self, a, b, c):
        """Calcula o perímetro de um triângulo dado os comprimentos dos lados."""
        return a + b + c

    def calcular_volume_cubo(self, lado):
        """Calcula o volume de um cubo dado o comprimento do lado."""
        return lado ** 3

    # Theorems
    def show_teoremas(self):
        def calcular_teorema():
            func = opcoes_var.get()
            if func == "Teorema de Pitágoras":
                a = float(entrada_a.get())
                b = float(entrada_b.get())
                resultado.set(self.teorema_pitagoras(a, b))
            elif func == "Teorema de Tales":
                a = float(entrada_a.get())
                b = float(entrada_b.get())
                c = float(entrada_c.get())
                resultado.set(self.teorema_tales(a, b, c))

        janela = tk.Toplevel(self.master)
        janela.title("Teoremas")
        janela.geometry("400x300")
        ttk.Label(janela, text="Escolha um teorema:", font=("Arial", 12)).pack(pady=10)
        opcoes_var = tk.StringVar(value="Teorema de Pitágoras")
        opcoes = ["Teorema de Pitágoras ", "Teorema de Tales"]
        ttk.OptionMenu(janela, opcoes_var, *opcoes).pack()

        entrada_a = ttk.Entry(janela)
        entrada_b = ttk.Entry(janela)
        entrada_c = ttk.Entry(janela)

        resultado = tk.StringVar(value="")
        ttk.Button(janela, text="Calcular", command=calcular_teorema).pack(pady=10)
        ttk.Label(janela, textvariable=resultado, font=("Arial", 12)).pack()

    def teorema_pitagoras(self, a, b):
        """Calcula a hipotenusa de um triângulo retângulo."""
        return (a**2 + b**2) ** 0.5

    def teorema_tales(self, a, b, c):
        """Calcula a proporção do Teorema de Tales."""
        return (a / b) * c

# Inicialização do programa
root = tk.Tk()
app = App(root)
root.mainloop()