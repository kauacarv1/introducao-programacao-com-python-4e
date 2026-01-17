# Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão por 2 e depois por todos os números ímpares até
# o número lido. Se o resto de um dessas divisões for igual a zero, o número não é primo. Observe
# que 0 e 1 não são primos e que 2 é o único primo que é par.

n = int(input("Digite um número: "))

if n <= 1:
    primo = False
elif n == 2:
    primo = True
elif n % 2 == 0:
    primo = False
else:
    primo = True
    x = 3
    raiz = int(n ** 0.5)
    while x<= raiz:
        if n%x == 0:
            primo = False
        x+=2

print(primo)