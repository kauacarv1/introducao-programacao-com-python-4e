# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor do salário: "))
pctg_aumento = float(input("Digite a porcentagem de aumento: "))
aumento = salario*pctg_aumento/100
salario *= 1 + pctg_aumento/100

print(f"O aumento foi de R${aumento}\nSalario final R${salario}")
