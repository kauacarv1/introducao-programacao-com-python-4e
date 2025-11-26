# Corrija o programa a seguir:
"""
média = input("Digite sua média:")
if média < 4:
    print("Infelizmente você reprovou")
if média < 7:
    print("Você ficou de recuperação")
if média > 7:
    print("Você passou de ano")
"""
média = float(input("Digite a sua média: "))
if média < 4:
    print("Você reprovou!")

elif média >= 4 and média < 7:
    print("Você ficou de recuperação!")

else:
    print("Você foi aprovado!")