# Manipulando chaves e valores em dicionários

pessoa = {}

pessoa['nome'] = 'Antonio'
print(pessoa)
print(pessoa['nome'])

# chave dinâmica
chave = 'sobrenome'
pessoa[chave] = 'Neves'
print(pessoa[chave])
pessoa[chave] = 'Lima Neves'
print(pessoa[chave])

# deletando chaves
chave2 = 'idade'
pessoa[chave2] = 37
print(pessoa[chave2])
del pessoa[chave2]
print(pessoa)

# verificando chave
if pessoa.get('idade') is None:
    print("Não existe a chave idade")
else:
    print(pessoa['idade'])
