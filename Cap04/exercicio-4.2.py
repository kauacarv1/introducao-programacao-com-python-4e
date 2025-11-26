# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba
# uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por
# km acima de 80 km/h.

velocidade = float(input("Qual a velocidade do carro? "))
limite_velocidade = 80
tarifa= 5
velo_excedente = velocidade - limite_velocidade
multa_total = velo_excedente * tarifa

if velocidade > limite_velocidade:
    print("Você foi multado em R$", multa_total)