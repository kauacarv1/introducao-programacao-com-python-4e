# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário,assim como a quantidade de dias
# pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$ 60 por dia e R$ 0,15 por km rodado.

km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))
km_rodado = 0.15
diaria_carro = 60

preco_total = km*km_rodado + dias*diaria_carro
print(f'O preço a pagar foi de R${preco_total}')