nome = "Antonio Neves"
altura = 1.78
peso = 88

imc = peso / altura ** 2


print(nome, " tem ", altura, "m de altura, pesa ", peso, " quilos e seu IMC é ", imc, sep="")

# Usando f-strings

texto = f"{nome} tem {altura:.2f}m de altura, pesa {peso} quilos e seu IMC é {imc:.2f}"
print(texto)