# Escreva um programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0(zero). No final da execução
#exiba a quantidade de números digitados, assim como a soma e a média aritmética

x = 1
total = 0
res = 0

while x != 0:
    x = int(input("Digite um número: "))
    if x!=0:
        res += x
        total +=1

print(f"Quantidade de números digitados: {total}.")
print(f"Soma: {res}")
print(f"Média: {res/total}")