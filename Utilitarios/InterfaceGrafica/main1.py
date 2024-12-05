import tkinter as tk
from tkinter import ttk, messagebox


# Classe Base para Categorias
class CategoriaFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding="10")
        self.master = master

    def mostrar(self):
        """Exibe o frame atual."""
        self.pack(fill="both", expand=True)

    def esconder(self):
        """Esconde o frame atual."""
        self.pack_forget()


# Categoria: Utilitários Matemáticos Básicos
class MatematicosBasicosFrame(CategoriaFrame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="Utilitários Matemáticos Básicos", font=("Arial", 16)).pack(pady=10)

        # Botões para funcionalidades
        ttk.Button(self, text="Calculadora Básica", command=self.abrir_calculadora).pack(pady=5)
        ttk.Button(self, text="Tabuada", command=self.abrir_tabuada).pack(pady=5)

    def abrir_calculadora(self):
        CalculadoraFrame(self.master).mostrar()

    def abrir_tabuada(self):
        TabuadaFrame(self.master).mostrar()


# Subcategoria: Calculadora
class CalculadoraFrame(CategoriaFrame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="Calculadora", font=("Arial", 14)).pack(pady=10)

        # Widgets da calculadora
        self.num1 = ttk.Entry(self, width=20)
        self.num2 = ttk.Entry(self, width=20)
        self.operacao = ttk.Entry(self, width=20)

        for widget, texto in zip([self.num1, self.num2, self.operacao], ["Primeiro número", "Segundo número", "Operação (+, -, *, /)"]):
            ttk.Label(self, text=texto).pack()
            widget.pack(pady=5)

        ttk.Button(self, text="Calcular", command=self.calcular).pack(pady=5)
        ttk.Button(self, text="Voltar", command=self.esconder).pack(pady=5)

    def calcular(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            operacao = self.operacao.get()
            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    raise ValueError("Divisão por zero.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida.")
            messagebox.showinfo("Resultado", f"O resultado é: {resultado}")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))


# Subcategoria: Tabuada
class TabuadaFrame(CategoriaFrame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="Tabuada", font=("Arial", 14)).pack(pady=10)

        self.num_entry = ttk.Entry(self, width=20)
        self.num_entry.pack(pady=5)
        self.num_entry.insert(0, "Digite um número")

        ttk.Button(self, text="Mostrar Tabuada", command=self.mostrar_tabuada).pack(pady=5)
        ttk.Button(self, text="Voltar", command=self.esconder).pack(pady=5)

    def mostrar_tabuada(self):
        try:
            num = int(self.num_entry.get())
            tabuada = "\n".join([f"{num} x {i} = {num * i}" for i in range(1, 11)])
            messagebox.showinfo("Tabuada", tabuada)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")


# Classe Principal
class App:
    def __init__(self, master):
        self.master = master
        master.title("Utilitários")
        master.geometry("500x400")
        master.configure(bg="#f0f0f0")

        # Menu Principal
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Opções do Menu
        self.utilitarios_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Menu Principal", menu=self.utilitarios_menu)

        # Frames de Categoria
        self.frames = {
            "mat_basicos": MatematicosBasicosFrame(master)
        }

        # Adicionando opções ao menu
        self.utilitarios_menu.add_command(label="Utilitários Matemáticos Básicos", command=self.mostrar_mat_basicos)
        self.utilitarios_menu.add_separator()
        self.utilitarios_menu.add_command(label="Sair", command=master.quit)

        # Mensagem inicial
        self.label_welcome = ttk.Label(master, text="Bem-vindo ao Programa de Utilitários!", font=("Arial", 16))
        self.label_welcome.pack(pady=20)

    def esconder_frames(self):
        """Esconde todos os frames."""
        for frame in self.frames.values():
            frame.esconder()

    def mostrar_mat_basicos(self):
        self.esconder_frames()
        self.frames["mat_basicos"].mostrar()


root = tk.Tk()
app = App(root)
root.mainloop()
