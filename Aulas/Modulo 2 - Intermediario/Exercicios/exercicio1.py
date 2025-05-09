"""
Exercicio com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o falar da varoável

Crie uma função que fala se o número é par ou ímpar
Retorne se o número é par ou ímpar
"""


def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


def par_impar(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par'
    return f'O número {numero} é ímpar'


print(multiplica(1, 2, 3, 4, 5))
print(par_impar(10))
print(par_impar(15))
