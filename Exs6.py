from datetime import date

idade = int(input("Digite seu ano de nascimemnto: "))
atual = date.today().year
categoria = atual - idade
print (f"O atleta tem {categoria}")

if categoria <= 9:
    print(f"Sua idade é {categoria}, portanto sua categoria é MIRIM.")

elif categoria <= 10:
    print(f"Sua idade é {categoria}, portanto sua categoria é INFANTIL.")

elif categoria <=19:
    print(f"Sua idade é {categoria}, portanto sua categoria é JUNIOR.")

elif categoria <=25:
    print(f"Sua idade é {categoria}, portanto sua categoria é SÊNIOR.")

else:
    print(f"Sua idade é {categoria}, portanto sua categoria é MASTER.")