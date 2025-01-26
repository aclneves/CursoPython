"""
Introdução ao desempacotamento
"""

nomes = ["João", "Maria", "José", "Ana", "Pedro"]

nome1, nome2, nome3, nome4, nome5 = nomes

print(nome4)

nome1, nome2, *_ = nomes # O * indica que os valores restantes serão armazenados em uma lista

print(*_) # O _ indica que não queremos armazenar o valor em uma variável, é uma convenção