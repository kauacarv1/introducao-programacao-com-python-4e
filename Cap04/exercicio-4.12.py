# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para
# comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

#+---------------------------------------+
#|   Preço por tipo e faixa de consumo   |
#+---------------------------------------+
#| Tipo        | Faixa (kWh)   | Preço   |
#+=======================================+
#| Residencial | Até 500       | R$ 0,40 |
#|             | Acima de 500  | R$ 0,65 |
#+---------------------------------------+
#| Comercial   | Até 1000      | R$ 0,55 |
#|             | Acima de 1000 | R$ 0,60 |
#+---------------------------------------+
#| Industrial  | Até 5000      | R$ 0,55 |
#|             | Acima de 5000 | R$ 0,60 |
#+---------------------------------------+

kwh = float(input("Quantidade de kWh consumida: "))
tipo = input("Tipo de instalação (r - residencial, c - comercial, i - industrial): ")
if tipo == "r":
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65

elif tipo == "c":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60

elif tipo == "i":
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60

else:
    print("Tipo de instalação inválido!")
    preco = 0
if preco !=0:
    total = kwh * preco
    print(f"Preço por kWh: R${preco:.2f}")
    print(f"Total a pagar: R${total:.2f}")
