import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("Utilitários")
        master.geometry("500x400")
        master.configure(bg="#f0f0f0")

        # Criando o menu de barra
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Opções do Menu Principal
        self.utilitarios_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Menu Principal", menu=self.utilitarios_menu)
        
        # Adicionando as opções ao menu
        self.utilitarios_menu.add_command(label="Utilitários Matemáticos Básicos", command=self.show_mat_basicos)
        self.utilitarios_menu.add_command(label="Utilitários Matemáticos Avançados", command=self.show_mat_avancados)
        self.utilitarios_menu.add_command(label="Verificadores de Números", command=self.show_verificadores)
        self.utilitarios_menu.add_command(label="Utilitários de Texto", command=self.show_texto)
        self.utilitarios_menu.add_command(label="Conversores de Unidades", command=self.show_conversores)
        self.utilitarios_menu.add_command(label="Finanças", command=self.show_financas)
        self.utilitarios_menu.add_command(label="Jogos", command=self.show_jogos)
        self.utilitarios_menu.add_separator()
        self.utilitarios_menu.add_command(label="Sair", command=master.quit)

        # Frames principais (para cada funcionalidade)
        self.frames = {
            "mat_basicos": ttk.Frame(master, padding="10"),
            "mat_avancados": ttk.Frame(master, padding="10"),
            "verificadores": ttk.Frame(master, padding="10"),
            "texto": ttk.Frame(master, padding="10"),
            "conversores": ttk.Frame(master, padding="10"),
            "financas": ttk.Frame(master, padding="10"),
            "jogos": ttk.Frame(master, padding="10")
        }

        # Bem-vindo
        self.label_welcome = ttk.Label(master, text="Bem-vindo ao Programa de Utilitários!", font=("Arial", 16))
        self.label_welcome.pack(pady=20)

    def hide_frames(self):
        """Esconde todos os frames ativos antes de exibir o próximo."""
        for frame in self.frames.values():
            frame.pack_forget()

    def show_mat_basicos(self):
        self.hide_frames()
        frame = self.frames["mat_basicos"]
        ttk.Label(frame, text="Utilitários Matemáticos Básicos", font=("Arial", 14)).pack(pady=10)
        ttk.Button(frame, text="Calculadora Básica", command=self.show_calculadora).pack(pady=5)
        ttk.Button(frame, text="Tabuada", command=self.show_tabuada).pack(pady=5)
        frame.pack(pady=20)
        
        # Frame para a calculadora
        self.calculadora_frame = ttk.Frame(self.master, padding="10")
        self.tabuada_frame = ttk.Frame(self.master, padding="10")

        # Widgets da calculadora
        self.num1_label = ttk.Label(self.calculadora_frame, text="Primeiro número:")
        self.num1_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.num1_entry = ttk.Entry(self.calculadora_frame, width=20)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)
        self.num1_entry.insert(0, "Ex: 5.5")

        self.num2_label = ttk.Label(self.calculadora_frame, text="Segundo número:")
        self.num2_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.num2_entry = ttk.Entry(self.calculadora_frame, width=20)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)
        self.num2_entry.insert(0, "Ex: 3.2")

        self.operacao_label = ttk.Label(self.calculadora_frame, text="Operação (+, -, *, /, **):")
        self.operacao_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.operacao_entry = ttk.Entry(self.calculadora_frame, width=20)
        self.operacao_entry.grid(row=2, column=1, padx=5, pady=5)
        self.operacao_entry.insert(0, "Ex: +")

        self.calcular_btn = ttk.Button(self.calculadora_frame, text="Calcular", command=self.calcular)
        self.calcular_btn.grid(row=3, column=0, padx=5, pady=10)

        self.limpar_btn = ttk.Button(self.calculadora_frame, text="Limpar", command=self.limpar_calculadora)
        self.limpar_btn.grid(row=3, column=1, padx=5, pady=10)

        # Widgets da tabuada
        self.tabuada_label = ttk.Label(self.tabuada_frame, text="Digite um número para ver a tabuada:")
        self.tabuada_label.pack(pady=10)
        self.tabuada_entry = ttk.Entry(self.tabuada_frame, width=20)
        self.tabuada_entry.pack(pady=5)
        self.tabuada_entry.insert(0, "Ex: 7")

        self.inicio_label = ttk.Label(self.tabuada_frame, text="Início do intervalo:")
        self.inicio_label.pack(pady=5)
        self.inicio_entry = ttk.Entry(self.tabuada_frame, width=20)
        self.inicio_entry.pack(pady=5)
        self.inicio_entry.insert(0, "Ex: 1")

        self.fim_label = ttk.Label(self.tabuada_frame, text="Fim do intervalo:")
        self.fim_label.pack(pady=5)
        self.fim_entry = ttk.Entry(self.tabuada_frame, width=20)
        self.fim_entry.pack(pady=5)
        self.fim_entry.insert(0, "Ex: 10")

        self.tabuada_btn = ttk.Button(self.tabuada_frame, text="Mostrar Tabuada", command=self.tabuada)
        self.tabuada_btn.pack(pady=10)

        self.tabuada_limpar_btn = ttk.Button(self.tabuada_frame, text="Limpar", command=self.limpar_tabuada)
        self.tabuada_limpar_btn.pack(pady=5)

    def show_calculadora(self):
        self.tabuada_frame.pack_forget()  # Esconder a tabuada
        self.calculadora_frame.pack(pady=20)  # Mostrar a calculadora

    def show_tabuada(self):
        self.calculadora_frame.pack_forget()  # Esconder a calculadora
        self.tabuada_frame.pack(pady=20)  # Mostrar a tabuada

    def calcular(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operacao = self.operacao_entry.get()

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    messagebox.showerror("Erro", "Divisão por zero não é permitida.")
                    return
                resultado = num1 / num2
            elif operacao == "**":
                resultado = num1 ** num2
            else:
                messagebox.showerror("Erro", "Operação inválida.")
                return

            messagebox.showinfo("Resultado", f"O resultado é: {resultado}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

    def tabuada(self):
        try:
            num = int(self.tabuada_entry.get())
            inicio = int(self.inicio_entry.get())
            fim = int(self.fim_entry.get())

            if inicio > fim:
                messagebox.showerror("Erro", "O início do intervalo deve ser menor ou igual ao fim.")
                return

            tabuada = "\n".join([f"{num} x {i} = {num * i}" for i in range(inicio, fim + 1)])
            messagebox.showinfo("Tabuada", tabuada)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos!")

    def limpar_calculadora(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.operacao_entry.delete(0, tk.END)

    def limpar_tabuada(self):
        self.tabuada_entry.delete(0, tk.END)
        self.inicio_entry.delete(0, tk.END)
        self.fim_entry.delete(0, tk.END)

    def show_mat_avancados(self):
        self.hide_frames()
        frame = self.frames["mat_avancados"]
        ttk.Label(frame, text="Utilitários Matemáticos Avançados (Em breve)", font=("Arial", 14)).pack(pady=10)
        frame.pack(pady=20)

    def show_verificadores(self):
        self.hide_frames()
        frame = self.frames["verificadores"]
        ttk.Label(frame, text="Verificadores de Números (Em breve)", font=("Arial", 14)).pack(pady=10)
        frame.pack(pady=20)

    def show_texto(self):
        self.hide_frames()
        frame = self.frames["texto"]
        ttk.Label(frame, text="Utilitários de Texto (Em breve)", font=("Arial", 14)).pack(pady=10)
        frame.pack(pady=20)

    def show_conversores(self):
        self.hide_frames()
        frame = self.frames["conversores"]
        ttk.Label(frame, text="Conversores de Unidades (Em breve)", font=("Arial", 14)).pack(pady=10)
        frame.pack(pady=20)

    def show_financas(self):
        self.hide_frames()
        frame = self.frames["financas"]
        ttk.Label(frame, text="Utilitários de Finanças (Em breve)", font=("Arial", 14)).pack(pady=10)
        frame.pack(pady=20)

    def show_jogos(self):
        self.hide_frames()
        frame = self.frames["jogos"]
        ttk.Label(frame, text="Jogos (Em breve)", font=("Arial", 14)).pack(pady=10)
        frame.pack(pady=20)

    def placeholder(self):
        """Mensagem de funcionalidade em desenvolvimento."""
        messagebox.showinfo("Em breve", "Essa funcionalidade será implementada em breve!")

root = tk.Tk()
app = App(root)
root.mainloop()
