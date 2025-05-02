"""
Iterando strings com while
"""

#       012345...
nome = "Antonio Neves"
contador = 0
nova_string = ""

while contador < len(nome):

    nova_string += "*" + nome[contador]

    if contador == len(nome) - 1:
        nova_string += "*"
    contador += 1

print(nova_string)
