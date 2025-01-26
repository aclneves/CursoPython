"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float,bool
"""
string = "antonio neves"
outra_variavel = f"{string[:3]}ABC{string[4:]}"

print(string)
print(outra_variavel)
print(string.capitalize())
print(string.isnumeric())

string2 = "1000"
print(string2.zfill(10))

numero_inteiro = 10
print(numero_inteiro.bit_count())
