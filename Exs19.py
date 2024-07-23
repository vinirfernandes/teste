velho = float('')
somaidade = 0
nomevelho = ''
totalmulheres = 0

for c in range(1, 5):
    print("---- PESSOA ----")
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo M/F: "))    
    somaidade += idade
    if c == 1 and sexo in "Mn":
        velho = idade
        nomevelho = velho
    if sexo in "Mn" and idade > velho:
        velho = idade
        nomevelho = velho
    if sexo in "Ff" and idade < 20:
        totalmulheres =+ 1

media = somaidade / 4
            
print(f"A média de idade do grupo é: {media}")
print(f"O homem mais velho tem {velho}, e se chama {nomevelho}")