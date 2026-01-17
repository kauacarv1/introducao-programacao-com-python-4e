# Escreva um programa que calcule o resto da divisão de dois números.
# Utilize apenas as operações de soma e subtração para calcular o resultado.

a = float(input("Digite o dividendo: "))
b = float(input("Digite o divisor: "))

resto = a
quociente = 0
while resto >= b:
    resto-=b
    quociente +=1

print(quociente)
print(resto)