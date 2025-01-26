# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + - 

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

# Corrigindo com precedência para dar 1024

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)

# Parenteses internos são executados primeiro

conta_3 = (1 + int((0.5 + 0.5))) ** (5 + 5)
print(conta_3)