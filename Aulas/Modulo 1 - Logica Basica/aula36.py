frase = "O python é uma linguagemn de programação multiparadigma. Python foi criado por Guido van Rossum em 1991."

i = 0
quantidade_vezes_letra_com_maior_ocorrencia = 0
letra_mais_repetida = ""

while i < len(frase):
    letra = frase[i].lower()
    if letra == " ":
        i += 1
        continue

    quantidade_vezes_letra_atual_aparece = frase.count(letra)
    if quantidade_vezes_letra_atual_aparece > quantidade_vezes_letra_com_maior_ocorrencia:
        quantidade_vezes_letra_com_maior_ocorrencia = frase.count(letra)
        letra_mais_repetida = letra
    i += 1

print(f'A letra mais repetida é a "{letra_mais_repetida}" com {quantidade_vezes_letra_com_maior_ocorrencia} ocorrências')
