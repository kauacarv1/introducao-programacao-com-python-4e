# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada,
# em vez de começar com 1 e 10.

n = int(input("Tabuada de : "))
inicio = int(input("Digite o número de início da tabuada: "))
fim = int(input("DIgite o número para o fim da tabuada: "))

while inicio <= fim:
    print(f"{n}*{inicio} = {n * inicio}.")
    inicio += 1