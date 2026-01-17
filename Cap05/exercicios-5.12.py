# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será
# depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

c = float(input("Digite o valor do depósito inicial: "))
i = float(input("Digite a taxa de juros(%) de uma poupança: "))
aporte = float(input("Digite o valor do aporte mensal: "))
mes = 1
m = c
print(f"Mês 0:{m:.2f}")
while mes <=24:
    m *= (1 + i/100)
    m += aporte
    print(f"Mês {mes}: {m:.2f}")
    mes +=1
total_ganho = m-c-aporte*24
print(f"o Total ganho com juros no período foi de: R${total_ganho:.2f}")