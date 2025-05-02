""""
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

print(pessoa.get('nome'))
print(pessoa.get('rg'))

altura = pessoa.pop('idade')
print(altura)
print(pessoa)

endereco = pessoa.popitem()
print(endereco)
print(pessoa)

pessoa.update(
    {'sobrenome': 'Lima Neves',
     'idade': 37}
)

pessoa.update(nome='Antonio Carlos', idade=38)
print(pessoa)

tupla = ('nome', 'Antonio'), ('idade', 38), ('sobrenome', 'Neves')
pessoa.update(tupla)
print(pessoa)
