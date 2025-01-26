# Operadores lógicos
# AND (and), OR (or), NOT (not)
# and - todas as condições precisam ser verdaderias
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (Que já vimos até agora): 0, 0.0, "" False
# Também existe o tipo None que é usado para representar um não valor

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

# Python usa avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)