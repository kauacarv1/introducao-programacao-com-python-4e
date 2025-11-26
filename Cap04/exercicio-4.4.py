# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Digite o Salário do funcionário: "))

if salario > 1250:
    salario *=1.1
if salario<= 1250:
    salario*=1.15

print(f"O salário final é de R${salario}. ")

