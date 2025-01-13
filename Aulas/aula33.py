"""
continuação de while
"""

contador = 0

while contador < 100:

    if contador % 2 == 1:
        contador += 1
        continue

    print(contador)

    if contador == 50:
        break

    contador += 1
