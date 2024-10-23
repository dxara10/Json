import json

class ManipuladorDadosAninhados:
    def __init__(self, dados):
        self.dados = dados

    def obter_valor(self, chave):
        try:
            return json.dumps(self.dados[chave])
        except KeyError:
            return f'A chave "{chave}" não existe nos dados.'

dados = {'pessoa': {'nome': 'Ana', 'idade': 28}}
manipulador = ManipuladorDadosAninhados(dados)
print("Valor da chave 'nome':", manipulador.obter_valor('nome'))
print("Valor da chave 'email':", manipulador.obter_valor('email'))
