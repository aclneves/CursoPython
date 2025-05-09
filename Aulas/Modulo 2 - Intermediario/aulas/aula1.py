"""
Introdução a funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao loongo do seu código.
Elas podem receber valorer para parâmetros(argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None(nada)
"""

print("A print foi usada várias vezes")  # Print é uma função sempre usada


def funcaoexemplo():
    print("Executando a função Python")


funcaoexemplo()
funcaoexemplo()


def soma(a, b):
    return a + b


print(soma(2, 3))
print(soma(5, 7))


def saudacao(nome='Desconhecido'):
    print(f'Olá, {nome}')


saudacao('Maria')
saudacao('José')
saudacao()
