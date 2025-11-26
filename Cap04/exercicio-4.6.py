# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input("Digite a distância que você deseja percorrer(em km): "))

if distancia <=200:
    preco_total = 0.5*distancia
else:
    preco_total = 0.45*distancia

print(f"O preço final é de R${preco_total}")