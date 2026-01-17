# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
# Pergunte também o valor mensal que será pago.
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

vi = float(input("Digite o valor inicial da dívida: "))
i = float(input("Digite a taxa de juros mensal (%): "))
vp = float(input("Digite o valor a ser pago mensalmente: "))

saldo = vi
mes = 0
total_pago = 0

if vp <= saldo * (i/100):
    print("A dívida nunca será quitada.")
else:
    while saldo > 0:
        saldo *= (1 + i/100)
        saldo -= vp
        mes += 1
        total_pago += vp

        if saldo < 0:
            saldo = 0

    total_juros = total_pago - vi

    print(f"Meses para quitar: {mes}")
    print(f"Total pago: R$ {total_pago:.2f}")
    print(f"Total de juros: R$ {total_juros:.2f}")

