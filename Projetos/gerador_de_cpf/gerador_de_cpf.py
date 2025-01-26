import random

condicao = True

while condicao:

    print("Bem vindo ao gerador de CPF")
    pontuacao = input("Você deseja gerar o CPF com pontuação?\n[S]im ou [N]ão ").lower().strip()

    if pontuacao == "s":
        com_pontuacao = True
    elif pontuacao == "n":
        com_pontuacao = False
    else:
        print("Por favor digite S ou N")
        continue

    nove_digitos_do_cpf = ""
    for i in range(9):
        nove_digitos_do_cpf += str(random.randint(0, 9))
    while True:
        cpf_numeros_repetidos = nove_digitos_do_cpf == nove_digitos_do_cpf[0] * len(nove_digitos_do_cpf)
        if cpf_numeros_repetidos:
            cpf_base = str(random.randint(000000000, 999999999))
            continue
        else:
            break

    # Validação do primeiro dígito verificador1

    contador_regressivo_primeiro_digito = 10
    soma_nove_digitos = 0

    for digito in nove_digitos_do_cpf:
        soma_nove_digitos += contador_regressivo_primeiro_digito * int(digito)
        contador_regressivo_primeiro_digito -= 1

    digito_verificador_1 = soma_nove_digitos * 10 % 11
    digito_verificador_1 = digito_verificador_1 if digito_verificador_1 <= 9 else 0

    # Validação do segundo dígito verificador

    dez_digitos_do_cpf = nove_digitos_do_cpf + str(digito_verificador_1)
    contador_regressivo_segundo_digito = 11
    soma_dez_digitos = 0

    for digito in dez_digitos_do_cpf:
        soma_dez_digitos += contador_regressivo_segundo_digito * int(digito)
        contador_regressivo_segundo_digito -= 1

    digito_verificador_2 = soma_dez_digitos * 10 % 11
    digito_verificador_2 = digito_verificador_2 if digito_verificador_2 <= 9 else 0

    cpf_gerado = f"{nove_digitos_do_cpf}{digito_verificador_1}{digito_verificador_2}"
    if com_pontuacao:
        print(cpf_gerado[0:3] + "." + cpf_gerado[3:6] + "." + cpf_gerado[6:9] + "-" + cpf_gerado[9:11])
    else:
        print(cpf_gerado)

    continuar = input("Deseja gerar outro CPF? [S]im ou [N]ão: \n\n").lower()
    if continuar == "s":
        continue
    else:
        break
