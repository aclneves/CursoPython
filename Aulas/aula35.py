"""
while/else
"""
string = input("Digite uma string: ")
i = 0

while i < len(string):
    letra = string[i]
    print(letra)

    if letra == " ":
        print("Espaço encontrado")
        break

    i += 1
else:
    print("O laço inteiro foi executado")

print("Esse é um print fora do laço")
