"""
Continuação de while
"""

quantidade_de_linhas = 5
quantidade_de_colunas = 5

linha = 1


while linha <= quantidade_de_linhas:
    coluna = 1
    while coluna <= quantidade_de_colunas:
        print(f"{linha=} {coluna=}")
        coluna += 1
    linha += 1
    print("")

