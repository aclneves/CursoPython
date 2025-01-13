"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input("Que horas são? (0-23): ")

try:
    hora = int(entrada)
    if hora < 0 or hora > 23:
        print("Hora inválida")
    elif hora < 12:
        print("Bom dia")
    elif hora < 18:
        print("Boa tarde")
    else:
        print("Boa noite")
except:
    print("Favor digite apenas números inteiros")