# Escreva um programa que leia uma string e imprima quantas
# vezes cada caracteres da segunda forma retirados da primeira.

s = input("Digite uma string: ")

usados = []

for letra in s:
    if letra not in usados:
        qtd = s.count(letra)
        print(f"{letra} : {qtd}x")
        usados.append(letra)





