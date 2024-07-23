totmenor = 0
totmaior = 0 
for idade in range (0, 7):
    idade = int(input("Em que ano nasceu a Pessoa? "))
    soma = 2024 - idade
        
    if soma >= 18:
        totmaior += 1

    else:
        totmenor += 1

print(f"O total {totmaior} de pessoas maiores de idade!")
print(f"O total {totmenor} de pessoas menores de idade!")
    

