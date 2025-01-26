"""
Desempacotamneto em chamadas de métodos e funções
"""

string = 'ABCD'
lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
tupla = "Python", "é", "legal"

a, b, *_, antipenultimo, ultimo = lista
print(a, b)
print(antipenultimo, ultimo)

for nome in lista:
    print(nome, end=" ")

print("\n")

print(*lista)
print(*string)
print(*tupla)

salas = [
    # 0           1
    ["Maria", "Helena"],
    # 0
    ["Elaine"],
    # 0        1         2           3
    ["Luiz", "João", "Eduarda"]
]

print(*salas, sep="\n")