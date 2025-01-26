"""
Tipo tupla - uma lista imutável
"""

nomes = 'Maria', 'João', 'Pedro', 'Ana'
nomes2 = ('Maria', 'João', 'Pedro', 'Ana')

print(nomes)

# nomes[0] = 'José' # TypeError: 'tuple' object does not support item assignment

nomes3 = ['Maria', 'João', 'Pedro', 'Ana']
nomes4 = tuple(nomes3)