"""
Exercicio
Exiba os índices da lista
"""

lista = ["Maria", "Helena", "luiz"]
lista.append("João")

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])