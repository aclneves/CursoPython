"""
Shallow COpy e Deep Copy
copy - retornar uma cópia rasa (shallow copy)
"""
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d2 = d1  # Mesmo endereço de memória, não copia
d2['c1'] = 10
print(f'D1:', d1)
print(f'D2:', d2)
print()

d3 = d1.copy()  # Vai copiar apenas o que for imutável, se tiver um item mutável não vai copiar e sim apontar pra memoória
d3['l1'][0] = 100
print(f'D1:', d1)
print(f'D3:', d3)
print()

d4 = copy.deepcopy(d1)
d4['l1'][1] = 100000
print(f'D1:', d1)
print(f'D4:', d4)
