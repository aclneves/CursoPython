"""
High Ordes Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executar(funcao, *args):
    return funcao(*args)


v = saudacao('Bom dia', 'Antonio')
print(v)

x = executar(saudacao, "Bom dia", 'Antonio')
print(x)
