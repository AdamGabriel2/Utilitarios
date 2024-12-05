from Menu import Menu

class UttsTexto:
    def __init__(self):
        menu_opcoes=["Analise de Texto"]
        menu = Menu("Utilitários de Texto", menu_opcoes)
        menu.desenhar()
        escolha = input("Escolha uma opção: ")
        match escolha:
            case "0": return
            case "1": AnaliseTexto()
            case _: print("Opção inválida. Por favor, escolha novamente.")

# --- ANÁLISE DE TEXTO ---
class AnaliseTexto:
    def __init__(self):
        """Contagem de palavras e caracteres no texto, e frequência de palavras e caracteres."""
        texto = input("Digite o texto para análise: ")
        palavras = texto.split()

        contador_palavras = Counter(palavras)
        contador_caracteres = Counter(texto)
        print(f"Número total de palavras: {len(palavras)}")
        print("Frequência de palavras:", dict(contador_palavras))
        print("Frequência de caracteres:", dict(contador_caracteres))
