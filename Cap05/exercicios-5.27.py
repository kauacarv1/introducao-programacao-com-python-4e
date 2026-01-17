# Escreva um programa que verifica se um número é um palíndromo.
# Um número é um palíndromo se continua o mesmo caso seus digitos sejam invertidos.
# Exemplos: 424, 10501

n = int(input("Digite um número: "))
inverso = 0

while n> 0:
    inverso*=10
    inverso += n%10
    n = n//10

print(n==inverso)
