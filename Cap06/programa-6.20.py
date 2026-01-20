# Programa 6.20: Ordenação pelo método de bolhas

l = [7,4,3,12,8]
fim = len(l)
while fim >1:
    trocou = False
    x = 0
    while x < (fim-1):
        if l[x] > l[x +1]:
            trocou = True
            l[x], l[x+1] = l[x+1], l[x]
        x+=1
    if not trocou:
        break
    fim -=1
for e in l:
    print(e)