"""
Calculadora com While
"""

while True:

    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")

    numeros_validos = None

    if operador not in "+-*/" or len(operador) > 1:
        print("Operador inválido")
        continue

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)

        if operador == "+":
            print(f"{numero_1_float} + {numero_2_float} = {numero_1_float + numero_2_float}")
        elif operador == "-":
            print(f"{numero_1_float} - {numero_2_float} = {numero_1_float - numero_2_float}")
        elif operador == "*":
            print(f"{numero_1_float} * {numero_2_float} = {numero_1_float * numero_2_float}")
        elif operador == "/":
            print(f"{numero_1_float} / {numero_2_float} = {numero_1_float / numero_2_float}")

    except ValueError as error:
        print("Você digitou algum número incorreto: ", error)
        numeros_validos = None
        continue

    sair = input("Quer sair [s]im ou [n]ao: ").lower().startswith("s")

    if sair:
        break
