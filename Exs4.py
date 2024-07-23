nascimento = int(input("Digite o ano de seu nascimento: "))
alistar = 2024 - nascimento
if alistar > 18:
    print(f"Você com {alistar} não pode se alistar. ")
elif alistar < 18:
    print(f"Você com {alistar} ainda não pode se alistar.")
elif alistar == 18:
    print(f"Você com {alistar} de idade pode se alistar")