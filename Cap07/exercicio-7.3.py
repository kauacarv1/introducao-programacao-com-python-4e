# Escreva um programa que leia e gere uma terceira
# apenas com os caracteres que aparecem em uma delas.
# A ordem dos caracteres de terceira string não é importante.

s1 = input("Digite a primeira string:")
s2 = input("Digite a segunda string:")

conjunto = (set(s1) -set(s2))|(set(s2)-set(s1))
conjunto = "".join(conjunto)
print(conjunto)