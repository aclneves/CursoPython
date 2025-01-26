a = "A"
b = "B"
c = 1.1
string = "a={}, b={}, c={:.2f}"
string2 = "a={0} b={2:.2f} c={1}"
string3 = "a={nome1}, b={nome2}, c={nome3:.2f}"
formato = string.format(a, b, c)
formato2 = string2.format(a, b, c)
formato3 = string3.format(nome1 =a, nome2=b, nome3=c)

print(formato)
print(formato2)
print(formato3)