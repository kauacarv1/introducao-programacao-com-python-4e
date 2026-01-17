# Modifique o programa para aceitar valores decimais, ou seja,
# também contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,5.

valor = float(input("Digite o valor a pagar: R$ "))
apagar = int(round(valor * 100))
cédulas = 0
atual = 10000

while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        print(f"{cédulas} cédula(s) de R${atual/100:.2f}")
        if apagar == 0:
            break

        if atual == 10000:
            atual = 5000
        elif atual == 5000:
            atual = 2000
        elif atual == 2000:
            atual = 1000
        elif atual == 1000:
            atual = 500
        elif atual == 500:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        cédulas = 0
