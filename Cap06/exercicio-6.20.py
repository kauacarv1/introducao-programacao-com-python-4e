# Escreva um programa que gere um dicionário, em que cada
# chave seja um caractere, e seu valor seja o número
# desse caractere encontrado em uma frase lida.

frase = input("Digite uma Frase: ")
frase = frase.replace(" ","")
d = {}
for i in frase:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1

print(d)


