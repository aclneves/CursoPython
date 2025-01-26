# Operadores lógicos
# AND (and), OR (or), NOT (not)
# or - Qualquer condição verdadeira avalia toda a expressão com verdadeira
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# São considerados falsy (Que já vimos até agora): 0, 0.0, "" False
# Também existe o tipo None que é usado para representar um não valor

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

# Python usa avaliação de curto circuito
print(True or False or True)
print(False or 1 or True)

senha = input("Senha: ") or "Senha não digitada"
print(senha)