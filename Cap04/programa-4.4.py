# Programa 4.4: Cálculo da mensalidade de um plano de celular da operadora Tchau

plano = input("Qual é o seu plano de celular? ")

if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preço = 50

if plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preço = 99

if plano != "falopouco" and plano != "falomuito":
    print("Não conheço este plano")

if plano == "falopouco" or plano == "falomuito":
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Voçê vai pagar: ")
    print("Preço do plano:R$", preço)
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
        print("suplemento R$", suplemento)
        print("Total R$", (preço + suplemento))