# escreva um programa que leia duas strings. Verifique se a segunda
# ocorre dentro da primeira e imprima a posição de início.


s = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")

pos = s.find(s2)

if pos != -1:
    print(f"{s2} encontrado na posição {pos} de {s1}")
else:
    print("A segunda string não ocorre na primeira.")
