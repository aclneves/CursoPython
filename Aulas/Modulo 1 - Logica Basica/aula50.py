"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = "Olha só que coisa interessante"
frase_2 = "Pois não, vai ser separado na virgula"
lista_palavras = frase.split()
print(lista_palavras)
lista_palavras = frase_2.split(",")
print(lista_palavras)

frase_3 = "        Olha só que       ,       coisa interessante         "
lista_frase_crua = frase_3.split(",")
print(lista_frase_crua)
lista_frase = []

for i, frase in enumerate(lista_frase_crua):
    lista_frase.append(lista_frase_crua[i].strip())

print(lista_frase)

frases_unidas = ", ".join(lista_frase)
print(frases_unidas)