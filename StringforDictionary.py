import json

class ConversorJSONParaDict:
    def __init__(self, json_string):
        self.json_string = json_string

    def converter_para_dict(self):
        return json.loads(self.json_string)

json_string = '{"nome": "Pedro", "idade": 35, "cidade": "Belo Horizonte"}'
conversor = ConversorJSONParaDict(json_string)
dados = conversor.converter_para_dict()
print("String JSON convertida para dicionário:", dados)
