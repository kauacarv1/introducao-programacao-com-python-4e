# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.
preco_mercadoria = float(input("Digite o preço da mercadoria: "))
desc_percentual = float(input("Digite o percentual de desconto: "))
desconto = preco_mercadoria*desc_percentual/100
preco_mercadoria *= 1-desc_percentual/100
print(f"O desconto foi de R${desconto}\nSalario final R${preco_mercadoria}")