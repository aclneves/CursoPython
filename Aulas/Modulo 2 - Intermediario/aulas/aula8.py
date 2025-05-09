"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'

    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_tarde = criar_saudacao('Boa tarde')

for nome in ['Maria', 'Helena', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))
