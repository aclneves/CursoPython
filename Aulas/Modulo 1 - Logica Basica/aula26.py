"""
Introdução ao try/except
try -> tentar executar código
excpet -> ocorreu algum erro ao tentar executar
"""

numero_str = input("Digite um número: ")


try:
    numero_float = float(numero_str)
    print(f"O dobro do {numero_str} é {numero_float * 2:.2f}")
except:
    print("Isso não é um número")