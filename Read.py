import json

class LeitorJSON:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def ler_arquivo_json(self):
        with open(self.nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados

leitor = LeitorJSON('dados.json')
dados = leitor.ler_arquivo_json()
print("Dados lidos do arquivo JSON:", dados)
