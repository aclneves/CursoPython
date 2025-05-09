"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamneto)
"""
# Lembrete de desempacoatamento
n, m, *resto = 1, 2, 3, 4, 5
print(n, m, resto)


def soma(x, y):
    return x + y


def soma_multiplos(*args):
    total = 0
    for numero in args:
        total += numero
    return total


print(soma(1, 2))
print(soma_multiplos(1, 2, 3, 4, 5))

numeros = 1, 2, 3, 4, 5
print(soma_multiplos(*numeros))

print(numeros)
print(*numeros)
