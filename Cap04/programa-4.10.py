# Programa 4.10: Planos da Tchau com elif

válido = True
plano  = input("Qual é o seu plano de celuar? ")

if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preço = 50

elif plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preço = 99

else:
    válido = False

if not válido:
    print("Erro: Não conheço este plano", plano)

else:
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print("Preço do plano R$", preço)

    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)

    print("Suplmento R$", round(suplemento, 2))
    print("Total R$", round(preço + suplemento, 2))