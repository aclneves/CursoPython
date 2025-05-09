"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valoor nao seja enviado
para o parâmetro, o valor padrão será usado.
Refatora: editar o código para melhorar a qualidade.
"""


def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 4)

soma(1, 2, 3)
soma(1, 2, 0)
