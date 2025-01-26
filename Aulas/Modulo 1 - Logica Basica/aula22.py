# Operadores in e not in
# String são iteráveis
#  0 1 2 3 4 5 6
#  A n t o n i o
# -7-6-5-4-3-2-1

nome = "Antonio"
print(nome[2])
print(nome[-5])

print("t" in nome)
print("z" in nome)
print("Ant" in nome)
print(10 * "-")
print("t" not in nome)
print("z" not in nome)
print("Ant" not in nome)

palavra = input("Digite uma palavra: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in palavra:
    print(f"{encontrar} está contido em {palavra}")
else:
    print(f"{encontrar} não está contido em {palavra}")
