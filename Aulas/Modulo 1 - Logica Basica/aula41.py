"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
COnhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

string = "ABCDE" # 5 caracteres (len)
lista_vazia = []
print(type(lista_vazia))
print(bool(lista_vazia))

#         0      1       2       3       4
#        -5     -4      -3      -2      -1
lista = [123, True, "Antonio", 10.5, [1, 2, 3]]

print(lista)
print(lista[2] + ":" + lista[-3])
print(type(lista[2].upper()), type(lista[4]))

lista[2] = "Neves"

print(lista)