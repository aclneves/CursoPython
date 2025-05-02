"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

"""
import re

cpf_digitado_usuario = input("Digite um CPF: ")
cpf_digitado_usuario = re.sub(r"[^0-9]", "", cpf_digitado_usuario)
# cpf_digitado_usuario = cpf_digitado_usuario.replace(".", "").replace("-", "")

tamanho_cpf_invalido = len(cpf_digitado_usuario) != 11
cpf_nao_numerico = not cpf_digitado_usuario.isnumeric()
if cpf_digitado_usuario:
    cpf_numeros_repetidos = cpf_digitado_usuario == cpf_digitado_usuario[0] * len(cpf_digitado_usuario)
else:
    cpf_numeros_repetidos = False

if tamanho_cpf_invalido or cpf_nao_numerico or cpf_numeros_repetidos:
    print("Você digitou um cpf inválido")
else:

    # Validação do primeiro dígito verificador1

    nove_digitos_do_cpf = cpf_digitado_usuario[:9]
    contador_regressivo_primeiro_digito = 10
    soma_nove_digitos = 0

    for digito in nove_digitos_do_cpf:
        soma_nove_digitos += contador_regressivo_primeiro_digito * int(digito)
        contador_regressivo_primeiro_digito -= 1

    digito_verificador_1 = soma_nove_digitos * 10 % 11
    digito_verificador_1 = digito_verificador_1 if digito_verificador_1 <= 9 else 0

    # Validação do segundo dígito verificador

    dez_digitos_do_cpf = cpf_digitado_usuario[:10]
    contador_regressivo_segundo_digito = 11
    soma_dez_digitos = 0

    for digito in dez_digitos_do_cpf:
        soma_dez_digitos += contador_regressivo_segundo_digito * int(digito)
        contador_regressivo_segundo_digito -= 1

    digito_verificador_2 = soma_dez_digitos * 10 % 11
    digito_verificador_2 = digito_verificador_2 if digito_verificador_2 <= 9 else 0

    cpf_gerado_calculo = f"{nove_digitos_do_cpf}{digito_verificador_1}{digito_verificador_2}"
    if cpf_digitado_usuario == cpf_gerado_calculo:
        print("O CPF é válido")
    else:
        print("O CPF é inválido")
