# Escreva um programa que peça ao usuário que digite uma frase e
# imprima quantas vogais ela contém. Não considere maiúsculas e minúsculas
# como diferentes. Exemplo: uma frase como "As casas" deve imprimir três "as".

s = input("Digite uma frase: ")
s =s.lower()
d = {}
vogais ='aeiou'
for letra in s:
    if letra in vogais:
        if letra in d:
            d[letra]+=1
        else:
            d[letra]=1

for letra in d.keys():
    print(f"{letra} : {d[letra]}")