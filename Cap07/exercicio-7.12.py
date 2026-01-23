# Escreva um jogo da velha para dois jogadores. O jogo deve perguntar
# onde você quer jogar e alternar entre os jogadores. A cada jogada, verifique-se
# a posição está livre. Verifique também quando um jogador venceu a partida.
# Um jogo da velha pode ser visto como uma lista de três elementos, na qual cada
# elemento é outra lista, também com três elementos.

# 7 | 8 | 9
# --+---+--
# 4 | 5 | 6
# --+---+--
# 1 | 2 | 3

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tab):
    print("\n")
    for i, linha in enumerate(tab):
        print(" | ".join(linha))
        if i < 2:
            print("--+---+--")
    print("\n")

def verificar_vitoria(tab, jogador):
    for linha in tab:
        if all(c == jogador for c in linha):
            return True
    for col in range(3):
        if all(tab[lin][col] == jogador for lin in range(3)):
            return True
    if all(tab[i][i] == jogador for i in range(3)):
        return True
    if all(tab[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tab):
    return all(tab[i][j] != " " for i in range(3) for j in range(3))

mapa_posicoes = {
    1: (2, 0), 2: (2, 1), 3: (2, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (0, 0), 8: (0, 1), 9: (0, 2)
}

jogador_atual = "X"

while True:
    mostrar_tabuleiro(tabuleiro)
    pos = int(input(f"{jogador_atual}, escolha uma posição (1-9): "))
    if pos not in mapa_posicoes:
        print("inválida! Digite um número de 1 a 9.")
        continue
    linha, coluna = mapa_posicoes[pos]
    if tabuleiro[linha][coluna] != " ":
        print("Posição ocupada!")
        continue

    tabuleiro[linha][coluna] = jogador_atual

    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f"{jogador_atual} venceu! ")
        break

    if verificar_empate(tabuleiro):
        mostrar_tabuleiro(tabuleiro)
        print("Empate!")
        break

    jogador_atual = "O" if jogador_atual == "X" else "X"

