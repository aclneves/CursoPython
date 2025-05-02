"""
Escope de funções em Python
Escopo significa o local onde aquele código pode atingir.
Exoste o escopo global e local.
O escopo global é o escopo onde que engloba toda parte do código
O escopo local é o descopo onde que engloba apenas o local onde foi declarado
"""

x = 2
z = 3


def escopo():
    global z
    x = 10
    z = 5

    def outro_escopo():
        x = 11
        y = 22
        print(x, y)

    outro_escopo()
    print(x, z)


print(f'Z impresso antes da função:', z)
escopo()
print(x)
print(f'Z impresso depois da função:', z)
