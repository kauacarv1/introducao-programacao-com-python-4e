# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos

l = [0, 1,"abacaxi"]
l2 = [1, 4,5, 6]

l3 = []

for i in l + l2:
    if i not in l3:
        l3.append(i)

print(l3)