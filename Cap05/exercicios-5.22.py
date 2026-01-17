# Escreva um programa que exiba uma lista de operações(menu):
# adição, subtração, divisão, multiplicação e sair: imprima a tabuada da operação escolhida
# Repita até que a opção saida seja escolhida

while True:
    print("\n==Lista de operações==")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    op = int(input("Escolha uma opção: "))

    if op == 5:
        print("Saindo...")
        break

    n = int(input("Digite um número para a tabuada: "))

    for i in range(1, 11):
        if op == 1:
            print(f"{n} + {i} = {n+i}")
        elif op == 2:
            print(f"{n} - {i} = {n-i}")
        elif op == 3:
            print(f"{n} x {i} = {n*i}")
        elif op == 4:
            print(f"{n} / {i} = {n/i:.2f}")
        else:
            print("Opção inválida")
            break
