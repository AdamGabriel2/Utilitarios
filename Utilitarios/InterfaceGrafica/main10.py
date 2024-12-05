import tkinter as tk
from tkinter import ttk, messagebox


class App:
    def __init__(self, master):
        self.master = master
        master.title("Utilitários")
        master.geometry("600x500")
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

    def show_frame(self, frame_key):
        """Mostra o frame especificado."""
        self.hide_frames()
        frame = self.frames[frame_key]
        frame.pack(fill="both", expand=True, pady=20)

    # Funções matemáticas básicas
    def show_mat_basicos(self):
        self.show_frame("mat_basicos")
        frame = self.frames["mat_basicos"]
        self.clear_frame(frame)

        ttk.Label(frame, text="Utilitários Matemáticos Básicos", font=("Arial", 14)).pack(pady=10)
        ttk.Button(frame, text="Calculadora Básica", command=self.show_calculadora).pack(pady=5)
        ttk.Button(frame, text="Tabuada", command=self.show_tabuada).pack(pady=5)

    # Funções matemáticas avançadas
    def show_mat_avancados(self):
        self.show_frame("mat_avancados")
        frame = self.frames["mat_avancados"]
        self.clear_frame(frame)

        ttk.Label(frame, text="Utilitários Matemáticos Avançados", font=("Arial", 14)).pack(pady=10)

        # Botões para funcionalidades específicas
        ttk.Button(frame, text="Cálculo de Fatorial", command=self.show_fatorial).pack(pady=5)
        ttk.Button(frame, text="Números Primos", command=self.show_primos).pack(pady=5)

    # Verificadores de números
    def show_verificadores(self):
        self.show_frame("verificadores")
        frame = self.frames["verificadores"]
        self.clear_frame(frame)

        ttk.Label(frame, text="Verificadores de Números", font=("Arial", 14)).pack(pady=10)

        # Botões para funcionalidades específicas
        ttk.Button(frame, text="Verificar Par/Ímpar", command=self.show_par_impar).pack(pady=5)
        ttk.Button(frame, text="Verificar Perfeito", command=self.show_perfeito).pack(pady=5)

    # Utilitários de texto
    def show_texto(self):
        self.show_frame("texto")
        frame = self.frames["texto"]
        self.clear_frame(frame)

        ttk.Label(frame, text="Utilitários de Texto", font=("Arial", 14)).pack(pady=10)

        ttk.Button(frame, text="Contador de Palavras", command=self.show_contador_palavras).pack(pady=5)
        ttk.Button(frame, text="Inversor de Texto", command=self.show_inversor_texto).pack(pady=5)

    # Conversores de unidades
    def show_conversores(self):
        self.show_frame("conversores")
        frame = self.frames["conversores"]
        self.clear_frame(frame)

        ttk.Label(frame, text="Conversores de Unidades", font=("Arial", 14)).pack(pady=10)

        ttk.Button(frame, text="Conversor de Temperatura", command=self.show_temp_converter).pack(pady=5)
        ttk.Button(frame, text="Conversor de Moedas (Em breve)", command=self.placeholder).pack(pady=5)

    # Finanças
    def show_financas(self):
        self.show_frame("financas")
        frame = self.frames["financas"]
        self.clear_frame(frame)

        ttk.Label(frame, text="Finanças", font=("Arial", 14)).pack(pady=10)

        ttk.Button(frame, text="Cálculo de Juros Compostos", command=self.show_juros_compostos).pack(pady=5)

    # Jogos
    def show_jogos(self):
        self.show_frame("jogos")
        frame = self.frames["jogos"]
        self.clear_frame(frame)

        ttk.Label(frame, text="Jogos", font=("Arial", 14)).pack(pady=10)

        ttk.Button(frame, text="Adivinhe o Número", command=self.show_adivinha_numero).pack(pady=5)

    # Funções de placeholder
    def placeholder(self):
        """Mensagem de funcionalidade em desenvolvimento."""
        messagebox.showinfo("Em breve", "Essa funcionalidade será implementada em breve!")

    # Utilitários Gerais
    def clear_frame(self, frame):
        """Remove todos os widgets de um frame."""
        for widget in frame.winfo_children():
            widget.destroy()

    # Funções Matemáticas e Conversores
    def show_calculadora(self):
        # Lógica de exibição da calculadora
        pass

    def show_tabuada(self):
        # Lógica de exibição da tabuada
        pass

    def show_fatorial(self):
        # Lógica de exibição de cálculo de fatorial
        pass

    def show_primos(self):
        # Lógica para mostrar números primos
        pass

    def show_par_impar(self):
        # Lógica para verificar par/ímpar
        pass

    def show_perfeito(self):
        # Lógica para verificar número perfeito
        pass

    def show_contador_palavras(self):
        # Lógica de contagem de palavras
        pass

    def show_inversor_texto(self):
        # Lógica para inverter texto
        pass

    def show_temp_converter(self):
        # Conversor de temperatura
        pass

    def show_juros_compostos(self):
        # Lógica de cálculo de juros compostos
        pass

    def show_adivinha_numero(self):
        # Jogo de adivinhar número
        pass


# Inicialização do programa
root = tk.Tk()
app = App(root)
root.mainloop()
