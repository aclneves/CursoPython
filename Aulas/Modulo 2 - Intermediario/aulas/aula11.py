"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se chave não existe
copy - retornar uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave específica
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Antonio',
    'sobrenome': 'Neves',
    'idade': 37,
    'altura': 1.78,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'qual qual', 'número': 321},
    ]
}

pessoa.setdefault('rg', None)
print(pessoa['rg'])
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)
