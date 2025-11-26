# Programa 4.3: Cálculo do Imposto de Renda

salário = float(input("Digite o salário para cálculo do imposto de renda: "))
base = salário
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000

if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print("Salário: R$", salário, "Imposto a pagar: R$", imposto)