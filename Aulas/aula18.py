# Utilizando os operadores de comparação:
# Ler dois valores e ver qual é o maior valor dos digitados

primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

if primeiro_valor == segundo_valor:
    print("Os valores são iguais.")
elif primeiro_valor > segundo_valor:
    print(f"O {primeiro_valor=} é maior que o {segundo_valor=}")
else:
    print(f"O {segundo_valor=} é maior que o {primeiro_valor=}")
