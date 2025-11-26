# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Digite a distância a percorrer: "))
velocidade_media = float(input("Digite a velocidade média esperada para a viagem: "))

tempo = distancia/velocidade_media
print(f" O tempo da viagem será de {tempo}")