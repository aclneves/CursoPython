"""
Continuação de list
extend e +
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista3 = lista1 + lista2
print(lista3)

lista4 = lista1.extend(lista2) # Não é possível fazer isso, o extend trabalha com a lista original

print(lista1) # O extend não retorna nada, ele modifica a lista original

lista1.clear()
print(lista1)