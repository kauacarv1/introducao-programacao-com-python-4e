# Escreva um programa que compare duas listas. Considere a primeira
# lista como a versão inicial e a segunda como a versão após alterações,
# Utilizando operações com conjuntos, seu programa deverá imprimir a lista de
# modificações entre essas duas versões, listando:
# * Os elemento que não mudaram
# * Os novos elementos
# * Os elementos que foram removidos

l1 = [3, 7, 12, 18, 25, 30]
l2 = [1, 7, 12, 20, 25, 40]

a = set(l1)
b = set(l2)

print(f"{a&b=}")
print(f"{b-a=}")
print(f"{a-b=}")