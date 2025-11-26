# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
op = input("Qual operação você deseja realizar (+, -, *, /)? ")

if op == '+':
    print(f"O resultado é {n1 + n2}")
elif op == '-':
    print(f"O resultado é {n1 - n2}")
elif op == '*':
    print(f"O resultado é {n1 * n2}")
elif op == '/':
    if n2 == 0:
        print("Erro: divisão por zero!")
    else:
        print(f"O resultado é {n1 / n2}")
else:
    print("Operação inválida!")