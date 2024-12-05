from Menu import Menu
from UttsMaths import UttsMaths
from VerifNums import VerifNums
from UttsTexto import UttsTexto
from ConvUni import ConvUni
from Others import Financas
from Jogos import Jogos
from Algoritmos import Algoritmos

class Utilitarios:
    def __init__(self):
        menu_opcoes = ["Utilitários Matemáticos","Verificadores de Números","Utilitários de Texto","Conversores de Unidades","Finanças","Jogos","Algoritmos"]
        while True:
            menu = Menu("Menu Principal", menu_opcoes)
            menu.desenhar()
            escolha = input("Escolha uma opção: ")
            match escolha:
                case "0": 
                    print("Fim do Programa.")
                    break
                case "1": UttsMaths()
                case "2": VerifNums()
                case "3": UttsTexto()
                case "4": ConvUni()
                case "5": Financas()
                case "6": Jogos()
                case "7": Algoritmos()
                case _: print("Opção inválida. Por favor, escolha novamente.")
