"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
COnhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
append - adiciona um elemento ao final da lista
insert - adiciona um elemento em um índice específico
pop - remove um elemento pelo índice ou do final da lista
del - remove um elemento pelo índice
clear - limpa a lista
extend - extende a lista com outra lista
+ - concatena listas
Create, Read, Update, Delete
Criar, ler, atualizar, deletar = lista[índice] (CRUD)
"""

# Create
lista = [1, 2, 3, 4]
lista.append(5)
lista.insert(2, 6)
print(lista)

# Read
print(lista[2])

# Update
lista[2] = 10
print(lista)

# Delete
del lista[4]
print(lista)
lista.pop()
print(lista)