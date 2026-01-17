# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo
#segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que
#podemos entender a multiplicação de dois números como somas sucessivas de um deles.
# Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

x = 1
res = 0
soma = ''
while x<=n1:
    res +=x
    if x == 1:
        soma+= str(n1)
    else:
        soma +="+" + str(n1)
    x+=1
print(f"{n1}*{n2} = {soma} = {n1*n2}")
