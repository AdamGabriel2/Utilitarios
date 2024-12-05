import json
from datetime import datetime

historico = []

def registrar_acao(classe, funcao, entrada, saida):
    """
    Registra a ação do usuário no histórico.

    Args:
        classe: Nome da classe.
        funcao: Nome da função.
        entrada: Entrada do usuário.
        saida: Saída do programa.
    """
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    acao = {
    "classe": classe,
        "funcao": funcao,
        "entrada": entrada,
        "saida": saida,
        "horario": agora
    }
    historico.append(acao)
    
def salvar_historico(nome_arquivo="historico.json"):
    """
    Salva o histórico em um arquivo JSON.

    Args:
        nome_arquivo: Nome do arquivo JSON.
    """
    with open(nome_arquivo, "w") as arquivo:
        json.dump(historico, arquivo, indent=2)

