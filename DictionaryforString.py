import json

class ConversorDictParaJSON:
    def __init__(self, dicionario):
        self.dicionario = dicionario

    def converter_para_json(self):
        return json.dumps(self.dicionario)

dados = {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'}
conversor = ConversorDictParaJSON(dados)
json_string = conversor.converter_para_json()
print("Dicionário convertido para JSON:", json_string)
