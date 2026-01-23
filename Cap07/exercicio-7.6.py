# Escreva um programa que leia três strings. Imprima o resultado
# da substituição na primeira, dos caracteres da segunda pelos da terceira.

s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")
s3 = input("Digite a terceira string: ")

resultado = ""

for letra in s1:
    if letra in s2:
        i = s2.index(letra)
        resultado += s3[i]
    else:
        resultado += letra

print(f"{resultado=}")

