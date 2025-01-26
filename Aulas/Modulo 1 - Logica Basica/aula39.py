"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
nxet -> entrega o próximo valor
iter -> entrega um iterador
"""
# for letra in texto

texto = "Python"
iterator = iter(texto)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
