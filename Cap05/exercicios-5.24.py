# Modifique o programa anterior de forma a ler um número n. imprima os n primeiros primos

n = int(input("Digite um número: "))

num = 2
contador = 0

while contador < n:
    primo = True
    if num <= 1:
        primo = False
    elif num == 2:
        primo = True
    elif num % 2 == 0:
        primo = False
    else:
        x = 3
        raiz = int(num ** 0.5)
        while x <= raiz:
            if num % x == 0:
                primo = False
                break
            x += 2

    if primo:
        print(num)
        contador+=1
    num+=1
