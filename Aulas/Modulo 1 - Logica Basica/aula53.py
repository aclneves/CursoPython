"""
Operação ternária(condicional de uma linha)
<valor> if <condição> else <outro valor>
"""

print("valor" if True else "Outro valor")

condicao = 10 == 10
variavel = "valor" if condicao else "outro valor"

print(variavel)

condicao = 10 < 5
variavel = "valor" if condicao else "outro valor"

print(variavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

digito = 10
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

hora = int(input("Digite a hora: "))
print("Bom dia" if hora < 12 else "Boa tarde" if hora < 18 else "Boa noite" if hora <24 else "Hora incorreta")
# Não deve ser utilizado, mas funciona