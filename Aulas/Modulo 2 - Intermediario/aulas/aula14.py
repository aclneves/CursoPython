# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set()  # set vazio
s2 = set('Antonio')
s3 = {'Antonio', 1, 2, 3}  # set com valores
print(s1, type(s1))
print(s2, type(s2))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
s4 = {1, 2, 3, 3, 3, 3, 3, 3, 3, 1, 1, 2, 2}
print(s4)
lista1 = [1, 2, 3, 3, 3, 3, 3, 3, 3, 1, 1, 2, 2]
s5 = set(lista1)
print(s5)
lista1 = list(s5)
print(lista1)
print(3 in s4)
print(4 not in s4)

# Métodos úteis:
# add, update, clear, discard
set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)
print(set1)
set1.update([1, 2, 3, 4, 5, 6])
print(set1)
set1.clear()
print(set1)
set1.update([1, 2, 3, 4, 5, 6])
set1.discard(4)
print(set1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
set2 = {1, 2, 3, 4, 5, 6}
set3 = {4, 5, 6, 7, 8, 9}
set4 = set2 | set3
print(set4)
set4 = set2 & set3
print(set4)
set4 = set2 - set3
print(set4)
set4 = set3 - set2
print(set4)
set4 = set2 ^ set3
print(set4)
