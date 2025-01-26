"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
"""

import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3) # 0.799999999999999

# Três maneiras de resolver
print(f"{numero_3:.2f}")
print(round(numero_3, 2)) # Se tiver 0 a direita, ele vai ocultar

numero_1 = decimal.Decimal(str(0.1))
numero_2 = decimal.Decimal(str(0.7))
numero_3 = numero_1 + numero_2

print(numero_3)
print(f"{numero_3:.2f}")
print(round(numero_3, 2))
