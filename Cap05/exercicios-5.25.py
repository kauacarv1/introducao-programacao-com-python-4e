# Escreva um programa que calcula a raiz quadrada de um número.
# Utilize o método de Newton para obter o resultado aproximado. Sendo n
# o número a obter a raiz quadrada, considere a base b = 2. calcule p usando a fórmula
# p = (b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule p usando a fórmula apresentada.
# pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.

n = float(input("Digite um número: "))

b = 2
p = (b + n/b)/2

while abs(n-p**2) >= 0.0001:
    b= p
    p= (b + n/b)/2

print(f"A raiz aproximada de {n} é {p:.2f}")

