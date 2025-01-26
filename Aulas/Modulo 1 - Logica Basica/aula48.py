"""
enumerate = enumera iteráveis (índices)
"""

lista = ['Maria', 'João', 'Pedro', 'Ana']
lista.append('José')

lista_enumerada = enumerate(lista)
print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)

# Depois de consumir o iterável, ele não pode ser consumido novamente
for item in lista_enumerada:
    print(item)

# Dessa forma abaixo, o iterável é criado sempre, então pode ser consumido quantas vezes quiser
for item in enumerate(lista):
    print(item)

lista_enumerada = list(enumerate(lista, start=1))
print(lista_enumerada)

for indice, nome in lista_enumerada:
    print(indice, nome)