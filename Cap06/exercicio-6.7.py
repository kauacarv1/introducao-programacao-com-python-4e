# Faça um programa que leia um expressão com parênteses.
# Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem
# correta. Exemplos:
#
# (())         OK
# ()()(()()))  OK
# ())          Erro


p = input("Digite os parênteses: ")

pilha = []
ok = True

for char in p:
    if char == "(":
        pilha.append("(")
    elif char == ")":
        if len(pilha) == 0:
            ok = False
            break
        pilha.pop()

if len(pilha) != 0:
    ok = False

print(ok)
