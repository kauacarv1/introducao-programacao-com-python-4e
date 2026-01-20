# Modifique o primeiro exemplo(Programa 6.9) de forma a realizar
# a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de
# saída do while.

l = [15, 7, 27,39]
p = int(input("Digite o valor a procurar: "))
x = 0
while x < len(l):
    if l[x] == p:
        break
    x+=1
if p == l[x]:
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")