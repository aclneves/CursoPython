def executa(funcao, *args):
    return funcao(*args)


def soma(a, b):
    return a + b


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica


# Normal
print(executa(soma, 2, 3))
# Lambda
print(executa(lambda x, y: x + y, 2, 3))

# Normal
duplicar = cria_multiplicador(2)
print(executa(duplicar, 2))
# Lambda
triplicar = executa(lambda m: lambda n: n * m, 3)
print(triplicar(2))

print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5))
