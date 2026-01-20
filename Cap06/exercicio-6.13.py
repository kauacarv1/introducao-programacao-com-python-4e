# A lista de temperaturas de Mons, na Bélgica, foi armazena na
# lista T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor
# e a maior temperatura, assim como a temperatura média

T = [-10, -8, 0, 1, 2, 5, -2, -4]

soma = 0
menor = T[0]
maior = T[0]

for i in T:
    soma +=i
    if i> maior:
        maior = i
    elif i< menor:
        menor = i

media = soma/len(T)
print(f"{menor=}, {maior=}, {media=}")
