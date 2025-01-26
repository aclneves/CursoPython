"""
Lista de listas e seus índices
"""

salas = [
    # 0           1
    ["Maria", "Helena"],
    # 0
    ["Elaine"],
    # 0        1         2           3
    ["Luiz", "João", "Eduarda"]
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])

for i, sala in enumerate(salas):
    print(f"A sala {i}: ")
    for item in sala:
        print(item)