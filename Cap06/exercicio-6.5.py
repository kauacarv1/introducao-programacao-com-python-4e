# Altere o Programa6.7 de forma a poder trabalhar com vários
# comandos digitados de uma só vez. Atualmente apenas um comando pode
# ser inserido por vez. Altere-o de forma a considerar operações como uma string
# Exemplos: FFAAAS 


último = 10
fila = list(range(1, último+1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operações = input("Operação (F, A ou S): ")

    for op in operações:
        if op == 'A':
            if len(fila)>0:
                fila.pop(0)
                print(f"Cliente atendido")
            else:
                print("Fila vasia! Ninguem para atender")
        elif op == 'F':
            último += 1
            fila.append(último)
        elif op == 'S':
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
