plano = input("Qual é o seu plano de celular? ")

if plano != "falopouco" and plano != "falomuito":
    print("Não conheço este plano")

else:
    if plano == "falopouco":
        minutos_no_plano = 100
        extra = 0.20
        preco = 50
    else:
        minutos_no_plano = 500
        extra = 0.15
        preco = 99

    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print("Preço do plano: R$", preco)

    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
        print("Suplemento: R$", suplemento)

    print("Total: R$", preco + suplemento)
