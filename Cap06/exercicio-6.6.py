# Modifique o programa para trabalhar com duas filas. Para facilitar
# seu trabalho, considere o comando A para atendimento da fila 1; e B, para
# atendimento da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G,
# para fila 2.

ultimo = 10

fila1 = list(range(1, ultimo + 1))
fila2 = list(range(11, ultimo + 11))

while True:
    print(f"\nFila 1: {fila1}")
    print(f"Fila 2: {fila2}")
    print("Comandos:")
    print("A = atender fila 1")
    print("B = atender fila 2")
    print("F = adicionar cliente na fila 1")
    print("G = adicionar cliente na fila 2")
    print("S = sair")

    operacoes = input("Digite os comandos (ex: FFGAA): ").upper()

    for op in operacoes:
        if op == 'A':
            if fila1:
                fila1.pop(0)
                print("Cliente atendido na fila 1")
            else:
                print("Fila 1 vazia!")

        elif op == 'B':
            if fila2:
                fila2.pop(0)
                print("Cliente atendido na fila 2")
            else:
                print("Fila 2 vazia!")

        elif op == 'F':
            ultimo += 1
            fila1.append(ultimo)

        elif op == 'G':
            ultimo += 1
            fila2.append(ultimo)

        elif op == 'S':
            print("Saindo...")
            exit()

        else:
            print("Comando inválido! Use A, B, F, G ou S")
