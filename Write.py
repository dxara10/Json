import json

class EscritorJSON:
    def __init__(self, nome_arquivo, dados):
        self.nome_arquivo = nome_arquivo
        self.dados = dados

    def escrever_arquivo_json(self):
        with open(self.nome_arquivo, 'w') as arquivo:
            json.dump(self.dados, arquivo, indent=4)

dados = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
escritor = EscritorJSON('dados.json', dados)
escritor.escrever_arquivo_json()
