# Escreva um programa que leia duas strings e gere uma terceira, na
# qual os caracteres da segunda foram retirados da primeira

s1 = input("Digite a primeira string:")
s2 = input("Digite a segunda string:")

res = ""
for l in s1:
    if l not in s2:
        res+=l

print(res)