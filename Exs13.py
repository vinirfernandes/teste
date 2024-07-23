soma = 0
cont = 0 
for c in range (1, 7):
    num = int(input(f"Escreva um numero: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"vc falou {cont} numeros e a soma deles é {soma}")


        


