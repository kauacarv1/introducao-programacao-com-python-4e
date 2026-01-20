# Programa 6.9 : Pesquisa sequencial

l = [15, 7, 27,39]
p = int(input("Digite o valor a procurar: "))
achou = False
x = 0
while x < len(l):
    if l[x] == p:
        achou = True
        break
    x+=1
if achou:
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")