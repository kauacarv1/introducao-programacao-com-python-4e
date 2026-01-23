# Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
# A ordem dos caracteres gerada não é importante, mas deve conter todas as letras comuns a ambas.

s1 = input("Digite a primeira string:")
s2 = input("Digite a segunda string:")
conjunto = set(s1)&set(s2)
conjunto = "".join(conjunto)
print(conjunto)