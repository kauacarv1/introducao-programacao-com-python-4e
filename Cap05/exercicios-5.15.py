# Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro "Código inválido".

d ={
    1: 0.5,
    2: 1,
    3: 4,
    5: 7,
    9: 8
}
res = 0
while True:
    a = int(input("Digite o codigo do produto: "))
    if a ==0:
        break
    elif a not in d.keys():
        print("Código inválido!")
    else:
        qtd = int(input("Digite a quantidade: "))
        res+= qtd*d[a]
print(f"O total das compras é de: R${res}")

