# Escreva um programa que leia três números e que imprima o maior e o menor.
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

print(f"O maior é {maior}.\nO menor é {menor}")