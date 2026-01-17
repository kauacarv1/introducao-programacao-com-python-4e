# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

c = float(input("Digite o valor do depósito inicial: "))
i = float(input("Digite a taxa de juros(%) de uma poupança: "))

mes = 1
m = c
print("Mês 0:",m)
while mes <=24:
    m *= (1 + i/100)
    print(f"Mês {mes}: {m:.2f}")
    mes +=1
total_ganho = m-c
print(f"o Total ganho com juros no período foi de: R${total_ganho:.2f}")