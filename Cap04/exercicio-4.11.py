# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
valor_casa = float(input("Digite o valor da casa a comprar: "))
salario = float(input("Digite o salário: "))
anos = float(input("Digite a quantidade de anos: "))

prestacao = valor_casa / (anos * 12)

print(f"Prestação mensal: R${prestacao}")
print(f"Limite permitido (30% do salário): R${salario * 0.30}")

if prestacao <= salario * 0.30:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")
