"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(<>^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou  -
Ex: 0>-100,1.f
Conversion flags - !r !s !a
"""

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel:7>10}")
print(f"{variavel:8<11}")
print(f"{variavel:-^11}")
print(f"{010000.4844464231231454:+,.2f}")
print(f"O hexadecimal de 1500 é {1500:04X}")


