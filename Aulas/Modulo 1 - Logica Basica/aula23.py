"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal(ABCDEF0123456789)
"""

nome = "Antonio"
preco = 99.904444100

variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)

print("O hexadecimal de %d é %04X" % (3500, 3500))