# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou
# Considere que um fumante perde 10 minutos de vida a cada cigarro
# calcule quantos dias de vida um fumante perderá. Exiba o total em dias

cigarros_dia = int(input("Digite a quantidade de cigarro fumados por dia: "))
anos = int(input("Digite a quantidade de anos fumando: "))
dias_perdidos = 10*cigarros_dia*365*anos/(60*24)
print(f"O fumante perderá {dias_perdidos} dias.")