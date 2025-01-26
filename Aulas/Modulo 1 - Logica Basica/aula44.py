"""
Cuidados com dados mutáveis
= - copiado o valor (imutável)
= - aoponta para o mesmo endereço de memória (mutável)
"""

lista_a = ["João", "Maria"]
lista_b = lista_a # Lista b aponta para o mesmo endereço de memória de lista a

lista_a.append("José") # Como alteramos a lista a, a lista b também é alterada
print(lista_b)

lista_b.append("Ana") # Como alteramos a lista b, a lista a também é alterada
print(lista_a)

lista_c = lista_a.copy() # Copia a lista, não aponta para o mesmo endereço de memória
lista_c.append("Pedro")
print(lista_a)
print(lista_c)