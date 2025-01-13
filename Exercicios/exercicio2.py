# Exercício - Calcular IMC
# IMC = peso / (altura x altura)
# Exibir o seguinte texto no final
# Nome tem Xm de altura, pesa Y quilos e seu IMC é Z

nome = "Antonio Neves"
altura = 1.78
peso = 88

imc = peso / altura ** 2

print(nome, " tem ", altura, "m de altura, pesa ", peso, " quilos e seu IMC é ", imc, sep="")