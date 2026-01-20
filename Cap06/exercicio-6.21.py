# Escreva um programa que compare duas listas. Utilizando operações
# Com conjuntos, imprima:
# * Os valores comuns às duas listas
# * Os valores que só existem na primeira
# * Os valores que existem apenas na segunda
# * Uma lista com elementos não repetidos das duas listas
# a primeira lista sem os elementos repetidos

l1 = [x for x in range(0,100)]
l2 = [x for x in  range(50, 100)]

a = set(l1)
b = set(l2)
print(a&b)
print(a-b)
print(b-a)
print(a^b)
print(a)
