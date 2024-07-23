sexo = str(input("Digite seu sexo: ")).upper()
while sexo not in 'MnFf':
    sexo = str(input("Inválido digite seu sexo novamente: ")).upper()
print(f"Sexo {sexo} registrado! ")
